# SharkMath MCP Server - Expected Test Results

## Overview
This document contains the expected results for all mathematical test prompts defined in `mcp_tests.md`. These results serve as the ground truth for validating AI agent responses using the SharkMath MCP server.

## Expected Results by Test Category

### 1. Basic Arithmetic Operations

#### Test ARITH_001: Simple Addition
- **Input**: 47 + 293
- **Expected Result**: 340
- **MCP Tool**: `add(a=47, b=293)`
- **Expected Response Format**: "✅ 47 + 293 = 340"

#### Test ARITH_002: Subtraction with Negative Result  
- **Input**: 125 - 347
- **Expected Result**: -222
- **MCP Tool**: `subtract(a=125, b=347)`
- **Expected Response Format**: "✅ 125 - 347 = -222"

#### Test ARITH_003: Multiplication of Decimals
- **Input**: 12.5 × 8.4
- **Expected Result**: 105.0
- **MCP Tool**: `multiply(a=12.5, b=8.4)`
- **Expected Response Format**: "✅ 12.5 × 8.4 = 105.0"

#### Test ARITH_004: Division with Remainder
- **Input**: 157 ÷ 23
- **Expected Result**: 6.826... (approximately 6.83)
- **MCP Tool**: `divide(a=157, b=23)`
- **Expected Response Format**: "✅ 157 ÷ 23 ≈ 6.83"

#### Test ARITH_005: Division by Zero (Error Handling)
- **Input**: 50 ÷ 0
- **Expected Result**: Error message about division by zero
- **MCP Tool**: `divide(a=50, b=0)`
- **Expected Response Format**: "❌ Error: Cannot divide by zero"

#### Test ARITH_006: Complex Expression
- **Input**: (15 + 3) * 4 - 8 / 2
- **Expected Result**: 68
- **MCP Tool**: `calculate(expression="(15 + 3) * 4 - 8 / 2")`
- **Expected Response Format**: "✅ (15 + 3) × 4 - 8 ÷ 2 = 68"

### 2. Power and Root Operations

#### Test POWER_001: Basic Exponentiation
- **Input**: 3^7
- **Expected Result**: 2187
- **MCP Tool**: `power(base=3, exponent=7)`
- **Expected Response Format**: "✅ 3^7 = 2187"

#### Test POWER_002: Square Calculation
- **Input**: 23²
- **Expected Result**: 529
- **MCP Tool**: `square(n=23)`
- **Expected Response Format**: "✅ 23² = 529"

#### Test POWER_003: Perfect Square Root
- **Input**: √169
- **Expected Result**: 13
- **MCP Tool**: `square_root(n=169)`
- **Expected Response Format**: "✅ √169 = 13"

#### Test POWER_004: Cube Calculation
- **Input**: 12³
- **Expected Result**: 1728
- **MCP Tool**: `cube(n=12)`
- **Expected Response Format**: "✅ 12³ = 1728"

#### Test POWER_005: Cube Root
- **Input**: ∛216
- **Expected Result**: 6
- **MCP Tool**: `cube_root(n=216)`
- **Expected Response Format**: "✅ ∛216 = 6"

#### Test POWER_006: Fourth Root
- **Input**: ⁴√81
- **Expected Result**: 3
- **MCP Tool**: `nth_root(n=81, root=4)`
- **Expected Response Format**: "✅ ⁴√81 = 3"

### 3. Trigonometric Functions

#### Test TRIG_001: Sine of Common Angle
- **Input**: sin(π/2)
- **Expected Result**: 1.0
- **MCP Tool**: `sin(angle_radians=1.5708)` (π/2 ≈ 1.5708)
- **Expected Response Format**: "✅ sin(π/2) = 1.0"

#### Test TRIG_002: Cosine in Degrees
- **Input**: cos(60°)
- **Expected Result**: 0.5
- **MCP Tool**: `cos_degrees(angle_degrees=60)`
- **Expected Response Format**: "✅ cos(60°) = 0.5"

#### Test TRIG_003: Tangent of Zero
- **Input**: tan(0)
- **Expected Result**: 0.0
- **MCP Tool**: `tan(angle_radians=0)`
- **Expected Response Format**: "✅ tan(0) = 0.0"

#### Test TRIG_004: Inverse Sine
- **Input**: arcsin(0.5)
- **Expected Result**: 0.5236 radians (30° or π/6)
- **MCP Tool**: `asin(value=0.5)`
- **Expected Response Format**: "✅ arcsin(0.5) = 0.5236 radians (30°)"

#### Test TRIG_005: Two-Argument Arctangent
- **Input**: atan2(4, 3)
- **Expected Result**: 0.9273 radians (53.13°)
- **MCP Tool**: `atan2(y=4, x=3)`
- **Expected Response Format**: "✅ atan2(4, 3) = 0.9273 radians"

### 4. Logarithmic and Exponential Functions

#### Test LOG_001: Natural Logarithm
- **Input**: ln(e²) = ln(7.389...)
- **Expected Result**: 2.0
- **MCP Tool**: `natural_log(n=7.38905609893)`
- **Expected Response Format**: "✅ ln(e²) = 2.0"

#### Test LOG_002: Base-10 Logarithm
- **Input**: log₁₀(1000)
- **Expected Result**: 3.0
- **MCP Tool**: `log_base_10(n=1000)`
- **Expected Response Format**: "✅ log₁₀(1000) = 3.0"

#### Test LOG_003: Custom Base Logarithm
- **Input**: log₂(32)
- **Expected Result**: 5.0
- **MCP Tool**: `log_base(n=32, base=2)`
- **Expected Response Format**: "✅ log₂(32) = 5.0"

#### Test LOG_004: Exponential Function
- **Input**: e³
- **Expected Result**: 20.0855
- **MCP Tool**: `exponential(n=3)`
- **Expected Response Format**: "✅ e³ ≈ 20.09"

### 5. Statistical Operations

#### Test STATS_001: Mean of Dataset
- **Input**: [12, 15, 18, 22, 25, 30]
- **Expected Result**: 20.33
- **MCP Tool**: `mean(numbers="12,15,18,22,25,30")`
- **Expected Response Format**: "✅ Mean = 20.33"

#### Test STATS_002: Median of Odd Dataset
- **Input**: [7, 12, 3, 19, 25, 8, 14] → [3, 7, 8, 12, 14, 19, 25]
- **Expected Result**: 12
- **MCP Tool**: `median(numbers="7,12,3,19,25,8,14")`
- **Expected Response Format**: "✅ Median = 12"

#### Test STATS_003: Mode Identification
- **Input**: [1, 2, 3, 2, 4, 2, 5, 6, 2]
- **Expected Result**: 2 (appears 4 times)
- **MCP Tool**: `mode(numbers="1,2,3,2,4,2,5,6,2")`
- **Expected Response Format**: "✅ Mode = 2 (appears 4 times)"

#### Test STATS_004: Standard Deviation
- **Input**: [10, 12, 14, 16, 18]
- **Expected Result**: 3.162
- **MCP Tool**: `standard_deviation(numbers="10,12,14,16,18")`
- **Expected Response Format**: "✅ Standard Deviation = 3.16"

#### Test STATS_005: Range and Statistics
- **Input**: [25, 12, 38, 45, 7, 33]
- **Expected Result**: Min=7, Max=45, Range=38
- **MCP Tool**: `range_stats(numbers="25,12,38,45,7,33")`
- **Expected Response Format**: "✅ Min: 7, Max: 45, Range: 38"

### 6. Matrix Operations

#### Test MATRIX_001: Matrix Addition
- **Input**: [[1,2],[3,4]] + [[5,6],[7,8]]
- **Expected Result**: [[6,8],[10,12]]
- **MCP Tool**: `matrix_add(matrix1="[[1,2],[3,4]]", matrix2="[[5,6],[7,8]]")`
- **Expected Response Format**: "✅ Matrix sum = [[6,8],[10,12]]"

#### Test MATRIX_002: Matrix Multiplication
- **Input**: [[2,1],[3,4]] × [[1,0],[2,5]]
- **Expected Result**: [[4,5],[11,20]]
- **MCP Tool**: `matrix_multiply(matrix1="[[2,1],[3,4]]", matrix2="[[1,0],[2,5]]")`
- **Expected Response Format**: "✅ Matrix product = [[4,5],[11,20]]"

#### Test MATRIX_003: Matrix Determinant
- **Input**: det([[3,2],[1,4]])
- **Expected Result**: 10
- **MCP Tool**: `matrix_determinant(matrix="[[3,2],[1,4]]")`
- **Expected Response Format**: "✅ Determinant = 10"

#### Test MATRIX_004: Matrix Transpose
- **Input**: [[1,2,3],[4,5,6]]ᵀ
- **Expected Result**: [[1,4],[2,5],[3,6]]
- **MCP Tool**: `matrix_transpose(matrix="[[1,2,3],[4,5,6]]")`
- **Expected Response Format**: "✅ Transpose = [[1,4],[2,5],[3,6]]"

### 7. Unit Conversions

#### Test CONV_001: Temperature Conversion
- **Input**: 25°C to °F
- **Expected Result**: 77°F
- **MCP Tool**: `celsius_to_fahrenheit(celsius=25)`
- **Expected Response Format**: "✅ 25°C = 77°F"

#### Test CONV_002: Distance Conversion
- **Input**: 50 km to miles
- **Expected Result**: 31.07 miles
- **MCP Tool**: `kilometers_to_miles(kilometers=50)`
- **Expected Response Format**: "✅ 50 km = 31.07 miles"

#### Test CONV_003: Weight Conversion
- **Input**: 150 lbs to kg
- **Expected Result**: 68.04 kg
- **MCP Tool**: `pounds_to_kilograms(pounds=150)`
- **Expected Response Format**: "✅ 150 lbs = 68.04 kg"

#### Test CONV_004: Volume Conversion
- **Input**: 5 gallons to liters
- **Expected Result**: 18.93 liters
- **MCP Tool**: `gallons_to_liters(gallons=5)`
- **Expected Response Format**: "✅ 5 gallons = 18.93 liters"

#### Test CONV_005: Angle Conversion
- **Input**: 90° to radians
- **Expected Result**: 1.5708 radians (π/2)
- **MCP Tool**: `degrees_to_radians(degrees=90)`
- **Expected Response Format**: "✅ 90° = 1.5708 radians (π/2)"

### 8. Advanced Mathematical Operations

#### Test ADV_001: Quadratic Equation
- **Input**: x² - 5x + 6 = 0
- **Expected Result**: x = 2, x = 3
- **MCP Tool**: `solve_quadratic(a=1, b=-5, c=6)`
- **Expected Response Format**: "✅ Solutions: x₁ = 2, x₂ = 3"

#### Test ADV_002: Distance Between Points
- **Input**: Distance from (3,4) to (7,1)
- **Expected Result**: 5.0 units
- **MCP Tool**: `distance_2d(x1=3, y1=4, x2=7, y2=1)`
- **Expected Response Format**: "✅ Distance = 5.0 units"

#### Test ADV_003: Slope Calculation
- **Input**: Slope through (2,3) and (6,11)
- **Expected Result**: 2.0
- **MCP Tool**: `slope(x1=2, y1=3, x2=6, y2=11)`
- **Expected Response Format**: "✅ Slope = 2.0"

#### Test ADV_004: Compound Interest
- **Input**: $1000, 5% annual, 3 years, annually compounded
- **Expected Result**: $1157.63
- **MCP Tool**: `compound_interest(principal=1000, rate=0.05, time=3, compounds_per_year=1)`
- **Expected Response Format**: "✅ Final amount: $1157.63"

### 9. Combinatorics and Number Theory

#### Test COMB_001: Factorial
- **Input**: 8!
- **Expected Result**: 40320
- **MCP Tool**: `factorial(n=8)`
- **Expected Response Format**: "✅ 8! = 40320"

#### Test COMB_002: Permutation
- **Input**: P(5,3) = 5!/(5-3)!
- **Expected Result**: 60
- **MCP Tool**: `permutation(n=5, r=3)`
- **Expected Response Format**: "✅ P(5,3) = 60"

#### Test COMB_003: Combination
- **Input**: C(10,4) = 10!/(4!×6!)
- **Expected Result**: 210
- **MCP Tool**: `combination(n=10, r=4)`
- **Expected Response Format**: "✅ C(10,4) = 210"

#### Test COMB_004: Fibonacci Number
- **Input**: 12th Fibonacci number
- **Expected Result**: 144 (sequence: 0,1,1,2,3,5,8,13,21,34,55,89,144)
- **MCP Tool**: `fibonacci(n=12)`
- **Expected Response Format**: "✅ F₁₂ = 144"

#### Test NUM_001: Prime Check
- **Input**: Is 97 prime?
- **Expected Result**: Yes, 97 is prime
- **MCP Tool**: `is_prime(n=97)`
- **Expected Response Format**: "✅ 97 is prime"

#### Test NUM_002: GCD Calculation
- **Input**: GCD(48, 18)
- **Expected Result**: 6
- **MCP Tool**: `gcd(a=48, b=18)`
- **Expected Response Format**: "✅ GCD(48, 18) = 6"

### 10. Precision and Rounding Operations

#### Test PREC_001: Decimal Rounding
- **Input**: Round 3.14159 to 3 decimal places
- **Expected Result**: 3.142
- **MCP Tool**: `round_to_decimal(n=3.14159, places=3)`
- **Expected Response Format**: "✅ 3.14159 rounded to 3 decimal places = 3.142"

#### Test PREC_002: Floor Function
- **Input**: floor(-2.7)
- **Expected Result**: -3
- **MCP Tool**: `floor(n=-2.7)`
- **Expected Response Format**: "✅ floor(-2.7) = -3"

#### Test PREC_003: Ceiling Function
- **Input**: ceiling(4.1)
- **Expected Result**: 5
- **MCP Tool**: `ceiling(n=4.1)`
- **Expected Response Format**: "✅ ceiling(4.1) = 5"

#### Test PREC_004: Absolute Value
- **Input**: |−15.8|
- **Expected Result**: 15.8
- **MCP Tool**: `absolute(n=-15.8)`
- **Expected Response Format**: "✅ |−15.8| = 15.8"

### 11. Hyperbolic Functions

#### Test HYP_001: Hyperbolic Sine
- **Input**: sinh(2)
- **Expected Result**: 3.626
- **MCP Tool**: `sinh(x=2)`
- **Expected Response Format**: "✅ sinh(2) = 3.63"

#### Test HYP_002: Hyperbolic Cosine
- **Input**: cosh(0)
- **Expected Result**: 1.0
- **MCP Tool**: `cosh(x=0)`
- **Expected Response Format**: "✅ cosh(0) = 1.0"

#### Test HYP_003: Hyperbolic Tangent
- **Input**: tanh(1)
- **Expected Result**: 0.762
- **MCP Tool**: `tanh(x=1)`
- **Expected Response Format**: "✅ tanh(1) = 0.76"

### 12. Complex Multi-Step Problems

#### Test COMPLEX_001: Engineering Problem
- **Input**: Tank radius=5m, height=3m. Find area, volume, convert to gallons.
- **Expected Results**: 
  - Area = π×5² = 78.54 m²
  - Volume = 78.54×3 = 235.62 m³
  - Volume = 235.62×1000 = 235,620 liters = 62,257 gallons
- **MCP Tools**: `power(base=5, exponent=2)`, `multiply(a=78.54, b=3.14159)`, `multiply(a=235.62, b=3)`, `liters_to_gallons(liters=235620)`
- **Expected Response**: "✅ Area: 78.54 m², Volume: 235.62 m³ (62,257 gallons)"

#### Test COMPLEX_002: Financial Analysis
- **Input**: $5000, 4% annual, quarterly compounding, 10 years
- **Expected Results**:
  - Final amount = $7,430.25
  - Increase = $2,430.25
  - Percentage increase = 48.61%
- **MCP Tools**: `compound_interest(principal=5000, rate=0.04, time=10, compounds_per_year=4)`, `subtract(a=7430.25, b=5000)`, `divide(a=2430.25, b=5000)`, `multiply(a=0.4861, b=100)`
- **Expected Response**: "✅ Final: $7,430.25, Increase: $2,430.25 (48.61%)"

#### Test COMPLEX_003: Statistical Analysis
- **Input**: [23, 45, 67, 34, 56, 78, 12, 89, 45, 56]
- **Expected Results**:
  - Mean = 50.5
  - Median = 50.5
  - Mode = 45, 56 (both appear twice)
  - Standard deviation = 22.85
  - Values within 1 std dev: 34, 45, 56, 67, 45, 56 (27.65 to 73.35 range)
- **MCP Tools**: `mean`, `median`, `mode`, `standard_deviation`, multiple `subtract` and `absolute` calls
- **Expected Response**: "✅ Mean: 50.5, Median: 50.5, Mode: 45&56, StdDev: 22.85, Within 1σ: 6 values"

#### Test COMPLEX_004: Geometry and Trigonometry
- **Input**: Right triangle, leg₁=3, hypotenuse=5, find leg₂ and angles
- **Expected Results**:
  - leg₂ = √(5²-3²) = √16 = 4
  - angle₁ = arcsin(3/5) = 36.87°
  - angle₂ = arcsin(4/5) = 53.13°
  - angle₃ = 90°
- **MCP Tools**: `power(base=5, exponent=2)`, `power(base=3, exponent=2)`, `subtract(a=25, b=9)`, `square_root(n=16)`, `divide(a=3, b=5)`, `asin(value=0.6)`, `radians_to_degrees`
- **Expected Response**: "✅ Other leg: 4, Angles: 36.87°, 53.13°, 90°"

#### Test COMPLEX_005: Matrix Operations Chain
- **Input**: A=[[2,3],[1,4]], B=[[1,2],[3,1]], find A+B, det(A+B), check perfect square
- **Expected Results**:
  - A+B = [[3,5],[4,5]]
  - det(A+B) = 3×5 - 5×4 = 15 - 20 = -5
  - |-5| = 5, √5 ≈ 2.236 (not perfect square)
- **MCP Tools**: `matrix_add(matrix1="[[2,3],[1,4]]", matrix2="[[1,2],[3,1]]")`, `matrix_determinant(matrix="[[3,5],[4,5]]")`, `absolute(n=-5)`, `is_perfect_square(n=5)`
- **Expected Response**: "✅ A+B=[[3,5],[4,5]], det=-5, |det|=5 (not perfect square)"

## Validation Criteria

### Accuracy Requirements
- **Numerical Results**: Must match expected values within 0.01 tolerance
- **Integer Results**: Must be exact matches
- **Error Messages**: Must contain appropriate error indicators

### Response Format Standards
- **Success Indicator**: ✅ prefix for successful calculations
- **Error Indicator**: ❌ prefix for error conditions
- **Precision**: Round to appropriate significant figures (typically 2-4 decimal places)
- **Units**: Include proper units in conversions and measurements

### Tool Usage Validation
- **Primary Tool**: Agent must use the expected primary MCP tool
- **Multi-Step**: Complex problems may use additional supporting tools
- **Efficiency**: Agent should use the most direct tool path available

## Testing Notes

- **Floating Point**: Minor variations in decimal places are acceptable due to floating-point arithmetic
- **Alternative Methods**: Some problems may be solved using different valid tool combinations
- **Error Handling**: Invalid inputs should produce helpful error messages, not crashes
- **Edge Cases**: Special values (0, 1, -1, π, e) should be handled correctly
