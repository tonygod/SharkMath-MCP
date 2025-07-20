"""
Number Theory Functions Module for SharkMath Server
Handles number theory operations including GCD, LCM, prime checking, and prime factorization.
"""

import math

def register_tools(mcp):
    """Register all number theory functions with the MCP server."""
    
    @mcp.tool()
    async def gcd(a: int, b: int) -> str:
        """Calculate the Greatest Common Divisor (GCD) of two integers."""
        try:
            # Convert to integers and get absolute values
            a_int = int(abs(a))
            b_int = int(abs(b))
            
            if a_int == 0 and b_int == 0:
                return "❌ GCD is undefined for gcd(0, 0)"
            
            result = math.gcd(a_int, b_int)
            return f"✅ gcd({a}, {b}) = {result}"
            
        except Exception as e:
            return f"❌ Error calculating GCD: {str(e)}"
    
    @mcp.tool()
    async def lcm(a: int, b: int) -> str:
        """Calculate the Least Common Multiple (LCM) of two integers."""
        try:
            # Convert to integers and get absolute values
            a_int = int(abs(a))
            b_int = int(abs(b))
            
            if a_int == 0 or b_int == 0:
                return f"✅ lcm({a}, {b}) = 0 (LCM with zero is always zero)"
            
            # LCM = |a * b| / GCD(a, b)
            gcd_value = math.gcd(a_int, b_int)
            result = (a_int * b_int) // gcd_value
            return f"✅ lcm({a}, {b}) = {result}"
            
        except Exception as e:
            return f"❌ Error calculating LCM: {str(e)}"
    
    @mcp.tool()
    async def is_prime(n: int) -> str:
        """Check if a number is prime."""
        try:
            n_int = int(n)
            
            if n_int < 2:
                return f"✅ {n} is not prime (primes must be ≥ 2)"
            
            if n_int == 2:
                return f"✅ {n} is prime"
            
            if n_int % 2 == 0:
                return f"✅ {n} is not prime (divisible by 2)"
            
            # Check odd divisors up to sqrt(n)
            for i in range(3, int(math.sqrt(n_int)) + 1, 2):
                if n_int % i == 0:
                    return f"✅ {n} is not prime (divisible by {i})"
            
            return f"✅ {n} is prime"
            
        except Exception as e:
            return f"❌ Error checking if number is prime: {str(e)}"
    
    @mcp.tool()
    async def prime_factors(n: int) -> str:
        """Find all prime factors of a number."""
        try:
            n_int = int(abs(n))
            
            if n_int == 0:
                return "❌ Prime factorization undefined for 0"
            if n_int == 1:
                return "✅ Prime factors of 1: [] (1 has no prime factors)"
            
            factors = []
            original_n = n_int
            
            # Check for factor of 2
            while n_int % 2 == 0:
                factors.append(2)
                n_int //= 2
            
            # Check for odd factors from 3 onwards
            i = 3
            while i * i <= n_int:
                while n_int % i == 0:
                    factors.append(i)
                    n_int //= i
                i += 2
            
            # If n_int is still > 1, it's a prime factor
            if n_int > 1:
                factors.append(n_int)
            
            factors_str = " × ".join(map(str, factors))
            return f"✅ Prime factors of {original_n}: {factors} = {factors_str}"
            
        except Exception as e:
            return f"❌ Error finding prime factors: {str(e)}"
    
    @mcp.tool()
    async def is_perfect_square(n: int) -> str:
        """Check if a number is a perfect square."""
        try:
            n_int = int(n)
            
            if n_int < 0:
                return f"✅ {n} is not a perfect square (negative numbers cannot be perfect squares)"
            
            if n_int == 0:
                return f"✅ {n} is a perfect square (0 = 0²)"
            
            # Find integer square root
            sqrt_n = int(math.sqrt(n_int))
            
            # Check if it's exact
            if sqrt_n * sqrt_n == n_int:
                return f"✅ {n} is a perfect square ({sqrt_n}² = {n})"
            else:
                return f"✅ {n} is not a perfect square (√{n} ≈ {math.sqrt(n_int):.3f})"
            
        except Exception as e:
            return f"❌ Error checking if number is perfect square: {str(e)}"

# For direct execution testing
if __name__ == "__main__":
    # Test the number theory functions directly
    print("Testing Number Theory Functions:")
    
    # Mock MCP object for testing
    class MockMCP:
        def tool(self):
            def decorator(func):
                return func
            return decorator
    
    mock_mcp = MockMCP()
    register_tools(mock_mcp)
    
    # Test cases would go here for development/debugging
    print("Number theory module loaded successfully!")
