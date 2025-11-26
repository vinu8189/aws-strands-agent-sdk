# Project 1 — Basic Strands + Ollama Agent

This project is a minimal example showing how to run a **Strands Agent** using a **local Ollama model**. It focuses on the essential workflow:

* Creating a Python virtual environment
* Installing the Strands Agent SDK
* Using an existing Ollama model
* Running an agent prompt and viewing metrics

**Note:** This project uses a *fully local* model (via Ollama).
No cloud API keys, internet access, or external model providers are required.

---

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate        # Windows
```

### 2. Install dependencies

```bash
pip install strands-agents ollama
```

### 3. Verify your local Ollama model

Ollama is already installed on your system.
To check available models:

```bash
ollama list
```

Pick a model name (e.g., `gemma3:1b`) and use it in your agent code:

```python
model_id="gemma3:1b"
host="http://localhost:11434"
```

**Prerequisite:** Ollama must be running locally with at least one model installed.

---

## Run the Agent

From the project folder:

```bash
python3 agent.py
```

You’ll see:

* The model response
* Total tokens consumed
* Execution duration

---

## Documentation

Official Strands documentation:
[https://strandsagents.com/latest/documentation/docs/](https://strandsagents.com/latest/documentation/docs/)

---

## Notes

* `.venv` is ignored and should not be committed
* Runs entirely offline
* Useful as a starter template before adding tools, reasoning loops, or observability


