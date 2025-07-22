"""
Test Suite for Solve Equations Consolidated Tool
Tests equation-solving functionality including quadratic and linear equations.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import asyncio
from solve_equations import register_tools

class TestSolveEquations(unittest.TestCase):
    """Test suite for the consolidated solve_equations tool."""
    
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
        
    async def async_test_helper(self, *args, **kwargs):
        """Helper to run the solve_equations tool function in tests."""
        if 'solve_equations' in self.mock_mcp.tools:
            return await self.mock_mcp.tools['solve_equations'](*args, **kwargs)
        else:
            raise ValueError("solve_equations tool not found")
    
    # Quadratic Equation Tests
    def test_quadratic_two_real_solutions(self):
        """Test quadratic equation with two distinct real solutions."""
        # x² - 5x + 6 = 0  (solutions: x = 2, 3)
        result = asyncio.run(self.async_test_helper(
            'quadratic', 1.0, -5.0, 6.0
        ))
        self.assertIn("✅", result)
        self.assertIn("Two real solutions", result)
        self.assertIn("3.0", result)
        self.assertIn("2.0", result)
        
    def test_quadratic_one_repeated_solution(self):
        """Test quadratic equation with one repeated real solution."""
        # x² - 6x + 9 = 0  (solution: x = 3)
        result = asyncio.run(self.async_test_helper(
            'quadratic', 1.0, -6.0, 9.0
        ))
        self.assertIn("✅", result)
        self.assertIn("One repeated real solution", result)
        self.assertIn("3.0", result)
        
    def test_quadratic_complex_solutions(self):
        """Test quadratic equation with complex solutions."""
        # x² + x + 1 = 0  (discriminant < 0)
        result = asyncio.run(self.async_test_helper(
            'quadratic', 1.0, 1.0, 1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("complex solutions", result)
        
    def test_quadratic_reduces_to_linear(self):
        """Test when a=0, equation reduces to linear."""
        # 0x² + 2x + 4 = 0  → 2x + 4 = 0  → x = -2
        result = asyncio.run(self.async_test_helper(
            'quadratic', 0.0, 2.0, 4.0
        ))
        self.assertIn("✅", result)
        self.assertIn("Linear equation solution", result)
        self.assertIn("-2", result)
        
    def test_quadratic_identity(self):
        """Test when equation is an identity (0 = 0)."""
        result = asyncio.run(self.async_test_helper(
            'quadratic', 0.0, 0.0, 0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("All real numbers are solutions", result)
        
    def test_quadratic_no_solution(self):
        """Test when equation has no solution."""
        # 0x² + 0x + 5 = 0  → 5 = 0 (impossible)
        result = asyncio.run(self.async_test_helper(
            'quadratic', 0.0, 0.0, 5.0
        ))
        self.assertIn("❌", result)
        self.assertIn("No solution exists", result)
        
    def test_quadratic_missing_parameters(self):
        """Test quadratic equation with missing parameters."""
        result = asyncio.run(self.async_test_helper(
            'quadratic', 1.0, 2.0
        ))
        self.assertIn("❌", result)
        self.assertIn("requires parameters: a, b, c", result)
        
    # Linear Equation Tests
    def test_linear_positive_solution(self):
        """Test linear equation with positive solution."""
        # 3x + 6 = 0  → x = -2
        result = asyncio.run(self.async_test_helper(
            'linear', 3.0, 6.0
        ))
        self.assertIn("✅", result)
        self.assertIn("Linear equation solution", result)
        self.assertIn("-2", result)
        
    def test_linear_negative_solution(self):
        """Test linear equation with negative solution."""
        # -2x + 8 = 0  → x = 4
        result = asyncio.run(self.async_test_helper(
            'linear', -2.0, 8.0
        ))
        self.assertIn("✅", result)
        self.assertIn("Linear equation solution", result)
        self.assertIn("4", result)
        
    def test_linear_fractional_solution(self):
        """Test linear equation with fractional solution."""
        # 2x + 1 = 0  → x = -0.5
        result = asyncio.run(self.async_test_helper(
            'linear', 2.0, 1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("Linear equation solution", result)
        self.assertIn("-0.5", result)
        
    def test_linear_zero_coefficient(self):
        """Test linear equation where coefficient is zero."""
        # 0x + 5 = 0  → 5 = 0 (impossible)
        result = asyncio.run(self.async_test_helper(
            'linear', 0.0, 5.0
        ))
        self.assertIn("❌", result)
        self.assertIn("No solution", result)
        
    def test_linear_identity(self):
        """Test linear equation that is an identity."""
        # 0x + 0 = 0  → 0 = 0 (always true)
        result = asyncio.run(self.async_test_helper(
            'linear', 0.0, 0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("All real numbers", result)
        
    def test_linear_missing_parameters(self):
        """Test linear equation with missing parameters."""
        result = asyncio.run(self.async_test_helper(
            'linear', 3.0
        ))
        self.assertIn("❌", result)
        self.assertIn("requires parameters: a, b", result)
        
    # Error Handling Tests
    def test_invalid_equation_type(self):
        """Test invalid equation type."""
        result = asyncio.run(self.async_test_helper(
            'cubic', 1.0, 2.0, 3.0
        ))
        self.assertIn("❌", result)
        self.assertIn("Invalid equation type", result)
        self.assertIn("cubic", result)
        
    def test_empty_equation_type(self):
        """Test empty equation type."""
        result = asyncio.run(self.async_test_helper(
            '', 1.0, 2.0, 3.0
        ))
        self.assertIn("❌", result)
        self.assertIn("Invalid equation type", result)

if __name__ == '__main__':
    unittest.main()
