import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        reload=True,
        port=3000,
        app="main:app"
    )