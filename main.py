from fastapi import APIRouter, FastAPI

API_GATEWAY_STAGE = "dev"
API_GATEWAY_RESOURCE = "api"
APPLICATION_ROOT = "sample"
ROOT_PASS = f"/{API_GATEWAY_STAGE}/{API_GATEWAY_RESOURCE}/{APPLICATION_ROOT}"

# FastAPI アプリケーションの初期化
app = FastAPI(
    docs_url=f"{ROOT_PASS}/docs",
    openapi_url=f"{ROOT_PASS}/openapi.json"
)

router = APIRouter(prefix=ROOT_PASS)


@router.get("/")
def read_root():
    """ルートエンドポイント"""
    return {"message": "Hello FastAPI!", "basePath": ROOT_PASS}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """アイテムエンドポイント"""
    return {"item_id": item_id, "query": q}


# ヘルスチェック
@router.get("/healthz")
def health():
    return {"status": "ok"}


app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    # Lambda Web Adapter でもローカル実行でも動くように 0.0.0.0:8000 で公開
    uvicorn.run(app, host="0.0.0.0", port=8000)
