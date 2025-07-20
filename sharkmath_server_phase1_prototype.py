"""
SharkMath MCP Server - Phase 1 Prototype
Testing consolidated tools with FastMCP integration.
"""

from mcp.server.fastmcp import FastMCP
from convert_units_prototype import register_tools as register_convert_units

# Create MCP server
mcp = FastMCP("SharkMath Server - Phase 1 Prototype")

# Register consolidated tools
register_convert_units(mcp)

if __name__ == "__main__":
    import asyncio
    print("🚀 Starting SharkMath Phase 1 Prototype Server...")
    print("✅ Consolidated convert_units tool registered")
    print("📊 Supporting 42+ unit conversions across 7 categories")
    asyncio.run(mcp.run())
