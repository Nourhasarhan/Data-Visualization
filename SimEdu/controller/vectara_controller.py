from fastapi import APIRouter, Query, UploadFile, File, HTTPException
from typing import Dict, Any
from SimEdu.service.vectara_service import query_vectara, upload_doc, list_docs, delete_doc

vectara_router = APIRouter()

@vectara_router.post("/query")
async def vectara_query(query: str = Query(...)):
    result = await query_vectara(query)
    return result

@vectara_router.post("/upload")
async def upload(file: UploadFile = File(...)):
    result = await upload_doc(file)
    return result

@vectara_router.get("/list", response_model=Dict[str, Any])
async def list_documents():
    return await list_docs()

@vectara_router.delete("/corpora/documents/{document_id}")
async def delete_document(document_id: str):
    result = await delete_doc(document_id)
    return result
