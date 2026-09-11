from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from tools import create_email, send_email


model = ChatOllama(
    model="qwen3:1.7b",
    temperature=0
)


agent = create_agent(
    model=model,
    tools=[
        create_email,
        send_email
    ],
    system_prompt="""
You are an email assistant.

You can create email drafts and send emails.

Use create_email when the user wants to prepare or draft
an email.

Never use send_email just because the user asks you to
draft or prepare an email.

Only use send_email when the user explicitly confirms
that the prepared email should be sent.

Do not pretend that an email was sent unless the
send_email tool was actually called.
"""
)