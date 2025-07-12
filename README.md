# Simple AI Chatbot (with Web Search)

This project gives you an AI chatbot (like ChatGPT) that can answer questions and search the web!

## Features

- Chat with AI (powered by OpenAI GPT)
- Search the web: Type `search: your question`
- Simple chat UI

## Prerequisites

- [Python 3.8+](https://www.python.org/)
- [Node.js + npm](https://nodejs.org/)
- OpenAI API key ([get yours](https://platform.openai.com/account/api-keys))
- Bing Search API key ([get one free here](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api))

## Setup Steps

### 1. Clone/download this repo

### 2. Backend setup

```bash
cd chatbot-ai/backend
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Set your API keys (replace YOUR_KEY with actual keys):

```bash
export OPENAI_API_KEY=YOUR_OPENAI_API_KEY
export BING_API_KEY=YOUR_BING_SEARCH_API_KEY
```
On Windows, use `set` instead of `export`.

Run the backend:
```bash
uvicorn main:app --reload
```

### 3. Frontend setup

```bash
cd ../frontend
npm install
npm start
```

Visit [http://localhost:3000](http://localhost:3000) in your browser.

---

## Usage

- Type messages and chat!
- To search the web, type: `search: what is the weather today in London?`

---

## FAQ

- **I get errors about API keys.**  
  Make sure you set your OpenAI and Bing Search keys in your terminal before running the backend.

- **Can I deploy this online?**  
  Yes! You can use [Vercel](https://vercel.com/) or [Netlify](https://www.netlify.com/) for frontend, and [Render](https://render.com/) or [Railway](https://railway.app/) for backend.

---

## Want more features?

Ask and I’ll help you add them, no coding skills needed!