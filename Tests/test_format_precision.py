"""
Test suite for consolidated format_precision tool.
Tests all precision and rounding operations with parameter-based routing.
"""

import unittest
import asyncio
import sys
import os
import math

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the precision module
import precision

class MockMCP:
    """Mock MCP server for testing purposes."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator

class TestFormatPrecision(unittest.TestCase):
    """Test cases for the consolidated format_precision tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp = MockMCP()
        precision.register_tools(self.mock_mcp)
        self.precision_tool = self.mock_mcp.tools['format_precision']
    
    # Round operation tests
    def test_round_positive(self):
        """Test rounding positive numbers."""
        result = asyncio.run(self.precision_tool("round", 3.14159, 2))
        self.assertIn("✅", result)
        self.assertIn("3.14159 rounded to 2 decimal places = 3.14", result)
        
        result = asyncio.run(self.precision_tool("round", 2.7182818, 4))
        self.assertIn("✅", result)
        self.assertIn("2.7183", result)
    
    def test_round_negative(self):
        """Test rounding negative numbers."""
        result = asyncio.run(self.precision_tool("round", -3.14159, 2))
        self.assertIn("✅", result)
        self.assertIn("-3.14159 rounded to 2 decimal places = -3.14", result)
        
        result = asyncio.run(self.precision_tool("round", -2.7182818, 3))
        self.assertIn("✅", result)
        self.assertIn("-2.718", result)
    
    def test_round_zero_places(self):
        """Test rounding to zero decimal places."""
        result = asyncio.run(self.precision_tool("round", 3.7, 0))
        self.assertIn("✅", result)
        self.assertIn("3.7 rounded to 0 decimal places = 4", result)
        
        result = asyncio.run(self.precision_tool("round", 3.2, 0))
        self.assertIn("✅", result)
        self.assertIn("3.2 rounded to 0 decimal places = 3", result)
    
    def test_round_negative_places_error(self):
        """Test rounding with negative decimal places."""
        result = asyncio.run(self.precision_tool("round", 3.14159, -1))
        self.assertIn("❌", result)
        self.assertIn("Decimal places cannot be negative", result)
    
    def test_round_missing_places_parameter(self):
        """Test round operation without places parameter."""
        result = asyncio.run(self.precision_tool("round", 3.14159))
        self.assertIn("❌", result)
        self.assertIn("'places' parameter required", result)
    
    # Floor operation tests
    def test_floor_positive(self):
        """Test floor with positive numbers."""
        result = asyncio.run(self.precision_tool("floor", 3.9))
        self.assertIn("✅", result)
        self.assertIn("floor(3.9) = 3", result)
        
        result = asyncio.run(self.precision_tool("floor", 5.1))
        self.assertIn("✅", result)
        self.assertIn("floor(5.1) = 5", result)
    
    def test_floor_negative(self):
        """Test floor with negative numbers."""
        result = asyncio.run(self.precision_tool("floor", -3.1))
        self.assertIn("✅", result)
        self.assertIn("floor(-3.1) = -4", result)  # Floor rounds down
        
        result = asyncio.run(self.precision_tool("floor", -2.9))
        self.assertIn("✅", result)
        self.assertIn("floor(-2.9) = -3", result)
    
    def test_floor_integer(self):
        """Test floor with integer values."""
        result = asyncio.run(self.precision_tool("floor", 5.0))
        self.assertIn("✅", result)
        self.assertIn("floor(5.0) = 5", result)
        
        result = asyncio.run(self.precision_tool("floor", -3.0))
        self.assertIn("✅", result)
        self.assertIn("floor(-3.0) = -3", result)
    
    # Ceiling operation tests
    def test_ceiling_positive(self):
        """Test ceiling with positive numbers."""
        result = asyncio.run(self.precision_tool("ceiling", 3.1))
        self.assertIn("✅", result)
        self.assertIn("ceil(3.1) = 4", result)
        
        result = asyncio.run(self.precision_tool("ceiling", 5.9))
        self.assertIn("✅", result)
        self.assertIn("ceil(5.9) = 6", result)
    
    def test_ceiling_negative(self):
        """Test ceiling with negative numbers."""
        result = asyncio.run(self.precision_tool("ceiling", -3.9))
        self.assertIn("✅", result)
        self.assertIn("ceil(-3.9) = -3", result)  # Ceiling rounds up
        
        result = asyncio.run(self.precision_tool("ceiling", -2.1))
        self.assertIn("✅", result)
        self.assertIn("ceil(-2.1) = -2", result)
    
    def test_ceiling_integer(self):
        """Test ceiling with integer values."""
        result = asyncio.run(self.precision_tool("ceiling", 4.0))
        self.assertIn("✅", result)
        self.assertIn("ceil(4.0) = 4", result)
        
        result = asyncio.run(self.precision_tool("ceiling", -7.0))
        self.assertIn("✅", result)
        self.assertIn("ceil(-7.0) = -7", result)
    
    # Truncate operation tests
    def test_truncate_positive(self):
        """Test truncate with positive numbers."""
        result = asyncio.run(self.precision_tool("truncate", 3.9))
        self.assertIn("✅", result)
        self.assertIn("trunc(3.9) = 3", result)
        
        result = asyncio.run(self.precision_tool("truncate", 5.1))
        self.assertIn("✅", result)
        self.assertIn("trunc(5.1) = 5", result)
    
    def test_truncate_negative(self):
        """Test truncate with negative numbers."""
        result = asyncio.run(self.precision_tool("truncate", -3.9))
        self.assertIn("✅", result)
        self.assertIn("trunc(-3.9) = -3", result)  # Truncate toward zero
        
        result = asyncio.run(self.precision_tool("truncate", -2.1))
        self.assertIn("✅", result)
        self.assertIn("trunc(-2.1) = -2", result)
    
    def test_truncate_integer(self):
        """Test truncate with integer values."""
        result = asyncio.run(self.precision_tool("truncate", 6.0))
        self.assertIn("✅", result)
        self.assertIn("trunc(6.0) = 6", result)
        
        result = asyncio.run(self.precision_tool("truncate", -4.0))
        self.assertIn("✅", result)
        self.assertIn("trunc(-4.0) = -4", result)
    
    # Absolute value operation tests
    def test_absolute_positive(self):
        """Test absolute value with positive numbers."""
        result = asyncio.run(self.precision_tool("absolute", 5.7))
        self.assertIn("✅", result)
        self.assertIn("|5.7| = 5.7", result)
        
        result = asyncio.run(self.precision_tool("absolute", 3.14159))
        self.assertIn("✅", result)
        self.assertIn("|3.14159| = 3.14159", result)
    
    def test_absolute_negative(self):
        """Test absolute value with negative numbers."""
        result = asyncio.run(self.precision_tool("absolute", -5.7))
        self.assertIn("✅", result)
        self.assertIn("|-5.7| = 5.7", result)
        
        result = asyncio.run(self.precision_tool("absolute", -3.14159))
        self.assertIn("✅", result)
        self.assertIn("|-3.14159| = 3.14159", result)
    
    def test_absolute_zero(self):
        """Test absolute value with zero."""
        result = asyncio.run(self.precision_tool("absolute", 0))
        self.assertIn("✅", result)
        self.assertIn("|0| = 0", result)
        
        result = asyncio.run(self.precision_tool("absolute", -0))
        self.assertIn("✅", result)
        self.assertIn("|0", result)
    
    def test_absolute_integer(self):
        """Test absolute value with integer values."""
        result = asyncio.run(self.precision_tool("absolute", 42))
        self.assertIn("✅", result)
        self.assertIn("|42| = 42", result)
        
        result = asyncio.run(self.precision_tool("absolute", -42))
        self.assertIn("✅", result)
        self.assertIn("|-42| = 42", result)
    
    # Error handling tests
    def test_invalid_operation(self):
        """Test handling of invalid operations."""
        result = asyncio.run(self.precision_tool("invalid_op", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation 'invalid_op'", result)
        self.assertIn("Available:", result)
        
        result = asyncio.run(self.precision_tool("sqrt", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation 'sqrt'", result)
        
        result = asyncio.run(self.precision_tool("", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation ''", result)
    
    def test_operation_case_sensitivity(self):
        """Test that operations are case sensitive."""
        result = asyncio.run(self.precision_tool("FLOOR", 3.5))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation", result)
        
        result = asyncio.run(self.precision_tool("Floor", 3.5))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation", result)
    
    def test_type_handling(self):
        """Test handling of different numeric types."""
        # Integer input
        result = asyncio.run(self.precision_tool("floor", 10))
        self.assertIn("✅", result)
        
        # Float input
        result = asyncio.run(self.precision_tool("ceiling", 10.5))
        self.assertIn("✅", result)
        
        # Scientific notation
        result = asyncio.run(self.precision_tool("absolute", -1e3))
        self.assertIn("✅", result)
        self.assertIn("1000", result)
    
    def test_edge_cases(self):
        """Test edge cases for precision operations."""
        # Very small numbers
        result = asyncio.run(self.precision_tool("round", 0.0000123, 6))
        self.assertIn("✅", result)
        
        # Very large numbers
        result = asyncio.run(self.precision_tool("floor", 1e6))
        self.assertIn("✅", result)
        
        # Numbers very close to integers
        result = asyncio.run(self.precision_tool("ceiling", 3.000001))
        self.assertIn("✅", result)
        self.assertIn("4", result)
        
        result = asyncio.run(self.precision_tool("floor", 2.999999))
        self.assertIn("✅", result)
        self.assertIn("2", result)

if __name__ == '__main__':
    unittest.main()
