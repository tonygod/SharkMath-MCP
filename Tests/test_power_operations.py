"""
Test suite for power_operations.py module

Tests power and root operations: power, square, cube, square_root, cube_root, nth_root
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import power_operations


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestPowerOperations:
    """Test class for power operations."""
    
    def __init__(self):
        self.mcp = MockMCP()
        power_operations.register_tools(self.mcp)
    
    async def test_power_positive_integers(self):
        """Test power with positive integers."""
        result = await self.mcp.tools['power'](2, 3)
        expected = "✅ 2.0^3.0 = 8.0"
        return result == expected
    
    async def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        result = await self.mcp.tools['power'](5, 0)
        expected = "✅ 5.0^0.0 = 1.0"
        return result == expected
    
    async def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        result = await self.mcp.tools['power'](2, -3)
        expected = "✅ 2.0^-3.0 = 0.125"
        return result == expected
    
    async def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        result = await self.mcp.tools['power'](9, 0.5)
        expected = "✅ 9.0^0.5 = 3.0"
        return result == expected
    
    async def test_square_positive(self):
        """Test square of positive number."""
        result = await self.mcp.tools['square'](4)
        expected = "✅ 4.0² = 16.0"
        return result == expected
    
    async def test_square_negative(self):
        """Test square of negative number."""
        result = await self.mcp.tools['square'](-5)
        expected = "✅ -5.0² = 25.0"
        return result == expected
    
    async def test_square_zero(self):
        """Test square of zero."""
        result = await self.mcp.tools['square'](0)
        expected = "✅ 0.0² = 0.0"
        return result == expected
    
    async def test_cube_positive(self):
        """Test cube of positive number."""
        result = await self.mcp.tools['cube'](3)
        expected = "✅ 3.0³ = 27.0"
        return result == expected
    
    async def test_cube_negative(self):
        """Test cube of negative number."""
        result = await self.mcp.tools['cube'](-2)
        expected = "✅ -2.0³ = -8.0"
        return result == expected
    
    async def test_square_root_perfect_square(self):
        """Test square root of perfect square."""
        result = await self.mcp.tools['square_root'](25)
        expected = "✅ √25.0 = 5.0"
        return result == expected
    
    async def test_square_root_non_perfect(self):
        """Test square root of non-perfect square."""
        result = await self.mcp.tools['square_root'](2)
        # Should be approximately 1.414
        return result.startswith("✅ √2.0 = 1.41421")
    
    async def test_square_root_zero(self):
        """Test square root of zero."""
        result = await self.mcp.tools['square_root'](0)
        expected = "✅ √0.0 = 0.0"
        return result == expected
    
    async def test_square_root_negative(self):
        """Test square root of negative number."""
        result = await self.mcp.tools['square_root'](-4)
        return result.startswith("❌") and "negative" in result.lower()
    
    async def test_cube_root_positive(self):
        """Test cube root of positive number."""
        result = await self.mcp.tools['cube_root'](27)
        expected = "✅ ∛27.0 = 3.0"
        return result == expected
    
    async def test_cube_root_negative(self):
        """Test cube root of negative number."""
        result = await self.mcp.tools['cube_root'](-8)
        expected = "✅ ∛-8.0 = -2.0"
        return result == expected
    
    async def test_cube_root_zero(self):
        """Test cube root of zero."""
        result = await self.mcp.tools['cube_root'](0)
        expected = "✅ ∛0.0 = 0.0"
        return result == expected
    
    async def test_nth_root_fourth_root(self):
        """Test nth root (4th root)."""
        result = await self.mcp.tools['nth_root'](16, 4)
        expected = "✅ 4th root of 16.0 = 2.0"
        return result == expected
    
    async def test_nth_root_invalid_even_root_negative(self):
        """Test nth root with invalid even root of negative."""
        result = await self.mcp.tools['nth_root'](-16, 4)
        return result.startswith("❌") and "even root" in result
    
    async def test_nth_root_odd_root_negative(self):
        """Test nth root with odd root of negative number."""
        result = await self.mcp.tools['nth_root'](-32, 5)
        expected = "✅ 5th root of -32.0 = -2.0"
        return result == expected
    
    async def test_nth_root_zero_root(self):
        """Test nth root with zero root."""
        result = await self.mcp.tools['nth_root'](10, 0)
        return result.startswith("❌") and "root cannot be zero" in result
