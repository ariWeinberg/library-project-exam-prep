import os
from fastapi import FastAPI
import uvicorn
from routes.book_routes import router as book_router
from routes.member_routes import router as member_router
from routes.report_routes import router as report_router


host = os.environ.get("LIBRARY_APP_HOST", "0.0.0.0")
port = os.environ.get("LIBRARY_APP_PORT", 80)

app = FastAPI()

app.include_router(book_router, prefix="/books")
app.include_router(member_router, prefix="/members")
app.include_router(report_router, prefix="/reports")



if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)