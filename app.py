from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    # Executar o script Flet como um processo separado
    subprocess.run(["python", "TelaInicial.py"])
    return {"message": "Flet app launched"}