import json

import aiohttp

from web.config import MODEL_API_URL


async def get_model_answer(body: dict) -> dict | None:
    body = json.loads(json.dumps(body, default=str, ensure_ascii=False))

    async with aiohttp.ClientSession() as session:
        res = await session.post(f"{MODEL_API_URL}/generate", json=body)

    if res.status != 200:
        return None

    return await res.json()
