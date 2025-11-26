from strands import Agent
from strands.models.ollama import OllamaModel

# 1.Agent
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="gemma3:1b",
)

agent = Agent(model=ollama_model)

response = agent("Tell me about planet jupiter in 50 words.")

print(response)

# Access metrics through the AgentResult
print(f"Total tokens: {response.metrics.accumulated_usage['totalTokens']}")
print(f"Execution time: {sum(response.metrics.cycle_durations):.2f} seconds")



