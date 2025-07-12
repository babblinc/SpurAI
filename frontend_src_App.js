import React, { useState } from "react";

const API_URL = "http://localhost:8000/chat";

function App() {
  const [input, setInput] = useState("");
  const [history, setHistory] = useState([]);
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input) return;
    setLoading(true);
    const newHistory = [...history, { role: "user", content: input }];
    setHistory(newHistory);

    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input, history: newHistory }),
    });
    const data = await res.json();
    setHistory([...newHistory, { role: "assistant", content: data.response }]);
    setResponse(data.response);
    setInput("");
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h2>AI Chatbot (ChatGPT + Web)</h2>
      <div
        style={{
          border: "1px solid #ddd",
          borderRadius: 8,
          padding: 16,
          minHeight: 300,
          marginBottom: 16,
          background: "#fafbfc",
        }}
      >
        {history.map((item, idx) => (
          <div
            key={idx}
            style={{
              textAlign: item.role === "user" ? "right" : "left",
              margin: "12px 0",
              color: item.role === "assistant" ? "#222" : "#0078d4",
            }}
          >
            <b>{item.role === "user" ? "You" : "AI"}: </b>
            {item.content}
          </div>
        ))}
        {loading && <div>Thinking...</div>}
      </div>
      <input
        style={{ width: "80%", padding: 12, fontSize: 16 }}
        placeholder="Type your message..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        disabled={loading}
      />
      <button
        style={{ padding: "12px 20px", marginLeft: 8 }}
        onClick={sendMessage}
        disabled={loading}
      >
        Send
      </button>
      <div style={{ marginTop: 16, fontSize: 14, color: "#888" }}>
        Type <b>search: your question</b> to browse the web!
      </div>
    </div>
  );
}

export default App;