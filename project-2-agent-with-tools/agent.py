from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator


# Agent Model selection
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen2.5:0.5b", #This model is capable of tool use
)

# Create agent with BOTH model and tools
agent = Agent(
    model=ollama_model,
    tools=[calculator]
)

# Agent will automatically determine when to use the calculator tool
response = agent("What is (5 + 3) * 7 ?")

print(response)


# Access metrics through the AgentResult
print(f"Total tokens: {response.metrics.accumulated_usage['totalTokens']}")
print(f"Execution time: {sum(response.metrics.cycle_durations):.2f} seconds")
print(f"Tools used: {list(response.metrics.tool_metrics.keys())}")