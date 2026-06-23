from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Logistique en cours de route mon caporal"}
