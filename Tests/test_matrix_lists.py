#!/usr/bin/env python3
"""
Test matrix operations with both JSON strings and Python lists.
"""
import asyncio
from matrix_operations import register_tools

# Mock MCP server for testing
class MockMCP:
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator

async def test_matrix_with_lists():
    print("Testing Matrix Operations with Python Lists")
    print("=" * 50)
    
    # Create mock MCP and register tools
    mcp = MockMCP()
    register_tools(mcp)
    
    # Test with Python lists (what MCP function calls will pass)
    print("\n1. Testing Matrix Addition with Lists:")
    result1 = await mcp.tools['matrix_add']([[1,2],[3,4]], [[5,6],[7,8]])
    print(f"   Result: {result1}")
    
    print("\n2. Testing Matrix Multiplication with Lists:")
    result2 = await mcp.tools['matrix_multiply']([[2,1],[3,4]], [[1,0],[2,5]])
    print(f"   Result: {result2}")
    
    print("\n3. Testing Matrix Determinant with List:")
    result3 = await mcp.tools['matrix_determinant']([[3,2],[1,4]])
    print(f"   Result: {result3}")
    
    print("\n4. Testing Matrix Transpose with List:")
    result4 = await mcp.tools['matrix_transpose']([[1,2,3],[4,5,6]])
    print(f"   Result: {result4}")
    
    print("\n" + "=" * 50)
    print("Matrix operations with lists testing complete!")

if __name__ == "__main__":
    asyncio.run(test_matrix_with_lists())
