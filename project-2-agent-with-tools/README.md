# Project 2 — Strands Agent With Tool Support (Ollama + Qwen 2.5 0.5B)

This project demonstrates how to build a **tool-enabled AI agent** using the **Strands Agent SDK** with a **local model running on Ollama**.
It expands on Project 1 by adding *action-taking abilities* using native tool/function-calling.

To keep it lightweight and fast, this project uses:

```bash
qwen2.5:0.5b
```

Surprisingly, this tiny model supports function-calling well enough for Strands tools, making it ideal for local experimentation.

---

## 🚀 Features Demonstrated

* Integrating **Strands tools** (calculator tool)
* Using a **tool-capable local model** (Qwen2.5 0.5B)
* Automatic tool selection (`Agent` decides when to call calculator)
* Execution metrics:

  * token usage
  * reasoning cycles
  * tool call metadata
  * execution time
* Fully offline, local-first workflow (no cloud APIs)

---

## 📦 Setup Instructions

### 1. Create and activate your virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows
```

### 2. Install dependencies

```bash
pip install strands-agents strands-tools ollama
```

### 3. Verify your local Ollama model

Ollama is already installed on your system.
To check available models:

```bash
ollama list
```

Pick a model name (e.g., `gemma3:1b`) and use it in your agent code:

```python
model_id="qwen2.5:0.5b"
host="http://localhost:11434"
```

**Prerequisite:** Ollama must be running locally with at least one model installed.

---

## 📊 What to Observe

* The agent uses **calculator tool** automatically.
* `response.metrics.tool_metrics` contains:

  * tool name
  * arguments passed
  * time taken
  * success/failure

Example:

```
Tools used: ['calculator']
```

This confirms the model made a structured tool call.

---

## 📁 Folder Structure

```
project2-agent-with-tools/
├── agent.py
├── README.md
├── .gitignore
└── .venv/   (not committed)
```

---

## 🌟 Notes

* `qwen2.5:0.5b` is one of the **smallest models in Ollama that supports native tool calling**.
* This project is a foundation for:

  * Adding multiple tools
  * Autonomous multi-step reasoning
  * Custom tools
  * Tool execution monitoring
  * Observability (coming in later projects)

---

## 📚 Reference

Strands Documentation:
[https://strandsagents.com/latest/documentation/docs/](https://strandsagents.com/latest/documentation/docs/)


