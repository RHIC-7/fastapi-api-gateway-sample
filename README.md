# FastAPI Sample with uv & AWS Lambda Web Adapter

このリポジトリは **FastAPI** を **uv (Astral)** で依存管理し、
**AWS Lambda Web Adapter** を利用してコンテナデプロイ可能にしたサンプルです。

---

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/your-org/fast-api-wagger-sample.git
cd fast-api-wagger-sample
```

### 2. 仮想環境の作成と有効化

```bash
uv venv .venv
source .venv/bin/activate
```

### 3. 依存関係のインストール

```bash
uv sync
```

FastAPI と Uvicorn は `pyproject.toml` に記載済みです。
新しいライブラリを追加する場合は:

```bash
uv add requests
```

---

## ローカル開発

### サーバー起動

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 動作確認

* API: [http://127.0.0.1:8000/dev/sample](http://127.0.0.1:8000/dev/sample)
* Swagger UI: [http://127.0.0.1:8000/dev/sample/docs](http://127.0.0.1:8000/dev/sample/docs)
* OpenAPI Spec: [http://127.0.0.1:8000/dev/sample/openapi.json](http://127.0.0.1:8000/dev/sample/openapi.json)

---

## コンテナ実行

### イメージビルド

```bash
docker build -f ./aws/Dockerfile -t fastapi-sample .
```

### ローカル起動

```bash
docker run -it --rm -p 8000:8000 fastapi-sample
```

---

## AWS Lambda デプロイ

### 1. ECR リポジトリ作成

```bash
aws ecr create-repository --repository-name fastapi-sample
```

### 2. イメージ push

```bash
docker build -t fastapi-sample .
docker tag fastapi-sample:latest <your_account_id>.dkr.ecr.<region>.amazonaws.com/fastapi-sample:latest
docker push <your_account_id>.dkr.ecr.<region>.amazonaws.com/fastapi-sample:latest
```

### 3. Lambda 関数作成

* ランタイム: **コンテナイメージ**
* イメージURI: 上記で push したものを指定

### 4. API Gateway 連携

* API Gateway (HTTP API) を作成し、Lambda に統合
* ステージ名と `APPLICATION_ROOT` は `main.py` の設定と合わせる

---

## 環境変数

| 変数名                 | デフォルト    | 説明                         |
| ------------------- | -------- | -------------------------- |
| `API_GATEWAY_RESOURCE`  | `api` | API Gateway リソース名             |
| `API_GATEWAY_STAGE` | `dev`    | API Gateway ステージ名          |
| `APPLICATION_ROOT`  | `sample` | アプリケーションのルートパス             |
| `PORT`              | `8000`   | Web Adapter が listen するポート |

---

## 開発用コマンド一覧

```bash
# 新しい依存を追加
uv add <package>

# 開発用依存を追加
uv add --dev pylint pytest

# Lint チェック
uv run pylint main.py

# テスト実行
uv run pytest
```

---

## 参考リンク

* [FastAPI 公式](https://fastapi.tiangolo.com/)
* [uv (Astral) ドキュメント](https://docs.astral.sh/uv/)
* [AWS Lambda Web Adapter](https://github.com/awslabs/aws-lambda-web-adapter)

