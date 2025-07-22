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
            'calculate', expression='2 + $invalid'
        ))
        self.assertIn("❌", result)
        self.assertIn("invalid characters", result)
    
    # Enhanced Character Validation Tests
    def test_enhanced_character_validation_allows_letters(self):
        """Test that enhanced character validation allows letters and additional operators."""
        # Test that letters are now allowed (though will cause NameError during evaluation)
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='abc'
        ))
        self.assertIn("❌", result)
        # Should get NameError, not character validation error
        self.assertNotIn("invalid characters", result)
        
    def test_enhanced_character_validation_rejects_dangerous_characters(self):
        """Test that enhanced character validation still rejects dangerous characters."""
        invalid_chars_tests = [
            ("2+3$", "$"),
            ("hello@world", "@"),  
            ("2#3", "#"),
            ("test%case", "%"),
        ]
        
        for expression, invalid_char in invalid_chars_tests:
            with self.subTest(expression=expression, invalid_char=invalid_char):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("❌", result)
                self.assertIn("invalid characters", result)
                self.assertIn(invalid_char, result)
    
    def test_exponentiation_caret_operator_basic(self):
        """Test basic exponentiation with ^ operator."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='2^3'
        ))
        self.assertIn("✅", result)
        self.assertIn("8", result)
        self.assertIn("2^3 = 8", result)
        
    def test_exponentiation_caret_operator_complex(self):
        """Test complex exponentiation expressions with ^ operator."""
        test_cases = [
            ("3^2", "9"),           # Basic exponentiation
            ("(2+3)^2", "25"),      # Parentheses with exponentiation
            ("2*3^2", "18"),        # Mixed operations
            ("2^3+1", "9"),         # Addition after exponentiation
            ("10^2-1", "99"),       # Subtraction after exponentiation
            ("4^0.5", "2"),         # Fractional exponent (square root)
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                self.assertIn(expected, result)
                self.assertIn(f"{expression} = {expected}", result)
    
    def test_exponentiation_operator_equivalence(self):
        """Test that ^ and ** operators give same results."""
        test_pairs = [
            ("2^3", "2**3"),
            ("3^2", "3**2"),
            ("(4+1)^2", "(4+1)**2"),
        ]
        
        for caret_expr, asterisk_expr in test_pairs:
            with self.subTest(caret=caret_expr, asterisk=asterisk_expr):
                result1 = asyncio.run(self.async_test_helper(
                    'calculate', expression=caret_expr
                ))
                result2 = asyncio.run(self.async_test_helper(
                    'calculate', expression=asterisk_expr
                ))
                
                # Both should succeed
                self.assertIn("✅", result1)
                self.assertIn("✅", result2)
                
                # Extract the numeric results for comparison
                import re
                match1 = re.search(r'= ([\d.]+)', result1)
                match2 = re.search(r'= ([\d.]+)', result2)
                
                if match1 and match2:
                    value1 = float(match1.group(1))
                    value2 = float(match2.group(1))
                    self.assertAlmostEqual(value1, value2, places=10)
    
    def test_exponentiation_nested_right_associative(self):
        """Test nested exponentiation is right associative."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='2^3^2'
        ))
        self.assertIn("✅", result)
        # 2^3^2 = 2^(3^2) = 2^9 = 512 (right associative)
        self.assertIn("512", result)
    
    def test_expression_backward_compatibility(self):
        """Test that existing functionality still works after enhancements."""
        test_cases = [
            ("2+3", "5"),
            ("10-4", "6"), 
            ("3*4", "12"),
            ("15/3", "5"),
            ("(2+3)*4", "20"),
            ("2**3", "8"),  # Existing ** support unchanged
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                self.assertIn(expected, result)
    
    # Phase 1.3 Mathematical Functions Tests
    def test_basic_functions(self):
        """Test Phase 1.3 basic mathematical functions."""
        test_cases = [
            ("sqrt(25)", "5"),
            ("pow(2, 3)", "8"),
            ("abs(-5)", "5"),
            ("round(3.7)", "4"),
            ("abs(5)", "5"),
            ("round(3.2)", "3"),
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                self.assertIn(expected, result)
    
    def test_trigonometric_functions(self):
        """Test Phase 1.3 trigonometric functions."""
        test_cases = [
            ("sin(0)", "0"),
            ("cos(0)", "1"),
            ("tan(0)", "0"),
            ("sin(pi/2)", "1"),
            ("cos(pi/2)", "6.123233995736766e-17"),  # Very close to 0 due to floating point precision
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                if expected != "6.123233995736766e-17":  # Special case for cos(pi/2)
                    self.assertIn(expected, result)
                else:
                    # For cos(pi/2), just check it's very close to 0
                    import re
                    match = re.search(r'= ([-.\de-]+)', result)
                    if match:
                        value = float(match.group(1))
                        self.assertLess(abs(value), 1e-15)
    
    def test_inverse_trigonometric_functions(self):
        """Test Phase 1.3 inverse trigonometric functions."""
        import math
        test_cases = [
            ("asin(1)", str(math.pi/2)),
            ("acos(1)", "0"),
            ("atan(1)", str(math.pi/4)),
            ("asin(0)", "0"),
            ("acos(0)", str(math.pi/2)),
        ]
        
        for expression, expected_str in test_cases:
            with self.subTest(expression=expression, expected=expected_str):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                # For trig functions, compare numerically due to precision
                import re
                match = re.search(r'= ([-.\de-]+)', result)
                if match:
                    actual_value = float(match.group(1))
                    expected_value = float(expected_str)
                    self.assertAlmostEqual(actual_value, expected_value, places=10)
    
    def test_logarithmic_functions(self):
        """Test Phase 1.3 logarithmic functions."""
        test_cases = [
            ("log(e)", "1"),
            ("log10(100)", "2"),
            ("ln(e)", "1"),
            ("log10(10)", "1"),
            ("log(1)", "0"),
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                # Check numerical value due to precision
                import re
                match = re.search(r'= ([-.\de-]+)', result)
                if match:
                    actual_value = float(match.group(1))
                    expected_value = float(expected)
                    self.assertAlmostEqual(actual_value, expected_value, places=10)
    
    def test_hyperbolic_functions(self):
        """Test Phase 1.3 hyperbolic functions."""
        test_cases = [
            ("sinh(0)", "0"),
            ("cosh(0)", "1"),
            ("tanh(0)", "0"),
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                self.assertIn(expected, result)
    
    def test_rounding_functions(self):
        """Test Phase 1.3 rounding functions."""
        test_cases = [
            ("floor(3.7)", "3"),
            ("ceil(3.2)", "4"),
            ("trunc(3.9)", "3"),
            ("floor(-2.3)", "-3"),  # floor of negative goes down
            ("ceil(-2.3)", "-2"),   # ceil of negative goes up
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                self.assertIn(expected, result)
    
    def test_mathematical_constants(self):
        """Test Phase 1.3 mathematical constants."""
        import math
        test_cases = [
            ("pi", math.pi),
            ("e", math.e),
            ("2*pi", 2*math.pi),
            ("e*2", 2*math.e),
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                # Check numerical value due to precision
                import re
                match = re.search(r'= ([-.\de-]+)', result)
                if match:
                    actual_value = float(match.group(1))
                    self.assertAlmostEqual(actual_value, expected, places=10)
    
    def test_complex_mathematical_expressions(self):
        """Test complex expressions combining multiple Phase 1.3 features."""
        test_cases = [
            ("sqrt(25) + sin(pi/2)", 6.0),  # 5 + 1 = 6
            ("sqrt((5-0)^2 + (12-0)^2)", 13.0),  # Distance formula: sqrt(25+144) = sqrt(169) = 13
            ("log(e^3)", 3.0),  # log(e^3) = 3
            ("pow(2, 3) + sqrt(16)", 12.0),  # 8 + 4 = 12
            ("abs(-10) + floor(3.9)", 13.0),  # 10 + 3 = 13
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("✅", result)
                # Check numerical value due to precision
                import re
                match = re.search(r'= ([-.\de-]+)', result)
                if match:
                    actual_value = float(match.group(1))
                    self.assertAlmostEqual(actual_value, expected, places=10)
    
    # Error Handling Tests for Phase 1.3 Functions
    def test_sqrt_negative_number_error(self):
        """Test sqrt domain error for negative numbers."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='sqrt(-1)'
        ))
        self.assertIn("❌", result)
        self.assertIn("Cannot calculate square root of negative number", result)
    
    def test_log_domain_errors(self):
        """Test logarithm domain errors."""
        error_cases = [
            ("log(0)", "Cannot calculate logarithm of non-positive number"),
            ("log(-1)", "Cannot calculate logarithm of non-positive number"),
            ("log10(0)", "Cannot calculate log10 of non-positive number"),
            ("ln(-5)", "Cannot calculate logarithm of non-positive number"),
        ]
        
        for expression, expected_error in error_cases:
            with self.subTest(expression=expression, error=expected_error):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("❌", result)
                self.assertIn(expected_error, result)
    
    def test_asin_acos_domain_errors(self):
        """Test inverse trigonometric domain errors."""
        error_cases = [
            ("asin(2)", "asin input must be between -1 and 1"),
            ("asin(-2)", "asin input must be between -1 and 1"),
            ("acos(1.5)", "acos input must be between -1 and 1"),
            ("acos(-1.5)", "acos input must be between -1 and 1"),
        ]
        
        for expression, expected_error in error_cases:
            with self.subTest(expression=expression, error=expected_error):
                result = asyncio.run(self.async_test_helper(
                    'calculate', expression=expression
                ))
                self.assertIn("❌", result)
                self.assertIn(expected_error, result)
    
    def test_unsupported_function_error(self):
        """Test error for unsupported function names."""
        result = asyncio.run(self.async_test_helper(
            'calculate', expression='unsupported_func(5)'
        ))
        self.assertIn("❌", result)
        self.assertIn("Unsupported function", result)
        
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
    
    def test_expression_preprocessing_method(self):
        """Test the _preprocess_expression method for exponentiation operator conversion."""
        test_cases = [
            ("2^3", "2**3"),
            ("a^b", "a**b"),
            ("2**3", "2**3"),      # Should remain unchanged
            ("2^3^4", "2**3**4"),
            ("x^(y+z)", "x**(y+z)"),
            ("(a^b)^c", "(a**b)**c"),
        ]
        
        for input_expr, expected_output in test_cases:
            with self.subTest(input=input_expr, expected=expected_output):
                result = self.tool._preprocess_expression(input_expr)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    # Run the test suite
    print("Running Calculate Arithmetic Test Suite...")
    print("=" * 60)
    unittest.main(verbosity=2)
