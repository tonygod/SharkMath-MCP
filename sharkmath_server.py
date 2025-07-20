from mcp.server.fastmcp import FastMCP

# Handle imports for both execution contexts
try:
    # When run as module from parent directory
    from . import arithmetic  # Consolidated: arithmetic + power operations (11 functions → 1 tool)
    from . import trigonometric  # Consolidated: trigonometric functions (10 functions → 1 tool)
    from . import stats_operations  # Consolidated: statistical functions (6 functions → 1 tool + percentiles)
    from . import convert_units  # Consolidated: unit conversions (42 functions → 1 tool)
    from . import logarithmic  # Consolidated: logarithmic and exponential functions (4 functions → 1 tool)
    from . import hyperbolic  # Consolidated: hyperbolic functions (3 functions → 1 tool)
    from . import precision  # Consolidated: precision and rounding functions (5 functions → 1 tool)
    from . import number_theory  # Consolidated: number theory + combinatorics (9 functions → 1 tool)
    from . import advanced_calc
    from . import matrix_operations
except ImportError:
    # When run directly from SharkMath directory
    import arithmetic  # Consolidated: arithmetic + power operations (11 functions → 1 tool)
    import trigonometric  # Consolidated: trigonometric functions (10 functions → 1 tool)
    import stats_operations  # Consolidated: statistical functions (6 functions → 1 tool + percentiles)
    import convert_units  # Consolidated: unit conversions (42 functions → 1 tool)
    import logarithmic  # Consolidated: logarithmic and exponential functions (4 functions → 1 tool)
    import hyperbolic  # Consolidated: hyperbolic functions (3 functions → 1 tool)
    import precision  # Consolidated: precision and rounding functions (5 functions → 1 tool)
    import number_theory  # Consolidated: number theory + combinatorics (9 functions → 1 tool)
    import advanced_calc
    import matrix_operations

# Initialize FastMCP server
mcp = FastMCP("SharkMath Server")

# Register tools from each module
arithmetic.register_tools(mcp)  # Consolidated: calculate_arithmetic (arithmetic + power operations)
trigonometric.register_tools(mcp)  # Consolidated: calculate_trigonometry (10 trig functions)
stats_operations.register_tools(mcp)  # Consolidated: calculate_statistics (6 stats + percentiles)
convert_units.register_tools(mcp)  # Consolidated: convert_units (42 unit conversions)
logarithmic.register_tools(mcp)  # Consolidated: calculate_logarithmic (4 logarithmic + exponential functions)
hyperbolic.register_tools(mcp)  # Consolidated: calculate_hyperbolic (3 hyperbolic functions)
precision.register_tools(mcp)  # Consolidated: format_precision (5 precision functions)
number_theory.register_tools(mcp)  # Consolidated: analyze_numbers (5 number theory + 4 combinatorial functions)
advanced_calc.register_tools(mcp)
matrix_operations.register_tools(mcp)

if __name__ == "__main__":
    import asyncio
    asyncio.run(mcp.run())
