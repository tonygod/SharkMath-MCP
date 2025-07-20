"""
Advanced Calculator Features Module for SharkMath MCP Server

This module provides advanced mathematical calculation functions including:
- Quadratic equation solver
- 2D geometry calculations  
- Financial calculations

All functions follow the SharkMath error handling standards with ✅/❌ prefixes.
"""

import math


def register_tools(mcp):
    """Register all advanced calculator tools with the MCP server."""
    
    @mcp.tool()
    async def solve_quadratic(a: float, b: float, c: float) -> str:
        """
        Solve quadratic equation ax² + bx + c = 0 using the quadratic formula.
        Returns real solutions or indicates complex/no solutions.
        
        Args:
            a: Coefficient of x² (must not be zero)
            b: Coefficient of x
            c: Constant term
            
        Returns:
            String with solutions or error message
        """
        try:
            # Validate that this is actually a quadratic equation
            if a == 0:
                if b == 0:
                    if c == 0:
                        return "✅ All real numbers are solutions (0 = 0)"
                    else:
                        return "❌ No solution exists (equation reduces to constant ≠ 0)"
                else:
                    # Linear equation: bx + c = 0
                    solution = -c / b
                    return f"✅ Linear equation solution: x = {solution}"
            
            # Calculate discriminant
            discriminant = b**2 - 4*a*c
            
            if discriminant > 0:
                # Two distinct real solutions
                sqrt_discriminant = math.sqrt(discriminant)
                x1 = (-b + sqrt_discriminant) / (2*a)
                x2 = (-b - sqrt_discriminant) / (2*a)
                return f"✅ Two real solutions: x₁ = {x1}, x₂ = {x2}"
            
            elif discriminant == 0:
                # One repeated real solution
                x = -b / (2*a)
                return f"✅ One repeated real solution: x = {x}"
            
            else:
                # Complex solutions
                real_part = -b / (2*a)
                imaginary_part = math.sqrt(-discriminant) / (2*a)
                return f"✅ Two complex solutions: x₁ = {real_part} + {imaginary_part}i, x₂ = {real_part} - {imaginary_part}i"
                
        except Exception as e:
            return f"❌ Error solving quadratic equation: {str(e)}"

    @mcp.tool()
    async def distance_2d(x1: float, y1: float, x2: float, y2: float) -> str:
        """
        Calculate the Euclidean distance between two points in 2D space.
        Uses the distance formula: d = √[(x₂-x₁)² + (y₂-y₁)²]
        
        Args:
            x1: X-coordinate of first point
            y1: Y-coordinate of first point
            x2: X-coordinate of second point
            y2: Y-coordinate of second point
            
        Returns:
            String with the calculated distance
        """
        try:
            # Calculate differences
            dx = x2 - x1
            dy = y2 - y1
            
            # Calculate distance using Pythagorean theorem
            distance = math.sqrt(dx**2 + dy**2)
            
            return f"✅ Distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance}"
            
        except Exception as e:
            return f"❌ Error calculating 2D distance: {str(e)}"

    @mcp.tool()
    async def slope(x1: float, y1: float, x2: float, y2: float) -> str:
        """
        Calculate the slope between two points in 2D space.
        Uses the slope formula: m = (y₂-y₁)/(x₂-x₁)
        
        Args:
            x1: X-coordinate of first point
            y1: Y-coordinate of first point
            x2: X-coordinate of second point
            y2: Y-coordinate of second point
            
        Returns:
            String with the calculated slope or indication of vertical line
        """
        try:
            # Check for vertical line (undefined slope)
            if x2 == x1:
                return f"✅ Slope is undefined (vertical line) between points ({x1}, {y1}) and ({x2}, {y2})"
            
            # Calculate slope
            slope_value = (y2 - y1) / (x2 - x1)
            
            # Provide additional context for special slopes
            if slope_value == 0:
                return f"✅ Slope between points ({x1}, {y1}) and ({x2}, {y2}) is 0 (horizontal line)"
            elif slope_value == 1:
                return f"✅ Slope between points ({x1}, {y1}) and ({x2}, {y2}) is 1 (45° upward)"
            elif slope_value == -1:
                return f"✅ Slope between points ({x1}, {y1}) and ({x2}, {y2}) is -1 (45° downward)"
            else:
                return f"✅ Slope between points ({x1}, {y1}) and ({x2}, {y2}) is {slope_value}"
            
        except Exception as e:
            return f"❌ Error calculating slope: {str(e)}"

    @mcp.tool()
    async def compound_interest(principal: float, rate: float, time: float, compounds_per_year: int = 1) -> str:
        """
        Calculate compound interest using the formula: A = P(1 + r/n)^(nt)
        
        Args:
            principal: Initial amount of money (P)
            rate: Annual interest rate as decimal (e.g., 0.05 for 5%)
            time: Time period in years (t)
            compounds_per_year: Number of times interest compounds per year (n), default 1
            
        Returns:
            String with final amount, interest earned, and calculation details
        """
        try:
            # Input validation
            if principal < 0:
                return "❌ Principal amount cannot be negative"
            
            if rate < 0:
                return "❌ Interest rate cannot be negative"
                
            if time < 0:
                return "❌ Time period cannot be negative"
                
            if compounds_per_year <= 0:
                return "❌ Compounds per year must be positive integer"
            
            # Calculate compound interest
            # A = P(1 + r/n)^(nt)
            final_amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
            interest_earned = final_amount - principal
            
            # Convert rate to percentage for display
            rate_percent = rate * 100
            
            # Determine compounding frequency description
            if compounds_per_year == 1:
                frequency = "annually"
            elif compounds_per_year == 2:
                frequency = "semi-annually"
            elif compounds_per_year == 4:
                frequency = "quarterly"
            elif compounds_per_year == 12:
                frequency = "monthly"
            elif compounds_per_year == 365:
                frequency = "daily"
            else:
                frequency = f"{compounds_per_year} times per year"
            
            return (f"✅ Compound Interest Calculation:\n"
                   f"   Principal: ${principal:,.2f}\n"
                   f"   Rate: {rate_percent}% compounded {frequency}\n"
                   f"   Time: {time} years\n"
                   f"   Final Amount: ${final_amount:,.2f}\n"
                   f"   Interest Earned: ${interest_earned:,.2f}")
            
        except Exception as e:
            return f"❌ Error calculating compound interest: {str(e)}"


# Support for direct execution (testing)
if __name__ == "__main__":
    print("Advanced Calculator Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
