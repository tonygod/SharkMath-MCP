"""
Power and root operations module for SharkMath MCP server.
Contains power, square, cube, square root, cube root, and nth root functions.
"""
import math

def register_tools(mcp):
    """Register all power and root operation tools with the MCP server."""
    
    @mcp.tool()
    async def power(base: float, exponent: float) -> str:
        """Calculate base raised to the power of exponent."""
        try:
            result = base ** exponent
            return f"✅ {base}^{exponent} = {result}"
        except OverflowError:
            return "❌ Error: Result too large to calculate!"
        except Exception as e:
            return f"❌ Error performing power operation: {str(e)}"

    @mcp.tool()
    async def square(n: float) -> str:
        """Calculate n²."""
        try:
            result = n * n
            return f"✅ {n}² = {result}"
        except Exception as e:
            return f"❌ Error calculating square: {str(e)}"

    @mcp.tool()
    async def cube(n: float) -> str:
        """Calculate n³."""
        try:
            result = n * n * n
            return f"✅ {n}³ = {result}"
        except Exception as e:
            return f"❌ Error calculating cube: {str(e)}"

    @mcp.tool()
    async def square_root(n: float) -> str:
        """Calculate √n with negative number validation."""
        try:
            if n < 0:
                return "❌ Error: Cannot calculate square root of negative number!"
            
            result = math.sqrt(n)
            return f"✅ √{n} = {result}"
        except Exception as e:
            return f"❌ Error calculating square root: {str(e)}"

    @mcp.tool()
    async def cube_root(n: float) -> str:
        """Calculate ∛n."""
        try:
            # Handle negative numbers for cube root (unlike square root, cube root of negative is valid)
            if n >= 0:
                result = n ** (1/3)
            else:
                result = -((-n) ** (1/3))
            
            return f"✅ ∛{n} = {result}"
        except Exception as e:
            return f"❌ Error calculating cube root: {str(e)}"

    @mcp.tool()
    async def nth_root(n: float, root: float) -> str:
        """Calculate nth root of a number."""
        try:
            if root == 0:
                return "❌ Error: Root cannot be zero!"
            
            # Handle even roots of negative numbers
            if n < 0 and root % 2 == 0:
                return f"❌ Error: Cannot calculate even root ({root}) of negative number ({n})!"
            
            # Calculate nth root
            if n >= 0:
                result = n ** (1/root)
            else:
                # For odd roots of negative numbers
                result = -((-n) ** (1/root))
            
            return f"✅ {n}^(1/{root}) = {result}"
        except ZeroDivisionError:
            return "❌ Error: Root cannot be zero!"
        except Exception as e:
            return f"❌ Error calculating nth root: {str(e)}"
