import httpx
from config import get_settings

settings = get_settings()


async def chat_with_model(
    messages: list[dict],
    temperature: float = 0.7,
    max_tokens: int = 512,
) -> str:
    """
    呼叫本地 Ollama 模型。
    messages 格式：[{"role": "user", "content": "..."}]
    """
    payload = {
        "model": settings.model_name,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
        },
    }

    async with httpx.AsyncClient(timeout=300.0) as client:
        try:
            response = await client.post(
                f"{settings.model_base_url}/api/chat",
                json=payload,
            )
            response.raise_for_status()
            data = response.json()
            return data["message"]["content"]

        except httpx.TimeoutException:
            raise RuntimeError("模型回應逾時，請稍後再試")

        except httpx.HTTPStatusError as e:
            raise RuntimeError(
                f"模型服務異常：{e.response.status_code}，回應內容：{e.response.text}"
            )

        except KeyError:
            raise RuntimeError("模型回傳格式異常")