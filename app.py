from fastapi import FastAPI
import TelaInicial
from TelaInicial import main
import flet as ft

app = FastAPI()


@app.get("/")
def read_root():
    TelaInicial.ft.app(target=main, assets_dir="assets")