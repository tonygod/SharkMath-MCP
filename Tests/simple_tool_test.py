#!/usr/bin/env python3
"""
Simple FastMCP Tool Count Test
"""

import sys
import os

# Add SharkMath directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.fastmcp import FastMCP
import arithmetic

def simple_tool_test():
    """Simple test to count registered tools"""
    
    print("Simple FastMCP Tool Count Test")
    print("="*40)
    
    # Create MCP server instance
    mcp = FastMCP("Test Server")
    
    print("Before registration:")
    try:
        tools = mcp.list_tools()
        print(f"  Tools count: {len(tools)}")
    except Exception as e:
        print(f"  list_tools() error: {e}")
    
    print("\nRegistering arithmetic tools...")
    arithmetic.register_tools(mcp)
    
    print("After registration:")
    try:
        tools = mcp.list_tools()
        print(f"  Tools count: {len(tools)}")
        print(f"  Tools type: {type(tools)}")
    except Exception as e:
        print(f"  list_tools() error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    simple_tool_test()
