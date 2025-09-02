from fastmcp import FastMCP

mcp = FastMCP("SoporteIA")

@mcp.tool()
def sumar(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
