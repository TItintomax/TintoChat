import micropip
import TelaInicial
from TelaInicial import main
import flet as ft

async def install_packages():
    await micropip.install("ssl")
if __name__ == "__main__":
    # Chame as funções diretamente
    install_packages()
    TelaInicial.ft.app(target=main, assets_dir="assets")
