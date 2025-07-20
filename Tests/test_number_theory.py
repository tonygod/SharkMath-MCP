"""
Test suite for number_theory.py module

Tests number theory functions: gcd, lcm, is_prime, prime_factors, is_perfect_square
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import number_theory


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestNumberTheory:
    """Test class for number theory functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        number_theory.register_tools(self.mcp)
    
    async def test_gcd_basic(self):
        """Test GCD of 12 and 8."""
        result = await self.mcp.tools['gcd'](12, 8)
        expected = "✅ GCD(12, 8) = 4"
        return result == expected
    
    async def test_gcd_coprime(self):
        """Test GCD of coprime numbers."""
        result = await self.mcp.tools['gcd'](7, 11)
        expected = "✅ GCD(7, 11) = 1"
        return result == expected
    
    async def test_gcd_one_is_multiple(self):
        """Test GCD when one number is multiple of other."""
        result = await self.mcp.tools['gcd'](15, 5)
        expected = "✅ GCD(15, 5) = 5"
        return result == expected
    
    async def test_gcd_with_zero(self):
        """Test GCD with zero."""
        result = await self.mcp.tools['gcd'](0, 5)
        expected = "✅ GCD(0, 5) = 5"
        return result == expected
    
    async def test_gcd_negative_numbers(self):
        """Test GCD with negative numbers."""
        result = await self.mcp.tools['gcd'](-12, 8)
        expected = "✅ GCD(-12, 8) = 4"
        return result == expected
    
    async def test_lcm_basic(self):
        """Test LCM of 4 and 6."""
        result = await self.mcp.tools['lcm'](4, 6)
        expected = "✅ LCM(4, 6) = 12"
        return result == expected
    
    async def test_lcm_coprime(self):
        """Test LCM of coprime numbers."""
        result = await self.mcp.tools['lcm'](3, 7)
        expected = "✅ LCM(3, 7) = 21"
        return result == expected
    
    async def test_lcm_one_is_multiple(self):
        """Test LCM when one number is multiple of other."""
        result = await self.mcp.tools['lcm'](12, 4)
        expected = "✅ LCM(12, 4) = 12"
        return result == expected
    
    async def test_lcm_with_zero(self):
        """Test LCM with zero."""
        result = await self.mcp.tools['lcm'](0, 5)
        expected = "✅ LCM(0, 5) = 0"
        return result == expected
    
    async def test_is_prime_small_primes(self):
        """Test is_prime with small prime numbers."""
        result2 = await self.mcp.tools['is_prime'](2)
        result3 = await self.mcp.tools['is_prime'](3)
        result7 = await self.mcp.tools['is_prime'](7)
        return ("2 is prime" in result2 and 
                "3 is prime" in result3 and 
                "7 is prime" in result7)
    
    async def test_is_prime_composite_numbers(self):
        """Test is_prime with composite numbers."""
        result4 = await self.mcp.tools['is_prime'](4)
        result9 = await self.mcp.tools['is_prime'](9)
        result15 = await self.mcp.tools['is_prime'](15)
        return ("4 is not prime" in result4 and 
                "9 is not prime" in result9 and 
                "15 is not prime" in result15)
    
    async def test_is_prime_edge_cases(self):
        """Test is_prime with edge cases."""
        result0 = await self.mcp.tools['is_prime'](0)
        result1 = await self.mcp.tools['is_prime'](1)
        result_neg = await self.mcp.tools['is_prime'](-5)
        return ("0 is not prime" in result0 and 
                "1 is not prime" in result1 and 
                "-5 is not prime" in result_neg)
    
    async def test_is_prime_large_prime(self):
        """Test is_prime with larger prime."""
        result = await self.mcp.tools['is_prime'](97)
        return "97 is prime" in result
    
    async def test_prime_factors_small_number(self):
        """Test prime factors of 12."""
        result = await self.mcp.tools['prime_factors'](12)
        expected = "✅ Prime factors of 12: [2, 2, 3]"
        return result == expected
    
    async def test_prime_factors_prime_number(self):
        """Test prime factors of prime number."""
        result = await self.mcp.tools['prime_factors'](17)
        expected = "✅ Prime factors of 17: [17]"
        return result == expected
    
    async def test_prime_factors_power_of_prime(self):
        """Test prime factors of power of prime."""
        result = await self.mcp.tools['prime_factors'](8)
        expected = "✅ Prime factors of 8: [2, 2, 2]"
        return result == expected
    
    async def test_prime_factors_one(self):
        """Test prime factors of 1."""
        result = await self.mcp.tools['prime_factors'](1)
        expected = "✅ Prime factors of 1: []"
        return result == expected
    
    async def test_prime_factors_negative(self):
        """Test prime factors with negative number."""
        result = await self.mcp.tools['prime_factors'](-12)
        return result.startswith("❌") and "positive" in result.lower()
    
    async def test_is_perfect_square_perfect_squares(self):
        """Test is_perfect_square with perfect squares."""
        result1 = await self.mcp.tools['is_perfect_square'](1)
        result4 = await self.mcp.tools['is_perfect_square'](4)
        result25 = await self.mcp.tools['is_perfect_square'](25)
        result100 = await self.mcp.tools['is_perfect_square'](100)
        return (all("is a perfect square" in r for r in [result1, result4, result25, result100]))
    
    async def test_is_perfect_square_non_perfect_squares(self):
        """Test is_perfect_square with non-perfect squares."""
        result2 = await self.mcp.tools['is_perfect_square'](2)
        result3 = await self.mcp.tools['is_perfect_square'](3)
        result15 = await self.mcp.tools['is_perfect_square'](15)
        return (all("is not a perfect square" in r for r in [result2, result3, result15]))
    
    async def test_is_perfect_square_zero(self):
        """Test is_perfect_square with zero."""
        result = await self.mcp.tools['is_perfect_square'](0)
        return "0 is a perfect square" in result
    
    async def test_is_perfect_square_negative(self):
        """Test is_perfect_square with negative number."""
        result = await self.mcp.tools['is_perfect_square'](-4)
        return result.startswith("❌") and "non-negative" in result.lower()
