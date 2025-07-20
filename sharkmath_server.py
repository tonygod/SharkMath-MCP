from mcp.server.fastmcp import FastMCP

# Handle imports for both execution contexts
try:
    # When run as module from parent directory
    from . import arithmetic
    from . import power_operations
    from . import logarithmic
    from . import hyperbolic
    from . import stats_operations
    from . import precision
    from . import trigonometric
    from . import combinatorics
    from . import number_theory
    from . import conversions
    from . import advanced_calc
    from . import matrix_operations
except ImportError:
    # When run directly from SharkMath directory
    import arithmetic
    import power_operations
    import logarithmic
    import hyperbolic
    import stats_operations
    import precision
    import trigonometric
    import combinatorics
    import number_theory
    import conversions
    import advanced_calc
    import matrix_operations

# Initialize FastMCP server
mcp = FastMCP("SharkMath Server")

# Register tools from each module
arithmetic.register_tools(mcp)
power_operations.register_tools(mcp)
logarithmic.register_tools(mcp)
hyperbolic.register_tools(mcp)
stats_operations.register_tools(mcp)
precision.register_tools(mcp)
trigonometric.register_tools(mcp)
combinatorics.register_tools(mcp)
number_theory.register_tools(mcp)
conversions.register_tools(mcp)
advanced_calc.register_tools(mcp)
matrix_operations.register_tools(mcp)

if __name__ == "__main__":
    import asyncio
    asyncio.run(mcp.run())
