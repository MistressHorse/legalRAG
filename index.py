HTML_PAGE = f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЮР ВЕБ</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .container {{
            background: #fff;
            padding: 30px 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            max-width: 500px;
            width: 100%;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 20px;
            color: #333;
            font-size: 1.4em;
        }}
        form {{
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        input[type="file"] {{
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
        }}
        button {{
            background-color: #4a90d9;
            color: #fff;
            border: none;
            padding: 12px;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }}
        button:hover {{
            background-color: #357abd;
        }}
        .result {{
            margin-top: 20px;
            padding: 15px;
            border-radius: 4px;
        }}
        .success {{
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }}
        .error {{
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }}
        .result p {{
            margin: 5px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Загрузка PDF файлов</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="files" multiple accept=".pdf" required>
            <button type="submit">Загрузить</button>
        </form>
        {{result_html}}
    </div>
</body>
</html>
'''