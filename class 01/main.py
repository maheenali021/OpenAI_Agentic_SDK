from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig #type:ignore
load_dotenv()
 
gemini_api_key = os.getenv("GEMINI_API_KEYS")
external_client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
     model= "gemini-2.0-flash",
     openai_client= external_client   
 )
config = RunConfig(
    model= model,
    tracing_disabled=True,
    model_provider= external_client # type: ignore
)

agent = Agent(
    name= "Assistant",
    instructions=" You are a helpful assiatnat",
    model= model
)

output = Runner.run_sync(
    agent,
    input= "who is the prime minister of Pakistan?",
    run_config=config
)

print(output.final_output)