"""
Test suite for precision.py module

Tests precision functions: round_to_decimal, floor, ceiling, truncate, absolute
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import precision


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestPrecision:
    """Test class for precision functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        precision.register_tools(self.mcp)
    
    async def test_round_to_decimal_two_places(self):
        """Test rounding to 2 decimal places."""
        result = await self.mcp.tools['round_to_decimal'](3.14159, 2)
        expected = "✅ 3.14159 rounded to 2 decimal places = 3.14"
        return result == expected
    
    async def test_round_to_decimal_zero_places(self):
        """Test rounding to 0 decimal places."""
        result = await self.mcp.tools['round_to_decimal'](3.7, 0)
        expected = "✅ 3.7 rounded to 0 decimal places = 4"
        return result == expected
    
    async def test_round_to_decimal_negative_places(self):
        """Test rounding with negative places."""
        result = await self.mcp.tools['round_to_decimal'](1234, -2)
        expected = "✅ 1234 rounded to -2 decimal places = 1200"
        return result == expected
    
    async def test_round_to_decimal_negative_number(self):
        """Test rounding negative number."""
        result = await self.mcp.tools['round_to_decimal'](-3.456, 1)
        expected = "✅ -3.456 rounded to 1 decimal places = -3.5"
        return result == expected
    
    async def test_floor_positive_decimal(self):
        """Test floor of positive decimal."""
        result = await self.mcp.tools['floor'](3.7)
        expected = "✅ floor(3.7) = 3"
        return result == expected
    
    async def test_floor_negative_decimal(self):
        """Test floor of negative decimal."""
        result = await self.mcp.tools['floor'](-3.2)
        expected = "✅ floor(-3.2) = -4"
        return result == expected
    
    async def test_floor_integer(self):
        """Test floor of integer."""
        result = await self.mcp.tools['floor'](5)
        expected = "✅ floor(5.0) = 5"
        return result == expected
    
    async def test_floor_zero(self):
        """Test floor of zero."""
        result = await self.mcp.tools['floor'](0)
        expected = "✅ floor(0.0) = 0"
        return result == expected
    
    async def test_ceiling_positive_decimal(self):
        """Test ceiling of positive decimal."""
        result = await self.mcp.tools['ceiling'](3.2)
        expected = "✅ ceiling(3.2) = 4"
        return result == expected
    
    async def test_ceiling_negative_decimal(self):
        """Test ceiling of negative decimal."""
        result = await self.mcp.tools['ceiling'](-3.7)
        expected = "✅ ceiling(-3.7) = -3"
        return result == expected
    
    async def test_ceiling_integer(self):
        """Test ceiling of integer."""
        result = await self.mcp.tools['ceiling'](5)
        expected = "✅ ceiling(5.0) = 5"
        return result == expected
    
    async def test_truncate_positive_decimal(self):
        """Test truncate of positive decimal."""
        result = await self.mcp.tools['truncate'](3.7)
        expected = "✅ truncate(3.7) = 3"
        return result == expected
    
    async def test_truncate_negative_decimal(self):
        """Test truncate of negative decimal."""
        result = await self.mcp.tools['truncate'](-3.7)
        expected = "✅ truncate(-3.7) = -3"
        return result == expected
    
    async def test_truncate_integer(self):
        """Test truncate of integer."""
        result = await self.mcp.tools['truncate'](5)
        expected = "✅ truncate(5.0) = 5"
        return result == expected
    
    async def test_absolute_positive(self):
        """Test absolute value of positive number."""
        result = await self.mcp.tools['absolute'](5.3)
        expected = "✅ |5.3| = 5.3"
        return result == expected
    
    async def test_absolute_negative(self):
        """Test absolute value of negative number."""
        result = await self.mcp.tools['absolute'](-7.2)
        expected = "✅ |-7.2| = 7.2"
        return result == expected
    
    async def test_absolute_zero(self):
        """Test absolute value of zero."""
        result = await self.mcp.tools['absolute'](0)
        expected = "✅ |0.0| = 0.0"
        return result == expected
