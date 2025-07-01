import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
import os

# Get the OpenRouter API key from environment variables
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
# Initialize the AsyncOpenAI client with OpenRouter configuration
client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)
# Disable tracing to prevent unnecessary logging
set_tracing_disabled(disabled=True)

async def main():
   # Create an agent instance with specific configuration
    agent = Agent(
        name="Assistant",
        instructions="You a python assistant.",
        model=OpenAIChatCompletionsModel(model="openrouter/cypher-alpha:free", openai_client=client),
    )
    # Run the agent with a query and get the result
    result = await Runner.run(
        agent,
        "what is an OOP",
    )
    # Print the final output from the agent
    print(result.final_output)
if __name__ == "__main__":
    ## Run the main async function
    asyncio.run(main())
     