"""
Test suite for advanced_calc.py module

Tests advanced calculator functions: solve_quadratic, distance_2d, slope, compound_interest
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import advanced_calc


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestAdvancedCalc:
    """Test class for advanced calculator functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        advanced_calc.register_tools(self.mcp)
    
    # Quadratic equation solver tests
    
    async def test_solve_quadratic_two_real_solutions(self):
        """Test quadratic with two real solutions: x² - 5x + 6 = 0."""
        result = await self.mcp.tools['solve_quadratic'](1, -5, 6)
        # Should have solutions x = 2 and x = 3
        return ("Two real solutions" in result and 
                "x₁ = 3.0" in result and 
                "x₂ = 2.0" in result)
    
    async def test_solve_quadratic_one_solution(self):
        """Test quadratic with one repeated solution: x² - 4x + 4 = 0."""
        result = await self.mcp.tools['solve_quadratic'](1, -4, 4)
        # Should have solution x = 2 (double root)
        return "One repeated real solution: x = 2.0" in result
    
    async def test_solve_quadratic_complex_solutions(self):
        """Test quadratic with complex solutions: x² + x + 1 = 0."""
        result = await self.mcp.tools['solve_quadratic'](1, 1, 1)
        # Should have complex solutions
        return ("Two complex solutions" in result and
                "0.866" in result)  # Imaginary part ≈ ±√3/2
    
    async def test_solve_quadratic_linear_equation(self):
        """Test when a=0 (linear equation): 0x² + 2x + 4 = 0."""
        result = await self.mcp.tools['solve_quadratic'](0, 2, 4)
        # Should solve as linear: 2x + 4 = 0, so x = -2
        return "Linear equation solution: x = -2.0" in result
    
    async def test_solve_quadratic_no_solution(self):
        """Test when a=0, b=0, c≠0: 0x² + 0x + 5 = 0."""
        result = await self.mcp.tools['solve_quadratic'](0, 0, 5)
        return "No solution exists" in result
    
    async def test_solve_quadratic_all_solutions(self):
        """Test when a=0, b=0, c=0: 0x² + 0x + 0 = 0."""
        result = await self.mcp.tools['solve_quadratic'](0, 0, 0)
        return "All real numbers are solutions" in result
    
    # 2D distance tests
    
    async def test_distance_2d_3_4_5_triangle(self):
        """Test distance for 3-4-5 right triangle."""
        result = await self.mcp.tools['distance_2d'](0, 0, 3, 4)
        return "Distance between points (0, 0) and (3, 4) is 5.0" in result
    
    async def test_distance_2d_same_point(self):
        """Test distance between same point."""
        result = await self.mcp.tools['distance_2d'](5, 5, 5, 5)
        return "Distance between points (5, 5) and (5, 5) is 0.0" in result
    
    async def test_distance_2d_negative_coordinates(self):
        """Test distance with negative coordinates."""
        result = await self.mcp.tools['distance_2d'](-1, -1, 1, 1)
        # Distance should be √((1-(-1))² + (1-(-1))²) = √(4+4) = √8 ≈ 2.828
        return "is 2.828" in result
    
    async def test_distance_2d_horizontal_line(self):
        """Test distance along horizontal line."""
        result = await self.mcp.tools['distance_2d'](0, 0, 5, 0)
        return "is 5.0" in result
    
    async def test_distance_2d_vertical_line(self):
        """Test distance along vertical line."""
        result = await self.mcp.tools['distance_2d'](0, 0, 0, 3)
        return "is 3.0" in result
    
    # Slope calculation tests
    
    async def test_slope_45_degree_line(self):
        """Test slope of 45° line."""
        result = await self.mcp.tools['slope'](0, 0, 2, 2)
        return "Slope between points (0, 0) and (2, 2) is 1 (45° upward)" in result
    
    async def test_slope_negative_45_degree_line(self):
        """Test slope of -45° line."""
        result = await self.mcp.tools['slope'](0, 0, 2, -2)
        return "Slope between points (0, 0) and (2, -2) is -1 (45° downward)" in result
    
    async def test_slope_horizontal_line(self):
        """Test slope of horizontal line."""
        result = await self.mcp.tools['slope'](1, 3, 5, 3)
        return "Slope between points (1, 3) and (5, 3) is 0 (horizontal line)" in result
    
    async def test_slope_vertical_line(self):
        """Test slope of vertical line (undefined)."""
        result = await self.mcp.tools['slope'](2, 1, 2, 5)
        return "Slope is undefined (vertical line)" in result
    
    async def test_slope_general_case(self):
        """Test slope of general line."""
        result = await self.mcp.tools['slope'](1, 2, 4, 8)
        # Slope = (8-2)/(4-1) = 6/3 = 2
        return "Slope between points (1, 2) and (4, 8) is 2.0" in result
    
    # Compound interest tests
    
    async def test_compound_interest_annual(self):
        """Test compound interest with annual compounding."""
        result = await self.mcp.tools['compound_interest'](1000, 0.05, 10, 1)
        # A = 1000(1.05)^10 ≈ 1628.89
        return ("Final Amount: $1,628.89" in result and
                "Interest Earned: $628.89" in result and
                "compounded annually" in result)
    
    async def test_compound_interest_monthly(self):
        """Test compound interest with monthly compounding."""
        result = await self.mcp.tools['compound_interest'](1000, 0.05, 10, 12)
        # A = 1000(1 + 0.05/12)^(12*10) ≈ 1647.01
        return ("Final Amount: $1,647.01" in result and
                "compounded monthly" in result)
    
    async def test_compound_interest_daily(self):
        """Test compound interest with daily compounding."""
        result = await self.mcp.tools['compound_interest'](1000, 0.05, 1, 365)
        # Should be slightly more than annual
        return ("compounded daily" in result and
                "Final Amount:" in result)
    
    async def test_compound_interest_zero_rate(self):
        """Test compound interest with zero interest rate."""
        result = await self.mcp.tools['compound_interest'](1000, 0, 5, 12)
        return ("Final Amount: $1,000.00" in result and
                "Interest Earned: $0.00" in result)
    
    async def test_compound_interest_zero_time(self):
        """Test compound interest with zero time."""
        result = await self.mcp.tools['compound_interest'](1000, 0.05, 0, 12)
        return ("Final Amount: $1,000.00" in result and
                "Interest Earned: $0.00" in result)
    
    # Error handling tests
    
    async def test_compound_interest_negative_principal(self):
        """Test compound interest with negative principal."""
        result = await self.mcp.tools['compound_interest'](-1000, 0.05, 10, 12)
        return result.startswith("❌") and "Principal amount cannot be negative" in result
    
    async def test_compound_interest_negative_rate(self):
        """Test compound interest with negative rate."""
        result = await self.mcp.tools['compound_interest'](1000, -0.05, 10, 12)
        return result.startswith("❌") and "Interest rate cannot be negative" in result
    
    async def test_compound_interest_negative_time(self):
        """Test compound interest with negative time."""
        result = await self.mcp.tools['compound_interest'](1000, 0.05, -10, 12)
        return result.startswith("❌") and "Time period cannot be negative" in result
    
    async def test_compound_interest_zero_compounds(self):
        """Test compound interest with zero compounds per year."""
        result = await self.mcp.tools['compound_interest'](1000, 0.05, 10, 0)
        return result.startswith("❌") and "Compounds per year must be positive" in result
