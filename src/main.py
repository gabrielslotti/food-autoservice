import uvicorn
from entrypoints.api.main import app  # noqa

if __name__ == '__main__':
    uvicorn.run("entrypoints.api.main:app", host="0.0.0.0", port=8000, reload=True)
