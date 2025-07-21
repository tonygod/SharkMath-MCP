"""
3D Geometry Calculations Module for SharkMath MCP Server

This module provides consolidated 3D geometry functions including:
- Distance between two 3D points (Euclidean distance)
- 3D midpoint calculations
- Vector operations (magnitude, dot product, cross product, angle)
- 3D shape volume calculations (sphere, cylinder, cone, rectangular prism)
- 3D shape surface area calculations

All functions follow the SharkMath error handling standards with ✅/❌ prefixes.
This is a consolidated tool using parameter-based routing.
"""

import math
from typing import Optional


def register_tools(mcp):
    """Register consolidated 3D geometry tool with the MCP server."""
    
    @mcp.tool()
    async def calculate_geometry_3d(
        operation: str,
        x1: Optional[float] = None,
        y1: Optional[float] = None,
        z1: Optional[float] = None,
        x2: Optional[float] = None,
        y2: Optional[float] = None,
        z2: Optional[float] = None,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        radius: Optional[float] = None,
        height: Optional[float] = None,
        length: Optional[float] = None,
        width: Optional[float] = None
    ) -> str:
        """
        Calculate various 3D geometry properties including distance, vectors, volumes, and surface areas.
        
        Args:
            operation: Type of calculation - "distance_3d", "midpoint_3d", "vector_magnitude", 
                      "vector_dot_product", "vector_cross_product", "vector_angle",
                      "sphere_volume", "sphere_surface_area", "cylinder_volume", "cylinder_surface_area",
                      "cone_volume", "cone_surface_area", "rectangular_prism_volume", "rectangular_prism_surface_area"
            x1, y1, z1: Coordinates of first point/vector
            x2, y2, z2: Coordinates of second point/vector
            x, y, z: Single vector coordinates
            radius: Radius for sphere, cylinder, cone calculations
            height: Height for cylinder, cone, rectangular prism calculations
            length, width: Additional dimensions for rectangular prism calculations
            
        Returns:
            String with calculated result
        """
        
        # Define valid operations
        valid_operations = {
            "distance_3d": _calculate_distance_3d,
            "midpoint_3d": _calculate_midpoint_3d,
            "vector_magnitude": _vector_magnitude,
            "vector_dot_product": _vector_dot_product,
            "vector_cross_product": _vector_cross_product,
            "vector_angle": _vector_angle,
            "sphere_volume": _sphere_volume,
            "sphere_surface_area": _sphere_surface_area,
            "cylinder_volume": _cylinder_volume,
            "cylinder_surface_area": _cylinder_surface_area,
            "cone_volume": _cone_volume,
            "cone_surface_area": _cone_surface_area,
            "rectangular_prism_volume": _rectangular_prism_volume,
            "rectangular_prism_surface_area": _rectangular_prism_surface_area
        }
        
        # Validate operation
        if operation not in valid_operations:
            valid_ops = ", ".join(valid_operations.keys())
            return f"❌ Invalid operation '{operation}'. Valid operations: {valid_ops}"
        
        try:
            # Route to appropriate function
            return valid_operations[operation](
                x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2,
                x=x, y=y, z=z, radius=radius, height=height,
                length=length, width=width
            )
            
        except Exception as e:
            return f"❌ Error calculating {operation}: {str(e)}"


def _calculate_distance_3d(x1: Optional[float], y1: Optional[float], z1: Optional[float], 
                          x2: Optional[float], y2: Optional[float], z2: Optional[float], **kwargs) -> str:
    """
    Calculate the Euclidean distance between two points in 3D space.
    Uses the 3D distance formula: d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]
    """
    # Validate required parameters
    if any(param is None for param in [x1, y1, z1, x2, y2, z2]):
        return "❌ 3D distance calculation requires parameters: x1, y1, z1, x2, y2, z2"
    
    # Calculate differences
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    
    # Calculate distance using 3D Pythagorean theorem
    distance = math.sqrt(dx**2 + dy**2 + dz**2)
    
    return f"✅ Distance between points ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is {distance}"


def _calculate_midpoint_3d(x1: Optional[float], y1: Optional[float], z1: Optional[float],
                          x2: Optional[float], y2: Optional[float], z2: Optional[float], **kwargs) -> str:
    """
    Calculate the midpoint between two points in 3D space.
    Uses the midpoint formula: ((x₁+x₂)/2, (y₁+y₂)/2, (z₁+z₂)/2)
    """
    # Validate required parameters
    if any(param is None for param in [x1, y1, z1, x2, y2, z2]):
        return "❌ 3D midpoint calculation requires parameters: x1, y1, z1, x2, y2, z2"
    
    # Calculate midpoint coordinates
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    mid_z = (z1 + z2) / 2
    
    return f"✅ Midpoint between ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is ({mid_x}, {mid_y}, {mid_z})"


def _vector_magnitude(x: Optional[float], y: Optional[float], z: Optional[float], **kwargs) -> str:
    """
    Calculate the magnitude (length) of a 3D vector.
    Uses the formula: |v| = √(x² + y² + z²)
    """
    # Validate required parameters
    if any(param is None for param in [x, y, z]):
        return "❌ Vector magnitude calculation requires parameters: x, y, z"
    
    # Calculate magnitude
    magnitude = math.sqrt(x**2 + y**2 + z**2)
    
    return f"✅ Magnitude of vector ({x}, {y}, {z}) is {magnitude}"


def _vector_dot_product(x1: Optional[float], y1: Optional[float], z1: Optional[float],
                       x2: Optional[float], y2: Optional[float], z2: Optional[float], **kwargs) -> str:
    """
    Calculate the dot product of two 3D vectors.
    Uses the formula: v₁ · v₂ = x₁x₂ + y₁y₂ + z₁z₂
    """
    # Validate required parameters
    if any(param is None for param in [x1, y1, z1, x2, y2, z2]):
        return "❌ Vector dot product calculation requires parameters: x1, y1, z1, x2, y2, z2"
    
    # Calculate dot product
    dot_product = x1*x2 + y1*y2 + z1*z2
    
    # Provide geometric interpretation
    magnitude1 = math.sqrt(x1**2 + y1**2 + z1**2)
    magnitude2 = math.sqrt(x2**2 + y2**2 + z2**2)
    
    if magnitude1 == 0 or magnitude2 == 0:
        interpretation = "(one or both vectors have zero magnitude)"
    elif dot_product == 0:
        interpretation = "(vectors are perpendicular)"
    elif dot_product > 0:
        interpretation = "(vectors point in similar directions)"
    else:
        interpretation = "(vectors point in opposite directions)"
    
    return f"✅ Dot product of vectors ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is {dot_product} {interpretation}"


def _vector_cross_product(x1: Optional[float], y1: Optional[float], z1: Optional[float],
                         x2: Optional[float], y2: Optional[float], z2: Optional[float], **kwargs) -> str:
    """
    Calculate the cross product of two 3D vectors.
    Uses the formula: v₁ × v₂ = (y₁z₂ - z₁y₂, z₁x₂ - x₁z₂, x₁y₂ - y₁x₂)
    """
    # Validate required parameters
    if any(param is None for param in [x1, y1, z1, x2, y2, z2]):
        return "❌ Vector cross product calculation requires parameters: x1, y1, z1, x2, y2, z2"
    
    # Calculate cross product components
    cross_x = y1*z2 - z1*y2
    cross_y = z1*x2 - x1*z2
    cross_z = x1*y2 - y1*x2
    
    # Calculate magnitude of cross product
    cross_magnitude = math.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
    
    return f"✅ Cross product of vectors ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is ({cross_x:.1f}, {cross_y:.1f}, {cross_z:.1f}) with magnitude {cross_magnitude:.1f}"


def _vector_angle(x1: Optional[float], y1: Optional[float], z1: Optional[float],
                 x2: Optional[float], y2: Optional[float], z2: Optional[float], **kwargs) -> str:
    """
    Calculate the angle between two 3D vectors.
    Uses the formula: cos(θ) = (v₁ · v₂) / (|v₁| × |v₂|)
    """
    # Validate required parameters
    if any(param is None for param in [x1, y1, z1, x2, y2, z2]):
        return "❌ Vector angle calculation requires parameters: x1, y1, z1, x2, y2, z2"
    
    # Calculate magnitudes
    magnitude1 = math.sqrt(x1**2 + y1**2 + z1**2)
    magnitude2 = math.sqrt(x2**2 + y2**2 + z2**2)
    
    # Check for zero vectors
    if magnitude1 == 0 or magnitude2 == 0:
        return "❌ Cannot calculate angle with zero vector"
    
    # Calculate dot product
    dot_product = x1*x2 + y1*y2 + z1*z2
    
    # Calculate cosine of angle
    cos_angle = dot_product / (magnitude1 * magnitude2)
    
    # Handle floating point errors
    cos_angle = max(-1.0, min(1.0, cos_angle))
    
    # Calculate angle in radians and degrees
    angle_radians = math.acos(cos_angle)
    angle_degrees = math.degrees(angle_radians)
    
    return f"✅ Angle between vectors ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is {angle_radians:.6f} radians ({angle_degrees:.2f} degrees)"


def _sphere_volume(radius: Optional[float], **kwargs) -> str:
    """
    Calculate the volume of a sphere using V = (4/3)πr³
    """
    # Validate required parameters
    if radius is None:
        return "❌ Sphere volume calculation requires parameter: radius"
    
    # Input validation
    if radius < 0:
        return "❌ Radius cannot be negative"
    
    if radius == 0:
        return "✅ Sphere volume with radius 0 is 0"
    
    volume = (4/3) * math.pi * radius**3
    return f"✅ Sphere volume with radius {radius} is {volume} (≈ {volume:.6f})"


def _sphere_surface_area(radius: Optional[float], **kwargs) -> str:
    """
    Calculate the surface area of a sphere using A = 4πr²
    """
    # Validate required parameters
    if radius is None:
        return "❌ Sphere surface area calculation requires parameter: radius"
    
    # Input validation
    if radius < 0:
        return "❌ Radius cannot be negative"
    
    if radius == 0:
        return "✅ Sphere surface area with radius 0 is 0"
    
    surface_area = 4 * math.pi * radius**2
    return f"✅ Sphere surface area with radius {radius} is {surface_area} (≈ {surface_area:.6f})"


def _cylinder_volume(radius: Optional[float], height: Optional[float], **kwargs) -> str:
    """
    Calculate the volume of a cylinder using V = πr²h
    """
    # Validate required parameters
    if radius is None or height is None:
        return "❌ Cylinder volume calculation requires parameters: radius, height"
    
    # Input validation
    if radius < 0 or height < 0:
        return "❌ Radius and height cannot be negative"
    
    if radius == 0 or height == 0:
        return "✅ Cylinder volume with radius 0 or height 0 is 0"
    
    volume = math.pi * radius**2 * height
    return f"✅ Cylinder volume with radius {radius} and height {height} is {volume} (≈ {volume:.6f})"


def _cylinder_surface_area(radius: Optional[float], height: Optional[float], **kwargs) -> str:
    """
    Calculate the total surface area of a cylinder using A = 2πr² + 2πrh
    """
    # Validate required parameters
    if radius is None or height is None:
        return "❌ Cylinder surface area calculation requires parameters: radius, height"
    
    # Input validation
    if radius < 0 or height < 0:
        return "❌ Radius and height cannot be negative"
    
    # Calculate surface area components
    base_area = 2 * math.pi * radius**2  # Two circular ends
    lateral_area = 2 * math.pi * radius * height  # Curved surface
    total_surface_area = base_area + lateral_area
    
    return f"✅ Cylinder surface area with radius {radius} and height {height} is {total_surface_area} (≈ {total_surface_area:.6f}) [Base: {base_area:.6f}, Lateral: {lateral_area:.6f}]"


def _cone_volume(radius: Optional[float], height: Optional[float], **kwargs) -> str:
    """
    Calculate the volume of a cone using V = (1/3)πr²h
    """
    # Validate required parameters
    if radius is None or height is None:
        return "❌ Cone volume calculation requires parameters: radius, height"
    
    # Input validation
    if radius < 0 or height < 0:
        return "❌ Radius and height cannot be negative"
    
    if radius == 0 or height == 0:
        return "✅ Cone volume with radius 0 or height 0 is 0"
    
    volume = (1/3) * math.pi * radius**2 * height
    return f"✅ Cone volume with radius {radius} and height {height} is {volume} (≈ {volume:.6f})"


def _cone_surface_area(radius: Optional[float], height: Optional[float], **kwargs) -> str:
    """
    Calculate the total surface area of a cone using A = πr² + πr√(r² + h²)
    """
    # Validate required parameters
    if radius is None or height is None:
        return "❌ Cone surface area calculation requires parameters: radius, height"
    
    # Input validation
    if radius < 0 or height < 0:
        return "❌ Radius and height cannot be negative"
    
    # Calculate slant height
    slant_height = math.sqrt(radius**2 + height**2)
    
    # Calculate surface area components
    base_area = math.pi * radius**2  # Circular base
    lateral_area = math.pi * radius * slant_height  # Curved surface
    total_surface_area = base_area + lateral_area
    
    return f"✅ Cone surface area with radius {radius} and height {height} is {total_surface_area} (≈ {total_surface_area:.6f}) [Base: {base_area:.6f}, Lateral: {lateral_area:.6f}, Slant height: {slant_height:.6f}]"


def _rectangular_prism_volume(length: Optional[float], width: Optional[float], height: Optional[float], **kwargs) -> str:
    """
    Calculate the volume of a rectangular prism (box) using V = length × width × height
    """
    # Validate required parameters
    if length is None or width is None or height is None:
        return "❌ Rectangular prism volume calculation requires parameters: length, width, height"
    
    # Input validation
    if length < 0 or width < 0 or height < 0:
        return "❌ Dimensions cannot be negative"
    
    volume = length * width * height
    return f"✅ Rectangular prism volume with dimensions {length} × {width} × {height} is {volume}"


def _rectangular_prism_surface_area(length: Optional[float], width: Optional[float], height: Optional[float], **kwargs) -> str:
    """
    Calculate the surface area of a rectangular prism using A = 2(lw + lh + wh)
    """
    # Validate required parameters
    if length is None or width is None or height is None:
        return "❌ Rectangular prism surface area calculation requires parameters: length, width, height"
    
    # Input validation
    if length < 0 or width < 0 or height < 0:
        return "❌ Dimensions cannot be negative"
    
    # Calculate surface area
    surface_area = 2 * (length*width + length*height + width*height)
    
    # Show breakdown
    face_lw = length * width
    face_lh = length * height
    face_wh = width * height
    
    return f"✅ Rectangular prism surface area with dimensions {length} × {width} × {height} is {surface_area} [Faces: 2×{face_lw:.3f} + 2×{face_lh:.3f} + 2×{face_wh:.3f}]"


# Support for direct execution (testing)
if __name__ == "__main__":
    print("3D Geometry Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
