# SharkMath MCP - Complete API Documentation

## Overview

SharkMath MCP is a comprehensive mathematical computation server built on the Model Context Protocol (MCP) framework. It provides **15 consolidated tools** covering **150+ mathematical operations** across all mathematical domains through an efficient parameter-based routing system.

## Architecture

### Consolidated Tool Pattern
SharkMath uses a **parameter-based routing architecture** where each tool accepts an `operation` parameter to specify the desired mathematical function. This approach provides:

- **Efficient tool registration**: 150+ functions consolidated into 15 tools
- **Logical domain grouping**: Related operations grouped by mathematical domain
- **Consistent error handling**: All tools use ✅/❌ prefixes for results
- **Comprehensive validation**: Input validation specific to each operation
- **MCP compatibility**: Avoids tool registration limits

## Tool Reference

### 1. calculate_arithmetic
**Domain**: Basic Arithmetic & Power Operations  
**Operations**: 11 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `a`, `b`: Operands for basic arithmetic
- `n`: Single operand for power operations
- `base`, `exponent`: For power calculations
- `root`: For nth root calculations
- `expression`: Mathematical expression string
- `precision`: Decimal places for calculations (default: 10)
- `timeout_seconds`: Expression timeout (default: 5.0)
- `max_complexity`: Expression complexity limit (default: 100)

#### Operations

**Basic Arithmetic**
- `add` - Addition: `a + b`
- `subtract` - Subtraction: `a - b`
- `multiply` - Multiplication: `a * b`
- `divide` - Division with zero protection: `a / b`

**Expression Evaluation**
- `calculate` - Enhanced expression evaluation with 20+ mathematical functions
  - **Basic Functions**: `sqrt()`, `pow()`, `abs()`, `round()`
  - **Trigonometric**: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`
  - **Logarithmic**: `log()`, `log10()`, `ln()` (natural log)
  - **Hyperbolic**: `sinh()`, `cosh()`, `tanh()`
  - **Rounding**: `floor()`, `ceil()`, `trunc()`
  - **Constants**: `pi`, `e`
  - **Exponentiation**: Support for both `^` and `**` operators

**Power Operations**
- `power` - Exponentiation: `base^exponent`
- `square` - Square: `n²`
- `cube` - Cube: `n³`
- `square_root` - Square root: `√n`
- `cube_root` - Cube root: `∛n`
- `nth_root` - Nth root: `n^(1/root)`

#### Security Features
- **Expression complexity limits**: Prevents DoS attacks
- **Function validation**: Whitelist-based function security
- **Timeout protection**: Prevents infinite evaluation
- **Domain validation**: Prevents invalid mathematical operations

#### Examples
```python
# Basic arithmetic
calculate_arithmetic("add", a=5, b=3)  # ✅ 5 + 3 = 8

# Enhanced expression evaluation
calculate_arithmetic("calculate", expression="sqrt(25) + sin(pi/2)")  # ✅ sqrt(25) + sin(pi/2) = 6.0
calculate_arithmetic("calculate", expression="sqrt((5-0)^2 + (12-0)^2)")  # ✅ Distance formula = 13.0

# Power operations
calculate_arithmetic("power", base=2, exponent=8)  # ✅ 2^8 = 256
calculate_arithmetic("square_root", n=25)  # ✅ √25 = 5.0
```

---

### 2. calculate_trigonometry
**Domain**: Trigonometric Functions  
**Operations**: 10 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `angle`: Input angle for trig functions
- `angle_unit`: "radians" or "degrees" (default: "radians")
- `value`: Input value for inverse trig functions
- `x`, `y`: Coordinates for atan2 function

#### Operations

**Standard Trigonometric Functions**
- `sin` - Sine function
- `cos` - Cosine function
- `tan` - Tangent function (with undefined value detection)

**Inverse Trigonometric Functions**
- `asin` - Inverse sine (domain: [-1, 1])
- `acos` - Inverse cosine (domain: [-1, 1])
- `atan` - Inverse tangent
- `atan2` - Two-argument arctangent (y, x coordinates)

#### Features
- **Dual unit support**: Both radians and degrees
- **Domain validation**: Prevents invalid inputs
- **Undefined value detection**: Handles tan(90°), tan(π/2), etc.
- **Comprehensive output**: Returns both radians and degrees for inverse functions

#### Examples
```python
# Standard trig functions
calculate_trigonometry("sin", angle=90, angle_unit="degrees")  # ✅ sin(90°) = 1.0
calculate_trigonometry("cos", angle=1.57, angle_unit="radians")  # ✅ cos(1.57 rad) ≈ 0.0

# Inverse trig functions
calculate_trigonometry("asin", value=0.5)  # ✅ arcsin(0.5) = 0.5236 rad = 30.0°
calculate_trigonometry("atan2", y=1, x=1)  # ✅ atan2(1, 1) = 0.7854 rad = 45.0°
```

---

### 3. calculate_statistics
**Domain**: Statistical Analysis  
**Operations**: 7 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `numbers` (required): Comma or space-separated number list
- `percentile`: Percentile value 0-100 (for percentile operation)

#### Operations

**Central Tendency**
- `mean` - Arithmetic mean (average)
- `median` - Middle value when sorted
- `mode` - Most frequently occurring value

**Dispersion Measures**
- `standard_deviation` - Population standard deviation
- `variance` - Population variance
- `range_stats` - Minimum, maximum, and range

**Percentile Analysis**
- `percentile` - Calculate specified percentile (requires percentile parameter)

#### Input Formats
- Comma-separated: `"1,2,3,4,5"`
- Space-separated: `"1 2 3 4 5"`
- Mixed format: `"2.5, 3.0, 3.5, 4.0"`

#### Examples
```python
# Central tendency
calculate_statistics("mean", "1,2,3,4,5")  # ✅ Mean of [1, 2, 3, 4, 5] = 3.0
calculate_statistics("median", "10 20 30 40 50")  # ✅ Median of [10, 20, 30, 40, 50] = 30.0

# Dispersion
calculate_statistics("standard_deviation", "2.5, 3.0, 3.5, 4.0")  # ✅ Standard Deviation = 0.559

# Percentiles
calculate_statistics("percentile", "1,2,3,4,5,6,7,8,9,10", percentile=75)  # ✅ 75th Percentile = 7.75
```

---

### 4. convert_units
**Domain**: Universal Unit Conversion  
**Operations**: 80+ conversions consolidated

#### Parameters
- `from_unit` (required): Source unit
- `to_unit` (required): Target unit
- `value` (required): Numeric value to convert
- `time_hours`: Time duration for energy conversions (default: 1.0)

#### Supported Unit Categories

**Energy**: watts, kilowatts, horsepower, joules, calories, btu  
**Temperature**: celsius, fahrenheit  
**Length**: meters, feet, inches, centimeters, kilometers, miles  
**Time**: seconds, minutes, hours, days, weeks, months, years, milliseconds  
**Weight**: kilograms, pounds  
**Volume**: liters, gallons  
**Area**: square_meters, square_feet, acres, hectares  
**Speed**: mps (m/s), kmh, mph, knots  
**Pressure**: pascals, atmospheres, psi, bar  
**Data**: bytes, kilobytes, megabytes, gigabytes, terabytes, petabytes, bits

#### Examples
```python
# Temperature
convert_units("celsius", "fahrenheit", 25)  # ✅ 25°C = 77.0°F

# Length
convert_units("meters", "feet", 10)  # ✅ 10 meters = 32.81 feet

# Data
convert_units("megabytes", "gigabytes", 1024)  # ✅ 1024 MB = 1.024 GB

# Energy with time
convert_units("kilowatts", "joules", 5, time_hours=2)  # ✅ 5 kW × 2 hours = 36,000,000 joules
```

---

### 5. calculate_logarithmic
**Domain**: Logarithmic & Exponential Functions  
**Operations**: 4 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `value` (required): Input number
- `base`: Base for custom logarithm (log_base operation only)

#### Operations
- `natural_log` - Natural logarithm (ln)
- `log_base_10` - Base-10 logarithm
- `log_base` - Custom base logarithm (requires base parameter)
- `exponential` - Exponential function (e^x)

#### Features
- **Domain validation**: Prevents log of non-positive numbers
- **Base validation**: Ensures valid logarithm bases
- **Overflow protection**: Handles large exponential results

#### Examples
```python
calculate_logarithmic("natural_log", 2.71828)  # ✅ ln(2.71828) ≈ 1.0
calculate_logarithmic("log_base_10", 1000)  # ✅ log₁₀(1000) = 3.0
calculate_logarithmic("log_base", 8, base=2)  # ✅ log₂(8) = 3.0
calculate_logarithmic("exponential", 2)  # ✅ e^2 ≈ 7.389
```

---

### 6. calculate_hyperbolic
**Domain**: Hyperbolic Functions  
**Operations**: 3 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `value` (required): Input number

#### Operations
- `sinh` - Hyperbolic sine
- `cosh` - Hyperbolic cosine
- `tanh` - Hyperbolic tangent

#### Features
- **Overflow protection**: Handles large input values safely
- **High precision**: Accurate calculations for all ranges

#### Examples
```python
calculate_hyperbolic("sinh", 1)  # ✅ sinh(1) ≈ 1.175
calculate_hyperbolic("cosh", 0)  # ✅ cosh(0) = 1.0
calculate_hyperbolic("tanh", 2)  # ✅ tanh(2) ≈ 0.964
```

---

### 7. format_precision
**Domain**: Number Formatting & Rounding  
**Operations**: 5 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `value` (required): Input number
- `places`: Decimal places (for round operation only)

#### Operations
- `round` - Round to specified decimal places (requires places parameter)
- `floor` - Round down to nearest integer
- `ceiling` - Round up to nearest integer
- `truncate` - Remove decimal portion
- `absolute` - Absolute value

#### Examples
```python
format_precision("round", 3.14159, places=2)  # ✅ Round 3.14159 to 2 places = 3.14
format_precision("floor", 4.7)  # ✅ Floor of 4.7 = 4
format_precision("ceiling", 4.1)  # ✅ Ceiling of 4.1 = 5
format_precision("absolute", -15)  # ✅ |−15| = 15
```

---

### 8. analyze_numbers
**Domain**: Number Theory & Combinatorics  
**Operations**: 9 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `value` (required): Primary number
- `second_value`: Second number (for gcd, lcm, permutation, combination)

#### Operations

**Number Theory**
- `gcd` - Greatest Common Divisor (requires second_value)
- `lcm` - Least Common Multiple (requires second_value)
- `is_prime` - Prime number test
- `prime_factors` - Prime factorization
- `is_perfect_square` - Perfect square test

**Combinatorics**
- `factorial` - Factorial (n!)
- `permutation` - Permutations P(n,r) (requires second_value)
- `combination` - Combinations C(n,r) (requires second_value)
- `fibonacci` - Nth Fibonacci number

#### Examples
```python
# Number theory
analyze_numbers("gcd", 48, second_value=18)  # ✅ GCD(48, 18) = 6
analyze_numbers("is_prime", 17)  # ✅ 17 is prime
analyze_numbers("prime_factors", 60)  # ✅ Prime factors: 2², 3, 5

# Combinatorics
analyze_numbers("factorial", 5)  # ✅ 5! = 120
analyze_numbers("permutation", 10, second_value=3)  # ✅ P(10,3) = 720
analyze_numbers("fibonacci", 10)  # ✅ F(10) = 55
```

---

### 9. solve_equations
**Domain**: Equation Solving  
**Operations**: 2 equation types

#### Parameters
- `equation_type` (required): "quadratic" or "linear"
- `a`: Coefficient (x² for quadratic, x for linear)
- `b`: Coefficient (x for quadratic, constant for linear)
- `c`: Constant term (quadratic only)

#### Operations
- `quadratic` - Solve ax² + bx + c = 0
- `linear` - Solve ax + b = 0

#### Features
- **Complex solutions**: Handles negative discriminants
- **Comprehensive results**: Shows discriminant and solution type
- **Edge case handling**: Manages special cases

#### Examples
```python
# Quadratic equations
solve_equations("quadratic", a=1, b=-5, c=6)  # ✅ Solutions: x = 3.0, x = 2.0
solve_equations("quadratic", a=1, b=0, c=1)  # ✅ Complex solutions: x = ±i

# Linear equations
solve_equations("linear", a=2, b=-6)  # ✅ Solution: x = 3.0
```

---

### 10. calculate_geometry_2d
**Domain**: 2D Geometry  
**Operations**: 8 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `x1`, `y1`, `x2`, `y2`: Coordinates for distance/slope
- `radius`: Circle radius
- `length`, `width`: Rectangle dimensions
- `base`, `height`: Triangle dimensions
- `side_a`, `side_b`: Right triangle sides

#### Operations

**Point Operations**
- `distance` - Distance between two points
- `slope` - Slope between two points

**Circle Calculations**
- `circle_area` - Area of circle (πr²)
- `circle_circumference` - Circumference (2πr)

**Rectangle Calculations**
- `rectangle_area` - Area (length × width)
- `rectangle_perimeter` - Perimeter (2(l + w))

**Triangle Calculations**
- `triangle_area` - Area (½ × base × height)
- `right_triangle_area` - Area using two sides (½ × a × b)

#### Examples
```python
# Points
calculate_geometry_2d("distance", x1=0, y1=0, x2=3, y2=4)  # ✅ Distance = 5.0
calculate_geometry_2d("slope", x1=0, y1=0, x2=2, y2=4)  # ✅ Slope = 2.0

# Shapes
calculate_geometry_2d("circle_area", radius=5)  # ✅ Area = 78.54
calculate_geometry_2d("rectangle_perimeter", length=4, width=3)  # ✅ Perimeter = 14.0
```

---

### 11. calculate_geometry_3d
**Domain**: 3D Geometry & Vector Operations  
**Operations**: 14 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `x1`, `y1`, `z1`, `x2`, `y2`, `z2`: 3D coordinates
- `x`, `y`, `z`: Single vector coordinates
- `radius`: Sphere/cylinder/cone radius
- `height`: Cylinder/cone/prism height
- `length`, `width`: Rectangular prism dimensions

#### Operations

**3D Point Operations**
- `distance_3d` - Distance between 3D points
- `midpoint_3d` - Midpoint between 3D points

**Vector Operations**
- `vector_magnitude` - Vector magnitude/length
- `vector_dot_product` - Dot product of vectors
- `vector_cross_product` - Cross product of vectors
- `vector_angle` - Angle between vectors

**3D Shape Volumes**
- `sphere_volume` - Volume (4/3 × π × r³)
- `cylinder_volume` - Volume (π × r² × h)
- `cone_volume` - Volume (1/3 × π × r² × h)
- `rectangular_prism_volume` - Volume (l × w × h)

**3D Shape Surface Areas**
- `sphere_surface_area` - Surface area (4 × π × r²)
- `cylinder_surface_area` - Surface area (2πr(r + h))
- `cone_surface_area` - Surface area (π × r × (r + s))
- `rectangular_prism_surface_area` - Surface area (2(lw + lh + wh))

#### Examples
```python
# 3D points
calculate_geometry_3d("distance_3d", x1=0, y1=0, z1=0, x2=1, y2=1, z2=1)  # ✅ Distance = 1.732

# Vectors
calculate_geometry_3d("vector_magnitude", x=3, y=4, z=5)  # ✅ Magnitude = 7.071
calculate_geometry_3d("vector_dot_product", x1=1, y1=2, z1=3, x2=4, y2=5, z2=6)  # ✅ Dot product = 32

# 3D shapes
calculate_geometry_3d("sphere_volume", radius=3)  # ✅ Volume = 113.097
calculate_geometry_3d("cylinder_surface_area", radius=2, height=5)  # ✅ Surface area = 87.965
```

---

### 12. manipulate_matrices
**Domain**: Matrix Operations & Linear Algebra  
**Operations**: 4 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `matrix1`: First matrix (JSON string or list)
- `matrix2`: Second matrix (JSON string or list)
- `matrix`: Single matrix (JSON string or list)

#### Matrix Input Format
Matrices can be provided as:
- JSON string: `"[[1,2],[3,4]]"`
- Python list: `[[1,2],[3,4]]`

#### Operations
- `add` - Matrix addition (requires matrix1, matrix2)
- `multiply` - Matrix multiplication (requires matrix1, matrix2)
- `determinant` - Determinant calculation (requires matrix)
- `transpose` - Matrix transpose (requires matrix)

#### Features
- **Dimension validation**: Ensures compatible matrix dimensions
- **Format flexibility**: Accepts JSON strings or Python lists
- **Comprehensive error handling**: Clear error messages for invalid operations

#### Examples
```python
# Matrix operations
manipulate_matrices("add", matrix1="[[1,2],[3,4]]", matrix2="[[5,6],[7,8]]")
# ✅ Result: [[6,8],[10,12]]

manipulate_matrices("multiply", matrix1="[[1,2],[3,4]]", matrix2="[[5,6],[7,8]]")
# ✅ Result: [[19,22],[43,50]]

manipulate_matrices("determinant", matrix="[[1,2],[3,4]]")  # ✅ Determinant = -2.0

manipulate_matrices("transpose", matrix="[[1,2,3],[4,5,6]]")
# ✅ Transpose: [[1,4],[2,5],[3,6]]
```

---

### 13. financial_calculations
**Domain**: Financial & Business Mathematics  
**Operations**: 11 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `principal`: Initial amount
- `rate`: Interest rate (decimal, e.g., 0.05 for 5%)
- `time`: Time period (years)
- `compounds_per_year`: Compounding frequency
- Additional parameters specific to each operation

#### Operations

**Interest Calculations**
- `simple_interest` - Simple interest calculation
- `compound_interest` - Compound interest calculation
- `present_value` - Present value calculation
- `future_value` - Future value calculation

**Loan & Investment Analysis**
- `loan_payment` - Monthly loan payment
- `mortgage_payment` - Mortgage payment calculation
- `roi` - Return on investment
- `net_present_value` - NPV with cash flow analysis

**Business Calculations**
- `straight_line_depreciation` - Asset depreciation
- `declining_balance_depreciation` - Accelerated depreciation
- `break_even_point` - Break-even analysis

#### Examples
```python
# Interest calculations
financial_calculations("compound_interest", principal=1000, rate=0.05, time=3, compounds_per_year=12)
# ✅ Final amount: $1,161.62, Interest earned: $161.62

# Loan analysis
financial_calculations("loan_payment", principal=200000, rate=0.04, time=30)
# ✅ Monthly payment: $954.83

# Investment analysis
financial_calculations("roi", initial_investment=1000, final_value=1200)
# ✅ ROI: 20.00%
```

---

### 14. computer_science_tools
**Domain**: Programming & Computer Science  
**Operations**: 12 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `value`: Integer value for conversions/operations
- `text`: String for hash/character operations
- `from_base`, `to_base`: Base conversion parameters
- `algorithm`: Algorithm name for complexity analysis
- Additional parameters specific to operations

#### Operations

**Base Conversions**
- `base_conversion` - Convert between binary, octal, decimal, hexadecimal

**Hash Functions**
- `hash_function` - MD5, SHA1, SHA256 hashing

**Algorithm Analysis**
- `big_o_analysis` - Time complexity analysis for common algorithms

**Bitwise Operations**
- `bitwise_and`, `bitwise_or`, `bitwise_xor`, `bitwise_not`
- `bit_shift_left`, `bit_shift_right`

**Character Operations**
- `ascii_to_char` - ASCII code to character
- `char_to_ascii` - Character to ASCII code

**Data Analysis**
- `data_size` - Calculate data type sizes

#### Examples
```python
# Base conversion
computer_science_tools("base_conversion", value=255, from_base=10, to_base=16)
# ✅ 255 (decimal) = FF (hexadecimal)

# Hash functions
computer_science_tools("hash_function", text="Hello World", hash_algorithm="sha256")
# ✅ SHA256: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

# Algorithm analysis
computer_science_tools("big_o_analysis", algorithm="bubble_sort", input_size=1000)
# ✅ Bubble Sort: O(n²) complexity, ~1,000,000 operations for input size 1000

# Bitwise operations
computer_science_tools("bitwise_and", operand1=12, operand2=10)  # ✅ 12 & 10 = 8
```

---

### 15. data_analysis
**Domain**: Advanced Statistical Analysis  
**Operations**: 10 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `data`: JSON array of numerical data
- `data2`: Second dataset for correlation
- `value`, `mean`, `std_dev`: For z-score calculations
- `confidence_level`: For confidence intervals
- `method`: Analysis method type

#### Operations

**Distribution Analysis**
- `z_score` - Z-score calculation
- `standardize_data` - Data standardization
- `skewness` - Distribution skewness
- `kurtosis` - Distribution kurtosis

**Correlation & Relationships**
- `correlation` - Pearson/Spearman correlation
- `coefficient_variation` - Coefficient of variation

**Quartile Analysis**
- `quartiles` - Q1, Q2, Q3 quartiles
- `iqr_analysis` - Interquartile range analysis

**Advanced Analysis**
- `outliers` - Outlier detection using IQR method
- `confidence_interval` - Confidence interval calculation

#### Examples
```python
# Distribution analysis
data_analysis("z_score", value=85, mean=75, std_dev=10)  # ✅ Z-score = 1.0

# Correlation analysis
data_analysis("correlation", data="[1,2,3,4,5]", data2="[2,4,6,8,10]", method="pearson")
# ✅ Pearson correlation = 1.0 (perfect positive correlation)

# Quartile analysis
data_analysis("quartiles", data="[1,2,3,4,5,6,7,8,9,10]")
# ✅ Q1: 3.0, Q2: 5.5, Q3: 8.0

# Outlier detection
data_analysis("outliers", data="[1,2,3,4,5,100]")  # ✅ Outliers detected: [100]
```

---

### 16. utility_functions
**Domain**: System Utilities & Help  
**Operations**: 5 functions consolidated

#### Parameters
- `operation` (required): Operation type
- `name`: Constant/operation name
- `value`: Numeric value for operations
- `operation_type`: Help category type

#### Operations
- `mathematical_constants` - Access 12+ mathematical constants
- `validate_input` - Validate numeric inputs
- `operation_help` - Get help for specific operation types
- `list_operations` - List all available SharkMath operations
- `format_number` - Advanced number formatting

#### Mathematical Constants Available
- `pi` (π), `e`, `tau` (2π), `phi` (golden ratio)
- `euler_gamma`, `sqrt_2`, `sqrt_3`, `ln_2`, `ln_10`
- `avogadro`, `planck`, `light_speed`, `gravitational`

#### Examples
```python
# Mathematical constants
utility_functions("mathematical_constants", name="pi")  # ✅ π = 3.141592653589793
utility_functions("mathematical_constants")  # ✅ Lists all constants

# Input validation
utility_functions("validate_input", value=42.5)  # ✅ Input value 42.5 is valid

# Help system
utility_functions("operation_help", operation_type="arithmetic")
# ✅ Arithmetic operations help with usage examples

# Number formatting
utility_functions("format_number", value=1234567.89)
# ✅ Multiple format representations (scientific, engineering, etc.)
```

---

## Error Handling

All SharkMath tools follow consistent error handling patterns:

### Success Format
```
✅ [Operation description] = [result]
```

### Error Format
```
❌ [Error type]: [Detailed error message]
```

### Common Error Types
- **Value errors**: Invalid input parameters
- **Domain errors**: Mathematical domain violations
- **Division errors**: Division by zero
- **Overflow errors**: Results too large
- **Timeout errors**: Expression evaluation timeouts
- **Format errors**: Invalid data formats

## Input Validation

### Numeric Validation
- Type checking for numeric parameters
- NaN and infinity detection
- Range validation for domain-specific functions
- Precision and overflow protection

### String Validation  
- Expression syntax validation
- Matrix format validation
- Unit name validation
- Algorithm name validation

### Security Features
- Expression complexity limits
- Function whitelist validation
- Timeout protection
- Pattern-based security checks

## Performance Considerations

### Optimization Features
- Parameter-based routing for efficient function calls
- Consolidated tool registration reduces MCP overhead
- Input validation prevents unnecessary calculations
- Timeout protection prevents resource exhaustion

### Scalability
- Stateless operation design
- No persistent data storage
- Thread-safe implementations
- Memory-efficient algorithms

## Integration Examples

### VS Code MCP Configuration
```json
{
  "mcpServers": {
    "sharkmath-mcp": {
      "command": "uv",
      "args": ["--directory", ".", "run", "sharkmath_server.py"],
      "cwd": "/path/to/SharkMath-MCP"
    }
  }
}
```

### Python Client Usage
```python
# Example MCP client integration
result = await mcp_client.call_tool("calculate_arithmetic", {
    "operation": "calculate",
    "expression": "sqrt(25) + sin(pi/2)"
})
print(result)  # ✅ sqrt(25) + sin(pi/2) = 6.0
```

## Best Practices

### Parameter Usage
1. Always provide the required `operation` parameter
2. Use appropriate parameter names for each operation
3. Follow input format specifications (especially for matrices and data arrays)
4. Set reasonable precision and timeout values for complex calculations

### Error Handling
1. Check for ❌ prefix in results to detect errors
2. Validate inputs before making tool calls
3. Handle domain-specific errors (e.g., negative square roots)
4. Consider timeout settings for complex expressions

### Performance
1. Use appropriate precision settings to balance accuracy and speed
2. Break complex calculations into simpler operations when possible
3. Validate inputs client-side when practical
4. Use specific operations rather than generic calculation when available

## Troubleshooting

### Common Issues

**Expression Evaluation Errors**
- Check for balanced parentheses
- Verify function names are supported
- Ensure numeric values are valid
- Consider expression complexity limits

**Domain Errors**
- Verify input ranges for trigonometric functions
- Check for positive values in logarithmic functions
- Ensure proper matrix dimensions for operations

**Format Errors**
- Use proper JSON format for matrices and data arrays
- Check unit names for conversions
- Verify parameter names match operation requirements

### Support Resources
- Tool-specific error messages provide detailed guidance
- Use `utility_functions("operation_help")` for operation-specific help
- Check `utility_functions("list_operations")` for available functions
- Review domain-specific documentation for parameter requirements

---

*This documentation covers all tools and mathematical operations available in SharkMath MCP. For additional support or feature requests, please refer to the project repository.*
