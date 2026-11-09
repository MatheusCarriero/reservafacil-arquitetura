from fastapi import FastAPI

app = FastAPI(
    title="ReservaFácil",
    description="API para gerenciamento de reservas de salas.",
    version="0.1.0",
)


@app.get("/health", tags=["Infraestrutura"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
