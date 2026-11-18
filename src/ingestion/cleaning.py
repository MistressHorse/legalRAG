import os
import pymupdf


def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    try:
        doc = pymupdf.open(file_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")

    return text


def process_all_pdfs(upload_dir: str, output_filename: str = "upload_documents.txt"):
    output_path = os.path.join(upload_dir, output_filename)
    pdf_files = [f for f in os.listdir(upload_dir) if f.lower().endswith('.pdf')]

    all_text = []

    for pdf_file in pdf_files:
        file_path = os.path.join(upload_dir, pdf_file)
        text = extract_text_from_pdf(file_path)

        if text.strip():
            all_text.append(f"Файл: {pdf_file}\n")
            all_text.append(f"{'='*60}\n")
            all_text.append(text)
            all_text.append("\n")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("".join(all_text))

    for filename in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(".pdf"):
            try:
                os.remove(file_path)
                print(f"Удален файл: {file_path}")
            except Exception as e:
                print(f"Не удалось удалить {file_path}: {e}")
    return len(pdf_files)
