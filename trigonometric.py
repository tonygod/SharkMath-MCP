"""
Trigonometric functions module for SharkMath MCP server.
Contains sine, cosine, tangent functions in both radians and degrees,
plus inverse trigonometric functions.
"""
import math

def register_tools(mcp):
    """Register all trigonometric tools with the MCP server."""
    
    @mcp.tool()
    async def sin(angle_radians: float) -> str:
        """Calculate the sine of an angle in radians."""
        try:
            result = math.sin(angle_radians)
            return f"✅ sin({angle_radians} rad) = {result}"
        except Exception as e:
            return f"❌ Error calculating sine: {str(e)}"

    @mcp.tool()
    async def cos(angle_radians: float) -> str:
        """Calculate the cosine of an angle in radians."""
        try:
            result = math.cos(angle_radians)
            return f"✅ cos({angle_radians} rad) = {result}"
        except Exception as e:
            return f"❌ Error calculating cosine: {str(e)}"

    @mcp.tool()
    async def tan(angle_radians: float) -> str:
        """Calculate the tangent of an angle in radians."""
        try:
            # Check for angles close to π/2 + nπ where tangent is undefined
            # Using a small tolerance to catch floating point approximations
            normalized_angle = angle_radians % math.pi
            if abs(normalized_angle - math.pi/2) < 1e-10:
                return f"❌ Error: Tangent is undefined at {angle_radians} rad (π/2 + nπ)"
            
            result = math.tan(angle_radians)
            
            # Check for very large results that might indicate near-undefined values
            if abs(result) > 1e10:
                return f"⚠️ tan({angle_radians} rad) = {result} (very large, near undefined)"
            
            return f"✅ tan({angle_radians} rad) = {result}"
        except Exception as e:
            return f"❌ Error calculating tangent: {str(e)}"

    @mcp.tool()
    async def sin_degrees(angle_degrees: float) -> str:
        """Calculate the sine of an angle in degrees."""
        try:
            angle_radians = math.radians(angle_degrees)
            result = math.sin(angle_radians)
            return f"✅ sin({angle_degrees}°) = {result}"
        except Exception as e:
            return f"❌ Error calculating sine: {str(e)}"

    @mcp.tool()
    async def cos_degrees(angle_degrees: float) -> str:
        """Calculate the cosine of an angle in degrees."""
        try:
            angle_radians = math.radians(angle_degrees)
            result = math.cos(angle_radians)
            return f"✅ cos({angle_degrees}°) = {result}"
        except Exception as e:
            return f"❌ Error calculating cosine: {str(e)}"

    @mcp.tool()
    async def tan_degrees(angle_degrees: float) -> str:
        """Calculate the tangent of an angle in degrees."""
        try:
            # Check for angles where tangent is undefined (90° + n*180°)
            normalized_degrees = angle_degrees % 180
            if abs(normalized_degrees - 90) < 1e-10:
                return f"❌ Error: Tangent is undefined at {angle_degrees}° (90° + n*180°)"
            
            angle_radians = math.radians(angle_degrees)
            result = math.tan(angle_radians)
            
            # Check for very large results
            if abs(result) > 1e10:
                return f"⚠️ tan({angle_degrees}°) = {result} (very large, near undefined)"
            
            return f"✅ tan({angle_degrees}°) = {result}"
        except Exception as e:
            return f"❌ Error calculating tangent: {str(e)}"

    @mcp.tool()
    async def asin(value: float) -> str:
        """Calculate the arcsine (inverse sine) of a value. Result in radians."""
        try:
            if value < -1 or value > 1:
                return f"❌ Error: arcsine domain is [-1, 1]. Input {value} is out of range!"
            
            result_radians = math.asin(value)
            result_degrees = math.degrees(result_radians)
            return f"✅ arcsin({value}) = {result_radians} rad = {result_degrees}°"
        except Exception as e:
            return f"❌ Error calculating arcsine: {str(e)}"

    @mcp.tool()
    async def acos(value: float) -> str:
        """Calculate the arccosine (inverse cosine) of a value. Result in radians."""
        try:
            if value < -1 or value > 1:
                return f"❌ Error: arccosine domain is [-1, 1]. Input {value} is out of range!"
            
            result_radians = math.acos(value)
            result_degrees = math.degrees(result_radians)
            return f"✅ arccos({value}) = {result_radians} rad = {result_degrees}°"
        except Exception as e:
            return f"❌ Error calculating arccosine: {str(e)}"

    @mcp.tool()
    async def atan(value: float) -> str:
        """Calculate the arctangent (inverse tangent) of a value. Result in radians."""
        try:
            result_radians = math.atan(value)
            result_degrees = math.degrees(result_radians)
            return f"✅ arctan({value}) = {result_radians} rad = {result_degrees}°"
        except Exception as e:
            return f"❌ Error calculating arctangent: {str(e)}"

    @mcp.tool()
    async def atan2(y: float, x: float) -> str:
        """Calculate the two-argument arctangent atan2(y,x). Result in radians."""
        try:
            if x == 0 and y == 0:
                return "❌ Error: atan2(0,0) is undefined!"
            
            result_radians = math.atan2(y, x)
            result_degrees = math.degrees(result_radians)
            return f"✅ atan2({y}, {x}) = {result_radians} rad = {result_degrees}°"
        except Exception as e:
            return f"❌ Error calculating atan2: {str(e)}"
