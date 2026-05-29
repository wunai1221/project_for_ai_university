from collections import defaultdict

# 暫存在記憶體（之後可換 Redis）
session_store: dict[str, list[dict]] = defaultdict(list)

def get_history(session_id: str) -> list[dict]:
    return session_store[session_id]

def add_message(session_id: str, role: str, content: str):
    session_store[session_id].append({"role": role, "content": content})

def clear_session(session_id: str):
    session_store[session_id] = []