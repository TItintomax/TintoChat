from fastapi import FastAPI
import TelaInicial
from TelaInicial import main


app = FastAPI()

#modificando para UTF-8
@app.get("/")
def read_root():
    TelaInicial.ft.app(target=main, assets_dir="assets")