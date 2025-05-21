import asyncio
import pytest
from fastmcp import Client
from time_server import mcp
from datetime import datetime

@pytest.mark.asyncio
async def test_get_current_time():
    async with Client(mcp) as client:
        # call_tool returns a list of ContentBlock objects (e.g., TextContent)
        results = await client.call_tool("get_current_time")
        # We expect a single result for this tool
        assert len(results) == 1
        content_block = results[0] # This should be a TextContent object
        
        # Access the 'text' attribute of the ContentBlock
        time_string = content_block.text 
        assert isinstance(time_string, str)
        try:
            datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pytest.fail(f"Time string '{time_string}' does not match format '%Y-%m-%d %H:%M:%S'")
