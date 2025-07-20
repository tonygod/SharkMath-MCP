# Copilot Instructions for MCP Python Tutorial Codebase

## Project Overview
This is an MCP server containing over 70 tools for solving mathematical problems

## Core Architecture

### MCP Server Types
1. **SharkMath Server** (`sharkmath_server.py`) - Mathematical tools

### Key Components
- **FastMCP servers** - All servers use `FastMCP("Server Name")` pattern
- **SharkMath Server** - Comprehensive mathematical calculation server with modular architecture (60+ functions consolidated into 8 tools across 12 domains)

## Development Patterns

### MCP Server Structure
```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Server Name")

@mcp.prompt()          # Template functions
@mcp.tool()            # Executable functions  
@mcp.resource()        # Data access functions
```

### Environment Setup
- Uses **uv** package manager (configured in `.vscode/mcp.json`)
- Virtual environment in `mcp-env/` directory
- VS Code MCP configuration: `uv --directory . run sharkmath_server.py`

### SharkMath Consolidated Architecture
- **Main server pattern** - `sharkmath_server.py` imports and registers tools from modules
- **Module registration** - Each module has `register_tools(mcp)` function
- **Dual import context** - Handles both direct execution and module imports
- **Consolidated tools** - Parameter-based routing reduces tool count from 70+ to 18
- **Consistent error handling** - All functions use ✅/❌ prefixes
- **Domain validation** - Input validation specific to each mathematical operation

## Critical Workflows

### Running MCP Servers
```bash
uv run SharkMath/sharkmath_server.py
```

### VS Code MCP Integration
- Configure servers in `.vscode/mcp.json`
- Use server name `"sharkmath-mcp"` for tools server
- MCP servers connect to VS Code Copilot chat via configuration

## Project-Specific Conventions

### Async/Context Patterns
- MCP tools use `Context` parameter for AI sampling
- Sampling pattern: `ctx.session.create_message()` with `SamplingMessage`
- Always handle JSON parsing errors in tools that generate content

### File Organization
- **Root level** - Consolidated mathematical calculation MCP server with parameter-based routing
  - `arithmetic.py` - **CONSOLIDATED**: `calculate_arithmetic` - 11 operations (add, subtract, multiply, divide, calculate, power, square, cube, square_root, cube_root, nth_root)
  - `trigonometric.py` - **CONSOLIDATED**: `calculate_trigonometry` - 10 operations (sin, cos, tan, asin, acos, atan, atan2 with radians/degrees support)
  - `stats_operations.py` - **CONSOLIDATED**: `calculate_statistics` - 7 operations (mean, median, mode, standard_deviation, variance, range_stats, percentile)
  - `convert_units.py` - **CONSOLIDATED**: `convert_units` - 42 unit conversions (temperature, length, weight, volume, energy, time, angle)
  - `logarithmic.py` - **CONSOLIDATED**: `calculate_logarithmic` - 4 operations (natural_log, log_base_10, log_base, exponential)
  - `hyperbolic.py` - **CONSOLIDATED**: `calculate_hyperbolic` - 3 operations (sinh, cosh, tanh)
  - `precision.py` - **CONSOLIDATED**: `format_precision` - 5 operations (round, floor, ceiling, truncate, absolute)
  - `number_theory.py` - **CONSOLIDATED**: `analyze_numbers` - 9 operations (5 number theory + 4 combinatorial: gcd, lcm, is_prime, prime_factors, is_perfect_square, factorial, permutation, combination, fibonacci)
  - `advanced_calc.py` - Advanced calculator functions (solve_quadratic, distance_2d, slope, compound_interest)
  - `matrix_operations.py` - Matrix calculations (matrix_add, matrix_multiply, matrix_determinant, matrix_transpose)
- **Tests** - Individual test suites per consolidated tool for comprehensive coverage  

### Error Handling
- Tools return descriptive error messages (❌ prefix)
- Success messages use checkmark prefix (✅)
- JSON errors include partial response for debugging

## Integration Points

### External Dependencies
- **FastMCP** - Core MCP server framework
- **Dataclasses** - Type-safe data models
- **JSON** - Primary data persistence format

### MCP Protocol Usage
- **Tools** execute functions and return status/results

### Mathematical Tools (SharkMath Server)
#### **Consolidated Arithmetic Operations** (`arithmetic.py`)
- **calculate_arithmetic(operation, a, b, expression, base, exponent, n, root)** - Consolidated tool with 11 operations:
  - add, subtract, multiply, divide (basic arithmetic)
  - calculate (expression evaluation)
  - power, square, cube (exponentiation)
  - square_root, cube_root, nth_root (root extraction)

#### **Consolidated Trigonometric Functions** (`trigonometric.py`)
- **calculate_trigonometry(operation, angle, angle_unit, value, y, x)** - Consolidated tool with 10 operations:
  - sin, cos, tan (basic trig functions with radians/degrees support)
  - asin, acos, atan (inverse trig functions)
  - atan2 (two-argument arctangent)

#### **Consolidated Statistical Functions** (`stats_operations.py`)
- **calculate_statistics(operation, numbers, percentile)** - Consolidated tool with 7 operations:
  - mean, median, mode (central tendency)
  - standard_deviation, variance (spread measures)
  - range_stats (min, max, range)
  - percentile (0-100th percentile calculation)

#### **Consolidated Unit Conversions** (`convert_units.py`)
- **convert_units(from_unit, to_unit, value, time_hours)** - Consolidated tool with 42 conversions:
  - Temperature: celsius ↔ fahrenheit
  - Length: meters ↔ feet, kilometers ↔ miles, inches ↔ centimeters
  - Weight: kilograms ↔ pounds
  - Volume: liters ↔ gallons  
  - Energy: watts ↔ kilowatts, horsepower ↔ watts, joules ↔ calories/BTU
  - Time: hours ↔ minutes/days, days ↔ weeks/months/years
  - Angle: degrees ↔ radians
- **floor(n)** - Floor function (largest integer ≤ n)
#### **Precision and Rounding Functions** (`precision.py`)
- **round_to_decimal(n, places)** - Round to specified decimal places
- **floor(n)** - Floor function (largest integer ≤ n)
- **ceiling(n)** - Ceiling function (smallest integer ≥ n)
- **truncate(n)** - Truncate decimal part (round toward zero)
- **absolute(n)** - Absolute value calculation

#### **Consolidated Logarithmic and Exponential Functions** (`logarithmic.py`)
- **calculate_logarithmic(operation, value, base)** - Consolidated tool with 4 operations:
  - natural_log (ln(n) with domain validation n > 0)
  - log_base_10 (log₁₀(n) with domain validation)
  - log_base (custom base logarithm with base validation)
  - exponential (e^n with overflow protection |n| ≤ 700)

#### **Consolidated Hyperbolic Functions** (`hyperbolic.py`)
- **calculate_hyperbolic(operation, value)** - Consolidated tool with 3 operations:
  - sinh (hyperbolic sine with overflow protection |x| ≤ 700)
  - cosh (hyperbolic cosine with overflow protection |x| ≤ 700)
  - tanh (hyperbolic tangent, naturally bounded between -1 and 1)

#### **Consolidated Precision and Rounding Functions** (`precision.py`)
- **format_precision(operation, value, places)** - Consolidated tool with 5 operations:
  - round (round to specified decimal places, places parameter required)
  - floor (largest integer ≤ n)
  - ceiling (smallest integer ≥ n)
  - truncate (round toward zero)
  - absolute (absolute value calculation)

#### **Consolidated Number Theory and Combinatorial Functions** (`number_theory.py`)
- **analyze_numbers(operation, value, second_value)** - Consolidated tool with 9 operations:
  - Number theory: gcd, lcm (second_value required), is_prime, prime_factors, is_perfect_square
  - Combinatorial: factorial, permutation, combination (second_value required), fibonacci
  - Domain validation and overflow protection for large numbers

#### **Advanced Calculator Functions** (`advanced_calc.py`)
- **solve_quadratic(a, b, c)** - Solve quadratic equations ax² + bx + c = 0 using quadratic formula, handles linear equations, complex solutions, and special cases
- **distance_2d(x1, y1, x2, y2)** - Calculate Euclidean distance between two points in 2D space using distance formula
- **slope(x1, y1, x2, y2)** - Calculate slope between two points with special handling for vertical/horizontal lines and 45° angles
- **compound_interest(principal, rate, time, compounds_per_year)** - Calculate compound interest with detailed breakdown of principal, final amount, and interest earned

#### **Matrix Operations** (`matrix_operations.py`)
- **matrix_add(matrix1, matrix2)** - Add two matrices of the same dimensions with JSON input format (e.g., "[[1,2],[3,4]]")
- **matrix_multiply(matrix1, matrix2)** - Multiply two matrices with compatibility validation (columns of first must equal rows of second)
- **matrix_determinant(matrix)** - Calculate determinant of square matrices up to 10×10 using recursive expansion
- **matrix_transpose(matrix)** - Transpose matrix (swap rows and columns) with JSON input/output format

## Key Files for Context
- `sharkmath_server.py` - Main mathematical MCP server with consolidated imports
- `arithmetic.py` - **CONSOLIDATED**: Basic arithmetic and power operations module
- `trigonometric.py` - **CONSOLIDATED**: Trigonometric and inverse trigonometric functions module  
- `stats_operations.py` - **CONSOLIDATED**: Statistical calculations module
- `convert_units.py` - **CONSOLIDATED**: Unit conversion functions (temperature, length, weight, volume, energy, time, angle)
- `logarithmic.py` - **CONSOLIDATED**: Logarithmic and exponential functions module
- `hyperbolic.py` - **CONSOLIDATED**: Hyperbolic functions module
- `precision.py` - **CONSOLIDATED**: Rounding and precision utilities module
- `number_theory.py` - **CONSOLIDATED**: Number theory and combinatorial mathematics module (includes former combinatorics.py)
- `advanced_calc.py` - Advanced calculator functions (quadratic solver, 2D geometry, financial calculations)
- `matrix_operations.py` - Matrix operations and linear algebra functions
- `sharkmath_tasklist.md` - Development roadmap and task tracking
- `pyproject.toml` - Project dependencies and tooling configuration
- `.vscode/mcp.json` - VS Code MCP server configuration
