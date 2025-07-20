"""
Test suite for logarithmic.py module

Tests logarithmic functions: natural_log, log_base_10, log_base, exponential
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import logarithmic


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestLogarithmic:
    """Test class for logarithmic operations."""
    
    def __init__(self):
        self.mcp = MockMCP()
        logarithmic.register_tools(self.mcp)
    
    async def test_natural_log_e(self):
        """Test natural log of e."""
        result = await self.mcp.tools['natural_log'](math.e)
        # ln(e) should be 1
        return result.startswith("✅ ln(") and "= 1.0" in result
    
    async def test_natural_log_one(self):
        """Test natural log of 1."""
        result = await self.mcp.tools['natural_log'](1)
        expected = "✅ ln(1.0) = 0.0"
        return result == expected
    
    async def test_natural_log_ten(self):
        """Test natural log of 10."""
        result = await self.mcp.tools['natural_log'](10)
        # ln(10) ≈ 2.3026
        return result.startswith("✅ ln(10.0) = 2.302")
    
    async def test_natural_log_zero(self):
        """Test natural log of zero (undefined)."""
        result = await self.mcp.tools['natural_log'](0)
        return result.startswith("❌") and ("zero" in result.lower() or "undefined" in result.lower())
    
    async def test_natural_log_negative(self):
        """Test natural log of negative number."""
        result = await self.mcp.tools['natural_log'](-5)
        return result.startswith("❌") and "positive" in result.lower()
    
    async def test_log_base_10_hundred(self):
        """Test base-10 log of 100."""
        result = await self.mcp.tools['log_base_10'](100)
        expected = "✅ log₁₀(100.0) = 2.0"
        return result == expected
    
    async def test_log_base_10_one(self):
        """Test base-10 log of 1."""
        result = await self.mcp.tools['log_base_10'](1)
        expected = "✅ log₁₀(1.0) = 0.0"
        return result == expected
    
    async def test_log_base_10_ten(self):
        """Test base-10 log of 10."""
        result = await self.mcp.tools['log_base_10'](10)
        expected = "✅ log₁₀(10.0) = 1.0"
        return result == expected
    
    async def test_log_base_10_zero(self):
        """Test base-10 log of zero."""
        result = await self.mcp.tools['log_base_10'](0)
        return result.startswith("❌") and ("zero" in result.lower() or "undefined" in result.lower())
    
    async def test_log_base_custom_base_2(self):
        """Test log base 2 of 8."""
        result = await self.mcp.tools['log_base'](8, 2)
        expected = "✅ log₂(8.0) = 3.0"
        return result == expected
    
    async def test_log_base_custom_base_same(self):
        """Test log base n of n."""
        result = await self.mcp.tools['log_base'](5, 5)
        expected = "✅ log₅(5.0) = 1.0"
        return result == expected
    
    async def test_log_base_invalid_base_zero(self):
        """Test log with base zero."""
        result = await self.mcp.tools['log_base'](10, 0)
        return result.startswith("❌") and "base must be positive" in result
    
    async def test_log_base_invalid_base_one(self):
        """Test log with base one."""
        result = await self.mcp.tools['log_base'](10, 1)
        return result.startswith("❌") and "base cannot be 1" in result
    
    async def test_log_base_invalid_base_negative(self):
        """Test log with negative base."""
        result = await self.mcp.tools['log_base'](10, -2)
        return result.startswith("❌") and "base must be positive" in result
    
    async def test_exponential_zero(self):
        """Test e^0."""
        result = await self.mcp.tools['exponential'](0)
        expected = "✅ e^0.0 = 1.0"
        return result == expected
    
    async def test_exponential_one(self):
        """Test e^1."""
        result = await self.mcp.tools['exponential'](1)
        # e^1 = e ≈ 2.718
        return result.startswith("✅ e^1.0 = 2.718")
    
    async def test_exponential_two(self):
        """Test e^2."""
        result = await self.mcp.tools['exponential'](2)
        # e^2 ≈ 7.389
        return result.startswith("✅ e^2.0 = 7.389")
    
    async def test_exponential_negative(self):
        """Test e^(-1)."""
        result = await self.mcp.tools['exponential'](-1)
        # e^(-1) ≈ 0.368
        return result.startswith("✅ e^-1.0 = 0.368")
    
    async def test_exponential_large_overflow(self):
        """Test exponential with very large input (overflow protection)."""
        result = await self.mcp.tools['exponential'](1000)
        return result.startswith("❌") and "overflow" in result.lower()
