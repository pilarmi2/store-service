from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn

from src.routers import municipalities, income_statement, loans_statement, score

app = FastAPI()
app.include_router(municipalities.router)
app.include_router(income_statement.router)
app.include_router(loans_statement.router)
app.include_router(score.router)


@app.get("/", include_in_schema=False, response_class=RedirectResponse)
async def api_spec():
    return "/docs"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
