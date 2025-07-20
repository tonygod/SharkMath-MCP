#!/usr/bin/env python3
"""
Simple test runner for SharkMath - tests just one module to verify approach
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import arithmetic module to test
import arithmetic

class MockMCP:
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator

async def test_arithmetic():
    """Test some arithmetic functions."""
    print("Testing arithmetic module...")
    
    mcp = MockMCP()
    arithmetic.register_tools(mcp)
    
    # Test addition
    result = await mcp.tools['add'](5, 3)
    print(f"5 + 3: {result}")
    
    # Test division by zero
    result = await mcp.tools['divide'](10, 0)
    print(f"10 / 0: {result}")
    
    # Test calculation
    result = await mcp.tools['calculate']("2 + 3 * 4")
    print(f"2 + 3 * 4: {result}")
    
    print("Arithmetic tests completed!")

if __name__ == "__main__":
    asyncio.run(test_arithmetic())
