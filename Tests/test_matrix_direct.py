#!/usr/bin/env python3
"""
Direct test of matrix operations to verify they work with JSON strings.
"""
import asyncio
import json
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

async def test_matrix_operations():
    print("Testing Matrix Operations with JSON Strings")
    print("=" * 50)
    
    # Create mock MCP and register tools
    mcp = MockMCP()
    register_tools(mcp)
    
    # Test 1: Matrix Addition
    print("\n1. Testing Matrix Addition:")
    print("   Matrix1: [[1,2],[3,4]]")
    print("   Matrix2: [[5,6],[7,8]]")
    result1 = await mcp.tools['matrix_add']('[[1,2],[3,4]]', '[[5,6],[7,8]]')
    print(f"   Result: {result1}")
    
    # Test 2: Matrix Multiplication
    print("\n2. Testing Matrix Multiplication:")
    print("   Matrix1: [[2,1],[3,4]]")
    print("   Matrix2: [[1,0],[2,5]]")
    result2 = await mcp.tools['matrix_multiply']('[[2,1],[3,4]]', '[[1,0],[2,5]]')
    print(f"   Result: {result2}")
    
    # Test 3: Matrix Determinant
    print("\n3. Testing Matrix Determinant:")
    print("   Matrix: [[3,2],[1,4]]")
    result3 = await mcp.tools['matrix_determinant']('[[3,2],[1,4]]')
    print(f"   Result: {result3}")
    
    # Test 4: Matrix Transpose
    print("\n4. Testing Matrix Transpose:")
    print("   Matrix: [[1,2,3],[4,5,6]]")
    result4 = await mcp.tools['matrix_transpose']('[[1,2,3],[4,5,6]]')
    print(f"   Result: {result4}")
    
    print("\n" + "=" * 50)
    print("Matrix operations testing complete!")

if __name__ == "__main__":
    asyncio.run(test_matrix_operations())
