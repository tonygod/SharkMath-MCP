"""
Number Theory and Combinatorics Functions Module for SharkMath Server - CONSOLIDATED
Consolidated tool for number theory operations and combinatorial mathematics.
Combines GCD, LCM, prime checking, factorization, factorial, permutations, combinations, and Fibonacci.
"""

import math

# Operation mapping for consolidated tool
NUMBER_ANALYSIS_OPERATIONS = {
    # Number theory operations
    "gcd": "gcd",
    "lcm": "lcm",
    "is_prime": "is_prime",
    "prime_factors": "prime_factors",
    "is_perfect_square": "is_perfect_square",
    # Combinatorial operations
    "factorial": "factorial",
    "permutation": "permutation",
    "combination": "combination",
    "fibonacci": "fibonacci"
}

def register_tools(mcp):
    """Register consolidated number theory and combinatorial analysis tool with the MCP server."""
    
    @mcp.tool()
    async def analyze_numbers(
        operation: str,
        value: int,
        second_value: int = None
    ) -> str:
        """
        Consolidated number theory and combinatorial analysis operations.
        
        Args:
            operation: The operation to perform ("gcd", "lcm", "is_prime", "prime_factors", 
                      "is_perfect_square", "factorial", "permutation", "combination", "fibonacci")
            value: The primary number to operate on
            second_value: The second number (required for gcd, lcm, permutation, combination)
            
        Returns:
            String with ✅ success result or ❌ error message
        """
        try:
            # Validate operation
            if operation not in NUMBER_ANALYSIS_OPERATIONS:
                available_ops = ", ".join(NUMBER_ANALYSIS_OPERATIONS.keys())
                return f"❌ Invalid operation '{operation}'. Available: {available_ops}"
            
            # Route to appropriate function based on operation type
            if operation == "gcd":
                if second_value is None:
                    return "❌ 'second_value' parameter required for gcd operation"
                return _calculate_gcd(value, second_value)
            elif operation == "lcm":
                if second_value is None:
                    return "❌ 'second_value' parameter required for lcm operation"
                return _calculate_lcm(value, second_value)
            elif operation == "is_prime":
                return _check_is_prime(value)
            elif operation == "prime_factors":
                return _find_prime_factors(value)
            elif operation == "is_perfect_square":
                return _check_is_perfect_square(value)
            elif operation == "factorial":
                return _calculate_factorial(value)
            elif operation == "permutation":
                if second_value is None:
                    return "❌ 'second_value' parameter required for permutation operation"
                return _calculate_permutation(value, second_value)
            elif operation == "combination":
                if second_value is None:
                    return "❌ 'second_value' parameter required for combination operation"
                return _calculate_combination(value, second_value)
            elif operation == "fibonacci":
                return _calculate_fibonacci(value)
            
        except Exception as e:
            return f"❌ Error in number analysis: {str(e)}"

# Number Theory Functions
def _calculate_gcd(a: int, b: int) -> str:
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

def _calculate_lcm(a: int, b: int) -> str:
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

def _check_is_prime(n: int) -> str:
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

def _find_prime_factors(n: int) -> str:
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

def _check_is_perfect_square(n: int) -> str:
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

# Combinatorial Functions
def _calculate_factorial(n: int) -> str:
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

def _calculate_permutation(n: int, r: int) -> str:
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

def _calculate_combination(n: int, r: int) -> str:
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

def _calculate_fibonacci(n: int) -> str:
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
