"""
Utility Functions - Helper utilities and constants for SharkMath MCP Server
Provides mathematical constants, input validation helpers, and operation documentation.
"""

import math


def register_tools(mcp):
    """Register the consolidated utility_functions tool with the MCP server."""
    
    @mcp.tool()
    async def utility_functions(operation: str, name: str = "", value: float = 0.0, operation_type: str = "") -> str:
        """Utility functions providing mathematical constants, validation, and help.
        
        Available operations:
        - mathematical_constants: Get common mathematical constants (pi, e, phi, etc.)
        - validate_input: Validate numeric input for mathematical operations
        - operation_help: Get help for specific mathematical operations
        - list_operations: List all available operations in SharkMath
        - format_number: Format numbers with specified precision and notation
        
        Args:
            operation: Type of utility operation to perform
            name: Name of constant/operation for help (for constants/help operations)
            value: Numeric value for validation or formatting operations
            operation_type: Type of operation for help (arithmetic, trigonometry, etc.)
        """
        
        try:
            # Mathematical constants
            if operation == "mathematical_constants":
                constants = {
                    "pi": math.pi,
                    "e": math.e,
                    "tau": 2 * math.pi,
                    "phi": (1 + math.sqrt(5)) / 2,  # Golden ratio
                    "euler_gamma": 0.5772156649015329,  # Euler-Mascheroni constant
                    "sqrt_2": math.sqrt(2),
                    "sqrt_3": math.sqrt(3),
                    "ln_2": math.log(2),
                    "ln_10": math.log(10),
                    "avogadro": 6.02214076e23,
                    "planck": 6.62607015e-34,
                    "light_speed": 299792458,  # meters per second
                    "gravitational": 6.67430e-11,  # m³/kg⋅s²
                }
                
                if name:
                    if name.lower() in constants:
                        value = constants[name.lower()]
                        return f"✅ Mathematical constant '{name}' = {value}"
                    else:
                        available = list(constants.keys())
                        return f"❌ Unknown constant '{name}'. Available: {', '.join(available)}"
                else:
                    result = "✅ Mathematical Constants:\n"
                    for const_name, const_value in constants.items():
                        result += f"  • {const_name}: {const_value}\n"
                    return result.strip()
            
            # Input validation
            elif operation == "validate_input":
                if not isinstance(value, (int, float)):
                    return f"❌ Value must be numeric, got {type(value).__name__}"
                
                if math.isnan(value):
                    return f"❌ Value cannot be NaN (Not a Number)"
                
                if math.isinf(value):
                    return f"❌ Value cannot be infinite"
                
                return f"✅ Input value {value} is valid for mathematical operations"
            
            # Operation help
            elif operation == "operation_help":
                help_docs = {
                    "arithmetic": {
                        "description": "Basic arithmetic operations",
                        "operations": ["add", "subtract", "multiply", "divide", "power", "square", "cube", "square_root", "cube_root", "nth_root", "calculate"],
                        "usage": "calculate_arithmetic(operation, a, b, expression, base, exponent, n, root)"
                    },
                    "trigonometry": {
                        "description": "Trigonometric functions",
                        "operations": ["sin", "cos", "tan", "asin", "acos", "atan", "atan2"],
                        "usage": "calculate_trigonometry(operation, angle, angle_unit, value, y, x)"
                    },
                    "statistics": {
                        "description": "Statistical calculations",
                        "operations": ["mean", "median", "mode", "standard_deviation", "variance", "range_stats", "percentile"],
                        "usage": "calculate_statistics(operation, numbers, percentile)"
                    },
                    "conversions": {
                        "description": "Unit conversions",
                        "operations": ["energy", "temperature", "length", "time", "weight", "volume", "area", "speed", "pressure", "data"],
                        "usage": "convert_units(from_unit, to_unit, value, time_hours)"
                    },
                    "logarithmic": {
                        "description": "Logarithmic and exponential functions",
                        "operations": ["natural_log", "log_base_10", "log_base", "exponential"],
                        "usage": "calculate_logarithmic(operation, value, base)"
                    },
                    "hyperbolic": {
                        "description": "Hyperbolic functions",
                        "operations": ["sinh", "cosh", "tanh"],
                        "usage": "calculate_hyperbolic(operation, value)"
                    },
                    "precision": {
                        "description": "Precision and rounding functions",
                        "operations": ["round", "floor", "ceiling", "truncate", "absolute"],
                        "usage": "format_precision(operation, value, places)"
                    },
                    "number_theory": {
                        "description": "Number theory and combinatorial functions",
                        "operations": ["gcd", "lcm", "is_prime", "prime_factors", "is_perfect_square", "factorial", "permutation", "combination", "fibonacci"],
                        "usage": "analyze_numbers(operation, value, second_value)"
                    },
                    "equations": {
                        "description": "Equation solving",
                        "operations": ["quadratic", "linear", "compound_interest", "simple_interest"],
                        "usage": "solve_equations(equation_type, a, b, c, extra_params)"
                    },
                    "geometry": {
                        "description": "2D geometry calculations",
                        "operations": ["distance", "slope", "circle_area", "circle_circumference", "triangle_area", "rectangle_area", "rectangle_perimeter"],
                        "usage": "calculate_geometry_2d(operation, params)"
                    },
                    "matrices": {
                        "description": "Matrix operations",
                        "operations": ["add", "multiply", "determinant", "transpose"],
                        "usage": "manipulate_matrices(operation, matrix1, matrix2)"
                    },
                    "financial": {
                        "description": "Financial calculations",
                        "operations": ["compound_interest", "simple_interest", "present_value", "future_value", "loan_payment", "roi", "depreciation", "mortgage", "break_even", "npv", "irr"],
                        "usage": "financial_calculations(operation, principal, rate, time, params)"
                    },
                    "computer_science": {
                        "description": "Computer science functions",
                        "operations": ["base_conversion", "hash_function", "big_o_analysis", "data_size_conversion", "bitwise_operations", "ascii_conversion"],
                        "usage": "computer_science_tools(operation, value, params)"
                    },
                    "data_analysis": {
                        "description": "Advanced data analysis",
                        "operations": ["z_score", "correlation", "quartiles", "skewness", "kurtosis", "coefficient_variation", "outliers", "confidence_interval", "standardize", "iqr"],
                        "usage": "data_analysis(operation, data, params)"
                    }
                }
                
                if operation_type:
                    if operation_type.lower() in help_docs:
                        info = help_docs[operation_type.lower()]
                        result = f"✅ {info['description'].title()}\n"
                        result += f"Usage: {info['usage']}\n"
                        result += f"Operations: {', '.join(info['operations'])}"
                        return result
                    else:
                        available = list(help_docs.keys())
                        return f"❌ Unknown operation type '{operation_type}'. Available: {', '.join(available)}"
                else:
                    result = "✅ Available Operation Types:\n"
                    for op_type, info in help_docs.items():
                        result += f"  • {op_type}: {info['description']}\n"
                    return result.strip()
            
            # List all operations
            elif operation == "list_operations":
                operations = {
                    "Core Mathematics": ["calculate_arithmetic", "calculate_trigonometry", "calculate_statistics", "calculate_logarithmic", "calculate_hyperbolic"],
                    "Applied Mathematics": ["solve_equations", "calculate_geometry_2d", "manipulate_matrices", "format_precision", "analyze_numbers"],
                    "Unit Conversions": ["convert_units"],
                    "Specialized Tools": ["financial_calculations", "computer_science_tools", "data_analysis"],
                    "Utilities": ["utility_functions"]
                }
                
                result = "✅ SharkMath Operations (14 Total Tools):\n"
                for category, tools in operations.items():
                    result += f"\n{category}:\n"
                    for tool in tools:
                        result += f"  • {tool}\n"
                
                return result.strip()
            
            # Number formatting
            elif operation == "format_number":
                if not isinstance(value, (int, float)):
                    return f"❌ Value must be numeric for formatting"
                
                # Format number with different notations
                scientific = f"{value:.3e}"
                engineering = f"{value:.6g}"
                fixed_2 = f"{value:.2f}"
                fixed_6 = f"{value:.6f}"
                
                result = f"✅ Number formatting for {value}:\n"
                result += f"  • Scientific: {scientific}\n"
                result += f"  • Engineering: {engineering}\n"
                result += f"  • Fixed (2 decimals): {fixed_2}\n"
                result += f"  • Fixed (6 decimals): {fixed_6}\n"
                result += f"  • Percentage: {value * 100:.2f}%"
                
                return result
            
            else:
                available_ops = ["mathematical_constants", "validate_input", "operation_help", "list_operations", "format_number"]
                return f"❌ Unknown utility operation '{operation}'. Available: {', '.join(available_ops)}"
                
        except Exception as e:
            return f"❌ Error in utility function: {str(e)}"


# For direct execution testing
if __name__ == "__main__":
    print("Testing Utility Functions Tool:")
    
    # Mock MCP object for testing
    class MockMCP:
        def tool(self):
            def decorator(func):
                return func
            return decorator
    
    mock_mcp = MockMCP()
    register_tools(mock_mcp)
    
    print("✅ utility_functions tool registered successfully!")
    print("✅ Provides mathematical constants, validation, and help")
    print("✅ Ready for MCP integration testing")
