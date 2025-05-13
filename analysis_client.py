import asyncio

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP

server = MCPServerHTTP(url="http://127.0.0.1:8000/sse")


agent = Agent('openai:gpt-4o-mini', mcp_servers=[server])

async def main():
    async with agent.run_mcp_servers():
        result = await agent.run('Multiply 42 times 42.')

        print(result.output)

if __name__ == "__main__":
    asyncio.run(main())