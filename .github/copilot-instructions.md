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

### SharkMath Modular Architecture
- **Main server pattern** - `sharkmath_server.py` imports and registers tools from modules
- **Module registration** - Each module has `register_tools(mcp)` function
- **Dual import context** - Handles both direct execution and module imports
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
- **Root level** - Modular mathematical calculation MCP server with specialized function modules
  - `arithmetic.py` - Basic operations (add, subtract, multiply, divide, calculate)
  - `power_operations.py` - Power and root functions (power, square, cube, square_root, cube_root, nth_root)
  - `logarithmic.py` - Logarithmic and exponential functions (natural_log, log_base_10, log_base, exponential)
  - `hyperbolic.py` - Hyperbolic functions (sinh, cosh, tanh)
  - `statistics.py` - Statistical functions (mean, median, mode, standard_deviation, variance, range_stats)
  - `precision.py` - Rounding and precision utilities (round_to_decimal, floor, ceiling, truncate, absolute)
  - `trigonometric.py` - Trigonometric functions (sin, cos, tan, sin_degrees, cos_degrees, tan_degrees, asin, acos, atan, atan2)
  - `combinatorics.py` - Combinatorial mathematics (factorial, permutation, combination, fibonacci)
  - `number_theory.py` - Number theory functions (gcd, lcm, is_prime, prime_factors, is_perfect_square)
  - `conversions.py` - Unit conversion functions (degrees_to_radians, radians_to_degrees, celsius_to_fahrenheit, fahrenheit_to_celsius, meters_to_feet, feet_to_meters, inches_to_centimeters, centimeters_to_inches, kilometers_to_miles, miles_to_kilometers, kilograms_to_pounds, pounds_to_kilograms, liters_to_gallons, gallons_to_liters)
  - `advanced_calc.py` - Advanced calculator functions (solve_quadratic, distance_2d, slope, compound_interest)
  - `matrix_operations.py` - Matrix calculations (matrix_add, matrix_multiply, matrix_determinant, matrix_transpose)
- **Tests** - Tests used to verify functionality during implementation of mathematical tools  

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
#### **Arithmetic Operations** (`arithmetic.py`)
- **add(a, b)** - Addition of two numbers
- **subtract(a, b)** - Subtraction (a - b)
- **multiply(a, b)** - Multiplication of two numbers
- **divide(a, b)** - Division with zero-division protection
- **calculate(expression)** - Safe evaluation of mathematical expressions with operator validation

#### **Power and Root Operations** (`power_operations.py`)
- **power(base, exponent)** - Calculate base raised to the power of exponent
- **square(n)** - Calculate n²
- **cube(n)** - Calculate n³
- **square_root(n)** - Calculate √n with negative number validation
- **cube_root(n)** - Calculate ∛n (handles negative numbers)
- **nth_root(n, root)** - Calculate nth root with domain validation

#### **Logarithmic and Exponential Functions** (`logarithmic.py`)
- **natural_log(n)** - Calculate ln(n) with domain validation (n > 0)
- **log_base_10(n)** - Calculate log₁₀(n) with domain validation
- **log_base(n, base)** - Calculate logarithm with custom base (base > 0, base ≠ 1)
- **exponential(n)** - Calculate e^n with overflow protection

#### **Hyperbolic Functions** (`hyperbolic.py`)
- **sinh(x)** - Hyperbolic sine with overflow protection (|x| ≤ 700)
- **cosh(x)** - Hyperbolic cosine with overflow protection (|x| ≤ 700)
- **tanh(x)** - Hyperbolic tangent (naturally bounded between -1 and 1)

#### **Statistical Functions** (`statistics.py`)
- **mean(numbers)** - Calculate arithmetic mean from comma-separated values
- **median(numbers)** - Calculate median from comma-separated values
- **mode(numbers)** - Calculate mode (most frequent value)
- **standard_deviation(numbers)** - Calculate standard deviation
- **variance(numbers)** - Calculate variance  
- **range_stats(numbers)** - Calculate min, max, and range statistics

#### **Precision and Rounding Functions** (`precision.py`)
- **round_to_decimal(n, places)** - Round to specified decimal places
- **floor(n)** - Floor function (largest integer ≤ n)
- **ceiling(n)** - Ceiling function (smallest integer ≥ n)
- **truncate(n)** - Truncate decimal part (round toward zero)
- **absolute(n)** - Absolute value calculation

#### **Trigonometric Functions** (`trigonometric.py`)
- **sin(angle_radians)** - Sine function with radian input
- **cos(angle_radians)** - Cosine function with radian input
- **tan(angle_radians)** - Tangent function with undefined value detection
- **sin_degrees(angle_degrees)** - Sine function with degree input
- **cos_degrees(angle_degrees)** - Cosine function with degree input
- **tan_degrees(angle_degrees)** - Tangent function with degree input
- **asin(value)** - Arcsine with domain validation [-1, 1]
- **acos(value)** - Arccosine with domain validation [-1, 1]
- **atan(value)** - Arctangent function
- **atan2(y, x)** - Two-argument arctangent

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

#### **Unit Conversion Functions** (`conversions.py`)
- **degrees_to_radians(degrees)** - Convert angle measurements from degrees to radians
- **radians_to_degrees(radians)** - Convert angle measurements from radians to degrees
- **celsius_to_fahrenheit(celsius)** - Convert temperature from Celsius to Fahrenheit
- **fahrenheit_to_celsius(fahrenheit)** - Convert temperature from Fahrenheit to Celsius
- **meters_to_feet(meters)** - Convert length from meters to feet
- **feet_to_meters(feet)** - Convert length from feet to meters
- **inches_to_centimeters(inches)** - Convert length from inches to centimeters
- **centimeters_to_inches(centimeters)** - Convert length from centimeters to inches
- **kilometers_to_miles(kilometers)** - Convert distance from kilometers to miles
- **miles_to_kilometers(miles)** - Convert distance from miles to kilometers
- **kilograms_to_pounds(kilograms)** - Convert weight from kilograms to pounds
- **pounds_to_kilograms(pounds)** - Convert weight from pounds to kilograms
- **liters_to_gallons(liters)** - Convert volume from liters to US gallons
- **gallons_to_liters(gallons)** - Convert volume from US gallons to liters

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
- `sharkmath_server.py` - Main mathematical MCP server with modular imports
- `arithmetic.py` - Basic arithmetic operations module
- `power_operations.py` - Power and root functions module
- `logarithmic.py` - Logarithmic and exponential functions module
- `hyperbolic.py` - Hyperbolic functions module
- `statistics.py` - Statistical calculations module
- `precision.py` - Rounding and precision utilities module
- `trigonometric.py` - Trigonometric and inverse trigonometric functions module
- `combinatorics.py` - Combinatorial mathematics and factorial operations module
- `number_theory.py` - Number theory and prime mathematics module
- `conversions.py` - Unit conversion functions (degrees/radians, celsius/fahrenheit, meters/feet, kilometers/miles, kilograms/pounds, liters/gallons)
- `advanced_calc.py` - Advanced calculator functions (quadratic solver, 2D geometry, financial calculations)
- `matrix_operations.py` - Matrix operations and linear algebra functions
- `sharkmath_tasklist.md` - Development roadmap and task tracking
- `pyproject.toml` - Project dependencies and tooling configuration
- `.vscode/mcp.json` - VS Code MCP server configuration
