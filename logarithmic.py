"""
Logarithmic and Exponential Functions Module for SharkMath Server - CONSOLIDATED
Consolidated tool for logarithmic and exponential calculations with parameter-based routing.
"""

import math

# Operation mapping for consolidated tool
LOGARITHMIC_OPERATIONS = {
    "natural_log": "ln",
    "log_base_10": "log10", 
    "log_base": "log_base",
    "exponential": "exp"
}

def register_tools(mcp):
    """Register consolidated logarithmic and exponential tool with the MCP server."""
    
    @mcp.tool()
    async def calculate_logarithmic(
        operation: str,
        value: float,
        base: float = None
    ) -> str:
        """
        Consolidated logarithmic and exponential calculations.
        
        Args:
            operation: The operation to perform ("natural_log", "log_base_10", "log_base", "exponential")
            value: The number to operate on
            base: The base for log_base operation (required only for log_base)
            
        Returns:
            String with ✅ success result or ❌ error message
        """
        try:
            # Validate operation
            if operation not in LOGARITHMIC_OPERATIONS:
                available_ops = ", ".join(LOGARITHMIC_OPERATIONS.keys())
                return f"❌ Invalid operation '{operation}'. Available: {available_ops}"
            
            # Route to appropriate function
            if operation == "natural_log":
                return _calculate_natural_log(value)
            elif operation == "log_base_10":
                return _calculate_log_base_10(value)
            elif operation == "log_base":
                if base is None:
                    return "❌ 'base' parameter required for log_base operation"
                return _calculate_log_base(value, base)
            elif operation == "exponential":
                return _calculate_exponential(value)
            
        except Exception as e:
            return f"❌ Error in logarithmic calculation: {str(e)}"

def _calculate_natural_log(n: float) -> str:
    """Calculate the natural logarithm (ln) of a number with domain validation."""
    try:
        if n <= 0:
            return f"❌ Natural logarithm undefined for n ≤ 0. Input: {n}"
        
        result = math.log(n)
        return f"✅ ln({n}) = {result}"
        
    except Exception as e:
        return f"❌ Error calculating natural logarithm: {str(e)}"

def _calculate_log_base_10(n: float) -> str:
    """Calculate the base-10 logarithm (log₁₀) of a number with domain validation."""
    try:
        if n <= 0:
            return f"❌ Base-10 logarithm undefined for n ≤ 0. Input: {n}"
        
        result = math.log10(n)
        return f"✅ log₁₀({n}) = {result}"
        
    except Exception as e:
        return f"❌ Error calculating base-10 logarithm: {str(e)}"

def _calculate_log_base(n: float, base: float) -> str:
    """Calculate the logarithm of n with a custom base with domain validation."""
    try:
        if n <= 0:
            return f"❌ Logarithm undefined for n ≤ 0. Input: {n}"
        if base <= 0 or base == 1:
            return f"❌ Logarithm base must be positive and not equal to 1. Base: {base}"
        
        result = math.log(n, base)
        return f"✅ log_{base}({n}) = {result}"
        
    except Exception as e:
        return f"❌ Error calculating logarithm with base {base}: {str(e)}"

def _calculate_exponential(n: float) -> str:
    """Calculate e^n (exponential function) with overflow protection."""
    try:
        if n > 700:  # Prevent overflow (e^709 ≈ 8.2e307, close to float max)
            return f"❌ Exponential result would overflow for n > 700. Input: {n}"
        
        result = math.exp(n)
        return f"✅ e^{n} = {result}"
        
    except OverflowError:
        return f"❌ Exponential result too large to represent for n = {n}"
    except Exception as e:
        return f"❌ Error calculating exponential: {str(e)}"

# For direct execution testing
if __name__ == "__main__":
    # Test the logarithmic functions directly
    print("Testing Logarithmic Functions:")
    
    # Mock MCP object for testing
    class MockMCP:
        def tool(self):
            def decorator(func):
                return func
            return decorator
    
    mock_mcp = MockMCP()
    register_tools(mock_mcp)
    
    # Test cases would go here for development/debugging
    print("Logarithmic module loaded successfully!")
