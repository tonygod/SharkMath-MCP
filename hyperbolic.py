"""
Hyperbolic Functions Module for SharkMath Server - CONSOLIDATED
Consolidated tool for hyperbolic sine, cosine, and tangent calculations with parameter-based routing.
"""

import math

# Operation mapping for consolidated tool
HYPERBOLIC_OPERATIONS = {
    "sinh": "sinh",
    "cosh": "cosh", 
    "tanh": "tanh"
}

def register_tools(mcp):
    """Register consolidated hyperbolic functions tool with the MCP server."""
    
    @mcp.tool()
    async def calculate_hyperbolic(
        operation: str,
        value: float
    ) -> str:
        """
        Consolidated hyperbolic function calculations.
        
        Args:
            operation: The operation to perform ("sinh", "cosh", "tanh")
            value: The number to operate on
            
        Returns:
            String with ✅ success result or ❌ error message
        """
        try:
            # Validate operation
            if operation not in HYPERBOLIC_OPERATIONS:
                available_ops = ", ".join(HYPERBOLIC_OPERATIONS.keys())
                return f"❌ Invalid operation '{operation}'. Available: {available_ops}"
            
            # Route to appropriate function
            if operation == "sinh":
                return _calculate_sinh(value)
            elif operation == "cosh":
                return _calculate_cosh(value)
            elif operation == "tanh":
                return _calculate_tanh(value)
            
        except Exception as e:
            return f"❌ Error in hyperbolic calculation: {str(e)}"

def _calculate_sinh(x: float) -> str:
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

def _calculate_cosh(x: float) -> str:
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

def _calculate_tanh(x: float) -> str:
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
