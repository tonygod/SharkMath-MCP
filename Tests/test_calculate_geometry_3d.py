"""
Test suite for calculate_geometry_3d consolidated tool.
Tests 3D geometry calculations including distance, vectors, volumes, and surface areas.

Run with: python Tests/test_calculate_geometry_3d.py
"""

import unittest
import sys
import os
import math

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculate_geometry_3d import register_tools


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestCalculateGeometry3D(unittest.TestCase):
    """Test cases for calculate_geometry_3d consolidated tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp = MockMCP()
        register_tools(self.mock_mcp)
        self.calculate_geometry_3d = self.mock_mcp.tools['calculate_geometry_3d']
    
    # 3D Distance Calculation Tests
    async def test_distance_3d_basic(self):
        """Test basic 3D distance calculation."""
        result = await self.calculate_geometry_3d("distance_3d", x1=0, y1=0, z1=0, x2=3, y2=4, z2=0)
        self.assertIn("✅ Distance between points", result)
        self.assertIn("5.0", result)  # 3-4-5 right triangle in 3D
    
    async def test_distance_3d_user_case(self):
        """Test the specific user case: distance between [10,10,10] and [120,130,140]."""
        result = await self.calculate_geometry_3d("distance_3d", x1=10, y1=10, z1=10, x2=120, y2=130, z2=140)
        self.assertIn("✅ Distance between points", result)
        # Calculate expected: sqrt((120-10)² + (130-10)² + (140-10)²) = sqrt(110² + 120² + 130²) = sqrt(12100 + 14400 + 16900) = sqrt(43400) ≈ 208.33
        expected_distance = math.sqrt(110**2 + 120**2 + 130**2)
        self.assertIn(f"{expected_distance}", result)
    
    async def test_distance_3d_negative_coordinates(self):
        """Test 3D distance with negative coordinates."""
        result = await self.calculate_geometry_3d("distance_3d", x1=-1, y1=-1, z1=-1, x2=2, y2=3, z2=5)
        self.assertIn("✅ Distance between points", result)
        # sqrt(3² + 4² + 6²) = sqrt(9 + 16 + 36) = sqrt(61)
        expected_distance = math.sqrt(61)
        self.assertIn(f"{expected_distance}", result)
    
    async def test_distance_3d_same_point(self):
        """Test 3D distance between same point."""
        result = await self.calculate_geometry_3d("distance_3d", x1=5, y1=5, z1=5, x2=5, y2=5, z2=5)
        self.assertIn("✅ Distance between points", result)
        self.assertIn("0.0", result)
    
    async def test_distance_3d_missing_parameters(self):
        """Test 3D distance with missing parameters."""
        result = await self.calculate_geometry_3d("distance_3d", x1=0, y1=0, z1=0, x2=3, y2=4)
        self.assertIn("❌ 3D distance calculation requires parameters: x1, y1, z1, x2, y2, z2", result)
    
    # 3D Midpoint Calculation Tests
    async def test_midpoint_3d_basic(self):
        """Test basic 3D midpoint calculation."""
        result = await self.calculate_geometry_3d("midpoint_3d", x1=0, y1=0, z1=0, x2=6, y2=8, z2=10)
        self.assertIn("✅ Midpoint between", result)
        self.assertIn("(3.0, 4.0, 5.0)", result)
    
    async def test_midpoint_3d_negative_coordinates(self):
        """Test 3D midpoint with negative coordinates."""
        result = await self.calculate_geometry_3d("midpoint_3d", x1=-2, y1=-4, z1=-6, x2=4, y2=8, z2=12)
        self.assertIn("✅ Midpoint between", result)
        self.assertIn("(1.0, 2.0, 3.0)", result)
    
    async def test_midpoint_3d_same_point(self):
        """Test 3D midpoint of same point."""
        result = await self.calculate_geometry_3d("midpoint_3d", x1=3, y1=7, z1=11, x2=3, y2=7, z2=11)
        self.assertIn("✅ Midpoint between", result)
        self.assertIn("(3.0, 7.0, 11.0)", result)
    
    async def test_midpoint_3d_missing_parameters(self):
        """Test 3D midpoint with missing parameters."""
        result = await self.calculate_geometry_3d("midpoint_3d", x1=0, y1=0, z1=0, x2=3, y2=4)
        self.assertIn("❌ 3D midpoint calculation requires parameters: x1, y1, z1, x2, y2, z2", result)
    
    # Vector Magnitude Tests
    async def test_vector_magnitude_basic(self):
        """Test basic vector magnitude calculation."""
        result = await self.calculate_geometry_3d("vector_magnitude", x=3, y=4, z=0)
        self.assertIn("✅ Magnitude of vector", result)
        self.assertIn("5.0", result)  # 3-4-5 right triangle
    
    async def test_vector_magnitude_3d_unit_vectors(self):
        """Test unit vector magnitudes."""
        # i unit vector
        result = await self.calculate_geometry_3d("vector_magnitude", x=1, y=0, z=0)
        self.assertIn("✅ Magnitude of vector", result)
        self.assertIn("1.0", result)
    
    async def test_vector_magnitude_zero_vector(self):
        """Test zero vector magnitude."""
        result = await self.calculate_geometry_3d("vector_magnitude", x=0, y=0, z=0)
        self.assertIn("✅ Magnitude of vector", result)
        self.assertIn("0.0", result)
    
    async def test_vector_magnitude_negative_components(self):
        """Test vector magnitude with negative components."""
        result = await self.calculate_geometry_3d("vector_magnitude", x=-3, y=-4, z=-12)
        self.assertIn("✅ Magnitude of vector", result)
        expected_magnitude = math.sqrt(9 + 16 + 144)  # sqrt(169) = 13
        self.assertIn("13.0", result)
    
    async def test_vector_magnitude_missing_parameters(self):
        """Test vector magnitude with missing parameters."""
        result = await self.calculate_geometry_3d("vector_magnitude", x=3, y=4)
        self.assertIn("❌ Vector magnitude calculation requires parameters: x, y, z", result)
    
    # Vector Dot Product Tests
    async def test_vector_dot_product_basic(self):
        """Test basic vector dot product."""
        result = await self.calculate_geometry_3d("vector_dot_product", x1=1, y1=2, z1=3, x2=4, y2=5, z2=6)
        self.assertIn("✅ Dot product of vectors", result)
        # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
        self.assertIn("32", result)
    
    async def test_vector_dot_product_perpendicular(self):
        """Test perpendicular vectors (dot product = 0)."""
        result = await self.calculate_geometry_3d("vector_dot_product", x1=1, y1=0, z1=0, x2=0, y2=1, z2=0)
        self.assertIn("✅ Dot product of vectors", result)
        self.assertIn("0", result)
        self.assertIn("(vectors are perpendicular)", result)
    
    async def test_vector_dot_product_parallel_same_direction(self):
        """Test parallel vectors pointing in same direction."""
        result = await self.calculate_geometry_3d("vector_dot_product", x1=2, y1=4, z1=6, x2=1, y2=2, z2=3)
        self.assertIn("✅ Dot product of vectors", result)
        # 2*1 + 4*2 + 6*3 = 2 + 8 + 18 = 28
        self.assertIn("28", result)
        self.assertIn("(vectors point in similar directions)", result)
    
    async def test_vector_dot_product_opposite_direction(self):
        """Test vectors pointing in opposite directions."""
        result = await self.calculate_geometry_3d("vector_dot_product", x1=1, y1=2, z1=3, x2=-2, y2=-4, z2=-6)
        self.assertIn("✅ Dot product of vectors", result)
        # 1*(-2) + 2*(-4) + 3*(-6) = -2 + -8 + -18 = -28
        self.assertIn("-28", result)
        self.assertIn("(vectors point in opposite directions)", result)
    
    async def test_vector_dot_product_missing_parameters(self):
        """Test vector dot product with missing parameters."""
        result = await self.calculate_geometry_3d("vector_dot_product", x1=1, y1=2, z1=3, x2=4, y2=5)
        self.assertIn("❌ Vector dot product calculation requires parameters: x1, y1, z1, x2, y2, z2", result)
    
    # Vector Cross Product Tests
    async def test_vector_cross_product_basic(self):
        """Test basic vector cross product."""
        result = await self.calculate_geometry_3d("vector_cross_product", x1=1, y1=0, z1=0, x2=0, y2=1, z2=0)
        self.assertIn("✅ Cross product of vectors", result)
        self.assertIn("(0.0, 0.0, 1.0)", result)  # i × j = k
        self.assertIn("magnitude 1.0", result)
    
    async def test_vector_cross_product_i_cross_j(self):
        """Test i × j = k."""
        result = await self.calculate_geometry_3d("vector_cross_product", x1=1, y1=0, z1=0, x2=0, y2=1, z2=0)
        self.assertIn("✅ Cross product of vectors", result)
        self.assertIn("(0.0, 0.0, 1.0)", result)
    
    async def test_vector_cross_product_parallel_vectors(self):
        """Test cross product of parallel vectors (result should be zero vector)."""
        result = await self.calculate_geometry_3d("vector_cross_product", x1=2, y1=4, z1=6, x2=1, y2=2, z2=3)
        self.assertIn("✅ Cross product of vectors", result)
        self.assertIn("(0.0, 0.0, 0.0)", result)
        self.assertIn("magnitude 0.0", result)
    
    async def test_vector_cross_product_missing_parameters(self):
        """Test vector cross product with missing parameters."""
        result = await self.calculate_geometry_3d("vector_cross_product", x1=1, y1=2, z1=3, x2=4, y2=5)
        self.assertIn("❌ Vector cross product calculation requires parameters: x1, y1, z1, x2, y2, z2", result)
    
    # Vector Angle Tests
    async def test_vector_angle_perpendicular(self):
        """Test angle between perpendicular vectors."""
        result = await self.calculate_geometry_3d("vector_angle", x1=1, y1=0, z1=0, x2=0, y2=1, z2=0)
        self.assertIn("✅ Angle between vectors", result)
        self.assertIn("1.570796", result)  # π/2 radians
        self.assertIn("90.00 degrees", result)
    
    async def test_vector_angle_parallel_same_direction(self):
        """Test angle between parallel vectors (same direction)."""
        result = await self.calculate_geometry_3d("vector_angle", x1=2, y1=4, z1=6, x2=1, y2=2, z2=3)
        self.assertIn("✅ Angle between vectors", result)
        self.assertIn("0.000000", result)  # 0 radians
        self.assertIn("0.00 degrees", result)
    
    async def test_vector_angle_parallel_opposite_direction(self):
        """Test angle between parallel vectors (opposite direction)."""
        result = await self.calculate_geometry_3d("vector_angle", x1=1, y1=2, z1=3, x2=-1, y2=-2, z2=-3)
        self.assertIn("✅ Angle between vectors", result)
        self.assertIn("3.141593", result)  # π radians
        self.assertIn("180.00 degrees", result)
    
    async def test_vector_angle_zero_vector(self):
        """Test angle calculation with zero vector."""
        result = await self.calculate_geometry_3d("vector_angle", x1=0, y1=0, z1=0, x2=1, y2=2, z2=3)
        self.assertIn("❌ Cannot calculate angle with zero vector", result)
    
    async def test_vector_angle_missing_parameters(self):
        """Test vector angle with missing parameters."""
        result = await self.calculate_geometry_3d("vector_angle", x1=1, y1=2, z1=3, x2=4, y2=5)
        self.assertIn("❌ Vector angle calculation requires parameters: x1, y1, z1, x2, y2, z2", result)
    
    # Sphere Volume Tests
    async def test_sphere_volume_basic(self):
        """Test basic sphere volume calculation."""
        result = await self.calculate_geometry_3d("sphere_volume", radius=3)
        self.assertIn("✅ Sphere volume with radius 3", result)
        expected_volume = (4/3) * math.pi * 27  # (4/3)πr³
        self.assertIn(f"{expected_volume}", result)
    
    async def test_sphere_volume_unit_sphere(self):
        """Test unit sphere volume."""
        result = await self.calculate_geometry_3d("sphere_volume", radius=1)
        self.assertIn("✅ Sphere volume with radius 1", result)
        expected_volume = (4/3) * math.pi
        self.assertIn(f"{expected_volume}", result)
    
    async def test_sphere_volume_zero_radius(self):
        """Test sphere volume with zero radius."""
        result = await self.calculate_geometry_3d("sphere_volume", radius=0)
        self.assertIn("✅ Sphere volume with radius 0 is 0", result)
    
    async def test_sphere_volume_negative_radius(self):
        """Test sphere volume with negative radius."""
        result = await self.calculate_geometry_3d("sphere_volume", radius=-5)
        self.assertIn("❌ Radius cannot be negative", result)
    
    async def test_sphere_volume_missing_parameter(self):
        """Test sphere volume with missing radius."""
        result = await self.calculate_geometry_3d("sphere_volume")
        self.assertIn("❌ Sphere volume calculation requires parameter: radius", result)
    
    # Sphere Surface Area Tests
    async def test_sphere_surface_area_basic(self):
        """Test basic sphere surface area calculation."""
        result = await self.calculate_geometry_3d("sphere_surface_area", radius=5)
        self.assertIn("✅ Sphere surface area with radius 5", result)
        expected_area = 4 * math.pi * 25  # 4πr²
        self.assertIn(f"{expected_area}", result)
    
    async def test_sphere_surface_area_unit_sphere(self):
        """Test unit sphere surface area."""
        result = await self.calculate_geometry_3d("sphere_surface_area", radius=1)
        self.assertIn("✅ Sphere surface area with radius 1", result)
        expected_area = 4 * math.pi
        self.assertIn(f"{expected_area}", result)
    
    async def test_sphere_surface_area_zero_radius(self):
        """Test sphere surface area with zero radius."""
        result = await self.calculate_geometry_3d("sphere_surface_area", radius=0)
        self.assertIn("✅ Sphere surface area with radius 0 is 0", result)
    
    async def test_sphere_surface_area_negative_radius(self):
        """Test sphere surface area with negative radius."""
        result = await self.calculate_geometry_3d("sphere_surface_area", radius=-3)
        self.assertIn("❌ Radius cannot be negative", result)
    
    # Cylinder Volume Tests
    async def test_cylinder_volume_basic(self):
        """Test basic cylinder volume calculation."""
        result = await self.calculate_geometry_3d("cylinder_volume", radius=4, height=6)
        self.assertIn("✅ Cylinder volume with radius 4 and height 6", result)
        expected_volume = math.pi * 16 * 6  # πr²h
        self.assertIn(f"{expected_volume}", result)
    
    async def test_cylinder_volume_unit_cylinder(self):
        """Test unit cylinder volume."""
        result = await self.calculate_geometry_3d("cylinder_volume", radius=1, height=1)
        self.assertIn("✅ Cylinder volume with radius 1 and height 1", result)
        expected_volume = math.pi
        self.assertIn(f"{expected_volume}", result)
    
    async def test_cylinder_volume_zero_dimensions(self):
        """Test cylinder volume with zero dimensions."""
        result = await self.calculate_geometry_3d("cylinder_volume", radius=0, height=5)
        self.assertIn("✅ Cylinder volume with radius 0 or height 0 is 0", result)
        
        result = await self.calculate_geometry_3d("cylinder_volume", radius=5, height=0)
        self.assertIn("✅ Cylinder volume with radius 0 or height 0 is 0", result)
    
    async def test_cylinder_volume_negative_dimensions(self):
        """Test cylinder volume with negative dimensions."""
        result = await self.calculate_geometry_3d("cylinder_volume", radius=-3, height=5)
        self.assertIn("❌ Radius and height cannot be negative", result)
    
    async def test_cylinder_volume_missing_parameters(self):
        """Test cylinder volume with missing parameters."""
        result = await self.calculate_geometry_3d("cylinder_volume", radius=5)
        self.assertIn("❌ Cylinder volume calculation requires parameters: radius, height", result)
    
    # Cylinder Surface Area Tests
    async def test_cylinder_surface_area_basic(self):
        """Test basic cylinder surface area calculation."""
        result = await self.calculate_geometry_3d("cylinder_surface_area", radius=3, height=8)
        self.assertIn("✅ Cylinder surface area with radius 3 and height 8", result)
        base_area = 2 * math.pi * 9  # 2πr²
        lateral_area = 2 * math.pi * 3 * 8  # 2πrh
        expected_total = base_area + lateral_area
        self.assertIn(f"{expected_total}", result)
        self.assertIn("Base:", result)
        self.assertIn("Lateral:", result)
    
    async def test_cylinder_surface_area_negative_dimensions(self):
        """Test cylinder surface area with negative dimensions."""
        result = await self.calculate_geometry_3d("cylinder_surface_area", radius=5, height=-2)
        self.assertIn("❌ Radius and height cannot be negative", result)
    
    # Cone Volume Tests
    async def test_cone_volume_basic(self):
        """Test basic cone volume calculation."""
        result = await self.calculate_geometry_3d("cone_volume", radius=6, height=9)
        self.assertIn("✅ Cone volume with radius 6 and height 9", result)
        expected_volume = (1/3) * math.pi * 36 * 9  # (1/3)πr²h
        self.assertIn(f"{expected_volume}", result)
    
    async def test_cone_volume_unit_cone(self):
        """Test unit cone volume."""
        result = await self.calculate_geometry_3d("cone_volume", radius=1, height=1)
        self.assertIn("✅ Cone volume with radius 1 and height 1", result)
        expected_volume = (1/3) * math.pi
        self.assertIn(f"{expected_volume}", result)
    
    async def test_cone_volume_zero_dimensions(self):
        """Test cone volume with zero dimensions."""
        result = await self.calculate_geometry_3d("cone_volume", radius=0, height=5)
        self.assertIn("✅ Cone volume with radius 0 or height 0 is 0", result)
    
    async def test_cone_volume_negative_dimensions(self):
        """Test cone volume with negative dimensions."""
        result = await self.calculate_geometry_3d("cone_volume", radius=3, height=-4)
        self.assertIn("❌ Radius and height cannot be negative", result)
    
    async def test_cone_volume_missing_parameters(self):
        """Test cone volume with missing parameters."""
        result = await self.calculate_geometry_3d("cone_volume", radius=5)
        self.assertIn("❌ Cone volume calculation requires parameters: radius, height", result)
    
    # Cone Surface Area Tests
    async def test_cone_surface_area_basic(self):
        """Test basic cone surface area calculation."""
        result = await self.calculate_geometry_3d("cone_surface_area", radius=3, height=4)
        self.assertIn("✅ Cone surface area with radius 3 and height 4", result)
        slant_height = math.sqrt(9 + 16)  # sqrt(r² + h²) = 5
        base_area = math.pi * 9  # πr²
        lateral_area = math.pi * 3 * 5  # πr × slant_height
        expected_total = base_area + lateral_area
        self.assertIn(f"{expected_total}", result)
        self.assertIn("Base:", result)
        self.assertIn("Lateral:", result)
        self.assertIn("Slant height: 5.0", result)
    
    async def test_cone_surface_area_negative_dimensions(self):
        """Test cone surface area with negative dimensions."""
        result = await self.calculate_geometry_3d("cone_surface_area", radius=-2, height=5)
        self.assertIn("❌ Radius and height cannot be negative", result)
    
    # Rectangular Prism Volume Tests
    async def test_rectangular_prism_volume_basic(self):
        """Test basic rectangular prism volume calculation."""
        result = await self.calculate_geometry_3d("rectangular_prism_volume", length=5, width=4, height=3)
        self.assertIn("✅ Rectangular prism volume with dimensions 5 × 4 × 3 is 60", result)
    
    async def test_rectangular_prism_volume_cube(self):
        """Test cube volume calculation."""
        result = await self.calculate_geometry_3d("rectangular_prism_volume", length=4, width=4, height=4)
        self.assertIn("✅ Rectangular prism volume with dimensions 4 × 4 × 4 is 64", result)
    
    async def test_rectangular_prism_volume_zero_dimension(self):
        """Test rectangular prism volume with zero dimension."""
        result = await self.calculate_geometry_3d("rectangular_prism_volume", length=0, width=4, height=3)
        self.assertIn("✅ Rectangular prism volume with dimensions 0 × 4 × 3 is 0", result)
    
    async def test_rectangular_prism_volume_negative_dimension(self):
        """Test rectangular prism volume with negative dimensions."""
        result = await self.calculate_geometry_3d("rectangular_prism_volume", length=5, width=-4, height=3)
        self.assertIn("❌ Dimensions cannot be negative", result)
    
    async def test_rectangular_prism_volume_missing_parameters(self):
        """Test rectangular prism volume with missing parameters."""
        result = await self.calculate_geometry_3d("rectangular_prism_volume", length=5, width=4)
        self.assertIn("❌ Rectangular prism volume calculation requires parameters: length, width, height", result)
    
    # Rectangular Prism Surface Area Tests
    async def test_rectangular_prism_surface_area_basic(self):
        """Test basic rectangular prism surface area calculation."""
        result = await self.calculate_geometry_3d("rectangular_prism_surface_area", length=6, width=4, height=2)
        self.assertIn("✅ Rectangular prism surface area with dimensions 6 × 4 × 2", result)
        # 2(lw + lh + wh) = 2(24 + 12 + 8) = 2(44) = 88
        self.assertIn("88", result)
        self.assertIn("Faces:", result)
        self.assertIn("2×24.000", result)  # length × width faces
        self.assertIn("2×12.000", result)  # length × height faces
        self.assertIn("2×8.000", result)   # width × height faces
    
    async def test_rectangular_prism_surface_area_cube(self):
        """Test cube surface area calculation."""
        result = await self.calculate_geometry_3d("rectangular_prism_surface_area", length=3, width=3, height=3)
        self.assertIn("✅ Rectangular prism surface area with dimensions 3 × 3 × 3", result)
        # 6 × 3² = 54
        self.assertIn("54", result)
    
    async def test_rectangular_prism_surface_area_negative_dimension(self):
        """Test rectangular prism surface area with negative dimensions."""
        result = await self.calculate_geometry_3d("rectangular_prism_surface_area", length=5, width=4, height=-3)
        self.assertIn("❌ Dimensions cannot be negative", result)
    
    async def test_rectangular_prism_surface_area_missing_parameters(self):
        """Test rectangular prism surface area with missing parameters."""
        result = await self.calculate_geometry_3d("rectangular_prism_surface_area", length=5, width=4)
        self.assertIn("❌ Rectangular prism surface area calculation requires parameters: length, width, height", result)
    
    # Error Handling Tests
    async def test_invalid_operation(self):
        """Test invalid operation."""
        result = await self.calculate_geometry_3d("invalid_operation", x=1, y=2, z=3)
        self.assertIn("❌ Invalid operation 'invalid_operation'", result)
        valid_operations = [
            "distance_3d", "midpoint_3d", "vector_magnitude", "vector_dot_product", 
            "vector_cross_product", "vector_angle", "sphere_volume", "sphere_surface_area",
            "cylinder_volume", "cylinder_surface_area", "cone_volume", "cone_surface_area",
            "rectangular_prism_volume", "rectangular_prism_surface_area"
        ]
        for op in valid_operations:
            self.assertIn(op, result)
    
    async def test_empty_operation(self):
        """Test empty operation."""
        result = await self.calculate_geometry_3d("", x=1, y=2, z=3)
        self.assertIn("❌ Invalid operation", result)


def run_async_test(coro):
    """Helper to run async test functions."""
    import asyncio
    return asyncio.run(coro)


if __name__ == '__main__':
    # Create test suite with async support
    test_instance = TestCalculateGeometry3D()
    test_instance.setUp()
    
    test_methods = [
        # 3D Distance tests
        'test_distance_3d_basic',
        'test_distance_3d_user_case',
        'test_distance_3d_negative_coordinates', 
        'test_distance_3d_same_point',
        'test_distance_3d_missing_parameters',
        # 3D Midpoint tests
        'test_midpoint_3d_basic',
        'test_midpoint_3d_negative_coordinates',
        'test_midpoint_3d_same_point',
        'test_midpoint_3d_missing_parameters',
        # Vector Magnitude tests
        'test_vector_magnitude_basic',
        'test_vector_magnitude_3d_unit_vectors',
        'test_vector_magnitude_zero_vector',
        'test_vector_magnitude_negative_components',
        'test_vector_magnitude_missing_parameters',
        # Vector Dot Product tests
        'test_vector_dot_product_basic',
        'test_vector_dot_product_perpendicular',
        'test_vector_dot_product_parallel_same_direction',
        'test_vector_dot_product_opposite_direction',
        'test_vector_dot_product_missing_parameters',
        # Vector Cross Product tests
        'test_vector_cross_product_basic',
        'test_vector_cross_product_i_cross_j',
        'test_vector_cross_product_parallel_vectors',
        'test_vector_cross_product_missing_parameters',
        # Vector Angle tests
        'test_vector_angle_perpendicular',
        'test_vector_angle_parallel_same_direction',
        'test_vector_angle_parallel_opposite_direction',
        'test_vector_angle_zero_vector',
        'test_vector_angle_missing_parameters',
        # Sphere Volume tests
        'test_sphere_volume_basic',
        'test_sphere_volume_unit_sphere',
        'test_sphere_volume_zero_radius',
        'test_sphere_volume_negative_radius',
        'test_sphere_volume_missing_parameter',
        # Sphere Surface Area tests
        'test_sphere_surface_area_basic',
        'test_sphere_surface_area_unit_sphere',
        'test_sphere_surface_area_zero_radius',
        'test_sphere_surface_area_negative_radius',
        # Cylinder Volume tests
        'test_cylinder_volume_basic',
        'test_cylinder_volume_unit_cylinder',
        'test_cylinder_volume_zero_dimensions',
        'test_cylinder_volume_negative_dimensions',
        'test_cylinder_volume_missing_parameters',
        # Cylinder Surface Area tests
        'test_cylinder_surface_area_basic',
        'test_cylinder_surface_area_negative_dimensions',
        # Cone Volume tests
        'test_cone_volume_basic',
        'test_cone_volume_unit_cone',
        'test_cone_volume_zero_dimensions',
        'test_cone_volume_negative_dimensions',
        'test_cone_volume_missing_parameters',
        # Cone Surface Area tests
        'test_cone_surface_area_basic',
        'test_cone_surface_area_negative_dimensions',
        # Rectangular Prism Volume tests
        'test_rectangular_prism_volume_basic',
        'test_rectangular_prism_volume_cube',
        'test_rectangular_prism_volume_zero_dimension',
        'test_rectangular_prism_volume_negative_dimension',
        'test_rectangular_prism_volume_missing_parameters',
        # Rectangular Prism Surface Area tests
        'test_rectangular_prism_surface_area_basic',
        'test_rectangular_prism_surface_area_cube',
        'test_rectangular_prism_surface_area_negative_dimension',
        'test_rectangular_prism_surface_area_missing_parameters',
        # Error Handling tests
        'test_invalid_operation',
        'test_empty_operation'
    ]
    
    print("Running calculate_geometry_3d consolidated tool tests...")
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
        print("✅ All calculate_geometry_3d tests passed!")
    else:
        print(f"❌ {failed} test(s) failed")
