from mcp.server.fastmcp import FastMCP

# Handle imports for both execution contexts
try:
    # When run as module from parent directory
    from . import arithmetic  # Consolidated: arithmetic + power operations (11 functions → 1 tool)
    from . import trigonometric  # Consolidated: trigonometric functions (10 functions → 1 tool)
    from . import stats_operations  # Consolidated: statistical functions (6 functions → 1 tool + percentiles)
    from . import convert_units  # Consolidated: unit conversions (80+ functions → 1 tool)
    from . import logarithmic  # Consolidated: logarithmic and exponential functions (4 functions → 1 tool)
    from . import hyperbolic  # Consolidated: hyperbolic functions (3 functions → 1 tool)
    from . import precision  # Consolidated: precision and rounding functions (5 functions → 1 tool)
    from . import number_theory  # Consolidated: number theory + combinatorics (9 functions → 1 tool)
    from . import solve_equations  # Consolidated: equation solvers (4 functions → 1 tool)
    from . import calculate_geometry_2d  # Consolidated: 2D geometry calculations (8 functions → 1 tool)
    from . import matrix_operations  # Consolidated: matrix operations (4 functions → 1 tool)
    from . import financial_calculations  # Consolidated: financial and business calculations (11 functions → 1 tool)
    from . import computer_science_tools  # Consolidated: CS functions (12 functions → 1 tool)
    from . import data_analysis  # Consolidated: advanced data analysis functions (10 functions → 1 tool)
    from . import utility_functions  # Consolidated: utility functions (5 functions → 1 tool)
except ImportError:
    # When run directly from SharkMath directory
    import arithmetic  # Consolidated: arithmetic + power operations (11 functions → 1 tool)
    import trigonometric  # Consolidated: trigonometric functions (10 functions → 1 tool)
    import stats_operations  # Consolidated: statistical functions (6 functions → 1 tool + percentiles)
    import convert_units  # Consolidated: unit conversions (80+ functions → 1 tool)
    import logarithmic  # Consolidated: logarithmic and exponential functions (4 functions → 1 tool)
    import hyperbolic  # Consolidated: hyperbolic functions (3 functions → 1 tool)
    import precision  # Consolidated: precision and rounding functions (5 functions → 1 tool)
    import number_theory  # Consolidated: number theory + combinatorics (9 functions → 1 tool)
    import solve_equations  # Consolidated: equation solvers (4 functions → 1 tool)
    import calculate_geometry_2d  # Consolidated: 2D geometry calculations (8 functions → 1 tool)
    import matrix_operations  # Consolidated: matrix operations (4 functions → 1 tool)
    import financial_calculations  # Consolidated: financial and business calculations (11 functions → 1 tool)
    import computer_science_tools  # Consolidated: CS functions (12 functions → 1 tool)
    import data_analysis  # Consolidated: advanced data analysis functions (10 functions → 1 tool)
    import utility_functions  # Consolidated: utility functions (5 functions → 1 tool)

# Initialize FastMCP server
mcp = FastMCP("SharkMath Server")

# Register tools from each module
arithmetic.register_tools(mcp)  # Consolidated: calculate_arithmetic (arithmetic + power operations)
trigonometric.register_tools(mcp)  # Consolidated: calculate_trigonometry (10 trig functions)
stats_operations.register_tools(mcp)  # Consolidated: calculate_statistics (6 stats + percentiles)
convert_units.register_tools(mcp)  # Consolidated: convert_units (80+ unit conversions)
logarithmic.register_tools(mcp)  # Consolidated: calculate_logarithmic (4 logarithmic + exponential functions)
hyperbolic.register_tools(mcp)  # Consolidated: calculate_hyperbolic (3 hyperbolic functions)
precision.register_tools(mcp)  # Consolidated: format_precision (5 precision functions)
number_theory.register_tools(mcp)  # Consolidated: analyze_numbers (5 number theory + 4 combinatorial functions)
solve_equations.register_tools(mcp)  # Consolidated: solve_equations (quadratic, linear, compound/simple interest)
calculate_geometry_2d.register_tools(mcp)  # Consolidated: calculate_geometry_2d (distance, slope, areas, perimeters)
matrix_operations.register_tools(mcp)  # Consolidated: manipulate_matrices (4 matrix operations)
financial_calculations.register_tools(mcp)  # Consolidated: financial_calculations (11 financial and business functions)
computer_science_tools.register_tools(mcp)  # Consolidated: computer_science_tools (12 CS and programming functions)
data_analysis.register_tools(mcp)  # Consolidated: data_analysis (10 advanced statistical analysis functions)
utility_functions.register_tools(mcp)  # Consolidated: utility_functions (5 utility functions)

if __name__ == "__main__":
    import asyncio
    asyncio.run(mcp.run())
