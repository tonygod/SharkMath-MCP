# Copilot Instructions for MCP Python Tutorial Codebase

## Project Overview
This is an MCP server containing over 70 tools for solving mathematical problems

## Core Architecture

### MCP Server Types
1. **SharkMath Server** (`sharkmath_server.py`) - Mathematical tools

### Key Components
- **FastMCP servers** - All servers use `FastMCP("Server Name")` pattern
- **SharkMath Server** - Comprehensive mathematical calculation server with modular architecture (70+ functions across 12 domains)

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
  - `logarithmic.py` - Logarithmic and exponential functions (natural_log, log_base_10, log_base, exponential)
  - `hyperbolic.py` - Hyperbolic functions (sinh, cosh, tanh)
  - `precision.py` - Rounding and precision utilities (round_to_decimal, floor, ceiling, truncate, absolute)
  - `combinatorics.py` - Combinatorial mathematics (factorial, permutation, combination, fibonacci)
  - `number_theory.py` - Number theory functions (gcd, lcm, is_prime, prime_factors, is_perfect_square)
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

#### **Logarithmic and Exponential Functions** (`logarithmic.py`)
- **natural_log(n)** - Calculate ln(n) with domain validation (n > 0)
- **log_base_10(n)** - Calculate log₁₀(n) with domain validation
- **log_base(n, base)** - Calculate logarithm with custom base (base > 0, base ≠ 1)
- **exponential(n)** - Calculate e^n with overflow protection

#### **Hyperbolic Functions** (`hyperbolic.py`)
- **sinh(x)** - Hyperbolic sine with overflow protection (|x| ≤ 700)
- **cosh(x)** - Hyperbolic cosine with overflow protection (|x| ≤ 700)
- **tanh(x)** - Hyperbolic tangent (naturally bounded between -1 and 1)

#### **Combinatorial Mathematics Functions** (`combinatorics.py`)
- **factorial(n)** - Calculate n! with non-negative integer validation
- **permutation(n, r)** - Calculate P(n,r) = n!/(n-r)! for permutations
- **combination(n, r)** - Calculate C(n,r) = n!/(r!(n-r)!) for combinations
- **fibonacci(n)** - Calculate nth Fibonacci number with sequence validation

#### **Number Theory Functions** (`number_theory.py`)
- **gcd(a, b)** - Calculate Greatest Common Divisor with zero handling
- **lcm(a, b)** - Calculate Least Common Multiple with zero handling
- **is_prime(n)** - Check if number is prime with optimized algorithm
- **prime_factors(n)** - List all prime factors with efficient factorization
- **is_perfect_square(n)** - Check if number is perfect square with exact calculation

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
- `logarithmic.py` - Logarithmic and exponential functions module
- `hyperbolic.py` - Hyperbolic functions module
- `precision.py` - Rounding and precision utilities module
- `combinatorics.py` - Combinatorial mathematics and factorial operations module
- `number_theory.py` - Number theory and prime mathematics module
- `advanced_calc.py` - Advanced calculator functions (quadratic solver, 2D geometry, financial calculations)
- `matrix_operations.py` - Matrix operations and linear algebra functions
- `sharkmath_tasklist.md` - Development roadmap and task tracking
- `pyproject.toml` - Project dependencies and tooling configuration
- `.vscode/mcp.json` - VS Code MCP server configuration
