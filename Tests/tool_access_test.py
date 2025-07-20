#!/usr/bin/env python3
"""
FastMCP Tool Access - Understanding how to count registered tools
"""

import sys
import os

# Add SharkMath directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.fastmcp import FastMCP
import arithmetic

def test_fastmcp_tools():
    """Test how to access registered tools in FastMCP"""
    
    print("FastMCP Tool Access Test")
    print("="*50)
    
    # Create MCP server instance
    mcp = FastMCP("Test Server")
    
    print("Available methods on FastMCP:")
    methods = [attr for attr in dir(mcp) if not attr.startswith('_') and callable(getattr(mcp, attr))]
    for method in sorted(methods):
        print(f"  • {method}()")
    
    print(f"\n{'='*50}")
    print("Before tool registration:")
    
    # Try using list_tools method
    try:
        tools_before = mcp.list_tools()
        print(f"list_tools() result: {tools_before}")
        print(f"Number of tools: {len(tools_before)}")
    except Exception as e:
        print(f"list_tools() failed: {e}")
    
    print(f"\n{'='*50}")
    print("Registering arithmetic tools...")
    
    # Register tools
    arithmetic.register_tools(mcp)
    print("Tools registered successfully")
    
    print(f"\n{'='*50}")
    print("After tool registration:")
    
    # Try using list_tools method again
    try:
        tools_after = mcp.list_tools()
        print(f"list_tools() result: {tools_after}")
        print(f"Number of tools: {len(tools_after)}")
        
        if hasattr(tools_after, 'tools'):
            print(f"tools_after.tools: {tools_after.tools}")
        
        # Try to access individual tools
        print(f"Type of tools_after: {type(tools_after)}")
        
        # If it's a list or similar, iterate through it
        if hasattr(tools_after, '__iter__'):
            print("Iterating through tools:")
            for i, tool in enumerate(tools_after):
                print(f"  Tool {i}: {tool}")
                if hasattr(tool, 'name'):
                    print(f"    Name: {tool.name}")
                
    except Exception as e:
        print(f"list_tools() failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_fastmcp_tools()
