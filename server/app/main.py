from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api.v1.router import api_router

app = FastAPI(title="ai document intelligence Platform")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)


# @app.get("/api/v1/health")
# async def health_check(db: AsyncSession = Depends(get_db)):
#     result = await db.execute(text("SELECT 1"))

#     return {"database": result.scalar_one()}


app.include_router(api_router, prefix="/api/v1")
