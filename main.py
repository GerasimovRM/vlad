import uvicorn


if __name__ == "__main__":
    uvicorn.run("server.server:app", host="localhost", port=5000)
