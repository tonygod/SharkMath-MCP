"""
2D Geometry Calculations Module for SharkMath MCP Server

This module provides consolidated 2D geometry functions including:
- Distance between two points (Euclidean distance)
- Slope between two points
- Circle area and circumference
- Rectangle area and perimeter
- Triangle area (using base and height)
- Right triangle area (using two sides)

All functions follow the SharkMath error handling standards with ✅/❌ prefixes.
This is a consolidated tool using parameter-based routing.
"""

import math
from typing import Optional


def register_tools(mcp):
    """Register consolidated 2D geometry tool with the MCP server."""
    
    @mcp.tool()
    async def calculate_geometry_2d(
        operation: str,
        x1: Optional[float] = None,
        y1: Optional[float] = None,
        x2: Optional[float] = None,
        y2: Optional[float] = None,
        radius: Optional[float] = None,
        length: Optional[float] = None,
        width: Optional[float] = None,
        base: Optional[float] = None,
        height: Optional[float] = None,
        side_a: Optional[float] = None,
        side_b: Optional[float] = None
    ) -> str:
        """
        Calculate various 2D geometry properties including distance, slope, areas, and perimeters.
        
        Args:
            operation: Type of calculation - "distance", "slope", "circle_area", "circle_circumference", 
                      "rectangle_area", "rectangle_perimeter", "triangle_area", "right_triangle_area"
            x1, y1: Coordinates of first point (for distance and slope)
            x2, y2: Coordinates of second point (for distance and slope)
            radius: Radius for circle calculations
            length, width: Dimensions for rectangle calculations
            base, height: Base and height for triangle area
            side_a, side_b: Two sides for right triangle area calculation
            
        Returns:
            String with calculated result
        """
        
        # Define valid operations
        valid_operations = {
            "distance": _calculate_distance,
            "slope": _calculate_slope,
            "circle_area": _circle_area,
            "circle_circumference": _circle_circumference,
            "rectangle_area": _rectangle_area,
            "rectangle_perimeter": _rectangle_perimeter,
            "triangle_area": _triangle_area,
            "right_triangle_area": _right_triangle_area
        }
        
        # Validate operation
        if operation not in valid_operations:
            valid_ops = ", ".join(valid_operations.keys())
            return f"❌ Invalid operation '{operation}'. Valid operations: {valid_ops}"
        
        try:
            # Route to appropriate function
            return valid_operations[operation](
                x1=x1, y1=y1, x2=x2, y2=y2,
                radius=radius, length=length, width=width,
                base=base, height=height, side_a=side_a, side_b=side_b
            )
            
        except Exception as e:
            return f"❌ Error calculating {operation}: {str(e)}"


def _calculate_distance(x1: Optional[float], y1: Optional[float], x2: Optional[float], y2: Optional[float], **kwargs) -> str:
    """
    Calculate the Euclidean distance between two points in 2D space.
    Uses the distance formula: d = √[(x₂-x₁)² + (y₂-y₁)²]
    """
    # Validate required parameters
    if any(param is None for param in [x1, y1, x2, y2]):
        return "❌ Distance calculation requires parameters: x1, y1, x2, y2"
    
    # Calculate differences
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate distance using Pythagorean theorem
    distance = math.sqrt(dx**2 + dy**2)
    
    return f"✅ Distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance}"


def _calculate_slope(x1: Optional[float], y1: Optional[float], x2: Optional[float], y2: Optional[float], **kwargs) -> str:
    """
    Calculate the slope between two points in 2D space.
    Uses the slope formula: m = (y₂-y₁)/(x₂-x₁)
    """
    # Validate required parameters
    if any(param is None for param in [x1, y1, x2, y2]):
        return "❌ Slope calculation requires parameters: x1, y1, x2, y2"
    
    # Check for vertical line (undefined slope)
    if x2 == x1:
        return f"✅ Slope is undefined (vertical line) between points ({x1}, {y1}) and ({x2}, {y2})"
    
    # Calculate slope
    slope_value = (y2 - y1) / (x2 - x1)
    
    # Provide additional context for special slopes
    if slope_value == 0:
        return f"✅ Slope between points ({x1}, {y1}) and ({x2}, {y2}) is 0 (horizontal line)"
    elif slope_value == 1:
        return f"✅ Slope between points ({x1}, {y1}) and ({x2}, {y2}) is 1 (45° upward)"
    elif slope_value == -1:
        return f"✅ Slope between points ({x1}, {y1}) and ({x2}, {y2}) is -1 (45° downward)"
    else:
        return f"✅ Slope between points ({x1}, {y1}) and ({x2}, {y2}) is {slope_value}"


def _circle_area(radius: Optional[float], **kwargs) -> str:
    """
    Calculate the area of a circle using A = πr²
    """
    # Validate required parameters
    if radius is None:
        return "❌ Circle area calculation requires parameter: radius"
    
    # Input validation
    if radius < 0:
        return "❌ Radius cannot be negative"
    
    if radius == 0:
        return "✅ Circle area with radius 0 is 0"
    
    area = math.pi * radius**2
    return f"✅ Circle area with radius {radius} is {area} (≈ {area:.6f})"


def _circle_circumference(radius: Optional[float], **kwargs) -> str:
    """
    Calculate the circumference of a circle using C = 2πr
    """
    # Validate required parameters
    if radius is None:
        return "❌ Circle circumference calculation requires parameter: radius"
    
    # Input validation
    if radius < 0:
        return "❌ Radius cannot be negative"
    
    if radius == 0:
        return "✅ Circle circumference with radius 0 is 0"
    
    circumference = 2 * math.pi * radius
    return f"✅ Circle circumference with radius {radius} is {circumference} (≈ {circumference:.6f})"


def _rectangle_area(length: Optional[float], width: Optional[float], **kwargs) -> str:
    """
    Calculate the area of a rectangle using A = length × width
    """
    # Validate required parameters
    if length is None or width is None:
        return "❌ Rectangle area calculation requires parameters: length, width"
    
    # Input validation
    if length < 0 or width < 0:
        return "❌ Length and width cannot be negative"
    
    area = length * width
    return f"✅ Rectangle area with length {length} and width {width} is {area}"


def _rectangle_perimeter(length: Optional[float], width: Optional[float], **kwargs) -> str:
    """
    Calculate the perimeter of a rectangle using P = 2(length + width)
    """
    # Validate required parameters
    if length is None or width is None:
        return "❌ Rectangle perimeter calculation requires parameters: length, width"
    
    # Input validation
    if length < 0 or width < 0:
        return "❌ Length and width cannot be negative"
    
    perimeter = 2 * (length + width)
    return f"✅ Rectangle perimeter with length {length} and width {width} is {perimeter}"


def _triangle_area(base: Optional[float], height: Optional[float], **kwargs) -> str:
    """
    Calculate the area of a triangle using A = (1/2) × base × height
    """
    # Validate required parameters
    if base is None or height is None:
        return "❌ Triangle area calculation requires parameters: base, height"
    
    # Input validation
    if base < 0 or height < 0:
        return "❌ Base and height cannot be negative"
    
    area = 0.5 * base * height
    return f"✅ Triangle area with base {base} and height {height} is {area}"


def _right_triangle_area(side_a: Optional[float], side_b: Optional[float], **kwargs) -> str:
    """
    Calculate the area of a right triangle using A = (1/2) × side_a × side_b
    """
    # Validate required parameters
    if side_a is None or side_b is None:
        return "❌ Right triangle area calculation requires parameters: side_a, side_b"
    
    # Input validation
    if side_a < 0 or side_b < 0:
        return "❌ Triangle sides cannot be negative"
    
    area = 0.5 * side_a * side_b
    return f"✅ Right triangle area with sides {side_a} and {side_b} is {area}"


# Support for direct execution (testing)
if __name__ == "__main__":
    print("2D Geometry Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
