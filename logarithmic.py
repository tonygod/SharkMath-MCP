"""
Logarithmic and Exponential Functions Module for SharkMath Server
Handles logarithmic calculations with domain validation and exponential operations.
"""

import math

def register_tools(mcp):
    """Register all logarithmic and exponential functions with the MCP server."""
    
    @mcp.tool()
    async def natural_log(n: float) -> str:
        """Calculate the natural logarithm (ln) of a number with domain validation."""
        try:
            if n <= 0:
                return f"❌ Natural logarithm undefined for n ≤ 0. Input: {n}"
            
            result = math.log(n)
            return f"✅ ln({n}) = {result}"
            
        except Exception as e:
            return f"❌ Error calculating natural logarithm: {str(e)}"
    
    @mcp.tool()
    async def log_base_10(n: float) -> str:
        """Calculate the base-10 logarithm (log₁₀) of a number with domain validation."""
        try:
            if n <= 0:
                return f"❌ Base-10 logarithm undefined for n ≤ 0. Input: {n}"
            
            result = math.log10(n)
            return f"✅ log₁₀({n}) = {result}"
            
        except Exception as e:
            return f"❌ Error calculating base-10 logarithm: {str(e)}"
    
    @mcp.tool()
    async def log_base(n: float, base: float) -> str:
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
    
    @mcp.tool()
    async def exponential(n: float) -> str:
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
