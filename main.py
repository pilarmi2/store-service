from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn

from src.routers import municipalities

app = FastAPI()
app.include_router(municipalities.router)


@app.get("/", include_in_schema=False, response_class=RedirectResponse)
async def api_spec():
    return "/docs"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
