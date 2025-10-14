from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool
def add(a: int, b: int) -> int:
    """将两个整数相加。"""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="http", port=9000)