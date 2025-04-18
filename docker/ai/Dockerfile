FROM python:3.11.11-bookworm

WORKDIR /ai

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Poetryをダウンロードしてインストール
RUN curl -sSL https://install.python-poetry.org | python -

# Pathを通す
ENV PATH /root/.local/bin:$PATH
# 仮想環境をたてない
RUN poetry config virtualenvs.create false

# アプリケーションの依存関係をインストール
COPY ./apps/ai/pyproject.toml ./apps/ai/poetry.lock .
RUN poetry install --no-root

COPY ./apps/ai .

CMD ["bash", "-c", "streamlit run main.py"]
