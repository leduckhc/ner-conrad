import spacy
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

model = spacy.load(Path("pretrained_models/en_conrad_ner"))

class NerRequest(BaseModel):
    text: str

class NerEntity(BaseModel):
    text: str
    label: str
    start_char: int
    end_char: int

class NerResponse(BaseModel):
    entities: List[NerEntity]

@app.post("/ner")
async def ner(req: NerRequest) -> NerResponse:
    doc = model(req.text)
    entities = []
    for ent in doc.ents:
        entities.append(
            NerEntity(text=ent.text, label=ent.label_, start_char=ent.start_char, end_char=ent.end_char)
        )
    return NerResponse(entities=entities)

