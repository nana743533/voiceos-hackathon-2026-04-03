from datetime import datetime

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-server")


@mcp.tool()
def get_current_time() -> str:
    """現在の時刻を返す"""
    return datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")


if __name__ == "__main__":
    mcp.run(transport="stdio")
