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
    name="run_analysis",           # LLM 的自定义工具名称
    description="对信息搜集表进行分析，生成分析的脚本,支持rna_seq 转录组分析 和dna_seq 基因组分析类型。", # 自定义描述
    tags={"rna", "analysis"},      # 用于组织/过滤的可选标签
)
def run_analysis(
    xls_file: Annotated[str, "信息搜集表的路径"],
    analysis_type: Annotated[str, "分析类型，例如转录组分析rna_seq或基因组分析dna_seq"]
) -> str:
    """对信息搜集表进行分析。"""
    if analysis_type == "rna_seq":
        return f"python3 rna_seq_analysis.py {xls_file} "
    elif analysis_type == "dna_seq":
        return f"python3 dna_seq_analysis.py {xls_file} "
    else:
        return "不支持的分析类型"

if __name__ == "__main__":
    mcp.run(transport="http", port=9000)