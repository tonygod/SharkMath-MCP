"""
Combinatorics and factorial operations module for SharkMath MCP server.
Contains factorial, permutation, combination, and Fibonacci functions.
"""
import math

def register_tools(mcp):
    """Register all combinatorial tools with the MCP server."""
    
    @mcp.tool()
    async def factorial(n: int) -> str:
        """Calculate n! (factorial) with non-negative integer validation."""
        try:
            if n < 0:
                return "❌ Error: Factorial is not defined for negative numbers!"
            
            if not isinstance(n, int) and not n.is_integer():
                return "❌ Error: Factorial requires a non-negative integer!"
            
            n = int(n)  # Convert to int if it's a float that represents an integer
            
            if n > 170:  # Factorial becomes very large very quickly
                return "❌ Error: Factorial too large to calculate (n > 170)!"
            
            result = math.factorial(n)
            return f"✅ {n}! = {result}"
        except Exception as e:
            return f"❌ Error calculating factorial: {str(e)}"

    @mcp.tool()
    async def permutation(n: int, r: int) -> str:
        """Calculate P(n,r) = n!/(n-r)! (permutations)."""
        try:
            if n < 0 or r < 0:
                return "❌ Error: Permutation requires non-negative integers!"
            
            if not (isinstance(n, int) and isinstance(r, int)) and not (n.is_integer() and r.is_integer()):
                return "❌ Error: Permutation requires integers!"
            
            n, r = int(n), int(r)  # Convert to int if needed
            
            if r > n:
                return "❌ Error: Cannot select more items (r) than available (n)!"
            
            if n > 170:  # Prevent overflow
                return "❌ Error: Values too large to calculate!"
            
            result = math.perm(n, r)
            return f"✅ P({n},{r}) = {n}!/({n}-{r})! = {result}"
        except Exception as e:
            return f"❌ Error calculating permutation: {str(e)}"

    @mcp.tool()
    async def combination(n: int, r: int) -> str:
        """Calculate C(n,r) = n!/(r!(n-r)!) (combinations)."""
        try:
            if n < 0 or r < 0:
                return "❌ Error: Combination requires non-negative integers!"
            
            if not (isinstance(n, int) and isinstance(r, int)) and not (n.is_integer() and r.is_integer()):
                return "❌ Error: Combination requires integers!"
            
            n, r = int(n), int(r)  # Convert to int if needed
            
            if r > n:
                return "❌ Error: Cannot select more items (r) than available (n)!"
            
            if n > 170:  # Prevent overflow
                return "❌ Error: Values too large to calculate!"
            
            result = math.comb(n, r)
            return f"✅ C({n},{r}) = {n}!/({r}!*({n}-{r})!) = {result}"
        except Exception as e:
            return f"❌ Error calculating combination: {str(e)}"

    @mcp.tool()
    async def fibonacci(n: int) -> str:
        """Calculate the nth Fibonacci number (0-indexed)."""
        try:
            if n < 0:
                return "❌ Error: Fibonacci sequence is not defined for negative indices!"
            
            if not isinstance(n, int) and not n.is_integer():
                return "❌ Error: Fibonacci requires a non-negative integer!"
            
            n = int(n)  # Convert to int if needed
            
            if n > 1000:  # Prevent very long calculations
                return "❌ Error: Fibonacci index too large (n > 1000)!"
            
            # Calculate Fibonacci using iterative approach for efficiency
            if n == 0:
                result = 0
            elif n == 1:
                result = 1
            else:
                a, b = 0, 1
                for _ in range(2, n + 1):
                    a, b = b, a + b
                result = b
            
            return f"✅ Fibonacci({n}) = {result}"
        except Exception as e:
            return f"❌ Error calculating Fibonacci: {str(e)}"
