"""
Hyperbolic Functions Module for SharkMath Server
Handles hyperbolic sine, cosine, and tangent calculations.
"""

import math

def register_tools(mcp):
    """Register all hyperbolic functions with the MCP server."""
    
    @mcp.tool()
    async def sinh(x: float) -> str:
        """Calculate the hyperbolic sine (sinh) of x."""
        try:
            # Check for potential overflow (sinh grows exponentially)
            if abs(x) > 700:  # Prevent overflow similar to exponential function
                return f"❌ Hyperbolic sine result would overflow for |x| > 700. Input: {x}"
            
            result = math.sinh(x)
            return f"✅ sinh({x}) = {result}"
            
        except OverflowError:
            return f"❌ Hyperbolic sine result too large to represent for x = {x}"
        except Exception as e:
            return f"❌ Error calculating hyperbolic sine: {str(e)}"
    
    @mcp.tool()
    async def cosh(x: float) -> str:
        """Calculate the hyperbolic cosine (cosh) of x."""
        try:
            # Check for potential overflow (cosh grows exponentially)
            if abs(x) > 700:  # Prevent overflow similar to exponential function
                return f"❌ Hyperbolic cosine result would overflow for |x| > 700. Input: {x}"
            
            result = math.cosh(x)
            return f"✅ cosh({x}) = {result}"
            
        except OverflowError:
            return f"❌ Hyperbolic cosine result too large to represent for x = {x}"
        except Exception as e:
            return f"❌ Error calculating hyperbolic cosine: {str(e)}"
    
    @mcp.tool()
    async def tanh(x: float) -> str:
        """Calculate the hyperbolic tangent (tanh) of x."""
        try:
            # tanh is bounded between -1 and 1, so no overflow concerns
            result = math.tanh(x)
            return f"✅ tanh({x}) = {result}"
            
        except Exception as e:
            return f"❌ Error calculating hyperbolic tangent: {str(e)}"

# For direct execution testing
if __name__ == "__main__":
    # Test the hyperbolic functions directly
    print("Testing Hyperbolic Functions:")
    
    # Mock MCP object for testing
    class MockMCP:
        def tool(self):
            def decorator(func):
                return func
            return decorator
    
    mock_mcp = MockMCP()
    register_tools(mock_mcp)
    
    # Test cases would go here for development/debugging
    print("Hyperbolic module loaded successfully!")
