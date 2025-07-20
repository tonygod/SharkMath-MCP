"""
Equation Solvers Module for SharkMath MCP Server

This module provides consolidated equation-solving functions including:
- Quadratic equations (ax² + bx + c = 0)
- Linear equations

Note: Financial calculations (compound_interest, simple_interest) have been 
migrated to the financial_calculations module for better organization.

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
        c: Optional[float] = None
    ) -> str:
        """
        Solve various types of equations including quadratic and linear equations.
        
        Note: Financial calculations (compound_interest, simple_interest) have been 
        migrated to the financial_calculations tool for better organization.
        
        Args:
            equation_type: Type of equation to solve - "quadratic", "linear"
            a: Coefficient of x² for quadratic equations, or coefficient of x for linear equations
            b: Coefficient of x for quadratic equations, or constant term for linear equations  
            c: Constant term for quadratic equations
            
        Returns:
            String with solution(s) or calculation results
        """
        
        # Define valid operations
        valid_operations = {
            "quadratic": _solve_quadratic,
            "linear": _solve_linear
        }
        
        # Validate operation
        if equation_type not in valid_operations:
            valid_ops = ", ".join(valid_operations.keys())
            return f"❌ Invalid equation type '{equation_type}'. Valid types: {valid_ops}"
        
        try:
            # Route to appropriate function
            return valid_operations[equation_type](
                a=a, b=b, c=c
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


# Support for direct execution (testing)
if __name__ == "__main__":
    print("Equation Solvers Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
