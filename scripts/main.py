import anyio
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage


async def main():
    async for message in query(
        prompt="Say 'Hello, World!'",
        options=ClaudeAgentOptions(max_turns=1),
    ):
        if isinstance(message, ResultMessage):
            print(message.result)


anyio.run(main)
