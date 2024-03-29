import uvicorn
from main import app

if __name__ == "__start__":
    uvicorn.run(app, host="0.0.0.0", port=8181)
