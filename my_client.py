import asyncio
from fastmcp import Client

async def main():
    try:
        # 使用正确的服务器地址
        # 如果客户端和服务器在同一台机器上，使用127.0.0.1
        # 如果客户端和服务器在不同机器上，使用服务器的实际IP地址
        client = Client("https://lexical-ivory-whippet.fastmcp.app/mcp")
        #client = Client("http://127.0.0.1:9000/mcp")
        
        print("Attempting to connect to MCP server...")
        async with client:
            print("Connected successfully!")
            result = await client.call_tool("greet", {"name": "Ford"})
            print(f"Tool call result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())

    