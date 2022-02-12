from fastapi import FastAPI

from .api import router


app = FastAPI(
    title="Employee information",
    description="Веб-сервис информации о сотрудниках компании",
    version="1.0",
)


app.include_router(router)
