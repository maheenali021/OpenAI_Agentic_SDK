## Chatbot Assistant with Gemini AI

This project implements a streaming chatbot assistant using Gemini AI (via OpenAI-compatible API) and Chainlit for the interactive UI. The assistant maintains conversation history and streams responses in real-time.

**Features**

✅ Gemini AI Integration – Uses gemini-2.0-flash via OpenAI-compatible API.

✅ Real-Time Streaming – Responses are streamed token-by-token for a smooth chat experience.

✅ Conversation Memory – Maintains chat history for context-aware replies.

✅ Chainlit UI – Simple and interactive web-based chat interface.

**Code Overview**

**Key Components**

1. Gemini AI Client (AsyncOpenAI)

. Connects to Gemini’s OpenAI-compatible API.

. Uses gemini-2.0-flash for fast responses.

2. Agent & Runner

. Agent: Defines the assistant’s behavior ("You are a helpful assistant").

. Runner: Handles execution and streaming.

3. Chainlit Handlers

. ***@cl.on_chat_start***: Initializes chat history.

. ***@cl.on_message***: Processes user input, streams responses, and updates history.

4. Conversation Memory

Maintains history as a list of ***{"role": "user/assistant", "content": "..."}.***

**How It Works**

. User sends a message → appended to history.

. Runner.run_streamed() sends the query to Gemini.

. Responses are streamed in real-time via msg.stream_token().

. Final output is saved in history for context.
