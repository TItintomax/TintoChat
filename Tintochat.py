import micropip
import TelaInicial
from TelaInicial import main
import flet as ft
import asyncio

async def install_packages():
    await micropip.install("ssl")

async def main_async():
    await install_packages()
    # Inicialize sua aplicação aqui
    TelaInicial.ft.app(target=main, assets_dir="assets")

# Executar o main_async em um loop de eventos
asyncio.run(main_async())
