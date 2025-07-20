"""
Equation Solvers Module for SharkMath MCP Server

This module provides consolidated equation-solving functions including:
- Quadratic equations (ax² + bx + c = 0)
- Linear equations
- Compound interest calculations
- Simple interest calculations

All functions follow the SharkMath error handling standards with ✅/❌ prefixes.
This is a consolidated tool using parameter-based routing.
"""

import math
from typing import Optional


def register_tools(mcp):
    """Register consolidated equation solver tool with the MCP server."""
    
    @mcp.tool()
    async def solve_equations(
        equation_type: str,
        a: Optional[float] = None,
        b: Optional[float] = None, 
        c: Optional[float] = None,
        principal: Optional[float] = None,
        rate: Optional[float] = None,
        time: Optional[float] = None,
        compounds_per_year: Optional[int] = None
    ) -> str:
        """
        Solve various types of equations including quadratic, linear, and financial calculations.
        
        Args:
            equation_type: Type of equation to solve - "quadratic", "linear", "compound_interest", "simple_interest"
            a: Coefficient of x² for quadratic equations, or coefficient of x for linear equations
            b: Coefficient of x for quadratic equations, or constant term for linear equations  
            c: Constant term for quadratic equations
            principal: Initial amount for interest calculations
            rate: Interest rate as decimal (e.g., 0.05 for 5%)
            time: Time period in years for interest calculations
            compounds_per_year: Number of compounding periods per year (default 1 for simple interest)
            
        Returns:
            String with solution(s) or calculation results
        """
        
        # Define valid operations
        valid_operations = {
            "quadratic": _solve_quadratic,
            "linear": _solve_linear,
            "compound_interest": _compound_interest,
            "simple_interest": _simple_interest
        }
        
        # Validate operation
        if equation_type not in valid_operations:
            valid_ops = ", ".join(valid_operations.keys())
            return f"❌ Invalid equation type '{equation_type}'. Valid types: {valid_ops}"
        
        try:
            # Route to appropriate function
            return valid_operations[equation_type](
                a=a, b=b, c=c, 
                principal=principal, rate=rate, time=time, 
                compounds_per_year=compounds_per_year
            )
            
        except Exception as e:
            return f"❌ Error solving {equation_type} equation: {str(e)}"


def _solve_quadratic(a: Optional[float], b: Optional[float], c: Optional[float], **kwargs) -> str:
    """
    Solve quadratic equation ax² + bx + c = 0 using the quadratic formula.
    Returns real solutions or indicates complex/no solutions.
    """
    # Validate required parameters
    if a is None or b is None or c is None:
        return "❌ Quadratic equation requires parameters: a, b, c for ax² + bx + c = 0"
    
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


def _solve_linear(a: Optional[float], b: Optional[float], **kwargs) -> str:
    """
    Solve linear equation ax + b = 0.
    """
    # Validate required parameters
    if a is None or b is None:
        return "❌ Linear equation requires parameters: a, b for ax + b = 0"
    
    if a == 0:
        if b == 0:
            return "✅ All real numbers are solutions (0 = 0)"
        else:
            return "❌ No solution exists (equation reduces to constant ≠ 0)"
    
    solution = -b / a
    return f"✅ Linear equation solution: x = {solution}"


def _compound_interest(principal: Optional[float], rate: Optional[float], time: Optional[float], 
                      compounds_per_year: Optional[int], **kwargs) -> str:
    """
    Calculate compound interest using the formula: A = P(1 + r/n)^(nt)
    """
    # Validate required parameters
    if principal is None or rate is None or time is None:
        return "❌ Compound interest requires parameters: principal, rate, time"
    
    # Default compounding frequency
    if compounds_per_year is None:
        compounds_per_year = 1
    
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


def _simple_interest(principal: Optional[float], rate: Optional[float], time: Optional[float], **kwargs) -> str:
    """
    Calculate simple interest using the formula: I = P × r × t, A = P + I
    """
    # Validate required parameters
    if principal is None or rate is None or time is None:
        return "❌ Simple interest requires parameters: principal, rate, time"
    
    # Input validation
    if principal < 0:
        return "❌ Principal amount cannot be negative"
    
    if rate < 0:
        return "❌ Interest rate cannot be negative"
        
    if time < 0:
        return "❌ Time period cannot be negative"
    
    # Calculate simple interest
    # I = P × r × t
    interest_earned = principal * rate * time
    final_amount = principal + interest_earned
    
    # Convert rate to percentage for display
    rate_percent = rate * 100
    
    return (f"✅ Simple Interest Calculation:\n"
           f"   Principal: ${principal:,.2f}\n"
           f"   Rate: {rate_percent}% per year\n"
           f"   Time: {time} years\n"
           f"   Final Amount: ${final_amount:,.2f}\n"
           f"   Interest Earned: ${interest_earned:,.2f}")


# Support for direct execution (testing)
if __name__ == "__main__":
    print("Equation Solvers Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
