"""
Test suite for consolidated calculate_logarithmic tool.
Tests all logarithmic and exponential operations with parameter-based routing.
"""

import unittest
import asyncio
import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the logarithmic module
import logarithmic

class MockMCP:
    """Mock MCP server for testing purposes."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator

class TestCalculateLogarithmic(unittest.TestCase):
    """Test cases for the consolidated calculate_logarithmic tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp = MockMCP()
        logarithmic.register_tools(self.mock_mcp)
        self.logarithmic_tool = self.mock_mcp.tools['calculate_logarithmic']
    
    def test_natural_log_positive(self):
        """Test natural logarithm with positive values."""
        result = asyncio.run(self.logarithmic_tool("natural_log", 2.718281828459045))
        self.assertIn("✅", result)
        self.assertIn("ln(", result)
        
        result = asyncio.run(self.logarithmic_tool("natural_log", 1))
        self.assertIn("✅", result)
        self.assertIn("0", result)  # ln(1) = 0
        
        result = asyncio.run(self.logarithmic_tool("natural_log", 10))
        self.assertIn("✅", result)
        self.assertIn("ln(10)", result)
    
    def test_natural_log_domain_validation(self):
        """Test natural logarithm domain validation (n > 0)."""
        result = asyncio.run(self.logarithmic_tool("natural_log", 0))
        self.assertIn("❌", result)
        self.assertIn("undefined for n ≤ 0", result)
        
        result = asyncio.run(self.logarithmic_tool("natural_log", -1))
        self.assertIn("❌", result)
        self.assertIn("undefined for n ≤ 0", result)
        
        result = asyncio.run(self.logarithmic_tool("natural_log", -10.5))
        self.assertIn("❌", result)
        self.assertIn("undefined for n ≤ 0", result)
    
    def test_log_base_10_positive(self):
        """Test base-10 logarithm with positive values."""
        result = asyncio.run(self.logarithmic_tool("log_base_10", 10))
        self.assertIn("✅", result)
        self.assertIn("1", result)  # log₁₀(10) = 1
        
        result = asyncio.run(self.logarithmic_tool("log_base_10", 100))
        self.assertIn("✅", result)
        self.assertIn("2", result)  # log₁₀(100) = 2
        
        result = asyncio.run(self.logarithmic_tool("log_base_10", 1))
        self.assertIn("✅", result)
        self.assertIn("0", result)  # log₁₀(1) = 0
    
    def test_log_base_10_domain_validation(self):
        """Test base-10 logarithm domain validation (n > 0)."""
        result = asyncio.run(self.logarithmic_tool("log_base_10", 0))
        self.assertIn("❌", result)
        self.assertIn("undefined for n ≤ 0", result)
        
        result = asyncio.run(self.logarithmic_tool("log_base_10", -5))
        self.assertIn("❌", result)
        self.assertIn("undefined for n ≤ 0", result)
    
    def test_log_base_custom(self):
        """Test logarithm with custom base."""
        result = asyncio.run(self.logarithmic_tool("log_base", 8, 2))
        self.assertIn("✅", result)
        self.assertIn("3", result)  # log₂(8) = 3
        
        result = asyncio.run(self.logarithmic_tool("log_base", 27, 3))
        self.assertIn("✅", result)
        self.assertIn("3", result)  # log₃(27) = 3
        
        result = asyncio.run(self.logarithmic_tool("log_base", 1, 5))
        self.assertIn("✅", result)
        self.assertIn("0", result)  # log₅(1) = 0
    
    def test_log_base_domain_validation(self):
        """Test custom base logarithm domain validation."""
        # Invalid value (n <= 0)
        result = asyncio.run(self.logarithmic_tool("log_base", 0, 2))
        self.assertIn("❌", result)
        self.assertIn("undefined for n ≤ 0", result)
        
        result = asyncio.run(self.logarithmic_tool("log_base", -1, 2))
        self.assertIn("❌", result)
        self.assertIn("undefined for n ≤ 0", result)
        
        # Invalid base (base <= 0)
        result = asyncio.run(self.logarithmic_tool("log_base", 10, 0))
        self.assertIn("❌", result)
        self.assertIn("base must be positive", result)
        
        result = asyncio.run(self.logarithmic_tool("log_base", 10, -2))
        self.assertIn("❌", result)
        self.assertIn("base must be positive", result)
        
        # Invalid base (base = 1)
        result = asyncio.run(self.logarithmic_tool("log_base", 10, 1))
        self.assertIn("❌", result)
        self.assertIn("not equal to 1", result)
    
    def test_log_base_missing_parameter(self):
        """Test log_base operation without base parameter."""
        result = asyncio.run(self.logarithmic_tool("log_base", 10))
        self.assertIn("❌", result)
        self.assertIn("'base' parameter required", result)
    
    def test_exponential_positive(self):
        """Test exponential function with positive values."""
        result = asyncio.run(self.logarithmic_tool("exponential", 0))
        self.assertIn("✅", result)
        self.assertIn("1", result)  # e^0 = 1
        
        result = asyncio.run(self.logarithmic_tool("exponential", 1))
        self.assertIn("✅", result)
        self.assertIn("e^1", result)
        
        result = asyncio.run(self.logarithmic_tool("exponential", 2))
        self.assertIn("✅", result)
        self.assertIn("e^2", result)
    
    def test_exponential_negative(self):
        """Test exponential function with negative values."""
        result = asyncio.run(self.logarithmic_tool("exponential", -1))
        self.assertIn("✅", result)
        self.assertIn("e^-1", result)
        
        result = asyncio.run(self.logarithmic_tool("exponential", -5))
        self.assertIn("✅", result)
        self.assertIn("e^-5", result)
    
    def test_exponential_overflow_protection(self):
        """Test exponential function overflow protection."""
        result = asyncio.run(self.logarithmic_tool("exponential", 701))
        self.assertIn("❌", result)
        self.assertIn("overflow for n > 700", result)
        
        result = asyncio.run(self.logarithmic_tool("exponential", 1000))
        self.assertIn("❌", result)
        self.assertIn("overflow for n > 700", result)
    
    def test_exponential_boundary(self):
        """Test exponential function at boundary values."""
        result = asyncio.run(self.logarithmic_tool("exponential", 700))
        self.assertIn("✅", result)  # Should work at boundary
        self.assertIn("e^700", result)
        
        result = asyncio.run(self.logarithmic_tool("exponential", -700))
        self.assertIn("✅", result)  # Negative values are fine
        self.assertIn("e^-700", result)
    
    def test_invalid_operation(self):
        """Test handling of invalid operations."""
        result = asyncio.run(self.logarithmic_tool("invalid_op", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation 'invalid_op'", result)
        self.assertIn("Available:", result)
        
        result = asyncio.run(self.logarithmic_tool("log", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation 'log'", result)
        
        result = asyncio.run(self.logarithmic_tool("", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation ''", result)
    
    def test_operation_case_sensitivity(self):
        """Test that operations are case sensitive."""
        result = asyncio.run(self.logarithmic_tool("NATURAL_LOG", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation", result)
        
        result = asyncio.run(self.logarithmic_tool("Natural_Log", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation", result)
    
    def test_type_handling(self):
        """Test handling of different numeric types."""
        # Integer input
        result = asyncio.run(self.logarithmic_tool("natural_log", 10))
        self.assertIn("✅", result)
        
        # Float input
        result = asyncio.run(self.logarithmic_tool("natural_log", 10.5))
        self.assertIn("✅", result)
        
        # Scientific notation
        result = asyncio.run(self.logarithmic_tool("natural_log", 1e2))
        self.assertIn("✅", result)

if __name__ == '__main__':
    unittest.main()
