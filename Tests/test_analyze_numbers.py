"""
Test suite for consolidated analyze_numbers tool.
Tests all number theory and combinatorial operations with parameter-based routing.
"""

import unittest
import asyncio
import sys
import os
import math

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the number_theory module
import number_theory

class MockMCP:
    """Mock MCP server for testing purposes."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator

class TestAnalyzeNumbers(unittest.TestCase):
    """Test cases for the consolidated analyze_numbers tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp = MockMCP()
        number_theory.register_tools(self.mock_mcp)
        self.analyze_tool = self.mock_mcp.tools['analyze_numbers']
    
    # GCD tests
    def test_gcd_positive_numbers(self):
        """Test GCD with positive numbers."""
        result = asyncio.run(self.analyze_tool("gcd", 12, 8))
        self.assertIn("✅", result)
        self.assertIn("gcd(12, 8) = 4", result)
        
        result = asyncio.run(self.analyze_tool("gcd", 21, 14))
        self.assertIn("✅", result)
        self.assertIn("gcd(21, 14) = 7", result)
    
    def test_gcd_coprime_numbers(self):
        """Test GCD with coprime numbers."""
        result = asyncio.run(self.analyze_tool("gcd", 13, 7))
        self.assertIn("✅", result)
        self.assertIn("gcd(13, 7) = 1", result)
        
        result = asyncio.run(self.analyze_tool("gcd", 25, 9))
        self.assertIn("✅", result)
        self.assertIn("gcd(25, 9) = 1", result)
    
    def test_gcd_with_zero(self):
        """Test GCD with zero values."""
        result = asyncio.run(self.analyze_tool("gcd", 15, 0))
        self.assertIn("✅", result)
        self.assertIn("gcd(15, 0) = 15", result)
        
        result = asyncio.run(self.analyze_tool("gcd", 0, 0))
        self.assertIn("❌", result)
        self.assertIn("GCD is undefined for gcd(0, 0)", result)
    
    def test_gcd_negative_numbers(self):
        """Test GCD with negative numbers."""
        result = asyncio.run(self.analyze_tool("gcd", -12, 8))
        self.assertIn("✅", result)
        self.assertIn("gcd(-12, 8) = 4", result)
        
        result = asyncio.run(self.analyze_tool("gcd", -15, -10))
        self.assertIn("✅", result)
        self.assertIn("gcd(-15, -10) = 5", result)
    
    def test_gcd_missing_parameter(self):
        """Test GCD without second_value parameter."""
        result = asyncio.run(self.analyze_tool("gcd", 12))
        self.assertIn("❌", result)
        self.assertIn("'second_value' parameter required", result)
    
    # LCM tests
    def test_lcm_positive_numbers(self):
        """Test LCM with positive numbers."""
        result = asyncio.run(self.analyze_tool("lcm", 12, 8))
        self.assertIn("✅", result)
        self.assertIn("lcm(12, 8) = 24", result)
        
        result = asyncio.run(self.analyze_tool("lcm", 15, 10))
        self.assertIn("✅", result)
        self.assertIn("lcm(15, 10) = 30", result)
    
    def test_lcm_with_zero(self):
        """Test LCM with zero values."""
        result = asyncio.run(self.analyze_tool("lcm", 15, 0))
        self.assertIn("✅", result)
        self.assertIn("lcm(15, 0) = 0", result)
        
        result = asyncio.run(self.analyze_tool("lcm", 0, 20))
        self.assertIn("✅", result)
        self.assertIn("lcm(0, 20) = 0", result)
    
    def test_lcm_coprime_numbers(self):
        """Test LCM with coprime numbers."""
        result = asyncio.run(self.analyze_tool("lcm", 7, 11))
        self.assertIn("✅", result)
        self.assertIn("lcm(7, 11) = 77", result)  # Product when coprime
    
    def test_lcm_missing_parameter(self):
        """Test LCM without second_value parameter."""
        result = asyncio.run(self.analyze_tool("lcm", 12))
        self.assertIn("❌", result)
        self.assertIn("'second_value' parameter required", result)
    
    # Prime checking tests
    def test_is_prime_small_primes(self):
        """Test prime checking with small prime numbers."""
        result = asyncio.run(self.analyze_tool("is_prime", 2))
        self.assertIn("✅", result)
        self.assertIn("2 is prime", result)
        
        result = asyncio.run(self.analyze_tool("is_prime", 3))
        self.assertIn("✅", result)
        self.assertIn("3 is prime", result)
        
        result = asyncio.run(self.analyze_tool("is_prime", 7))
        self.assertIn("✅", result)
        self.assertIn("7 is prime", result)
        
        result = asyncio.run(self.analyze_tool("is_prime", 17))
        self.assertIn("✅", result)
        self.assertIn("17 is prime", result)
    
    def test_is_prime_composite_numbers(self):
        """Test prime checking with composite numbers."""
        result = asyncio.run(self.analyze_tool("is_prime", 4))
        self.assertIn("✅", result)
        self.assertIn("4 is not prime", result)
        
        result = asyncio.run(self.analyze_tool("is_prime", 9))
        self.assertIn("✅", result)
        self.assertIn("9 is not prime", result)
        
        result = asyncio.run(self.analyze_tool("is_prime", 15))
        self.assertIn("✅", result)
        self.assertIn("15 is not prime", result)
    
    def test_is_prime_edge_cases(self):
        """Test prime checking with edge cases."""
        result = asyncio.run(self.analyze_tool("is_prime", 1))
        self.assertIn("✅", result)
        self.assertIn("1 is not prime", result)
        
        result = asyncio.run(self.analyze_tool("is_prime", 0))
        self.assertIn("✅", result)
        self.assertIn("0 is not prime", result)
        
        result = asyncio.run(self.analyze_tool("is_prime", -5))
        self.assertIn("✅", result)
        self.assertIn("-5 is not prime", result)
    
    # Prime factorization tests
    def test_prime_factors_small_numbers(self):
        """Test prime factorization with small numbers."""
        result = asyncio.run(self.analyze_tool("prime_factors", 12))
        self.assertIn("✅", result)
        self.assertIn("Prime factors of 12: [2, 2, 3]", result)
        self.assertIn("2 × 2 × 3", result)
        
        result = asyncio.run(self.analyze_tool("prime_factors", 15))
        self.assertIn("✅", result)
        self.assertIn("Prime factors of 15: [3, 5]", result)
        self.assertIn("3 × 5", result)
    
    def test_prime_factors_prime_numbers(self):
        """Test prime factorization with prime numbers."""
        result = asyncio.run(self.analyze_tool("prime_factors", 7))
        self.assertIn("✅", result)
        self.assertIn("Prime factors of 7: [7]", result)
        self.assertIn("7", result)
        
        result = asyncio.run(self.analyze_tool("prime_factors", 13))
        self.assertIn("✅", result)
        self.assertIn("Prime factors of 13: [13]", result)
    
    def test_prime_factors_edge_cases(self):
        """Test prime factorization edge cases."""
        result = asyncio.run(self.analyze_tool("prime_factors", 1))
        self.assertIn("✅", result)
        self.assertIn("Prime factors of 1: []", result)
        
        result = asyncio.run(self.analyze_tool("prime_factors", 0))
        self.assertIn("❌", result)
        self.assertIn("Prime factorization undefined for 0", result)
    
    # Perfect square tests
    def test_is_perfect_square_true(self):
        """Test perfect square checking with perfect squares."""
        result = asyncio.run(self.analyze_tool("is_perfect_square", 4))
        self.assertIn("✅", result)
        self.assertIn("4 is a perfect square (2² = 4)", result)
        
        result = asyncio.run(self.analyze_tool("is_perfect_square", 16))
        self.assertIn("✅", result)
        self.assertIn("16 is a perfect square (4² = 16)", result)
        
        result = asyncio.run(self.analyze_tool("is_perfect_square", 0))
        self.assertIn("✅", result)
        self.assertIn("0 is a perfect square (0 = 0²)", result)
    
    def test_is_perfect_square_false(self):
        """Test perfect square checking with non-perfect squares."""
        result = asyncio.run(self.analyze_tool("is_perfect_square", 3))
        self.assertIn("✅", result)
        self.assertIn("3 is not a perfect square", result)
        
        result = asyncio.run(self.analyze_tool("is_perfect_square", 15))
        self.assertIn("✅", result)
        self.assertIn("15 is not a perfect square", result)
    
    def test_is_perfect_square_negative(self):
        """Test perfect square checking with negative numbers."""
        result = asyncio.run(self.analyze_tool("is_perfect_square", -4))
        self.assertIn("✅", result)
        self.assertIn("-4 is not a perfect square (negative numbers", result)
    
    # Factorial tests
    def test_factorial_small_numbers(self):
        """Test factorial with small numbers."""
        result = asyncio.run(self.analyze_tool("factorial", 0))
        self.assertIn("✅", result)
        self.assertIn("0! = 1", result)
        
        result = asyncio.run(self.analyze_tool("factorial", 1))
        self.assertIn("✅", result)
        self.assertIn("1! = 1", result)
        
        result = asyncio.run(self.analyze_tool("factorial", 5))
        self.assertIn("✅", result)
        self.assertIn("5! = 120", result)
        
        result = asyncio.run(self.analyze_tool("factorial", 7))
        self.assertIn("✅", result)
        self.assertIn("7! = 5040", result)
    
    def test_factorial_negative_error(self):
        """Test factorial with negative numbers."""
        result = asyncio.run(self.analyze_tool("factorial", -1))
        self.assertIn("❌", result)
        self.assertIn("Factorial is not defined for negative numbers", result)
        
        result = asyncio.run(self.analyze_tool("factorial", -5))
        self.assertIn("❌", result)
        self.assertIn("Factorial is not defined for negative numbers", result)
    
    def test_factorial_large_number_error(self):
        """Test factorial with very large numbers."""
        result = asyncio.run(self.analyze_tool("factorial", 171))
        self.assertIn("❌", result)
        self.assertIn("Factorial too large to calculate", result)
    
    # Permutation tests
    def test_permutation_basic(self):
        """Test basic permutation calculations."""
        result = asyncio.run(self.analyze_tool("permutation", 5, 3))
        self.assertIn("✅", result)
        self.assertIn("P(5,3) = 5!/(5-3)! = 60", result)
        
        result = asyncio.run(self.analyze_tool("permutation", 4, 2))
        self.assertIn("✅", result)
        self.assertIn("P(4,2) = 4!/(4-2)! = 12", result)
    
    def test_permutation_edge_cases(self):
        """Test permutation edge cases."""
        result = asyncio.run(self.analyze_tool("permutation", 5, 0))
        self.assertIn("✅", result)
        self.assertIn("P(5,0) = 5!/(5-0)! = 1", result)
        
        result = asyncio.run(self.analyze_tool("permutation", 3, 3))
        self.assertIn("✅", result)
        self.assertIn("P(3,3) = 3!/(3-3)! = 6", result)
    
    def test_permutation_invalid_parameters(self):
        """Test permutation with invalid parameters."""
        result = asyncio.run(self.analyze_tool("permutation", 3, 5))
        self.assertIn("❌", result)
        self.assertIn("Cannot select more items (r) than available (n)", result)
        
        result = asyncio.run(self.analyze_tool("permutation", -1, 2))
        self.assertIn("❌", result)
        self.assertIn("Permutation requires non-negative integers", result)
    
    def test_permutation_missing_parameter(self):
        """Test permutation without second_value parameter."""
        result = asyncio.run(self.analyze_tool("permutation", 5))
        self.assertIn("❌", result)
        self.assertIn("'second_value' parameter required", result)
    
    # Combination tests
    def test_combination_basic(self):
        """Test basic combination calculations."""
        result = asyncio.run(self.analyze_tool("combination", 5, 3))
        self.assertIn("✅", result)
        self.assertIn("C(5,3) = 5!/(3!*(5-3)!) = 10", result)
        
        result = asyncio.run(self.analyze_tool("combination", 6, 2))
        self.assertIn("✅", result)
        self.assertIn("C(6,2) = 6!/(2!*(6-2)!) = 15", result)
    
    def test_combination_edge_cases(self):
        """Test combination edge cases."""
        result = asyncio.run(self.analyze_tool("combination", 5, 0))
        self.assertIn("✅", result)
        self.assertIn("C(5,0) = 5!/(0!*(5-0)!) = 1", result)
        
        result = asyncio.run(self.analyze_tool("combination", 4, 4))
        self.assertIn("✅", result)
        self.assertIn("C(4,4) = 4!/(4!*(4-4)!) = 1", result)
    
    def test_combination_invalid_parameters(self):
        """Test combination with invalid parameters."""
        result = asyncio.run(self.analyze_tool("combination", 3, 5))
        self.assertIn("❌", result)
        self.assertIn("Cannot select more items (r) than available (n)", result)
        
        result = asyncio.run(self.analyze_tool("combination", -1, 2))
        self.assertIn("❌", result)
        self.assertIn("Combination requires non-negative integers", result)
    
    def test_combination_missing_parameter(self):
        """Test combination without second_value parameter."""
        result = asyncio.run(self.analyze_tool("combination", 5))
        self.assertIn("❌", result)
        self.assertIn("'second_value' parameter required", result)
    
    # Fibonacci tests
    def test_fibonacci_small_numbers(self):
        """Test Fibonacci with small indices."""
        result = asyncio.run(self.analyze_tool("fibonacci", 0))
        self.assertIn("✅", result)
        self.assertIn("Fibonacci(0) = 0", result)
        
        result = asyncio.run(self.analyze_tool("fibonacci", 1))
        self.assertIn("✅", result)
        self.assertIn("Fibonacci(1) = 1", result)
        
        result = asyncio.run(self.analyze_tool("fibonacci", 5))
        self.assertIn("✅", result)
        self.assertIn("Fibonacci(5) = 5", result)
        
        result = asyncio.run(self.analyze_tool("fibonacci", 10))
        self.assertIn("✅", result)
        self.assertIn("Fibonacci(10) = 55", result)
    
    def test_fibonacci_negative_error(self):
        """Test Fibonacci with negative indices."""
        result = asyncio.run(self.analyze_tool("fibonacci", -1))
        self.assertIn("❌", result)
        self.assertIn("Fibonacci sequence is not defined for negative indices", result)
        
        result = asyncio.run(self.analyze_tool("fibonacci", -5))
        self.assertIn("❌", result)
        self.assertIn("Fibonacci sequence is not defined for negative indices", result)
    
    def test_fibonacci_large_number_error(self):
        """Test Fibonacci with very large indices."""
        result = asyncio.run(self.analyze_tool("fibonacci", 1001))
        self.assertIn("❌", result)
        self.assertIn("Fibonacci index too large (n > 1000)", result)
    
    # Error handling tests
    def test_invalid_operation(self):
        """Test handling of invalid operations."""
        result = asyncio.run(self.analyze_tool("invalid_op", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation 'invalid_op'", result)
        self.assertIn("Available:", result)
        
        result = asyncio.run(self.analyze_tool("sqrt", 10))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation 'sqrt'", result)
    
    def test_operation_case_sensitivity(self):
        """Test that operations are case sensitive."""
        result = asyncio.run(self.analyze_tool("GCD", 12, 8))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation", result)
        
        result = asyncio.run(self.analyze_tool("Prime_factors", 12))
        self.assertIn("❌", result)
        self.assertIn("Invalid operation", result)

if __name__ == '__main__':
    unittest.main()
