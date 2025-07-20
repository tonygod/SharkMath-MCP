"""
Test suite for solve_equations consolidated tool.
Tests equation solving operations including quadratic, linear, and interest calculations.

Run with: python Tests/test_solve_equations.py
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solve_equations import register_tools


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestSolveEquations(unittest.TestCase):
    """Test cases for solve_equations consolidated tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp = MockMCP()
        register_tools(self.mock_mcp)
        self.solve_equations = self.mock_mcp.tools['solve_equations']
    
    # Quadratic Equations Tests
    async def test_quadratic_two_real_solutions(self):
        """Test quadratic with two distinct real solutions."""
        result = await self.solve_equations("quadratic", a=1, b=-5, c=6)
        self.assertIn("✅ Two real solutions", result)
        self.assertIn("x₁ = 3.0", result)
        self.assertIn("x₂ = 2.0", result)
    
    async def test_quadratic_one_solution(self):
        """Test quadratic with one repeated real solution."""
        result = await self.solve_equations("quadratic", a=1, b=-6, c=9)
        self.assertIn("✅ One repeated real solution", result)
        self.assertIn("x = 3.0", result)
    
    async def test_quadratic_complex_solutions(self):
        """Test quadratic with complex solutions."""
        result = await self.solve_equations("quadratic", a=1, b=0, c=4)
        self.assertIn("✅ Two complex solutions", result)
        self.assertIn("0.0 + 2.0i", result)
        self.assertIn("0.0 - 2.0i", result)
    
    async def test_quadratic_reduces_to_linear(self):
        """Test quadratic that reduces to linear (a=0)."""
        result = await self.solve_equations("quadratic", a=0, b=2, c=-6)
        self.assertIn("✅ Linear equation solution", result)
        self.assertIn("x = 3.0", result)
    
    async def test_quadratic_no_solution(self):
        """Test degenerate case with no solution."""
        result = await self.solve_equations("quadratic", a=0, b=0, c=5)
        self.assertIn("❌ No solution exists", result)
    
    async def test_quadratic_identity(self):
        """Test identity case (0 = 0)."""
        result = await self.solve_equations("quadratic", a=0, b=0, c=0)
        self.assertIn("✅ All real numbers are solutions", result)
    
    async def test_quadratic_missing_parameters(self):
        """Test quadratic with missing parameters."""
        result = await self.solve_equations("quadratic", a=1, b=2)
        self.assertIn("❌ Quadratic equation requires parameters: a, b, c", result)
    
    # Linear Equations Tests
    async def test_linear_basic(self):
        """Test basic linear equation."""
        result = await self.solve_equations("linear", a=3, b=-9)
        self.assertIn("✅ Linear equation solution", result)
        self.assertIn("x = 3.0", result)
    
    async def test_linear_negative_solution(self):
        """Test linear equation with negative solution."""
        result = await self.solve_equations("linear", a=2, b=8)
        self.assertIn("✅ Linear equation solution", result)
        self.assertIn("x = -4.0", result)
    
    async def test_linear_no_solution(self):
        """Test linear equation with no solution (a=0, b≠0)."""
        result = await self.solve_equations("linear", a=0, b=5)
        self.assertIn("❌ No solution exists", result)
    
    async def test_linear_identity(self):
        """Test linear identity (a=0, b=0)."""
        result = await self.solve_equations("linear", a=0, b=0)
        self.assertIn("✅ All real numbers are solutions", result)
    
    async def test_linear_missing_parameters(self):
        """Test linear with missing parameters."""
        result = await self.solve_equations("linear", a=2)
        self.assertIn("❌ Linear equation requires parameters: a, b", result)
    
    # Compound Interest Tests
    async def test_compound_interest_annual(self):
        """Test compound interest with annual compounding."""
        result = await self.solve_equations("compound_interest", principal=1000, rate=0.05, time=10, compounds_per_year=1)
        self.assertIn("✅ Compound Interest Calculation", result)
        self.assertIn("Principal: $1,000.00", result)
        self.assertIn("Rate: 5.0% compounded annually", result)
        self.assertIn("Time: 10 years", result)
        self.assertIn("Final Amount: $1,628.89", result)
        self.assertIn("Interest Earned: $628.89", result)
    
    async def test_compound_interest_monthly(self):
        """Test compound interest with monthly compounding."""
        result = await self.solve_equations("compound_interest", principal=5000, rate=0.04, time=5, compounds_per_year=12)
        self.assertIn("✅ Compound Interest Calculation", result)
        self.assertIn("Principal: $5,000.00", result)
        self.assertIn("Rate: 4.0% compounded monthly", result)
        self.assertIn("Time: 5 years", result)
        self.assertIn("Final Amount: $6,104.85", result)
        self.assertIn("Interest Earned: $1,104.85", result)
    
    async def test_compound_interest_daily(self):
        """Test compound interest with daily compounding."""
        result = await self.solve_equations("compound_interest", principal=2000, rate=0.03, time=3, compounds_per_year=365)
        self.assertIn("✅ Compound Interest Calculation", result)
        self.assertIn("Principal: $2,000.00", result)
        self.assertIn("Rate: 3.0% compounded daily", result)
        self.assertIn("Time: 3 years", result)
    
    async def test_compound_interest_default_compounding(self):
        """Test compound interest with default compounding (annual)."""
        result = await self.solve_equations("compound_interest", principal=1000, rate=0.06, time=2)
        self.assertIn("✅ Compound Interest Calculation", result)
        self.assertIn("Rate: 6.0% compounded annually", result)
    
    async def test_compound_interest_negative_principal(self):
        """Test compound interest with negative principal."""
        result = await self.solve_equations("compound_interest", principal=-1000, rate=0.05, time=1, compounds_per_year=1)
        self.assertIn("❌ Principal amount cannot be negative", result)
    
    async def test_compound_interest_negative_rate(self):
        """Test compound interest with negative rate."""
        result = await self.solve_equations("compound_interest", principal=1000, rate=-0.05, time=1, compounds_per_year=1)
        self.assertIn("❌ Interest rate cannot be negative", result)
    
    async def test_compound_interest_negative_time(self):
        """Test compound interest with negative time."""
        result = await self.solve_equations("compound_interest", principal=1000, rate=0.05, time=-1, compounds_per_year=1)
        self.assertIn("❌ Time period cannot be negative", result)
    
    async def test_compound_interest_invalid_compounds(self):
        """Test compound interest with invalid compounds per year."""
        result = await self.solve_equations("compound_interest", principal=1000, rate=0.05, time=1, compounds_per_year=0)
        self.assertIn("❌ Compounds per year must be positive integer", result)
    
    async def test_compound_interest_missing_parameters(self):
        """Test compound interest with missing parameters."""
        result = await self.solve_equations("compound_interest", principal=1000, rate=0.05)
        self.assertIn("❌ Compound interest requires parameters: principal, rate, time", result)
    
    # Simple Interest Tests
    async def test_simple_interest_basic(self):
        """Test basic simple interest calculation."""
        result = await self.solve_equations("simple_interest", principal=1000, rate=0.05, time=10)
        self.assertIn("✅ Simple Interest Calculation", result)
        self.assertIn("Principal: $1,000.00", result)
        self.assertIn("Rate: 5.0% per year", result)
        self.assertIn("Time: 10 years", result)
        self.assertIn("Final Amount: $1,500.00", result)
        self.assertIn("Interest Earned: $500.00", result)
    
    async def test_simple_interest_fractional_time(self):
        """Test simple interest with fractional time."""
        result = await self.solve_equations("simple_interest", principal=2000, rate=0.04, time=2.5)
        self.assertIn("✅ Simple Interest Calculation", result)
        self.assertIn("Principal: $2,000.00", result)
        self.assertIn("Rate: 4.0% per year", result)
        self.assertIn("Time: 2.5 years", result)
        self.assertIn("Final Amount: $2,200.00", result)
        self.assertIn("Interest Earned: $200.00", result)
    
    async def test_simple_interest_zero_rate(self):
        """Test simple interest with zero rate."""
        result = await self.solve_equations("simple_interest", principal=1000, rate=0, time=5)
        self.assertIn("✅ Simple Interest Calculation", result)
        self.assertIn("Final Amount: $1,000.00", result)
        self.assertIn("Interest Earned: $0.00", result)
    
    async def test_simple_interest_negative_principal(self):
        """Test simple interest with negative principal."""
        result = await self.solve_equations("simple_interest", principal=-1000, rate=0.05, time=1)
        self.assertIn("❌ Principal amount cannot be negative", result)
    
    async def test_simple_interest_missing_parameters(self):
        """Test simple interest with missing parameters."""
        result = await self.solve_equations("simple_interest", principal=1000, rate=0.05)
        self.assertIn("❌ Simple interest requires parameters: principal, rate, time", result)
    
    # Error Handling Tests
    async def test_invalid_equation_type(self):
        """Test invalid equation type."""
        result = await self.solve_equations("invalid_equation", a=1, b=2, c=3)
        self.assertIn("❌ Invalid equation type 'invalid_equation'", result)
        self.assertIn("Valid types: quadratic, linear, compound_interest, simple_interest", result)
    
    async def test_empty_equation_type(self):
        """Test empty equation type."""
        result = await self.solve_equations("", a=1, b=2, c=3)
        self.assertIn("❌ Invalid equation type", result)


def run_async_test(coro):
    """Helper to run async test functions."""
    import asyncio
    return asyncio.run(coro)


if __name__ == '__main__':
    # Create test suite with async support
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test methods
    test_instance = TestSolveEquations()
    test_instance.setUp()
    
    test_methods = [
        'test_quadratic_two_real_solutions',
        'test_quadratic_one_solution', 
        'test_quadratic_complex_solutions',
        'test_quadratic_reduces_to_linear',
        'test_quadratic_no_solution',
        'test_quadratic_identity',
        'test_quadratic_missing_parameters',
        'test_linear_basic',
        'test_linear_negative_solution',
        'test_linear_no_solution',
        'test_linear_identity',
        'test_linear_missing_parameters',
        'test_compound_interest_annual',
        'test_compound_interest_monthly',
        'test_compound_interest_daily',
        'test_compound_interest_default_compounding',
        'test_compound_interest_negative_principal',
        'test_compound_interest_negative_rate',
        'test_compound_interest_negative_time',
        'test_compound_interest_invalid_compounds',
        'test_compound_interest_missing_parameters',
        'test_simple_interest_basic',
        'test_simple_interest_fractional_time',
        'test_simple_interest_zero_rate',
        'test_simple_interest_negative_principal',
        'test_simple_interest_missing_parameters',
        'test_invalid_equation_type',
        'test_empty_equation_type'
    ]
    
    print("Running solve_equations consolidated tool tests...")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for method_name in test_methods:
        try:
            method = getattr(test_instance, method_name)
            run_async_test(method())
            print(f"✅ {method_name}")
            passed += 1
        except Exception as e:
            print(f"❌ {method_name}: {str(e)}")
            failed += 1
    
    print("=" * 50)
    print(f"Tests passed: {passed}")
    print(f"Tests failed: {failed}")
    print(f"Total tests: {passed + failed}")
    
    if failed == 0:
        print("✅ All solve_equations tests passed!")
    else:
        print(f"❌ {failed} test(s) failed")
