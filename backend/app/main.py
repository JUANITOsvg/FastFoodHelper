import requests
from flask import Flask, jsonify, request
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import asyncio

app = Flask(__name__)
MCP_URL = "http://mcp:8000/mcp/"

async def call_sum_tool(a: int, b: int):
    async with streamablehttp_client(url=MCP_URL) as (reader, writer, _):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            tools = await session.list_tools()
            # asumo que "sumar" está disponible
            result = await session.call_tool("sumar", {"a": a, "b": b})
            return result

@app.route("/sumar", methods=["GET"])
def sumar_route():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = asyncio.run(call_sum_tool(a, b))
    return jsonify({"resultado": result.content[0].text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
