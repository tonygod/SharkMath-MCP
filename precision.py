"""
Precision and rounding operations module for SharkMath MCP server - CONSOLIDATED
Consolidated tool for rounding, floor, ceiling, truncate, and absolute value functions.
"""
import math

# Operation mapping for consolidated tool
PRECISION_OPERATIONS = {
    "round": "round_to_decimal",
    "floor": "floor",
    "ceiling": "ceiling", 
    "truncate": "truncate",
    "absolute": "absolute"
}

def register_tools(mcp):
    """Register consolidated precision and rounding tool with the MCP server."""
    
    @mcp.tool()
    async def format_precision(
        operation: str,
        value: float,
        places: int = None
    ) -> str:
        """
        Consolidated precision and rounding operations.
        
        Args:
            operation: The operation to perform ("round", "floor", "ceiling", "truncate", "absolute")
            value: The number to operate on
            places: Number of decimal places (required only for round operation)
            
        Returns:
            String with ✅ success result or ❌ error message
        """
        try:
            # Validate operation
            if operation not in PRECISION_OPERATIONS:
                available_ops = ", ".join(PRECISION_OPERATIONS.keys())
                return f"❌ Invalid operation '{operation}'. Available: {available_ops}"
            
            # Route to appropriate function
            if operation == "round":
                if places is None:
                    return "❌ 'places' parameter required for round operation"
                return _round_to_decimal(value, places)
            elif operation == "floor":
                return _floor(value)
            elif operation == "ceiling":
                return _ceiling(value)
            elif operation == "truncate":
                return _truncate(value)
            elif operation == "absolute":
                return _absolute(value)
            
        except Exception as e:
            return f"❌ Error in precision calculation: {str(e)}"

def _round_to_decimal(n: float, places: int) -> str:
    """Round a number to specified decimal places."""
    try:
        if places < 0:
            return "❌ Error: Decimal places cannot be negative!"
        
        result = round(n, places)
        return f"✅ {n} rounded to {places} decimal places = {result}"
    except Exception as e:
        return f"❌ Error rounding number: {str(e)}"

def _floor(n: float) -> str:
    """Calculate the floor of a number (largest integer ≤ n)."""
    try:
        result = math.floor(n)
        return f"✅ floor({n}) = {result}"
    except Exception as e:
        return f"❌ Error calculating floor: {str(e)}"

def _ceiling(n: float) -> str:
    """Calculate the ceiling of a number (smallest integer ≥ n)."""
    try:
        result = math.ceil(n)
        return f"✅ ceil({n}) = {result}"
    except Exception as e:
        return f"❌ Error calculating ceiling: {str(e)}"

def _truncate(n: float) -> str:
    """Truncate the decimal part of a number (round toward zero)."""
    try:
        result = math.trunc(n)
        return f"✅ trunc({n}) = {result}"
    except Exception as e:
        return f"❌ Error truncating number: {str(e)}"

def _absolute(n: float) -> str:
    """Calculate the absolute value of a number."""
    try:
        result = abs(n)
        return f"✅ |{n}| = {result}"
    except Exception as e:
        return f"❌ Error calculating absolute value: {str(e)}"
