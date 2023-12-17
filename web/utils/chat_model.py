import json

import httpx

from web.config import MODEL_API_URL


async def get_model_answer(body: dict) -> dict | None:
    body = json.dumps(body, indent=4, ensure_ascii=False, default=str)

    async with httpx.AsyncClient() as client:
        res = await client.post(f"{MODEL_API_URL}/generate", json=body)

    if res.status_code != 200:
        return None

    return res.json()
