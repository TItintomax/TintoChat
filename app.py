from fastapi import FastAPI
import TelaInicial
from TelaInicial import main
import micropip

async def install_packages():
    await micropip.install('anyio==3.7.1')
    # Outras instalações necessárias

install_packages()

app = FastAPI()

#modificando para UTF-8
@app.get("/")
def read_root():
    TelaInicial.ft.app(target=main, assets_dir="assets")