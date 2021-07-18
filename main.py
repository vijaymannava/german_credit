import uvicorn
from scipy.sparse import issparse
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict
from datetime import datetime, timezone

app = FastAPI(
    title="German Credit",
    docs_url="/"
)
@app.get("/")
def read_root():
    return {"German credit"}


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8888, reload=True)
