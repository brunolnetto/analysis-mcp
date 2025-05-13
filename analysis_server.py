from mcp.server.fastmcp import FastMCP, Context
import math

mcp = FastMCP("Hello World")

@mcp.tool()
async def add(a: int, b: int, ctx: Context) -> int:
    await ctx.info(f"Tool 'add' called with arguments: a={a}, b={b}")
    return a + b

@mcp.tool()
async def subtract(a: int, b: int, ctx: Context) -> int:
    await ctx.info(f"Tool 'subtract' called with arguments: a={a}, b={b}")
    return a - b

@mcp.tool()
async def multiply(a: int, b: int, ctx: Context) -> int:
    await ctx.info(f"Tool 'multiply' called with arguments: a={a}, b={b}")
    return a * b

@mcp.tool()
async def divide(a: int, b: int, ctx: Context) -> float:
    await ctx.info(f"Tool 'divide' called with arguments: a={a}, b={b}")
    return a / b

@mcp.tool()
async def power(a: int, b: int, ctx: Context) -> int:
    await ctx.info(f"Tool 'power' called with arguments: a={a}, b={b}")
    return a ** b

@mcp.tool()
async def sqrt(a: int, ctx: Context) -> float:
    await ctx.info(f"Tool 'sqrt' called with argument: a={a}")
    return math.sqrt(a)

@mcp.tool()
async def cbrt(a: int, ctx: Context) -> float:
    await ctx.info(f"Tool 'cbrt' called with argument: a={a}")
    return a ** (1/3)

@mcp.tool()
async def factorial(a: int, ctx: Context) -> int:
    await ctx.info(f"Tool 'factorial' called with argument: a={a}")
    return math.factorial(a)

@mcp.tool()
async def log(a: int, ctx: Context) -> float:
    await ctx.info(f"Tool 'log' called with argument: a={a}")
    return math.log(a)

@mcp.tool()
async def remainder(a: int, b: int, ctx: Context) -> int:
    await ctx.info(f"Tool 'remainder' called with arguments: a={a}, b={b}")
    return a % b

@mcp.tool()
async def sin(a: int, ctx: Context) -> float:
    await ctx.info(f"Tool 'sin' called with argument: a={a}")
    return math.sin(a)

@mcp.tool()
async def cos(a: int, ctx: Context) -> float:
    await ctx.info(f"Tool 'cos' called with argument: a={a}")
    return math.cos(a)

@mcp.tool()
async def tan(a: int, ctx: Context) -> float:
    await ctx.info(f"Tool 'tan' called with argument: a={a}")
    return math.tan(a)

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="sse")
