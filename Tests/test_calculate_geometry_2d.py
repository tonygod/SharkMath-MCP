"""
Test suite for calculate_geometry_2d consolidated tool.
Tests 2D geometry calculations including distance, slope, areas, and perimeters.

Run with: python Tests/test_calculate_geometry_2d.py
"""

import unittest
import sys
import os
import math

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculate_geometry_2d import register_tools


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestCalculateGeometry2D(unittest.TestCase):
    """Test cases for calculate_geometry_2d consolidated tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp = MockMCP()
        register_tools(self.mock_mcp)
        self.calculate_geometry_2d = self.mock_mcp.tools['calculate_geometry_2d']
    
    # Distance Calculation Tests
    async def test_distance_basic(self):
        """Test basic distance calculation."""
        result = await self.calculate_geometry_2d("distance", x1=0, y1=0, x2=3, y2=4)
        self.assertIn("✅ Distance between points", result)
        self.assertIn("5.0", result)  # 3-4-5 right triangle
    
    async def test_distance_negative_coordinates(self):
        """Test distance with negative coordinates."""
        result = await self.calculate_geometry_2d("distance", x1=-1, y1=-1, x2=2, y2=3)
        self.assertIn("✅ Distance between points", result)
        self.assertIn("5.0", result)  # 3-4-5 right triangle
    
    async def test_distance_same_point(self):
        """Test distance between same point."""
        result = await self.calculate_geometry_2d("distance", x1=5, y1=5, x2=5, y2=5)
        self.assertIn("✅ Distance between points", result)
        self.assertIn("0.0", result)
    
    async def test_distance_missing_parameters(self):
        """Test distance with missing parameters."""
        result = await self.calculate_geometry_2d("distance", x1=0, y1=0, x2=3)
        self.assertIn("❌ Distance calculation requires parameters: x1, y1, x2, y2", result)
    
    # Slope Calculation Tests
    async def test_slope_positive(self):
        """Test positive slope calculation."""
        result = await self.calculate_geometry_2d("slope", x1=0, y1=0, x2=2, y2=6)
        self.assertIn("✅ Slope between points", result)
        self.assertIn("3.0", result)
    
    async def test_slope_negative(self):
        """Test negative slope calculation."""
        result = await self.calculate_geometry_2d("slope", x1=0, y1=4, x2=2, y2=0)
        self.assertIn("✅ Slope between points", result)
        self.assertIn("-2.0", result)
    
    async def test_slope_zero_horizontal(self):
        """Test zero slope (horizontal line)."""
        result = await self.calculate_geometry_2d("slope", x1=1, y1=5, x2=8, y2=5)
        self.assertIn("✅ Slope between points", result)
        self.assertIn("0 (horizontal line)", result)
    
    async def test_slope_undefined_vertical(self):
        """Test undefined slope (vertical line)."""
        result = await self.calculate_geometry_2d("slope", x1=3, y1=1, x2=3, y2=7)
        self.assertIn("✅ Slope is undefined (vertical line)", result)
    
    async def test_slope_forty_five_degrees_up(self):
        """Test slope of 1 (45° upward)."""
        result = await self.calculate_geometry_2d("slope", x1=0, y1=0, x2=5, y2=5)
        self.assertIn("✅ Slope between points", result)
        self.assertIn("1 (45° upward)", result)
    
    async def test_slope_forty_five_degrees_down(self):
        """Test slope of -1 (45° downward)."""
        result = await self.calculate_geometry_2d("slope", x1=0, y1=5, x2=5, y2=0)
        self.assertIn("✅ Slope between points", result)
        self.assertIn("-1 (45° downward)", result)
    
    async def test_slope_missing_parameters(self):
        """Test slope with missing parameters."""
        result = await self.calculate_geometry_2d("slope", x1=0, y1=0, x2=3)
        self.assertIn("❌ Slope calculation requires parameters: x1, y1, x2, y2", result)
    
    # Circle Area Tests
    async def test_circle_area_basic(self):
        """Test basic circle area calculation."""
        result = await self.calculate_geometry_2d("circle_area", radius=5)
        self.assertIn("✅ Circle area with radius 5", result)
        expected_area = math.pi * 25  # π * r²
        self.assertIn(f"{expected_area}", result)
    
    async def test_circle_area_unit_circle(self):
        """Test unit circle area."""
        result = await self.calculate_geometry_2d("circle_area", radius=1)
        self.assertIn("✅ Circle area with radius 1", result)
        self.assertIn(f"{math.pi}", result)
    
    async def test_circle_area_zero_radius(self):
        """Test circle area with zero radius."""
        result = await self.calculate_geometry_2d("circle_area", radius=0)
        self.assertIn("✅ Circle area with radius 0 is 0", result)
    
    async def test_circle_area_negative_radius(self):
        """Test circle area with negative radius."""
        result = await self.calculate_geometry_2d("circle_area", radius=-3)
        self.assertIn("❌ Radius cannot be negative", result)
    
    async def test_circle_area_missing_parameter(self):
        """Test circle area with missing radius."""
        result = await self.calculate_geometry_2d("circle_area")
        self.assertIn("❌ Circle area calculation requires parameter: radius", result)
    
    # Circle Circumference Tests  
    async def test_circle_circumference_basic(self):
        """Test basic circle circumference calculation."""
        result = await self.calculate_geometry_2d("circle_circumference", radius=10)
        self.assertIn("✅ Circle circumference with radius 10", result)
        expected_circumference = 2 * math.pi * 10  # 2πr
        self.assertIn(f"{expected_circumference}", result)
    
    async def test_circle_circumference_unit_circle(self):
        """Test unit circle circumference."""
        result = await self.calculate_geometry_2d("circle_circumference", radius=1)
        self.assertIn("✅ Circle circumference with radius 1", result)
        self.assertIn(f"{2 * math.pi}", result)
    
    async def test_circle_circumference_zero_radius(self):
        """Test circle circumference with zero radius."""
        result = await self.calculate_geometry_2d("circle_circumference", radius=0)
        self.assertIn("✅ Circle circumference with radius 0 is 0", result)
    
    async def test_circle_circumference_negative_radius(self):
        """Test circle circumference with negative radius."""
        result = await self.calculate_geometry_2d("circle_circumference", radius=-5)
        self.assertIn("❌ Radius cannot be negative", result)
    
    # Rectangle Area Tests
    async def test_rectangle_area_basic(self):
        """Test basic rectangle area calculation."""
        result = await self.calculate_geometry_2d("rectangle_area", length=6, width=4)
        self.assertIn("✅ Rectangle area with length 6 and width 4 is 24", result)
    
    async def test_rectangle_area_square(self):
        """Test square area calculation."""
        result = await self.calculate_geometry_2d("rectangle_area", length=5, width=5)
        self.assertIn("✅ Rectangle area with length 5 and width 5 is 25", result)
    
    async def test_rectangle_area_zero_dimension(self):
        """Test rectangle area with zero dimension."""
        result = await self.calculate_geometry_2d("rectangle_area", length=5, width=0)
        self.assertIn("✅ Rectangle area with length 5 and width 0 is 0", result)
    
    async def test_rectangle_area_negative_dimension(self):
        """Test rectangle area with negative dimensions."""
        result = await self.calculate_geometry_2d("rectangle_area", length=-3, width=4)
        self.assertIn("❌ Length and width cannot be negative", result)
    
    async def test_rectangle_area_missing_parameters(self):
        """Test rectangle area with missing parameters."""
        result = await self.calculate_geometry_2d("rectangle_area", length=5)
        self.assertIn("❌ Rectangle area calculation requires parameters: length, width", result)
    
    # Rectangle Perimeter Tests
    async def test_rectangle_perimeter_basic(self):
        """Test basic rectangle perimeter calculation."""
        result = await self.calculate_geometry_2d("rectangle_perimeter", length=6, width=4)
        self.assertIn("✅ Rectangle perimeter with length 6 and width 4 is 20", result)
    
    async def test_rectangle_perimeter_square(self):
        """Test square perimeter calculation."""
        result = await self.calculate_geometry_2d("rectangle_perimeter", length=5, width=5)
        self.assertIn("✅ Rectangle perimeter with length 5 and width 5 is 20", result)
    
    async def test_rectangle_perimeter_zero_dimension(self):
        """Test rectangle perimeter with zero dimension."""
        result = await self.calculate_geometry_2d("rectangle_perimeter", length=0, width=8)
        self.assertIn("✅ Rectangle perimeter with length 0 and width 8 is 16", result)
    
    async def test_rectangle_perimeter_negative_dimension(self):
        """Test rectangle perimeter with negative dimensions."""
        result = await self.calculate_geometry_2d("rectangle_perimeter", length=5, width=-2)
        self.assertIn("❌ Length and width cannot be negative", result)
    
    # Triangle Area Tests
    async def test_triangle_area_basic(self):
        """Test basic triangle area calculation."""
        result = await self.calculate_geometry_2d("triangle_area", base=8, height=6)
        self.assertIn("✅ Triangle area with base 8 and height 6 is 24.0", result)
    
    async def test_triangle_area_right_triangle(self):
        """Test right triangle area calculation."""
        result = await self.calculate_geometry_2d("triangle_area", base=3, height=4)
        self.assertIn("✅ Triangle area with base 3 and height 4 is 6.0", result)
    
    async def test_triangle_area_zero_dimension(self):
        """Test triangle area with zero dimension."""
        result = await self.calculate_geometry_2d("triangle_area", base=0, height=5)
        self.assertIn("✅ Triangle area with base 0 and height 5 is 0.0", result)
    
    async def test_triangle_area_negative_dimension(self):
        """Test triangle area with negative dimensions."""
        result = await self.calculate_geometry_2d("triangle_area", base=-4, height=5)
        self.assertIn("❌ Base and height cannot be negative", result)
    
    async def test_triangle_area_missing_parameters(self):
        """Test triangle area with missing parameters."""
        result = await self.calculate_geometry_2d("triangle_area", base=5)
        self.assertIn("❌ Triangle area calculation requires parameters: base, height", result)
    
    # Right Triangle Area Tests
    async def test_right_triangle_area_basic(self):
        """Test basic right triangle area calculation."""
        result = await self.calculate_geometry_2d("right_triangle_area", side_a=6, side_b=8)
        self.assertIn("✅ Right triangle area with sides 6 and 8 is 24.0", result)
    
    async def test_right_triangle_area_unit_triangle(self):
        """Test right triangle with unit sides."""
        result = await self.calculate_geometry_2d("right_triangle_area", side_a=1, side_b=1)
        self.assertIn("✅ Right triangle area with sides 1 and 1 is 0.5", result)
    
    async def test_right_triangle_area_zero_side(self):
        """Test right triangle area with zero side."""
        result = await self.calculate_geometry_2d("right_triangle_area", side_a=0, side_b=5)
        self.assertIn("✅ Right triangle area with sides 0 and 5 is 0.0", result)
    
    async def test_right_triangle_area_negative_side(self):
        """Test right triangle area with negative side."""
        result = await self.calculate_geometry_2d("right_triangle_area", side_a=-3, side_b=4)
        self.assertIn("❌ Triangle sides cannot be negative", result)
    
    async def test_right_triangle_area_missing_parameters(self):
        """Test right triangle area with missing parameters."""
        result = await self.calculate_geometry_2d("right_triangle_area", side_a=5)
        self.assertIn("❌ Right triangle area calculation requires parameters: side_a, side_b", result)
    
    # Error Handling Tests
    async def test_invalid_operation(self):
        """Test invalid operation."""
        result = await self.calculate_geometry_2d("invalid_operation", x1=0, y1=0, x2=1, y2=1)
        self.assertIn("❌ Invalid operation 'invalid_operation'", result)
        self.assertIn("Valid operations: distance, slope, circle_area, circle_circumference, rectangle_area, rectangle_perimeter, triangle_area, right_triangle_area", result)
    
    async def test_empty_operation(self):
        """Test empty operation."""
        result = await self.calculate_geometry_2d("", radius=5)
        self.assertIn("❌ Invalid operation", result)


def run_async_test(coro):
    """Helper to run async test functions."""
    import asyncio
    return asyncio.run(coro)


if __name__ == '__main__':
    # Create test suite with async support
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test methods
    test_instance = TestCalculateGeometry2D()
    test_instance.setUp()
    
    test_methods = [
        'test_distance_basic',
        'test_distance_negative_coordinates',
        'test_distance_same_point',
        'test_distance_missing_parameters',
        'test_slope_positive',
        'test_slope_negative',
        'test_slope_zero_horizontal',
        'test_slope_undefined_vertical',
        'test_slope_forty_five_degrees_up',
        'test_slope_forty_five_degrees_down',
        'test_slope_missing_parameters',
        'test_circle_area_basic',
        'test_circle_area_unit_circle',
        'test_circle_area_zero_radius',
        'test_circle_area_negative_radius',
        'test_circle_area_missing_parameter',
        'test_circle_circumference_basic',
        'test_circle_circumference_unit_circle',
        'test_circle_circumference_zero_radius',
        'test_circle_circumference_negative_radius',
        'test_rectangle_area_basic',
        'test_rectangle_area_square',
        'test_rectangle_area_zero_dimension',
        'test_rectangle_area_negative_dimension',
        'test_rectangle_area_missing_parameters',
        'test_rectangle_perimeter_basic',
        'test_rectangle_perimeter_square',
        'test_rectangle_perimeter_zero_dimension',
        'test_rectangle_perimeter_negative_dimension',
        'test_triangle_area_basic',
        'test_triangle_area_right_triangle',
        'test_triangle_area_zero_dimension',
        'test_triangle_area_negative_dimension',
        'test_triangle_area_missing_parameters',
        'test_right_triangle_area_basic',
        'test_right_triangle_area_unit_triangle',
        'test_right_triangle_area_zero_side',
        'test_right_triangle_area_negative_side',
        'test_right_triangle_area_missing_parameters',
        'test_invalid_operation',
        'test_empty_operation'
    ]
    
    print("Running calculate_geometry_2d consolidated tool tests...")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for method_name in test_methods:
        try:
            method = getattr(test_instance, method_name)
            run_async_test(method())
            print(f"✅ {method_name}")
            passed += 1
        except Exception as e:
            print(f"❌ {method_name}: {str(e)}")
            failed += 1
    
    print("=" * 50)
    print(f"Tests passed: {passed}")
    print(f"Tests failed: {failed}")
    print(f"Total tests: {passed + failed}")
    
    if failed == 0:
        print("✅ All calculate_geometry_2d tests passed!")
    else:
        print(f"❌ {failed} test(s) failed")
