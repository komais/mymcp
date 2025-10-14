from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """向某人打招呼。"""
    return f"Hello, {name}!"


@mcp.tool(
    name="add",           # LLM 的自定义工具名称
    description="将两个整数相加。", # 自定义描述
    tags={"math", "add"},      # 用于组织/过滤的可选标签
)
def add(a: int, b: int) -> int:
    """将两个整数相加。"""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="http", port=9000)