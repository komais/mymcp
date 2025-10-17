from fastmcp import FastMCP
from typing import Annotated

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """向某人打招呼。  """
    return f"Hello, {name}!"


@mcp.tool(
    name="add",           # LLM 的自定义工具名称
    description="将两个整数相加。", # 自定义描述
    tags={"math", "add"},      # 用于组织/过滤的可选标签
)
def add(a: int, b: int) -> int:
    """将两个整数相加。"""
    return a + b

@mcp.tool(
    name="rna_seq_analysis",           # LLM 的自定义工具名称
    description="对信息搜集表进行分析，生成分析结果。", # 自定义描述
    tags={"rna", "analysis"},      # 用于组织/过滤的可选标签
)
def rna_seq_analysis(
    xls_file: Annotated[str, "信息搜集表的路径"]
) -> str:
    """对信息搜集表进行分析。"""
    return f"python3 rna_seq_analysis.py {xls_file}"


if __name__ == "__main__":
    mcp.run(transport="http", port=9000)