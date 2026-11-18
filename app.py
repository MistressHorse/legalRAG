import os
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from typing import List
from src.ingestion.loaders import validate_format, check_empty, read_pdf
from index import HTML_PAGE
from src.ingestion.cleaning import process_all_pdfs
from src.retrieval.chuncking import chunk_text


app = FastAPI()
UPLOAD_PATH = "data/uploads"
os.makedirs(UPLOAD_PATH, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTML_PAGE.replace("{result_html}", "")


@app.post("/upload", response_class=HTMLResponse)
async def upload_files(files: List[UploadFile] = File(...)):
    if len(files) > 5:
        result_html = '<div class="result error"><p>Можно загрузить не более 5 файлов.</p></div>'
        return HTMLResponse(content=HTML_PAGE.replace("{result_html}", result_html))

    messages = []
    has_error = False

    for file in files:
        filename = file.filename
        content = await file.read()

        if not validate_format(filename):
            messages.append("<p>Ошибка формата!</p>")
            has_error = True
            continue

        if check_empty(content):
            messages.append(f"<p>Файл {filename} пуст!</p>")
            has_error = True
            continue

        doc = read_pdf(content)
        if doc is None:
            messages.append("<p>Невозможно прочитать файлы!</p>")
            has_error = True
            continue

        doc.close()

        file_path = os.path.join(UPLOAD_PATH, filename)
        with open(file_path, 'wb') as f:
            f.write(content)

    

    if has_error:
        result_html = '<div class="result error">' + "".join(messages) + '</div>'
    else:
        num_files = process_all_pdfs(UPLOAD_PATH)
        with open(UPLOAD_PATH+'/upload_documents.txt', 'r') as f:
            user_document_text = f.read()
        user_chunks = chunk_text(
            text=user_document_text,
            chunk_size=1500,
            chunk_overlap=150,
            metadata={
                "source": "user_upload"
            }
        )
        print(f"\n\nПользовательские документы разбиты на {len(user_chunks)} чанков")
        for i, chunk in enumerate(user_chunks, 1):
            print(f"\n--- Чанк {i} (позиция {chunk.metadata.get('start_index', 'N/A')}) ---")
            print(f"Метаданные: {chunk.metadata}")
            print(f"Текст: {chunk.page_content[:100]}...")
        result_html = f'<div class="result success">Извлечен текст из {num_files} файлов в upload_documents.txt. Текст успешно разбит на чанки<p></p></div>'

    return HTMLResponse(content=HTML_PAGE.replace("{result_html}", result_html))