from fastmcp import FastMCP
import datetime

mcp = FastMCP("TimeServer")

@mcp.tool()
def get_current_time() -> str:
    """Returns the current server time."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    mcp.run()
