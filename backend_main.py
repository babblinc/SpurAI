import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BING_API_KEY = os.getenv("BING_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
BING_SEARCH_URL = "https://api.bing.microsoft.com/v7.0/search"

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    history: list

@app.post("/chat")
def chat(req: ChatRequest):
    """
    Sends user message and chat history to OpenAI and gets a response.
    If the message contains 'search:', does a web search and includes results in prompt.
    """
    user_message = req.message
    history = req.history or []

    # Web search if user types: search: <query>
    if user_message.lower().startswith("search:"):
        query = user_message[len("search:"):].strip()
        web_results = bing_web_search(query)
        system_prompt = f"You are ChatGPT with live web browsing. Use this info to answer:\n\n{web_results}"
        messages = [{"role": "system", "content": system_prompt}]
        messages += [{"role": m["role"], "content": m["content"]} for m in history]
        messages.append({"role": "user", "content": user_message})
    else:
        messages = [{"role": m["role"], "content": m["content"]} for m in history]
        messages.append({"role": "user", "content": user_message})

    response = openai_chat(messages)
    return {"response": response}

def openai_chat(messages):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-4o",
        "messages": messages,
        "max_tokens": 500,
    }
    r = requests.post(OPENAI_API_URL, headers=headers, json=payload)
    try:
        return r.json()["choices"][0]["message"]["content"]
    except Exception:
        return "Sorry, something went wrong with the AI service."

def bing_web_search(query):
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    r = requests.get(BING_SEARCH_URL, headers=headers, params=params)
    try:
        results = r.json()["webPages"]["value"]
        snippets = "\n\n".join([f"{item['name']}\n{item['snippet']}\n{item['url']}" for item in results[:3]])
        return f"Web search results for '{query}':\n{snippets}"
    except Exception:
        return "Web search failed or no results."

@app.get("/")
def root():
    return {"msg": "Chatbot backend is running"}