"""
Test suite for statistics.py module

Tests statistical functions: mean, median, mode, standard_deviation, variance, range_stats
"""

import asyncio
import math
import sys
import importlib.util
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the SharkMath statistics module by explicit path
import importlib.util
stats_module_path = Path(__file__).parent.parent / "statistics.py"
spec = importlib.util.spec_from_file_location("sharkmath_statistics", stats_module_path)
stats_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stats_module)


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestStatistics:
    """Test class for statistical functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        stats_module.register_tools(self.mcp)
    
    async def test_mean_simple(self):
        """Test mean of simple numbers."""
        result = await self.mcp.tools['mean']("1,2,3,4,5")
        expected = "✅ Mean of [1.0, 2.0, 3.0, 4.0, 5.0] = 3.0"
        return result == expected
    
    async def test_mean_with_decimals(self):
        """Test mean with decimal numbers."""
        result = await self.mcp.tools['mean']("1.5,2.5,3.5")
        expected = "✅ Mean of [1.5, 2.5, 3.5] = 2.5"
        return result == expected
    
    async def test_mean_negative_numbers(self):
        """Test mean with negative numbers."""
        result = await self.mcp.tools['mean']("-1,0,1")
        expected = "✅ Mean of [-1.0, 0.0, 1.0] = 0.0"
        return result == expected
    
    async def test_mean_single_number(self):
        """Test mean of single number."""
        result = await self.mcp.tools['mean']("42")
        expected = "✅ Mean of [42.0] = 42.0"
        return result == expected
    
    async def test_mean_empty_input(self):
        """Test mean with empty input."""
        result = await self.mcp.tools['mean']("")
        return result.startswith("❌")
    
    async def test_median_odd_count(self):
        """Test median with odd number of values."""
        result = await self.mcp.tools['median']("1,3,5,7,9")
        expected = "✅ Median of [1.0, 3.0, 5.0, 7.0, 9.0] = 5.0"
        return result == expected
    
    async def test_median_even_count(self):
        """Test median with even number of values."""
        result = await self.mcp.tools['median']("1,2,3,4")
        expected = "✅ Median of [1.0, 2.0, 3.0, 4.0] = 2.5"
        return result == expected
    
    async def test_median_unsorted(self):
        """Test median with unsorted input."""
        result = await self.mcp.tools['median']("5,1,9,3,7")
        expected = "✅ Median of [1.0, 3.0, 5.0, 7.0, 9.0] = 5.0"
        return result == expected
    
    async def test_median_single_number(self):
        """Test median of single number."""
        result = await self.mcp.tools['median']("42")
        expected = "✅ Median of [42.0] = 42.0"
        return result == expected
    
    async def test_mode_single_mode(self):
        """Test mode with single most frequent value."""
        result = await self.mcp.tools['mode']("1,2,2,3,3,3,4")
        expected = "✅ Mode of [1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0] = [3.0]"
        return result == expected
    
    async def test_mode_multiple_modes(self):
        """Test mode with multiple modes."""
        result = await self.mcp.tools['mode']("1,1,2,2,3")
        # Should show both 1.0 and 2.0 as modes
        return result.startswith("✅") and "[1.0, 2.0]" in result
    
    async def test_mode_no_mode(self):
        """Test mode when all values appear equally."""
        result = await self.mcp.tools['mode']("1,2,3,4")
        expected = "✅ No mode found (all values appear equally)"
        return result == expected
    
    async def test_standard_deviation_simple(self):
        """Test standard deviation of simple dataset."""
        result = await self.mcp.tools['standard_deviation']("2,4,4,4,5,5,7,9")
        # Should be 2.0
        return result.startswith("✅") and "= 2.0" in result
    
    async def test_standard_deviation_identical_values(self):
        """Test standard deviation when all values are the same."""
        result = await self.mcp.tools['standard_deviation']("5,5,5,5,5")
        expected = "✅ Standard deviation of [5.0, 5.0, 5.0, 5.0, 5.0] = 0.0"
        return result == expected
    
    async def test_variance_simple(self):
        """Test variance of simple dataset."""
        result = await self.mcp.tools['variance']("2,4,4,4,5,5,7,9")
        # Variance should be 4.0 (standard deviation squared)
        return result.startswith("✅") and "= 4.0" in result
    
    async def test_variance_identical_values(self):
        """Test variance when all values are the same."""
        result = await self.mcp.tools['variance']("3,3,3,3")
        expected = "✅ Variance of [3.0, 3.0, 3.0, 3.0] = 0.0"
        return result == expected
    
    async def test_range_stats_simple(self):
        """Test range statistics."""
        result = await self.mcp.tools['range_stats']("1,3,7,2,9,4")
        expected = "✅ Range statistics of [1.0, 2.0, 3.0, 4.0, 7.0, 9.0]:\n   Min: 1.0, Max: 9.0, Range: 8.0"
        return result == expected
    
    async def test_range_stats_single_value(self):
        """Test range statistics with single value."""
        result = await self.mcp.tools['range_stats']("42")
        expected = "✅ Range statistics of [42.0]:\n   Min: 42.0, Max: 42.0, Range: 0.0"
        return result == expected
    
    async def test_range_stats_negative_numbers(self):
        """Test range statistics with negative numbers."""
        result = await self.mcp.tools['range_stats']("-5,0,10,-2")
        expected = "✅ Range statistics of [-5.0, -2.0, 0.0, 10.0]:\n   Min: -5.0, Max: 10.0, Range: 15.0"
        return result == expected
