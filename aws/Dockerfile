# ベースは AWS Lambda の Python 3.12 コンテナランタイム
FROM public.ecr.aws/lambda/python:3.12

# Lambda Web Adapter を拡張として追加
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.3 /lambda-adapter /opt/extensions/lambda-adapter

# 依存インストール
RUN pip install --no-cache-dir fastapi uvicorn

# アプリ配置
WORKDIR /var/task
COPY main.py ./

# Web アダプタと Uvicorn のポートを合わせる
ENV PORT=8000
ENV AWS_LWA_PORT=8000
ENV AWS_LWA_LOG_LEVEL=info
# 圧縮を有効化する場合（任意）
# ENV AWS_LWA_ENABLE_COMPRESSION=true

# コンテナ起動時に Uvicorn を立ち上げる
# Lambda Web Adapter が 127.0.0.1:$PORT に来たリクエストを転送してくれる
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
