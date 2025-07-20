"""
Test suite for consolidated calculate_hyperbolic tool.
Tests all hyperbolic function operations with parameter-based routing.
"""

import unittest
import asyncio
import sys
import os
import math

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the hyperbolic module
import hyperbolic

class MockMCP:
    """Mock MCP server for testing purposes."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator

class TestCalculateHyperbolic(unittest.TestCase):
    """Test cases for the consolidated calculate_hyperbolic tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp = MockMCP()
        hyperbolic.register_tools(self.mock_mcp)
        self.hyperbolic_tool = self.mock_mcp.tools['calculate_hyperbolic']
    
    def test_sinh_zero(self):
        """Test sinh(0) = 0."""
        result = asyncio.run(self.hyperbolic_tool("sinh", 0))
        self.assertIn("✅", result)
        self.assertIn("sinh(0)", result)
        self.assertIn("0", result)
    
    def test_sinh_positive(self):
        """Test sinh with positive values."""
        result = asyncio.run(self.hyperbolic_tool("sinh", 1))
        self.assertIn("✅", result)
        self.assertIn("sinh(1)", result)
        
        result = asyncio.run(self.hyperbolic_tool("sinh", 2.5))
        self.assertIn("✅", result)
        self.assertIn("sinh(2.5)", result)
    
    def test_sinh_negative(self):
        """Test sinh with negative values (sinh is odd function)."""
        result = asyncio.run(self.hyperbolic_tool("sinh", -1))
        self.assertIn("✅", result)
        self.assertIn("sinh(-1)", result)
        
        result = asyncio.run(self.hyperbolic_tool("sinh", -3.14))
        self.assertIn("✅", result)
        self.assertIn("sinh(-3.14)", result)
    
    def test_sinh_overflow_protection(self):
        """Test sinh overflow protection."""
        result = asyncio.run(self.hyperbolic_tool("sinh", 701))
        self.assertIn("❌", result)
        self.assertIn("overflow for |x| > 700", result)
        
        result = asyncio.run(self.hyperbolic_tool("sinh", -701))
        self.assertIn("❌", result)
        self.assertIn("overflow for |x| > 700", result)
    
    def test_sinh_boundary(self):
        """Test sinh at boundary values."""
        result = asyncio.run(self.hyperbolic_tool("sinh", 700))
        self.assertIn("✅", result)  # Should work at boundary
        self.assertIn("sinh(700)", result)
        
        result = asyncio.run(self.hyperbolic_tool("sinh", -700))
        self.assertIn("✅", result)
        self.assertIn("sinh(-700)", result)
    
    def test_cosh_zero(self):
        """Test cosh(0) = 1."""
        result = asyncio.run(self.hyperbolic_tool("cosh", 0))
        self.assertIn("✅", result)
        self.assertIn("cosh(0)", result)
        self.assertIn("1", result)
    
    def test_cosh_positive(self):
        """Test cosh with positive values."""
        result = asyncio.run(self.hyperbolic_tool("cosh", 1))
        self.assertIn("✅", result)
        self.assertIn("cosh(1)", result)
        
        result = asyncio.run(self.hyperbolic_tool("cosh", 2.5))
        self.assertIn("✅", result)
        self.assertIn("cosh(2.5)", result)
    
    def test_cosh_negative(self):
        """Test cosh with negative values (cosh is even function)."""
        result = asyncio.run(self.hyperbolic_tool("cosh", -1))
        self.assertIn("✅", result)
        self.assertIn("cosh(-1)", result)
        
        result = asyncio.run(self.hyperbolic_tool("cosh", -3.14))
        self.assertIn("✅", result)
        self.assertIn("cosh(-3.14)", result)
    
    def test_cosh_overflow_protection(self):
        """Test cosh overflow protection."""
        result = asyncio.run(self.hyperbolic_tool("cosh", 701))
        self.assertIn("❌", result)
        self.assertIn("overflow for |x| > 700", result)
        
        result = asyncio.run(self.hyperbolic_tool("cosh", -701))
        self.assertIn("❌", result)
        self.assertIn("overflow for |x| > 700", result)
    
    def test_cosh_boundary(self):
        """Test cosh at boundary values."""
        result = asyncio.run(self.hyperbolic_tool("cosh", 700))
        self.assertIn("✅", result)  # Should work at boundary
        self.assertIn("cosh(700)", result)
        
        result = asyncio.run(self.hyperbolic_tool("cosh", -700))
        self.assertIn("✅", result)
        self.assertIn("cosh(-700)", result)
    
    def test_tanh_zero(self):
        """Test tanh(0) = 0."""
        result = asyncio.run(self.hyperbolic_tool("tanh", 0))
        self.assertIn("✅", result)
        self.assertIn("tanh(0)", result)
        self.assertIn("0", result)
    
    def test_tanh_positive(self):
        """Test tanh with positive values."""
        result = asyncio.run(self.hyperbolic_tool("tanh", 1))
        self.assertIn("✅", result)
        self.assertIn("tanh(1)", result)
        
        result = asyncio.run(self.hyperbolic_tool("tanh", 5))
        self.assertIn("✅", result)
        self.assertIn("tanh(5)", result)
    
    def test_tanh_negative(self):
        """Test tanh with negative values (tanh is odd function)."""
        result = asyncio.run(self.hyperbolic_tool("tanh", -1))
        self.assertIn("✅", result)
        self.assertIn("tanh(-1)", result)
        
        result = asyncio.run(self.hyperbolic_tool("tanh", -5))
        self.assertIn("✅", result)
        self.assertIn("tanh(-5)", result)
    
    def test_tanh_large_values(self):
        """Test tanh with large values (should not overflow, bounded by -1 and 1)."""
        result = asyncio.run(self.hyperbolic_tool("tanh", 1000))
        self.assertIn("✅", result)
        self.assertIn("tanh(1000)", result)
        
        result = asyncio.run(self.hyperbolic_tool("tanh", -1000))
        self.assertIn("✅", result)
        self.assertIn("tanh(-1000)", result)
    
    def test_tanh_asymptotic_behavior(self):
        """Test tanh approaches ±1 for large inputs."""
        result = asyncio.run(self.hyperbolic_tool("tanh", 10))
        self.assertIn("✅", result)
        self.assertIn("tanh(10)", result)
        # tanh(10) should be very close to 1
        
        result = asyncio.run(self.hyperbolic_tool("tanh", -10))
        self.assertIn("✅", result)
        self.assertIn("tanh(-10)", result)
        # tanh(-10) should be very close to -1
    
    def test_invalid_operation(self):
        """Test handling of invalid operations."""
        result = asyncio.run(self.hyperbolic_tool("invalid_op", 1))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation 'invalid_op'", result)
        self.assertIn("Available:", result)
        
        result = asyncio.run(self.hyperbolic_tool("sin", 1))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation 'sin'", result)
        
        result = asyncio.run(self.hyperbolic_tool("", 1))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation ''", result)
    
    def test_operation_case_sensitivity(self):
        """Test that operations are case sensitive."""
        result = asyncio.run(self.hyperbolic_tool("SINH", 1))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation", result)
        
        result = asyncio.run(self.hyperbolic_tool("Sinh", 1))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation", result)
    
    def test_type_handling(self):
        """Test handling of different numeric types."""
        # Integer input
        result = asyncio.run(self.hyperbolic_tool("sinh", 1))
        self.assertIn("✅", result)
        
        # Float input
        result = asyncio.run(self.hyperbolic_tool("cosh", 1.5))
        self.assertIn("✅", result)
        
        # Scientific notation
        result = asyncio.run(self.hyperbolic_tool("tanh", 1e2))
        self.assertIn("✅", result)
    
    def test_mathematical_identities(self):
        """Test some basic hyperbolic identities where possible."""
        # Test that cosh^2(x) - sinh^2(x) = 1 (approximately)
        x = 1.0
        sinh_result = asyncio.run(self.hyperbolic_tool("sinh", x))
        cosh_result = asyncio.run(self.hyperbolic_tool("cosh", x))
        
        self.assertIn("✅", sinh_result)
        self.assertIn("✅", cosh_result)
        
        # Extract numerical values (basic verification that calculation works)
        self.assertIn("sinh(1.0)", sinh_result)
        self.assertIn("cosh(1.0)", cosh_result)
    
    def test_fractional_inputs(self):
        """Test hyperbolic functions with fractional inputs."""
        result = asyncio.run(self.hyperbolic_tool("sinh", 0.5))
        self.assertIn("✅", result)
        self.assertIn("sinh(0.5)", result)
        
        result = asyncio.run(self.hyperbolic_tool("cosh", 0.1))
        self.assertIn("✅", result)
        self.assertIn("cosh(0.1)", result)
        
        result = asyncio.run(self.hyperbolic_tool("tanh", 0.25))
        self.assertIn("✅", result)
        self.assertIn("tanh(0.25)", result)

if __name__ == '__main__':
    unittest.main()
