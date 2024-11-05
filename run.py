import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        reload=True,
        port=27017,
        app="main:app"
    )