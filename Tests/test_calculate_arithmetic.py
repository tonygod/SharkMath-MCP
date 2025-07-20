"""
Test Suite for Calculate Arithmetic Consolidated Tool
Tests all arithmetic and power operations in the consolidated calculate_arithmetic tool.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import asyncio
from arithmetic import register_tools

class TestCalculateArithmetic(unittest.TestCase):
    """Test suite for the consolidated calculate_arithmetic tool."""
    
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
        """Helper to run the calculate_arithmetic tool function in tests."""
        if 'calculate_arithmetic' in self.mock_mcp.tools:
            return await self.mock_mcp.tools['calculate_arithmetic'](*args, **kwargs)
        else:
            raise ValueError("calculate_arithmetic tool not found")
    
    # Basic Arithmetic Operations Tests
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = asyncio.run(self.async_test_helper(
            'add', 47.0, 293.0
        ))
        self.assertIn("✅", result)
        self.assertIn("340", result)
        self.assertIn("47.0 + 293.0 = 340", result)
        
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = asyncio.run(self.async_test_helper(
            'add', -15.0, 25.0
        ))
        self.assertIn("✅", result)
        self.assertIn("10", result)
        
    def test_subtract_positive_result(self):
        """Test subtraction with positive result."""
        result = asyncio.run(self.async_test_helper(
            'subtract', 100.0, 23.0
        ))
        self.assertIn("✅", result)
        self.assertIn("77", result)
        self.assertIn("100.0 - 23.0 = 77", result)
        
    def test_subtract_negative_result(self):
        """Test subtraction with negative result."""
        result = asyncio.run(self.async_test_helper(
            'subtract', 50.0, 75.0
        ))
        self.assertIn("✅", result)
        self.assertIn("-25", result)
        
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        result = asyncio.run(self.async_test_helper(
            'multiply', 12.0, 8.0
        ))
        self.assertIn("✅", result)
        self.assertIn("96", result)
        self.assertIn("12.0 × 8.0 = 96", result)
        
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = asyncio.run(self.async_test_helper(
            'multiply', 42.0, 0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("0", result)
        
    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        result = asyncio.run(self.async_test_helper(
            'multiply', -6.0, -7.0
        ))
        self.assertIn("✅", result)
        self.assertIn("42", result)
        
    def test_divide_exact_division(self):
        """Test exact division."""
        result = asyncio.run(self.async_test_helper(
            'divide', 84.0, 12.0
        ))
        self.assertIn("✅", result)
        self.assertIn("7", result)
        self.assertIn("84.0 ÷ 12.0 = 7", result)
        
    def test_divide_with_decimal_result(self):
        """Test division with decimal result."""
        result = asyncio.run(self.async_test_helper(
            'divide', 10.0, 3.0
        ))
        self.assertIn("✅", result)
        self.assertIn("3.333", result)
        
    def test_divide_by_zero_error(self):
        """Test division by zero error handling."""
        result = asyncio.run(self.async_test_helper(
            'divide', 10.0, 0.0
        ))
        self.assertIn("❌", result)
        self.assertIn("Cannot divide by zero", result)
        
    # Expression Calculation Tests
    def test_calculate_simple_expression(self):
        """Test simple expression calculation."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='2 + 3 * 4'
        ))
        self.assertIn("✅", result)
        self.assertIn("14", result)
        self.assertIn("2 + 3 * 4 = 14", result)
        
    def test_calculate_parentheses_expression(self):
        """Test expression with parentheses."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='(2 + 3) * 4'
        ))
        self.assertIn("✅", result)
        self.assertIn("20", result)
        
    def test_calculate_decimal_expression(self):
        """Test expression with decimal numbers."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='10.5 / 2.5'
        ))
        self.assertIn("✅", result)
        self.assertIn("4.2", result)
        
    def test_calculate_division_by_zero_in_expression(self):
        """Test division by zero in expression."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='10 / 0'
        ))
        self.assertIn("❌", result)
        self.assertIn("Division by zero", result)
        
    def test_calculate_invalid_expression_syntax(self):
        """Test invalid expression syntax."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='2 +* 3'
        ))
        self.assertIn("❌", result)
        self.assertIn("Invalid mathematical expression", result)
        
    def test_calculate_invalid_characters(self):
        """Test expression with invalid characters."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='2 + abc'
        ))
        self.assertIn("❌", result)
        self.assertIn("invalid characters", result)
        
    # Power Operations Tests
    def test_power_positive_integers(self):
        """Test power with positive integers."""
        result = asyncio.run(self.async_test_helper(
            'power', base=2.0, exponent=8.0
        ))
        self.assertIn("✅", result)
        self.assertIn("256", result)
        self.assertIn("2.0^8.0 = 256", result)
        
    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        result = asyncio.run(self.async_test_helper(
            'power', base=16.0, exponent=0.5
        ))
        self.assertIn("✅", result)
        self.assertIn("4", result)
        
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        result = asyncio.run(self.async_test_helper(
            'power', base=5.0, exponent=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("1", result)
        
    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        result = asyncio.run(self.async_test_helper(
            'power', base=2.0, exponent=-3.0
        ))
        self.assertIn("✅", result)
        self.assertIn("0.125", result)
        
    def test_square_positive_number(self):
        """Test square of positive number."""
        result = asyncio.run(self.async_test_helper(
            'square', n=9.0
        ))
        self.assertIn("✅", result)
        self.assertIn("81", result)
        self.assertIn("9.0² = 81", result)
        
    def test_square_negative_number(self):
        """Test square of negative number."""
        result = asyncio.run(self.async_test_helper(
            'square', n=-7.0
        ))
        self.assertIn("✅", result)
        self.assertIn("49", result)
        
    def test_square_decimal(self):
        """Test square of decimal number."""
        result = asyncio.run(self.async_test_helper(
            'square', n=2.5
        ))
        self.assertIn("✅", result)
        self.assertIn("6.25", result)
        
    def test_cube_positive_number(self):
        """Test cube of positive number."""
        result = asyncio.run(self.async_test_helper(
            'cube', n=4.0
        ))
        self.assertIn("✅", result)
        self.assertIn("64", result)
        self.assertIn("4.0³ = 64", result)
        
    def test_cube_negative_number(self):
        """Test cube of negative number."""
        result = asyncio.run(self.async_test_helper(
            'cube', n=-3.0
        ))
        self.assertIn("✅", result)
        self.assertIn("-27", result)
        
    # Root Operations Tests
    def test_square_root_perfect_square(self):
        """Test square root of perfect square."""
        result = asyncio.run(self.async_test_helper(
            'square_root', n=25.0
        ))
        self.assertIn("✅", result)
        self.assertIn("5", result)
        self.assertIn("√25.0 = 5", result)
        
    def test_square_root_non_perfect_square(self):
        """Test square root of non-perfect square."""
        result = asyncio.run(self.async_test_helper(
            'square_root', n=10.0
        ))
        self.assertIn("✅", result)
        self.assertIn("3.162", result)
        
    def test_square_root_zero(self):
        """Test square root of zero."""
        result = asyncio.run(self.async_test_helper(
            'square_root', n=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("0", result)
        
    def test_square_root_negative_error(self):
        """Test square root of negative number error."""
        result = asyncio.run(self.async_test_helper(
            'square_root', n=-25.0
        ))
        self.assertIn("❌", result)
        self.assertIn("negative number", result)
        
    def test_cube_root_positive(self):
        """Test cube root of positive number."""
        result = asyncio.run(self.async_test_helper(
            'cube_root', n=27.0
        ))
        self.assertIn("✅", result)
        self.assertIn("3", result)
        self.assertIn("∛27.0 = 3", result)
        
    def test_cube_root_negative(self):
        """Test cube root of negative number."""
        result = asyncio.run(self.async_test_helper(
            'cube_root', n=-8.0
        ))
        self.assertIn("✅", result)
        self.assertIn("-2", result)
        
    def test_nth_root_fourth_root(self):
        """Test fourth root calculation."""
        result = asyncio.run(self.async_test_helper(
            'nth_root', n=16.0, root=4.0
        ))
        self.assertIn("✅", result)
        self.assertIn("2", result)
        self.assertIn("16.0^(1/4.0) = 2", result)
        
    def test_nth_root_odd_root_negative(self):
        """Test odd root of negative number."""
        result = asyncio.run(self.async_test_helper(
            'nth_root', n=-8.0, root=3.0
        ))
        self.assertIn("✅", result)
        self.assertIn("-2", result)
        
    def test_nth_root_even_root_negative_error(self):
        """Test even root of negative number error."""
        result = asyncio.run(self.async_test_helper(
            'nth_root', n=-16.0, root=4.0
        ))
        self.assertIn("❌", result)
        self.assertIn("even root", result)
        self.assertIn("negative number", result)
        
    def test_nth_root_zero_root_error(self):
        """Test nth root with zero root error."""
        result = asyncio.run(self.async_test_helper(
            'nth_root', n=16.0, root=0.0
        ))
        self.assertIn("❌", result)
        self.assertIn("Root cannot be zero", result)
        
    # Parameter Validation Tests
    def test_invalid_operation(self):
        """Test invalid operation error handling."""
        result = asyncio.run(self.async_test_helper(
            'invalid_operation', 1.0, 2.0
        ))
        self.assertIn("❌", result)
        self.assertIn("not supported", result)
        self.assertIn("invalid_operation", result)
        
    def test_missing_parameters_add(self):
        """Test missing parameters for add operation."""
        result = asyncio.run(self.async_test_helper(
            'add', 5.0
        ))
        self.assertIn("❌", result)
        self.assertIn("requires parameters 'a' and 'b'", result)
        
    def test_missing_parameters_power(self):
        """Test missing parameters for power operation."""
        result = asyncio.run(self.async_test_helper(
            'power', base=2.0
        ))
        self.assertIn("❌", result)
        self.assertIn("requires parameters 'base' and 'exponent'", result)
        
    def test_missing_expression_parameter(self):
        """Test missing expression parameter for calculate."""
        result = asyncio.run(self.async_test_helper(
            'calculate'
        ))
        self.assertIn("❌", result)
        self.assertIn("requires parameter 'expression'", result)
        
    def test_missing_n_parameter(self):
        """Test missing n parameter for square operation."""
        result = asyncio.run(self.async_test_helper(
            'square'
        ))
        self.assertIn("❌", result)
        self.assertIn("requires parameter 'n'", result)
        
    # Edge Cases and Boundary Tests
    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        result = asyncio.run(self.async_test_helper(
            'add', 1e10, 2e10
        ))
        self.assertIn("✅", result)
        # Accept either scientific notation or full number representation
        self.assertTrue("3e+10" in result or "30000000000" in result)
        
    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        result = asyncio.run(self.async_test_helper(
            'multiply', 1e-10, 2e-10
        ))
        self.assertIn("✅", result)
        
    def test_power_overflow_protection(self):
        """Test power operation overflow protection."""
        result = asyncio.run(self.async_test_helper(
            'power', base=10.0, exponent=1000.0
        ))
        # Should either succeed or give overflow error
        self.assertTrue("✅" in result or "❌" in result)
        if "❌" in result:
            self.assertIn("too large", result.lower())

class TestArithmeticToolIntegration(unittest.TestCase):
    """Integration tests for the arithmetic tool class itself."""
    
    def setUp(self):
        """Set up arithmetic tool for direct testing."""
        from arithmetic import ArithmeticTool
        self.tool = ArithmeticTool()
        
    def test_supported_operations_list(self):
        """Test that all expected operations are supported."""
        operations = self.tool.get_supported_operations()
        expected_operations = [
            'add', 'subtract', 'multiply', 'divide', 'calculate',
            'power', 'square', 'cube', 'square_root', 'cube_root', 'nth_root'
        ]
        
        for op in expected_operations:
            self.assertIn(op, operations, f"Operation '{op}' not found in supported operations")
            
    def test_operation_count(self):
        """Test that we have the expected number of operations."""
        operations = self.tool.get_supported_operations()
        self.assertEqual(len(operations), 11, f"Expected 11 operations, got {len(operations)}")


if __name__ == '__main__':
    # Run the test suite
    print("Running Calculate Arithmetic Test Suite...")
    print("=" * 60)
    unittest.main(verbosity=2)
