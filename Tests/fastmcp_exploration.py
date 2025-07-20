#!/usr/bin/env python3
"""
FastMCP API Exploration - Understanding how to access registered tools
"""

import sys
import os

# Add SharkMath directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.fastmcp import FastMCP
import arithmetic

def explore_fastmcp():
    """Explore FastMCP object to understand its structure"""
    
    print("FastMCP API Exploration")
    print("="*50)
    
    # Create MCP server instance
    mcp = FastMCP("Test Server")
    
    print(f"FastMCP object type: {type(mcp)}")
    print(f"FastMCP object attributes:")
    
    # List all attributes of FastMCP object
    for attr in sorted(dir(mcp)):
        if not attr.startswith('_'):
            attr_value = getattr(mcp, attr)
            print(f"  • {attr}: {type(attr_value)}")
    
    print(f"\n{'='*50}")
    print("Before tool registration:")
    
    # Check if there are any tool-related attributes
    if hasattr(mcp, 'tools'):
        print(f"mcp.tools exists: {mcp.tools}")
    else:
        print("mcp.tools does NOT exist")
    
    if hasattr(mcp, '_tools'):
        print(f"mcp._tools exists: {mcp._tools}")
    else:
        print("mcp._tools does NOT exist")
        
    if hasattr(mcp, 'handlers'):
        print(f"mcp.handlers exists: {mcp.handlers}")
    else:
        print("mcp.handlers does NOT exist")
    
    print(f"\n{'='*50}")
    print("Registering arithmetic tools...")
    
    # Register tools
    arithmetic.register_tools(mcp)
    
    print("After tool registration:")
    
    # Check again after registration
    if hasattr(mcp, 'tools'):
        print(f"mcp.tools exists: {len(mcp.tools)} tools")
    else:
        print("mcp.tools still does NOT exist")
    
    if hasattr(mcp, '_tools'):
        print(f"mcp._tools exists: {type(mcp._tools)}")
        if hasattr(mcp._tools, '__len__'):
            print(f"  Length: {len(mcp._tools)}")
    else:
        print("mcp._tools still does NOT exist")
        
    if hasattr(mcp, 'handlers'):
        print(f"mcp.handlers exists: {type(mcp.handlers)}")
        if hasattr(mcp.handlers, '__len__'):
            print(f"  Length: {len(mcp.handlers)}")
    else:
        print("mcp.handlers still does NOT exist")
    
    # Try other possible attributes
    for attr in ['_handlers', 'tool_handlers', '_tool_handlers', 'registered_tools']:
        if hasattr(mcp, attr):
            attr_value = getattr(mcp, attr)
            print(f"Found {attr}: {type(attr_value)}")
            if hasattr(attr_value, '__len__'):
                try:
                    print(f"  Length: {len(attr_value)}")
                except:
                    print(f"  Cannot get length")
    
    print(f"\n{'='*50}")
    print("Attribute exploration after registration:")
    
    # List all attributes again after registration
    for attr in sorted(dir(mcp)):
        if not attr.startswith('__'):  # Show private attributes too
            try:
                attr_value = getattr(mcp, attr)
                attr_type = type(attr_value)
                if hasattr(attr_value, '__len__') and not callable(attr_value):
                    try:
                        length = len(attr_value)
                        print(f"  • {attr}: {attr_type} (length: {length})")
                    except:
                        print(f"  • {attr}: {attr_type}")
                else:
                    print(f"  • {attr}: {attr_type}")
            except:
                print(f"  • {attr}: <unable to access>")

if __name__ == "__main__":
    explore_fastmcp()
