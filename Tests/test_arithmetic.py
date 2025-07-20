"""
Test suite for arithmetic.py module

Tests basic arithmetic operations: add, subtract, multiply, divide, calculate
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import arithmetic


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestArithmetic:
    """Test class for arithmetic operations."""
    
    def __init__(self):
        self.mcp = MockMCP()
        arithmetic.register_tools(self.mcp)
    
    async def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = await self.mcp.tools['add'](10, 5)
        expected = "✅ 10.0 + 5.0 = 15.0"
        return result == expected
    
    async def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = await self.mcp.tools['add'](-5, -3)
        expected = "✅ -5.0 + -3.0 = -8.0"
        return result == expected
    
    async def test_add_zero(self):
        """Test addition with zero."""
        result = await self.mcp.tools['add'](0, 42)
        expected = "✅ 0.0 + 42.0 = 42.0"
        return result == expected
    
    async def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        result = await self.mcp.tools['subtract'](10, 3)
        expected = "✅ 10.0 - 3.0 = 7.0"
        return result == expected
    
    async def test_subtract_negative_result(self):
        """Test subtraction resulting in negative."""
        result = await self.mcp.tools['subtract'](5, 10)
        expected = "✅ 5.0 - 10.0 = -5.0"
        return result == expected
    
    async def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        result = await self.mcp.tools['multiply'](4, 7)
        expected = "✅ 4.0 × 7.0 = 28.0"
        return result == expected
    
    async def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = await self.mcp.tools['multiply'](42, 0)
        expected = "✅ 42.0 × 0.0 = 0.0"
        return result == expected
    
    async def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        result = await self.mcp.tools['multiply'](-3, 4)
        expected = "✅ -3.0 × 4.0 = -12.0"
        return result == expected
    
    async def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        result = await self.mcp.tools['divide'](15, 3)
        expected = "✅ 15.0 ÷ 3.0 = 5.0"
        return result == expected
    
    async def test_divide_with_decimal_result(self):
        """Test division with decimal result."""
        result = await self.mcp.tools['divide'](10, 3)
        expected = "✅ 10.0 ÷ 3.0 = 3.3333333333333335"
        return result == expected
    
    async def test_divide_by_zero(self):
        """Test division by zero error handling."""
        result = await self.mcp.tools['divide'](10, 0)
        return result.startswith("❌") and "division by zero" in result.lower()
    
    async def test_calculate_simple_expression(self):
        """Test calculation of simple expression."""
        result = await self.mcp.tools['calculate']("2 + 3 * 4")
        expected = "✅ 2 + 3 * 4 = 14"
        return result == expected
    
    async def test_calculate_parentheses(self):
        """Test calculation with parentheses."""
        result = await self.mcp.tools['calculate']("(2 + 3) * 4")
        expected = "✅ (2 + 3) * 4 = 20"
        return result == expected
    
    async def test_calculate_division(self):
        """Test calculation with division."""
        result = await self.mcp.tools['calculate']("10 / 2 + 1")
        expected = "✅ 10 / 2 + 1 = 6.0"
        return result == expected
    
    async def test_calculate_invalid_expression(self):
        """Test calculation with invalid expression."""
        result = await self.mcp.tools['calculate']("2 + + 3")
        return result.startswith("❌")
    
    async def test_calculate_unsafe_expression(self):
        """Test calculation rejects unsafe expressions."""
        result = await self.mcp.tools['calculate']("__import__('os').system('ls')")
        return result.startswith("❌") and "not allowed" in result
    
    async def test_calculate_complex_expression(self):
        """Test calculation of complex valid expression."""
        result = await self.mcp.tools['calculate']("((10 + 5) * 2) / 3")
        expected = "✅ ((10 + 5) * 2) / 3 = 10.0"
        return result == expected
