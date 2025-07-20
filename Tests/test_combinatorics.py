"""
Test suite for combinatorics.py module

Tests combinatorial functions: factorial, permutation, combination, fibonacci
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import combinatorics


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestCombinatorics:
    """Test class for combinatorial functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        combinatorics.register_tools(self.mcp)
    
    async def test_factorial_zero(self):
        """Test factorial of 0."""
        result = await self.mcp.tools['factorial'](0)
        expected = "✅ 0! = 1"
        return result == expected
    
    async def test_factorial_one(self):
        """Test factorial of 1."""
        result = await self.mcp.tools['factorial'](1)
        expected = "✅ 1! = 1"
        return result == expected
    
    async def test_factorial_five(self):
        """Test factorial of 5."""
        result = await self.mcp.tools['factorial'](5)
        expected = "✅ 5! = 120"
        return result == expected
    
    async def test_factorial_ten(self):
        """Test factorial of 10."""
        result = await self.mcp.tools['factorial'](10)
        expected = "✅ 10! = 3628800"
        return result == expected
    
    async def test_factorial_negative(self):
        """Test factorial of negative number."""
        result = await self.mcp.tools['factorial'](-1)
        return result.startswith("❌") and "non-negative" in result.lower()
    
    async def test_permutation_basic(self):
        """Test basic permutation P(5,3)."""
        result = await self.mcp.tools['permutation'](5, 3)
        expected = "✅ P(5,3) = 5!/(5-3)! = 60"
        return result == expected
    
    async def test_permutation_full(self):
        """Test full permutation P(4,4)."""
        result = await self.mcp.tools['permutation'](4, 4)
        expected = "✅ P(4,4) = 4!/(4-4)! = 24"
        return result == expected
    
    async def test_permutation_zero_r(self):
        """Test permutation with r=0."""
        result = await self.mcp.tools['permutation'](5, 0)
        expected = "✅ P(5,0) = 5!/(5-0)! = 1"
        return result == expected
    
    async def test_permutation_invalid_r_greater_n(self):
        """Test permutation with r > n."""
        result = await self.mcp.tools['permutation'](3, 5)
        return result.startswith("❌") and "greater than" in result.lower()
    
    async def test_permutation_negative_n(self):
        """Test permutation with negative n."""
        result = await self.mcp.tools['permutation'](-1, 2)
        return result.startswith("❌") and "non-negative" in result.lower()
    
    async def test_combination_basic(self):
        """Test basic combination C(5,3)."""
        result = await self.mcp.tools['combination'](5, 3)
        expected = "✅ C(5,3) = 5!/(3!(5-3)!) = 10"
        return result == expected
    
    async def test_combination_choose_all(self):
        """Test combination C(4,4)."""
        result = await self.mcp.tools['combination'](4, 4)
        expected = "✅ C(4,4) = 4!/(4!(4-4)!) = 1"
        return result == expected
    
    async def test_combination_choose_none(self):
        """Test combination C(5,0)."""
        result = await self.mcp.tools['combination'](5, 0)
        expected = "✅ C(5,0) = 5!/(0!(5-0)!) = 1"
        return result == expected
    
    async def test_combination_symmetry(self):
        """Test combination symmetry C(6,2) = C(6,4)."""
        result1 = await self.mcp.tools['combination'](6, 2)
        result2 = await self.mcp.tools['combination'](6, 4)
        # Both should equal 15
        return "= 15" in result1 and "= 15" in result2
    
    async def test_combination_invalid_r_greater_n(self):
        """Test combination with r > n."""
        result = await self.mcp.tools['combination'](3, 5)
        return result.startswith("❌") and "greater than" in result.lower()
    
    async def test_fibonacci_zero(self):
        """Test Fibonacci F(0)."""
        result = await self.mcp.tools['fibonacci'](0)
        expected = "✅ F(0) = 0"
        return result == expected
    
    async def test_fibonacci_one(self):
        """Test Fibonacci F(1)."""
        result = await self.mcp.tools['fibonacci'](1)
        expected = "✅ F(1) = 1"
        return result == expected
    
    async def test_fibonacci_sequence(self):
        """Test Fibonacci sequence values."""
        # F(5) should be 5, F(10) should be 55
        result5 = await self.mcp.tools['fibonacci'](5)
        result10 = await self.mcp.tools['fibonacci'](10)
        return "F(5) = 5" in result5 and "F(10) = 55" in result10
    
    async def test_fibonacci_larger(self):
        """Test larger Fibonacci number F(20)."""
        result = await self.mcp.tools['fibonacci'](20)
        expected = "✅ F(20) = 6765"
        return result == expected
    
    async def test_fibonacci_negative(self):
        """Test Fibonacci with negative input."""
        result = await self.mcp.tools['fibonacci'](-1)
        return result.startswith("❌") and "non-negative" in result.lower()
