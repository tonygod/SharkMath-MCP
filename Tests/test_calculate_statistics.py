"""
Test Suite for Consolidated Statistics Tool
Tests all statistical operations with comprehensive coverage including edge cases.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import asyncio
from stats_operations import register_tools

class TestCalculateStatistics(unittest.TestCase):
    """Test suite for consolidated statistics calculations."""
    
    def setUp(self):
        """Set up test fixtures with MockMCP."""
        class MockMCP:
            def __init__(self):
                self.tools = {}
            
            def tool(self):
                def decorator(func):
                    tool_name = func.__name__
                    self.tools[tool_name] = func
                    return func
                return decorator
        
        self.mock_mcp = MockMCP()
        register_tools(self.mock_mcp)
        
    async def async_test_helper(self, tool_name, *args, **kwargs):
        """Helper to run async tool functions in tests."""
        if tool_name in self.mock_mcp.tools:
            return await self.mock_mcp.tools[tool_name](*args, **kwargs)
        else:
            raise ValueError(f"Tool {tool_name} not found")

    # Basic Statistics Tests - Mean
    def test_mean_simple(self):
        """Test mean with simple integer values."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', '1,2,3,4,5'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 3.0", result)

    def test_mean_decimals(self):
        """Test mean with decimal values."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', '2.5, 3.5, 4.5'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 3.5", result)

    def test_mean_space_separated(self):
        """Test mean with space-separated input."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', '10 20 30 40 50'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 30.0", result)

    # Basic Statistics Tests - Median
    def test_median_odd_count(self):
        """Test median with odd number of values."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'median', '1,3,3,6,7,8,9'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 6.0", result)

    def test_median_even_count(self):
        """Test median with even number of values."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'median', '1,2,3,4'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 2.5", result)

    def test_median_single_value(self):
        """Test median with single value."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'median', '42'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 42.0", result)

    # Basic Statistics Tests - Mode
    def test_mode_clear_winner(self):
        """Test mode with clear most frequent value."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mode', '1,2,2,3,4,4,4'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 4.0", result)

    def test_mode_all_equal(self):
        """Test mode when all values appear equally."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mode', '1,2,3,4'
        ))
        self.assertIn("✅", result)
        # Python's mode() returns first value when all appear equally
        self.assertIn("= 1.0", result)

    def test_mode_single_value(self):
        """Test mode with single value."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mode', '5'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 5.0", result)

    # Spread Measures Tests - Standard Deviation
    def test_standard_deviation_normal(self):
        """Test standard deviation with normal dataset."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'standard_deviation', '2,4,4,4,5,5,7,9'
        ))
        self.assertIn("✅", result)
        # Expected std dev is approximately 2.138
        self.assertIn("2.138", result)

    def test_standard_deviation_identical_values(self):
        """Test standard deviation with identical values."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'standard_deviation', '5,5,5,5'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 0.0", result)

    def test_standard_deviation_two_values(self):
        """Test standard deviation with minimum valid count."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'standard_deviation', '1,3'
        ))
        self.assertIn("✅", result)
        # Expected std dev for [1,3] is sqrt(2) ≈ 1.414
        self.assertIn("1.414", result)

    # Spread Measures Tests - Variance
    def test_variance_normal(self):
        """Test variance with normal dataset."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'variance', '2,4,4,4,5,5,7,9'
        ))
        self.assertIn("✅", result)
        # Expected variance is approximately 4.571
        self.assertIn("4.571", result)

    def test_variance_identical_values(self):
        """Test variance with identical values."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'variance', '10,10,10'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 0.0", result)

    def test_variance_two_values(self):
        """Test variance with minimum valid count."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'variance', '2,4'
        ))
        self.assertIn("✅", result)
        # Expected variance for [2,4] is 2.0
        self.assertIn("= 2.0", result)

    # Range Statistics Tests
    def test_range_stats_normal(self):
        """Test range statistics with normal dataset."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'range_stats', '1,3,5,7,9'
        ))
        self.assertIn("✅", result)
        self.assertIn("Min = 1.0", result)
        self.assertIn("Max = 9.0", result) 
        self.assertIn("Range = 8.0", result)

    def test_range_stats_single_value(self):
        """Test range statistics with single value."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'range_stats', '42'
        ))
        self.assertIn("✅", result)
        self.assertIn("Min = 42.0", result)
        self.assertIn("Max = 42.0", result)
        self.assertIn("Range = 0.0", result)

    def test_range_stats_negative_values(self):
        """Test range statistics with negative values."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'range_stats', '-5,-2,0,3,7'
        ))
        self.assertIn("✅", result)
        self.assertIn("Min = -5.0", result)
        self.assertIn("Max = 7.0", result)
        self.assertIn("Range = 12.0", result)

    # Percentile Tests
    def test_percentile_25th(self):
        """Test 25th percentile calculation."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'percentile', '1,2,3,4,5,6,7,8,9,10', percentile=25
        ))
        self.assertIn("✅", result)
        self.assertIn("25th percentile", result)
        self.assertIn("= 3.25", result)

    def test_percentile_50th_median(self):
        """Test 50th percentile (should equal median)."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'percentile', '1,2,3,4,5', percentile=50
        ))
        self.assertIn("✅", result)
        self.assertIn("50th percentile", result)
        self.assertIn("= 3.0", result)

    def test_percentile_75th(self):
        """Test 75th percentile calculation."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'percentile', '1,2,3,4,5,6,7,8,9,10', percentile=75
        ))
        self.assertIn("✅", result)
        self.assertIn("75th percentile", result)
        self.assertIn("= 7.75", result)

    def test_percentile_0th_minimum(self):
        """Test 0th percentile (should equal minimum)."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'percentile', '5,2,8,1,9', percentile=0
        ))
        self.assertIn("✅", result)
        self.assertIn("0th percentile", result)
        self.assertIn("= 1.0", result)

    def test_percentile_100th_maximum(self):
        """Test 100th percentile (should equal maximum)."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'percentile', '5,2,8,1,9', percentile=100
        ))
        self.assertIn("✅", result)
        self.assertIn("100th percentile", result)
        self.assertIn("= 9.0", result)

    # Error Handling Tests
    def test_mean_empty_string(self):
        """Test mean with empty string."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', ''
        ))
        self.assertIn("❌", result)
        self.assertIn("No numbers provided", result)

    def test_mean_invalid_format(self):
        """Test mean with invalid number format."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', '1,2,abc,4'
        ))
        self.assertIn("❌", result)
        self.assertIn("Invalid number format", result)

    def test_standard_deviation_single_value(self):
        """Test standard deviation with insufficient data."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'standard_deviation', '5'
        ))
        self.assertIn("❌", result)
        self.assertIn("Need at least 2 numbers", result)

    def test_variance_single_value(self):
        """Test variance with insufficient data."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'variance', '10'
        ))
        self.assertIn("❌", result)
        self.assertIn("Need at least 2 numbers", result)

    def test_percentile_missing_parameter(self):
        """Test percentile without percentile parameter."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'percentile', '1,2,3,4,5'
        ))
        self.assertIn("❌", result)
        self.assertIn("requires 'percentile' parameter", result)

    def test_percentile_invalid_range_high(self):
        """Test percentile with value > 100."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'percentile', '1,2,3', percentile=150
        ))
        self.assertIn("❌", result)
        self.assertIn("must be between 0 and 100", result)

    def test_percentile_invalid_range_negative(self):
        """Test percentile with negative value."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'percentile', '1,2,3', percentile=-10
        ))
        self.assertIn("❌", result)
        self.assertIn("must be between 0 and 100", result)

    def test_invalid_operation(self):
        """Test invalid operation parameter."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'invalid_op', '1,2,3'
        ))
        self.assertIn("❌", result)
        self.assertIn("not supported", result)

    # Edge Cases and Precision Tests
    def test_mean_large_numbers(self):
        """Test mean with large numbers."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', '1000000,2000000,3000000'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 2000000.0", result)

    def test_mean_small_decimals(self):
        """Test mean with small decimal numbers."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', '0.001, 0.002, 0.003'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 0.002", result)

    def test_median_duplicates(self):
        """Test median with duplicate values."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'median', '1,2,2,2,3'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 2.0", result)

    def test_range_stats_floats(self):
        """Test range statistics with floating point numbers."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'range_stats', '1.5, 2.7, 3.2, 0.8'
        ))
        self.assertIn("✅", result)
        self.assertIn("Min = 0.8", result)
        self.assertIn("Max = 3.2", result)

    # Input Format Flexibility Tests  
    def test_mixed_spacing(self):
        """Test with mixed comma and space separation."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', '1, 2 ,3,  4,5'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 3.0", result)

    def test_trailing_comma(self):
        """Test with trailing comma in input."""
        result = asyncio.run(self.async_test_helper(
            'calculate_statistics', 'mean', '1,2,3,'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 2.0", result)

if __name__ == '__main__':
    # Run the test suite
    print("Running Consolidated Statistics Test Suite...")
    unittest.main(verbosity=2)
