from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig # type: ignore
import os
import chainlit as cl
from openai.types.responses import ResponseTextDeltaEvent
load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client

)

config = RunConfig(
    model=model,
    model_provider= external_client, # type: ignore
    tracing_disabled=True
)

agent = Agent(
    name= "Assistant ",
    instructions="You are a helpful assistant",
    model= model
)

   
@cl.on_chat_start
async def handle_start_chat():
    cl.user_session.set("history" ,[])
    await cl.Message(content="Hello! How can i help you ").send()
    

@cl.on_message
async def on_message(message: cl.Message):
    history = cl.user_session.get("history")
    msg = cl.Message(content="")
    await msg.send()
    
    history.append({"role":"user", "content":message.content}) # type: ignore
   
    
    result = Runner.run_streamed(
        agent ,
        input= history, # type: ignore
        run_config= config
    )
  
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)
            
    history.append({"role":"assistant" ,"content":result.final_output})# type: ignore
    
  
    cl.user_session.set("history", history)
    # await cl.Message(content = result.final_output).send()