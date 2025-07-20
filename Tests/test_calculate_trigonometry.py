"""
Test Suite for Consolidated Trigonometry Tool
Tests all trigonometric operations with comprehensive coverage including edge cases.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import asyncio
import math
from trigonometric import register_tools

class TestCalculateTrigonometry(unittest.TestCase):
    """Test suite for consolidated trigonometry calculations."""
    
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

    # Basic Trigonometric Functions (Radians)
    def test_sin_radians_zero(self):
        """Test sine of 0 radians."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'sin', angle=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("sin(0.0 rad) = 0.0", result)

    def test_sin_radians_pi_half(self):
        """Test sine of π/2 radians."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'sin', angle=math.pi/2
        ))
        self.assertIn("✅", result)
        self.assertIn("= 1.0", result)

    def test_cos_radians_zero(self):
        """Test cosine of 0 radians."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'cos', angle=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 1.0", result)

    def test_cos_radians_pi_half(self):
        """Test cosine of π/2 radians."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'cos', angle=math.pi/2
        ))
        self.assertIn("✅", result)
        # Cosine of π/2 should be approximately 0
        self.assertTrue("6.123233995736766e-17" in result or "= 0" in result)

    def test_tan_radians_zero(self):
        """Test tangent of 0 radians."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'tan', angle=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 0.0", result)

    def test_tan_radians_pi_quarter(self):
        """Test tangent of π/4 radians."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'tan', angle=math.pi/4
        ))
        self.assertIn("✅", result)
        # Account for floating-point precision
        self.assertTrue("= 1.0" in result or "= 0.9999999999999999" in result)

    # Basic Trigonometric Functions (Degrees)
    def test_sin_degrees_zero(self):
        """Test sine of 0 degrees."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'sin', angle=0.0, angle_unit='degrees'
        ))
        self.assertIn("✅", result)
        self.assertIn("sin(0.0°) = 0.0", result)

    def test_sin_degrees_ninety(self):
        """Test sine of 90 degrees."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'sin', angle=90.0, angle_unit='degrees'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 1.0", result)

    def test_cos_degrees_zero(self):
        """Test cosine of 0 degrees."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'cos', angle=0.0, angle_unit='degrees'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 1.0", result)

    def test_cos_degrees_ninety(self):
        """Test cosine of 90 degrees."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'cos', angle=90.0, angle_unit='degrees'
        ))
        self.assertIn("✅", result)
        # Should be approximately 0
        self.assertTrue("6.123233995736766e-17" in result or "= 0" in result)

    def test_tan_degrees_zero(self):
        """Test tangent of 0 degrees."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'tan', angle=0.0, angle_unit='degrees'
        ))
        self.assertIn("✅", result)
        self.assertIn("= 0.0", result)

    def test_tan_degrees_fortyfive(self):
        """Test tangent of 45 degrees."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'tan', angle=45.0, angle_unit='degrees'
        ))
        self.assertIn("✅", result)
        # Account for floating-point precision
        self.assertTrue("= 1.0" in result or "= 0.9999999999999999" in result)

    # Inverse Trigonometric Functions
    def test_asin_zero(self):
        """Test arcsine of 0."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'asin', value=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("arcsin(0.0)", result)
        self.assertIn("= 0.0 rad = 0.0°", result)

    def test_asin_one(self):
        """Test arcsine of 1."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'asin', value=1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 90.0°", result)

    def test_asin_half(self):
        """Test arcsine of 0.5."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'asin', value=0.5
        ))
        self.assertIn("✅", result)
        # Account for floating-point precision
        self.assertTrue("= 30.0°" in result or "= 29.999999999999996°" in result)

    def test_acos_zero(self):
        """Test arccosine of 0."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'acos', value=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 90.0°", result)

    def test_acos_one(self):
        """Test arccosine of 1."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'acos', value=1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 0.0°", result)

    def test_acos_half(self):
        """Test arccosine of 0.5."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'acos', value=0.5
        ))
        self.assertIn("✅", result)
        # Account for floating-point precision
        self.assertTrue("= 60.0°" in result or "= 59.99999999999999°" in result)

    def test_atan_zero(self):
        """Test arctangent of 0."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan', value=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 0.0°", result)

    def test_atan_one(self):
        """Test arctangent of 1."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan', value=1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 45.0°", result)

    def test_atan_negative_one(self):
        """Test arctangent of -1."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan', value=-1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= -45.0°", result)

    # Two-argument arctangent
    def test_atan2_positive_quadrant(self):
        """Test atan2 in first quadrant."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan2', y=1.0, x=1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 45.0°", result)

    def test_atan2_negative_x(self):
        """Test atan2 in second quadrant."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan2', y=1.0, x=-1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 135.0°", result)

    def test_atan2_negative_quadrant(self):
        """Test atan2 in third quadrant."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan2', y=-1.0, x=-1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= -135.0°", result)

    def test_atan2_positive_x_axis(self):
        """Test atan2 on positive x-axis."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan2', y=0.0, x=1.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 0.0°", result)

    def test_atan2_positive_y_axis(self):
        """Test atan2 on positive y-axis."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan2', y=1.0, x=0.0
        ))
        self.assertIn("✅", result)
        self.assertIn("= 90.0°", result)

    # Error Handling Tests
    def test_tan_undefined_degrees(self):
        """Test tangent undefined at 90 degrees."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'tan', angle=90.0, angle_unit='degrees'
        ))
        self.assertIn("❌", result)
        self.assertIn("Tangent is undefined at 90", result)

    def test_tan_undefined_radians(self):
        """Test tangent undefined at π/2 radians."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'tan', angle=math.pi/2
        ))
        self.assertIn("❌", result)
        self.assertIn("Tangent is undefined", result)

    def test_asin_out_of_domain_positive(self):
        """Test arcsine with value > 1."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'asin', value=2.0
        ))
        self.assertIn("❌", result)
        self.assertIn("out of range", result)

    def test_asin_out_of_domain_negative(self):
        """Test arcsine with value < -1."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'asin', value=-2.0
        ))
        self.assertIn("❌", result)
        self.assertIn("out of range", result)

    def test_acos_out_of_domain_positive(self):
        """Test arccosine with value > 1."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'acos', value=1.5
        ))
        self.assertIn("❌", result)
        self.assertIn("out of range", result)

    def test_acos_out_of_domain_negative(self):
        """Test arccosine with value < -1."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'acos', value=-1.5
        ))
        self.assertIn("❌", result)
        self.assertIn("out of range", result)

    def test_atan2_undefined(self):
        """Test atan2 with both arguments zero."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan2', y=0.0, x=0.0
        ))
        self.assertIn("❌", result)
        self.assertIn("atan2(0,0) is undefined", result)

    def test_invalid_angle_unit(self):
        """Test invalid angle unit parameter."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'sin', angle=45.0, angle_unit='invalid'
        ))
        self.assertIn("❌", result)
        self.assertIn("must be 'radians' or 'degrees'", result)

    def test_invalid_operation(self):
        """Test invalid operation parameter."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'invalid_op', angle=1.0
        ))
        self.assertIn("❌", result)
        self.assertIn("not supported", result)

    # Parameter Validation Tests
    def test_sin_missing_angle(self):
        """Test sin without angle parameter."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'sin'
        ))
        self.assertIn("❌", result)
        self.assertIn("requires 'angle' parameter", result)

    def test_asin_missing_value(self):
        """Test asin without value parameter."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'asin'
        ))
        self.assertIn("❌", result)
        self.assertIn("requires 'value' parameter", result)

    def test_atan2_missing_y(self):
        """Test atan2 with missing y parameter."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan2', x=1.0
        ))
        self.assertIn("❌", result)
        self.assertIn("requires both 'y' and 'x' parameters", result)

    def test_atan2_missing_x(self):
        """Test atan2 with missing x parameter."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'atan2', y=1.0
        ))
        self.assertIn("❌", result)
        self.assertIn("requires both 'y' and 'x' parameters", result)

    # Large Angle Tests
    def test_sin_large_angle_degrees(self):
        """Test sine with large degree value."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'sin', angle=450.0, angle_unit='degrees'
        ))
        self.assertIn("✅", result)
        # 450° = 90° (mod 360°), so sin(450°) = sin(90°) = 1
        self.assertIn("= 1.0", result)

    def test_cos_negative_angle(self):
        """Test cosine with negative angle."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'cos', angle=-90.0, angle_unit='degrees'
        ))
        self.assertIn("✅", result)
        # cos(-90°) = cos(90°) = 0
        self.assertTrue("6.123233995736766e-17" in result or "= 0" in result)

    # Edge Case - Very Small Values
    def test_sin_very_small_angle(self):
        """Test sine with very small angle."""
        result = asyncio.run(self.async_test_helper(
            'calculate_trigonometry', 'sin', angle=1e-10
        ))
        self.assertIn("✅", result)
        # For very small x, sin(x) ≈ x
        self.assertIn("1e-10", result)

if __name__ == '__main__':
    # Run the test suite
    print("Running Consolidated Trigonometry Test Suite...")
    unittest.main(verbosity=2)
