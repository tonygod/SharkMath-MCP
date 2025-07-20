"""
Precision and rounding operations module for SharkMath MCP server.
Contains rounding, floor, ceiling, truncate, and absolute value functions.
"""
import math

def register_tools(mcp):
    """Register all precision and rounding tools with the MCP server."""
    
    @mcp.tool()
    async def round_to_decimal(n: float, places: int) -> str:
        """Round a number to specified decimal places."""
        try:
            if places < 0:
                return "❌ Error: Decimal places cannot be negative!"
            
            result = round(n, places)
            return f"✅ {n} rounded to {places} decimal places = {result}"
        except Exception as e:
            return f"❌ Error rounding number: {str(e)}"

    @mcp.tool()
    async def floor(n: float) -> str:
        """Calculate the floor of a number (largest integer ≤ n)."""
        try:
            result = math.floor(n)
            return f"✅ floor({n}) = {result}"
        except Exception as e:
            return f"❌ Error calculating floor: {str(e)}"

    @mcp.tool()
    async def ceiling(n: float) -> str:
        """Calculate the ceiling of a number (smallest integer ≥ n)."""
        try:
            result = math.ceil(n)
            return f"✅ ceil({n}) = {result}"
        except Exception as e:
            return f"❌ Error calculating ceiling: {str(e)}"

    @mcp.tool()
    async def truncate(n: float) -> str:
        """Truncate the decimal part of a number (round toward zero)."""
        try:
            result = math.trunc(n)
            return f"✅ trunc({n}) = {result}"
        except Exception as e:
            return f"❌ Error truncating number: {str(e)}"

    @mcp.tool()
    async def absolute(n: float) -> str:
        """Calculate the absolute value of a number."""
        try:
            result = abs(n)
            return f"✅ |{n}| = {result}"
        except Exception as e:
            return f"❌ Error calculating absolute value: {str(e)}"
