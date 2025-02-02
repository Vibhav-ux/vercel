from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data
with open("q-vercel-python.json", "r") as file:  
    marks_list = json.load(file)

# Convert list to a dictionary for fast lookup
marks_data = {entry["name"]: entry for entry in marks_list}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    """
    Get student marks by name. If no name is provided, return an empty list.
    """
    result = [marks_data.get(n, {"name": n, "marks": None}) for n in name]
    return {"marks": result}
