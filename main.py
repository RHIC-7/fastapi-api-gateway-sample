from fastapi import FastAPI

# FastAPI アプリケーションの初期化
app = FastAPI(
    docs_url="/sample/docs",  # ドキュメントのURLを変更
    openapi_url="/sample/openapi.json"
)


@app.get("/")
def read_root():
    """
    ルートエンドポイントの定義
    """
    return {"message": "Hello FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """
    アイテムエンドポイントの定義
    """
    return {"item_id": item_id, "query": q}
