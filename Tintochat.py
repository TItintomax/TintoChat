import micropip
import TelaInicial
from TelaInicial import main
import flet as ft
if __name__ == "__main__":
    # Chame as funções diretamente
    async def install_packages():
        await micropip.install("ssl")

    TelaInicial.ft.app(target=main, assets_dir="assets")
