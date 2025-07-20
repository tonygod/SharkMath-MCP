"""
Test suite for hyperbolic.py module

Tests hyperbolic functions: sinh, cosh, tanh
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import hyperbolic


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestHyperbolic:
    """Test class for hyperbolic functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        hyperbolic.register_tools(self.mcp)
    
    async def test_sinh_zero(self):
        """Test sinh(0)."""
        result = await self.mcp.tools['sinh'](0)
        expected = "✅ sinh(0.0) = 0.0"
        return result == expected
    
    async def test_sinh_positive(self):
        """Test sinh of positive number."""
        result = await self.mcp.tools['sinh'](1)
        # sinh(1) ≈ 1.175
        return result.startswith("✅ sinh(1.0) = 1.175")
    
    async def test_sinh_negative(self):
        """Test sinh of negative number."""
        result = await self.mcp.tools['sinh'](-1)
        # sinh(-1) ≈ -1.175 (odd function)
        return result.startswith("✅ sinh(-1.0) = -1.175")
    
    async def test_sinh_large_overflow(self):
        """Test sinh with large input (overflow protection)."""
        result = await self.mcp.tools['sinh'](800)
        return result.startswith("❌") and "overflow" in result.lower()
    
    async def test_cosh_zero(self):
        """Test cosh(0)."""
        result = await self.mcp.tools['cosh'](0)
        expected = "✅ cosh(0.0) = 1.0"
        return result == expected
    
    async def test_cosh_positive(self):
        """Test cosh of positive number."""
        result = await self.mcp.tools['cosh'](1)
        # cosh(1) ≈ 1.543
        return result.startswith("✅ cosh(1.0) = 1.543")
    
    async def test_cosh_negative(self):
        """Test cosh of negative number."""
        result = await self.mcp.tools['cosh'](-1)
        # cosh(-1) = cosh(1) ≈ 1.543 (even function)
        return result.startswith("✅ cosh(-1.0) = 1.543")
    
    async def test_cosh_large_overflow(self):
        """Test cosh with large input (overflow protection)."""
        result = await self.mcp.tools['cosh'](800)
        return result.startswith("❌") and "overflow" in result.lower()
    
    async def test_tanh_zero(self):
        """Test tanh(0)."""
        result = await self.mcp.tools['tanh'](0)
        expected = "✅ tanh(0.0) = 0.0"
        return result == expected
    
    async def test_tanh_positive(self):
        """Test tanh of positive number."""
        result = await self.mcp.tools['tanh'](1)
        # tanh(1) ≈ 0.762
        return result.startswith("✅ tanh(1.0) = 0.762")
    
    async def test_tanh_negative(self):
        """Test tanh of negative number."""
        result = await self.mcp.tools['tanh'](-1)
        # tanh(-1) ≈ -0.762 (odd function)
        return result.startswith("✅ tanh(-1.0) = -0.762")
    
    async def test_tanh_large_positive(self):
        """Test tanh of large positive number."""
        result = await self.mcp.tools['tanh'](10)
        # tanh approaches 1 for large positive values
        return result.startswith("✅ tanh(10.0) = 1.0") or "0.999999" in result
    
    async def test_tanh_large_negative(self):
        """Test tanh of large negative number."""
        result = await self.mcp.tools['tanh'](-10)
        # tanh approaches -1 for large negative values
        return result.startswith("✅ tanh(-10.0) = -1.0") or "-0.999999" in result
