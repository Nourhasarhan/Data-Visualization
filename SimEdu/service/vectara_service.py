import httpx, requests
from fastapi import HTTPException,UploadFile
from typing import Dict, Any
from SimEdu.config import BASE_URL, API_KEY, CORPUS_KEY

async def query_vectara(query: str) -> Dict[str, Any]:
    url = "https://api.vectara.io/v2/query"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': API_KEY
    }
    payload = {
        "query": query,
        "search": {
            "corpora": [{"corpus_key": CORPUS_KEY}],
            "limit": 5
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()

async def upload_doc(file: UploadFile) -> Dict[str, Any]:
    url = f"{BASE_URL}/{CORPUS_KEY}/upload_file"
    headers = {'Accept': 'application/json', 'x-api-key': API_KEY}
    files = {'file': (file.filename, file.file, file.content_type)}

    response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()

async def list_docs() -> Dict[str, Any]:
    url = f"{BASE_URL}/{CORPUS_KEY}/documents"
    headers = {'Accept': 'application/json', 'x-api-key': API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

    return response.json()

async def delete_doc(document_id: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{CORPUS_KEY}/documents/{document_id}"
    headers = {'Accept': 'application/json', 'x-api-key': API_KEY}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()

        if response.status_code in [200, 204]:
            return {"message": "Item has been deleted successfully"}
        else:
            raise HTTPException(status_code=response.status_code, detail="Unexpected response status")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
