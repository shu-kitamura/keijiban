# Pythonの公式イメージをベースにする
FROM python:3.13.2

# 作業ディレクトリ
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# uvicornでFastAPIを起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]