# SharkMath MCP Server - Expected Test Results

## Overview
This document contains the expected results for all mathematical test prompts defined in `mcp_tests.md`. These results serve as the ground truth for validating AI agent responses using the SharkMath MCP server.

**Note**: The server uses 15 consolidated tools with parameter-based routing. All 70+ original mathematical functions have been consolidated into these tools.

**Enhancement Updates (July 20, 2025):**
- Added test cases ARITH_007-ARITH_011 for Enhanced Character Validation and Exponentiation Support features
- Exponentiation support enables `^` operator (e.g., `2^8` = 256)
- Enhanced character validation allows mathematical expressions with letters while blocking dangerous characters
- New error handling demonstrates improved validation messages for invalid characters

## Expected Results by Test Category

### 1. Basic Arithmetic Operations (calculate_arithmetic tool)

#### Test ARITH_001: Simple Addition
- **Input**: 47 + 293
- **Expected Result**: 340
- **MCP Tool**: `calculate_arithmetic(operation='add', a=47, b=293)`
- **Expected Response Format**: "✅ 47 + 293 = 340"

#### Test ARITH_002: Subtraction with Negative Result  
- **Input**: 125 - 347
- **Expected Result**: -222
- **MCP Tool**: `calculate_arithmetic(operation='subtract', a=125, b=347)`
- **Expected Response Format**: "✅ 125 - 347 = -222"

#### Test ARITH_003: Multiplication of Decimals
- **Input**: 12.5 × 8.4
- **Expected Result**: 105.0
- **MCP Tool**: `calculate_arithmetic(operation='multiply', a=12.5, b=8.4)`
- **Expected Response Format**: "✅ 12.5 × 8.4 = 105.0"

#### Test ARITH_004: Division with Remainder
- **Input**: 157 ÷ 23
- **Expected Result**: 6.826... (approximately 6.83)
- **MCP Tool**: `calculate_arithmetic(operation='divide', a=157, b=23)`
- **Expected Response Format**: "✅ 157 ÷ 23 ≈ 6.83"

#### Test ARITH_005: Division by Zero (Error Handling)
- **Input**: 50 ÷ 0
- **Expected Result**: Error message about division by zero
- **MCP Tool**: `calculate_arithmetic(operation='divide', a=50, b=0)`
- **Expected Response Format**: "❌ Error: Cannot divide by zero"

#### Test ARITH_006: Complex Expression
- **Input**: (15 + 3) * 4 - 8 / 2
- **Expected Result**: 68
- **MCP Tool**: `calculate_arithmetic(operation='calculate', expression="(15 + 3) * 4 - 8 / 2")`
- **Expected Response Format**: "✅ (15 + 3) × 4 - 8 ÷ 2 = 68"

#### Test ARITH_007: Exponentiation with ^ Operator
- **Input**: 2^8
- **Expected Result**: 256
- **MCP Tool**: `calculate_arithmetic(operation='calculate', expression="2^8")`
- **Expected Response Format**: "✅ 2^8 = 256"

#### Test ARITH_008: Complex Expression with Exponentiation
- **Input**: (3+2)^3 - 4*2^2
- **Expected Result**: 109 (5^3 - 4*4 = 125 - 16 = 109)
- **MCP Tool**: `calculate_arithmetic(operation='calculate', expression="(3+2)^3 - 4*2^2")`
- **Expected Response Format**: "✅ (3+2)^3 - 4*2^2 = 109"

#### Test ARITH_009: Nested Exponentiation
- **Input**: 2^3^2 (right-associative: 2^(3^2) = 2^9)
- **Expected Result**: 512
- **MCP Tool**: `calculate_arithmetic(operation='calculate', expression="2^3^2")`
- **Expected Response Format**: "✅ 2^3^2 = 512"

#### Test ARITH_010: Mixed Exponentiation Operators
- **Input**: 3^2 * 2**3
- **Expected Result**: 72 (9 * 8 = 72)
- **MCP Tool**: `calculate_arithmetic(operation='calculate', expression="3^2 * 2**3")`
- **Expected Response Format**: "✅ 3^2 * 2**3 = 72"

#### Test ARITH_011: Enhanced Character Validation Error
- **Input**: 2+3$invalid
- **Expected Result**: Error message about invalid characters
- **MCP Tool**: `calculate_arithmetic(operation='calculate', expression="2+3$invalid")`
- **Expected Response Format**: "❌ Value error: Expression contains invalid characters: ['$']. Supported: numbers, operators (+, -, *, /, **, ^), parentheses, letters, underscore, comma"

### 2. Power and Root Operations

#### Test POWER_001: Basic Exponentiation
- **Input**: 3^7
- **Expected Result**: 2187
- **MCP Tool**: `calculate_arithmetic(operation='power', base=3, exponent=7)`
- **Expected Response Format**: "✅ 3^7 = 2187"

#### Test POWER_002: Square Calculation
- **Input**: 23²
- **Expected Result**: 529
- **MCP Tool**: `calculate_arithmetic(operation='square', a=23)`
- **Expected Response Format**: "✅ 23² = 529"

#### Test POWER_003: Perfect Square Root
- **Input**: √169
- **Expected Result**: 13
- **MCP Tool**: `calculate_arithmetic(operation='square_root', a=169)`
- **Expected Response Format**: "✅ √169 = 13"

#### Test POWER_004: Cube Calculation
- **Input**: 12³
- **Expected Result**: 1728
- **MCP Tool**: `calculate_arithmetic(operation='cube', a=12)`
- **Expected Response Format**: "✅ 12³ = 1728"

#### Test POWER_005: Cube Root
- **Input**: ∛216
- **Expected Result**: 6
- **MCP Tool**: `calculate_arithmetic(operation='cube_root', a=216)`
- **Expected Response Format**: "✅ ∛216 = 6"

#### Test POWER_006: Fourth Root
- **Input**: ⁴√81
- **Expected Result**: 3
- **MCP Tool**: `calculate_arithmetic(operation='nth_root', a=81, n=4)`
- **Expected Response Format**: "✅ ⁴√81 = 3"

### 3. Trigonometric Functions (calculate_trigonometry tool)

#### Test TRIG_001: Sine of Common Angle
- **Input**: sin(π/2)
- **Expected Result**: 1.0
- **MCP Tool**: `calculate_trigonometry(operation='sin', angle=1.5708, angle_unit='radians')`
- **Expected Response Format**: "✅ sin(π/2) = 1.0"

#### Test TRIG_002: Cosine in Degrees
- **Input**: cos(60°)
- **Expected Result**: 0.5
- **MCP Tool**: `calculate_trigonometry(operation='cos', angle=60, angle_unit='degrees')`
- **Expected Response Format**: "✅ cos(60°) = 0.5"

#### Test TRIG_003: Tangent of Zero
- **Input**: tan(0)
- **Expected Result**: 0.0
- **MCP Tool**: `calculate_trigonometry(operation='tan', angle=0, angle_unit='radians')`
- **Expected Response Format**: "✅ tan(0) = 0.0"

#### Test TRIG_004: Inverse Sine
- **Input**: arcsin(0.5)
- **Expected Result**: 0.5236 radians (30° or π/6)
- **MCP Tool**: `calculate_trigonometry(operation='asin', value=0.5)`
- **Expected Response Format**: "✅ arcsin(0.5) = 0.5236 radians (30°)"

#### Test TRIG_005: Two-Argument Arctangent
- **Input**: atan2(4, 3)
- **Expected Result**: 0.9273 radians (53.13°)
- **MCP Tool**: `calculate_trigonometry(operation='atan2', y=4, x=3)`
- **Expected Response Format**: "✅ atan2(4, 3) = 0.9273 radians"

### 4. Logarithmic and Exponential Functions (calculate_logarithmic tool)

#### Test LOG_001: Natural Logarithm
- **Input**: ln(e²) = ln(7.389...)
- **Expected Result**: 2.0
- **MCP Tool**: `calculate_logarithmic(operation='natural_log', value=7.38905609893)`
- **Expected Response Format**: "✅ ln(e²) = 2.0"

#### Test LOG_002: Base-10 Logarithm
- **Input**: log₁₀(1000)
- **Expected Result**: 3.0
- **MCP Tool**: `calculate_logarithmic(operation='log_base_10', value=1000)`
- **Expected Response Format**: "✅ log₁₀(1000) = 3.0"

#### Test LOG_003: Custom Base Logarithm
- **Input**: log₂(32)
- **Expected Result**: 5.0
- **MCP Tool**: `calculate_logarithmic(operation='log_base', value=32, base=2)`
- **Expected Response Format**: "✅ log₂(32) = 5.0"

#### Test LOG_004: Exponential Function
- **Input**: e³
- **Expected Result**: 20.0855
- **MCP Tool**: `calculate_logarithmic(operation='exponential', value=3)`
- **Expected Response Format**: "✅ e³ ≈ 20.09"

### 5. Statistical Operations (calculate_statistics tool)

#### Test STATS_001: Mean of Dataset
- **Input**: [12, 15, 18, 22, 25, 30]
- **Expected Result**: 20.33
- **MCP Tool**: `calculate_statistics(operation='mean', numbers=[12,15,18,22,25,30])`
- **Expected Response Format**: "✅ Mean = 20.33"

#### Test STATS_002: Median of Odd Dataset
- **Input**: [7, 12, 3, 19, 25, 8, 14] → [3, 7, 8, 12, 14, 19, 25]
- **Expected Result**: 12
- **MCP Tool**: `calculate_statistics(operation='median', numbers=[7,12,3,19,25,8,14])`
- **Expected Response Format**: "✅ Median = 12"

#### Test STATS_003: Mode Identification
- **Input**: [1, 2, 3, 2, 4, 2, 5, 6, 2]
- **Expected Result**: 2 (appears 4 times)
- **MCP Tool**: `calculate_statistics(operation='mode', numbers=[1,2,3,2,4,2,5,6,2])`
- **Expected Response Format**: "✅ Mode = 2 (appears 4 times)"

#### Test STATS_004: Standard Deviation
- **Input**: [10, 12, 14, 16, 18]
- **Expected Result**: 3.162
- **MCP Tool**: `calculate_statistics(operation='standard_deviation', numbers=[10,12,14,16,18])`
- **Expected Response Format**: "✅ Standard Deviation = 3.16"

#### Test STATS_005: Range and Statistics
- **Input**: [25, 12, 38, 45, 7, 33]
- **Expected Result**: Min=7, Max=45, Range=38
- **MCP Tool**: `calculate_statistics(operation='range_stats', numbers=[25,12,38,45,7,33])`
- **Expected Response Format**: "✅ Min: 7, Max: 45, Range: 38"

### 9. 3D Geometry & Vector Operations Tests - Expected Results

#### Expected Result GEO3D_001
**Prompt**: Calculate the distance between points (0,0,0) and (3,4,5)
```
✅ Distance between (0, 0, 0) and (3, 4, 5) is 7.07 units
```

#### Expected Result GEO3D_002
**Prompt**: Find the midpoint between (-1, 2, -3) and (3, -2, 5)
```
✅ Midpoint between (-1, 2, -3) and (3, -2, 5) is (1.0, 0.0, 1.0)
```

#### Expected Result GEO3D_003
**Prompt**: Calculate the distance between [10,10,10] and [120,130,140]
```
✅ Distance between (10, 10, 10) and (120, 130, 140) is 208.33 units
```

#### Expected Result GEO3D_004
**Prompt**: Calculate the magnitude of vector [3, 4, 12]
```
✅ Vector magnitude of [3, 4, 12] is 13.0
```

#### Expected Result GEO3D_005
**Prompt**: Find the dot product of vectors [1, 2, 3] and [4, 5, 6]
```
✅ Dot product of [1, 2, 3] · [4, 5, 6] = 32
```

#### Expected Result GEO3D_006
**Prompt**: Calculate the cross product of vectors [2, 1, 0] and [1, 3, 2]
```
✅ Cross product of [2, 1, 0] × [1, 3, 2] = [2, -4, 5]
```

#### Expected Result GEO3D_007
**Prompt**: Find the angle between vectors [1, 0, 0] and [0, 1, 0] in degrees
```
✅ Angle between [1, 0, 0] and [0, 1, 0] is 90.0 degrees (1.57 radians)
```

#### Expected Result GEO3D_008
**Prompt**: Calculate the volume of a sphere with radius 5
```
✅ Volume of sphere with radius 5 is 523.60 cubic units
```

#### Expected Result GEO3D_009
**Prompt**: Find the surface area of a cylinder with radius 3 and height 8
```
✅ Surface area of cylinder (r=3, h=8) is 207.35 square units
```

#### Expected Result GEO3D_010
**Prompt**: Calculate the volume of a rectangular prism with dimensions 4×6×8
```
### 14. Complex Multi-Step Problems - Expected Results
```

#### Test MATRIX_001: Matrix Addition
- **Input**: [[1,2],[3,4]] + [[5,6],[7,8]]
- **Expected Result**: [[6,8],[10,12]]
- **MCP Tool**: `manipulate_matrices(operation='add', matrix1=[[1,2],[3,4]], matrix2=[[5,6],[7,8]])`
- **Expected Response Format**: "✅ Matrix sum = [[6,8],[10,12]]"

#### Test MATRIX_002: Matrix Multiplication
- **Input**: [[2,1],[3,4]] × [[1,0],[2,5]]
- **Expected Result**: [[4,5],[11,20]]
- **MCP Tool**: `manipulate_matrices(operation='multiply', matrix1=[[2,1],[3,4]], matrix2=[[1,0],[2,5]])`
- **Expected Response Format**: "✅ Matrix product = [[4,5],[11,20]]"

#### Test MATRIX_003: Matrix Determinant
- **Input**: det([[3,2],[1,4]])
- **Expected Result**: 10
- **MCP Tool**: `manipulate_matrices(operation='determinant', matrix1=[[3,2],[1,4]])`
- **Expected Response Format**: "✅ Determinant = 10"

#### Test MATRIX_004: Matrix Transpose
- **Input**: [[1,2,3],[4,5,6]]ᵀ
- **Expected Result**: [[1,4],[2,5],[3,6]]
- **MCP Tool**: `manipulate_matrices(operation='transpose', matrix1=[[1,2,3],[4,5,6]])`
- **Expected Response Format**: "✅ Transpose = [[1,4],[2,5],[3,6]]"

### 7. Unit Conversions (convert_units tool)

#### Test CONV_001: Temperature Conversion
- **Input**: 25°C to °F
- **Expected Result**: 77°F
- **MCP Tool**: `convert_units(from_unit='celsius', to_unit='fahrenheit', value=25)`
- **Expected Response Format**: "✅ 25°C = 77°F"

#### Test CONV_002: Distance Conversion
- **Input**: 50 km to miles
- **Expected Result**: 31.07 miles
- **MCP Tool**: `convert_units(from_unit='kilometers', to_unit='miles', value=50)`
- **Expected Response Format**: "✅ 50 km = 31.07 miles"

#### Test CONV_003: Weight Conversion
- **Input**: 150 lbs to kg
- **Expected Result**: 68.04 kg
- **MCP Tool**: `convert_units(from_unit='pounds', to_unit='kilograms', value=150)`
- **Expected Response Format**: "✅ 150 lbs = 68.04 kg"

#### Test CONV_004: Volume Conversion
- **Input**: 5 gallons to liters
- **Expected Result**: 18.93 liters
- **MCP Tool**: `convert_units(from_unit='gallons', to_unit='liters', value=5)`
- **Expected Response Format**: "✅ 5 gallons = 18.93 liters"

#### Test CONV_005: Angle Conversion
- **Input**: 90° to radians
- **Expected Result**: 1.5708 radians (π/2)
- **MCP Tool**: `convert_units(from_unit='degrees', to_unit='radians', value=90)`
- **Expected Response Format**: "✅ 90° = 1.5708 radians (π/2)"

### 8. Advanced Mathematical Operations

#### Test ADV_001: Quadratic Equation
- **Input**: x² - 5x + 6 = 0
- **Expected Result**: x = 2, x = 3
- **MCP Tool**: `solve_equations(equation_type='quadratic', a=1, b=-5, c=6)`
- **Expected Response Format**: "✅ Solutions: x₁ = 2, x₂ = 3"

#### Test ADV_002: Distance Between Points
- **Input**: Distance from (3,4) to (7,1)
- **Expected Result**: 5.0 units
- **MCP Tool**: `calculate_geometry_2d(operation='distance', x1=3, y1=4, x2=7, y2=1)`
- **Expected Response Format**: "✅ Distance = 5.0 units"

#### Test ADV_003: Slope Calculation
- **Input**: Slope through (2,3) and (6,11)
- **Expected Result**: 2.0
- **MCP Tool**: `calculate_geometry_2d(operation='slope', x1=2, y1=3, x2=6, y2=11)`
- **Expected Response Format**: "✅ Slope = 2.0"

#### Test ADV_004: Compound Interest
- **Input**: $1000, 5% annual, 3 years, annually compounded
- **Expected Result**: $1157.63
- **MCP Tool**: `financial_calculations(operation='compound_interest', principal=1000, rate=0.05, time=3, compounds_per_year=1)`
- **Expected Response Format**: "✅ Final amount: $1157.63"

### 9. Combinatorics and Number Theory (analyze_numbers tool)

#### Test COMB_001: Factorial
- **Input**: 8!
- **Expected Result**: 40320
- **MCP Tool**: `analyze_numbers(operation='factorial', value=8)`
- **Expected Response Format**: "✅ 8! = 40320"

#### Test COMB_002: Permutation
- **Input**: P(5,3) = 5!/(5-3)!
- **Expected Result**: 60
- **MCP Tool**: `analyze_numbers(operation='permutation', value=5, second_value=3)`
- **Expected Response Format**: "✅ P(5,3) = 60"

#### Test COMB_003: Combination
- **Input**: C(10,4) = 10!/(4!×6!)
- **Expected Result**: 210
- **MCP Tool**: `analyze_numbers(operation='combination', value=10, second_value=4)`
- **Expected Response Format**: "✅ C(10,4) = 210"

#### Test COMB_004: Fibonacci Number
- **Input**: 12th Fibonacci number
- **Expected Result**: 144 (sequence: 0,1,1,2,3,5,8,13,21,34,55,89,144)
- **MCP Tool**: `analyze_numbers(operation='fibonacci', value=12)`
- **Expected Response Format**: "✅ F₁₂ = 144"

#### Test NUM_001: Prime Check
- **Input**: Is 97 prime?
- **Expected Result**: Yes, 97 is prime
- **MCP Tool**: `analyze_numbers(operation='is_prime', value=97)`
- **Expected Response Format**: "✅ 97 is prime"

#### Test NUM_002: GCD Calculation
- **Input**: GCD(48, 18)
- **Expected Result**: 6
- **MCP Tool**: `analyze_numbers(operation='gcd', value=48, second_value=18)`
- **Expected Response Format**: "✅ GCD(48, 18) = 6"

### 10. Precision and Rounding Operations (format_precision tool)

#### Test PREC_001: Decimal Rounding
- **Input**: Round 3.14159 to 3 decimal places
- **Expected Result**: 3.142
- **MCP Tool**: `format_precision(operation='round', value=3.14159, places=3)`
- **Expected Response Format**: "✅ 3.14159 rounded to 3 decimal places = 3.142"

#### Test PREC_002: Floor Function
- **Input**: floor(-2.7)
- **Expected Result**: -3
- **MCP Tool**: `format_precision(operation='floor', value=-2.7)`
- **Expected Response Format**: "✅ floor(-2.7) = -3"

#### Test PREC_003: Ceiling Function
- **Input**: ceiling(4.1)
- **Expected Result**: 5
- **MCP Tool**: `format_precision(operation='ceiling', value=4.1)`
- **Expected Response Format**: "✅ ceiling(4.1) = 5"

#### Test PREC_004: Absolute Value
- **Input**: |−15.8|
- **Expected Result**: 15.8
- **MCP Tool**: `format_precision(operation='absolute', value=-15.8)`
- **Expected Response Format**: "✅ |−15.8| = 15.8"

### 11. Hyperbolic Functions (calculate_hyperbolic tool)

#### Test HYP_001: Hyperbolic Sine
- **Input**: sinh(2)
- **Expected Result**: 3.626
- **MCP Tool**: `calculate_hyperbolic(operation='sinh', value=2)`
- **Expected Response Format**: "✅ sinh(2) = 3.63"

#### Test HYP_002: Hyperbolic Cosine
- **Input**: cosh(0)
- **Expected Result**: 1.0
- **MCP Tool**: `calculate_hyperbolic(operation='cosh', value=0)`
- **Expected Response Format**: "✅ cosh(0) = 1.0"

#### Test HYP_003: Hyperbolic Tangent
- **Input**: tanh(1)
- **Expected Result**: 0.762
- **MCP Tool**: `calculate_hyperbolic(operation='tanh', value=1)`
- **Expected Response Format**: "✅ tanh(1) = 0.76"

### 12. Complex Multi-Step Problems

#### Test COMPLEX_001: Engineering Problem
- **Input**: Tank radius=5m, height=3m. Find area, volume, convert to gallons.
- **Expected Results**: 
  - Area = π×5² = 78.54 m²
  - Volume = 78.54×3 = 235.62 m³
  - Volume = 235.62×1000 = 235,620 liters = 62,257 gallons
- **MCP Tools**: `calculate_arithmetic(operation='power', a=5, b=2)`, `calculate_arithmetic(operation='multiply', a=78.54, b=3.14159)`, `calculate_arithmetic(operation='multiply', a=235.62, b=3)`, `convert_units(from_unit='liters', to_unit='gallons', value=235620)`
- **Expected Response**: "✅ Area: 78.54 m², Volume: 235.62 m³ (62,257 gallons)"

#### Test COMPLEX_002: Financial Analysis
- **Input**: $5000, 4% annual, quarterly compounding, 10 years
- **Expected Results**:
  - Final amount = $7,430.25
  - Increase = $2,430.25
  - Percentage increase = 48.61%
- **MCP Tools**: `financial_calculations(operation='compound_interest', principal=5000, rate=0.04, time=10, compounds_per_year=4)`, `calculate_arithmetic(operation='subtract', a=7430.25, b=5000)`, `calculate_arithmetic(operation='divide', a=2430.25, b=5000)`, `calculate_arithmetic(operation='multiply', a=0.4861, b=100)`
- **Expected Response**: "✅ Final: $7,430.25, Increase: $2,430.25 (48.61%)"

#### Test COMPLEX_003: Statistical Analysis
- **Input**: [23, 45, 67, 34, 56, 78, 12, 89, 45, 56]
- **Expected Results**:
  - Mean = 50.5
  - Median = 50.5
  - Mode = 45, 56 (both appear twice)
  - Standard deviation = 22.85
  - Values within 1 std dev: 34, 45, 56, 67, 45, 56 (27.65 to 73.35 range)
- **MCP Tools**: `calculate_statistics`, `calculate_arithmetic`, `format_precision`
- **Expected Response**: "✅ Mean: 50.5, Median: 50.5, Mode: 45&56, StdDev: 22.85, Within 1σ: 6 values"

#### Test COMPLEX_004: Geometry and Trigonometry
- **Input**: Right triangle, leg₁=3, hypotenuse=5, find leg₂ and angles
- **Expected Results**:
  - leg₂ = √(5²-3²) = √16 = 4
  - angle₁ = arcsin(3/5) = 36.87°
  - angle₂ = arcsin(4/5) = 53.13°
  - angle₃ = 90°
- **MCP Tools**: `calculate_arithmetic(operation='power', a=5, b=2)`, `calculate_arithmetic(operation='power', a=3, b=2)`, `calculate_arithmetic(operation='subtract', a=25, b=9)`, `calculate_arithmetic(operation='square_root', a=16)`, `calculate_arithmetic(operation='divide', a=3, b=5)`, `calculate_trigonometry(operation='asin', value=0.6)`, `convert_units(from_unit='radians', to_unit='degrees')`
- **Expected Response**: "✅ Other leg: 4, Angles: 36.87°, 53.13°, 90°"

#### Test COMPLEX_005: Matrix Operations Chain
- **Input**: A=[[2,3],[1,4]], B=[[1,2],[3,1]], find A+B, det(A+B), check perfect square
- **Expected Results**:
  - A+B = [[3,5],[4,5]]
  - det(A+B) = 3×5 - 5×4 = 15 - 20 = -5
  - |-5| = 5, √5 ≈ 2.236 (not perfect square)
- **MCP Tools**: `manipulate_matrices(operation='add', matrix1=[[2,3],[1,4]], matrix2=[[1,2],[3,1]])`, `manipulate_matrices(operation='determinant', matrix1=[[3,5],[4,5]])`, `format_precision(operation='absolute', value=-5)`, `analyze_numbers(operation='is_perfect_square', value=5)`
- **Expected Response**: "✅ A+B=[[3,5],[4,5]], det=-5, |det|=5 (not perfect square)"

#### Test COMPLEX_006: 3D Vector Analysis
- **Input**: vectors u=[2,3,6] and v=[1,4,2], calculate dot product, cross product, angle between them, and magnitude of cross product
- **Expected Results**:
  - dot product = 2×1 + 3×4 + 6×2 = 2 + 12 + 12 = 26
  - cross product = [3×2-6×4, 6×1-2×2, 2×4-3×1] = [6-24, 6-4, 8-3] = [-18, 2, 5]
  - angle = arccos(26/(7×√21)) = arccos(0.79) = 41.63°
  - magnitude of cross product = √((-18)²+2²+5²) = √(324+4+25) = √353 = 18.68
- **MCP Tools**: `calculate_geometry_3d(operation='vector_dot_product')`, `calculate_geometry_3d(operation='vector_cross_product')`, `calculate_geometry_3d(operation='vector_angle')`, `calculate_geometry_3d(operation='vector_magnitude')`
- **Expected Response**: "✅ Dot product: 26, Cross product: [-18, 2, 5], Angle: 41.63°, Cross magnitude: 18.68"

## Validation Criteria

### Accuracy Requirements
- **Numerical Results**: Must match expected values within 0.01 tolerance
- **Integer Results**: Must be exact matches
- **Error Messages**: Must contain appropriate error indicators

### Enhanced Feature Validation
- **Exponentiation Support**: Both `^` and `**` operators must produce identical results
- **Character Validation**: Letters and underscores should be allowed, dangerous characters ($, @, #, %) should be rejected
- **Preprocessing**: `^` operator must be correctly converted to `**` before evaluation
- **Error Messages**: Enhanced validation should provide clear feedback about which characters are invalid

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
- **Consolidated Tools**: All tests use the 15 consolidated tools with parameter-based routing
- **Parameter Validation**: Tools should validate operation names and required parameters

## Complete List of Consolidated Tools

The SharkMath MCP server provides these 16 consolidated tools:

1. **`calculate_arithmetic`** - Basic arithmetic and power operations (add, subtract, multiply, divide, power, square, cube, square_root, cube_root, nth_root, calculate)
2. **`calculate_trigonometry`** - Trigonometric functions (sin, cos, tan, asin, acos, atan, atan2) with support for radians/degrees
3. **`calculate_statistics`** - Statistical operations (mean, median, mode, standard_deviation, variance, range_stats, percentile)
4. **`convert_units`** - Unit conversions (80+ conversion types including temperature, length, weight, volume, time, energy, etc.)
5. **`calculate_logarithmic`** - Logarithmic and exponential functions (natural_log, log_base_10, log_base, exponential)
6. **`calculate_hyperbolic`** - Hyperbolic functions (sinh, cosh, tanh)
7. **`format_precision`** - Precision and rounding operations (round, floor, ceiling, truncate, absolute)
8. **`analyze_numbers`** - Number theory and combinatorics (factorial, gcd, lcm, is_prime, prime_factors, is_perfect_square, fibonacci, permutation, combination)
9. **`solve_equations`** - Equation solvers (quadratic, linear, compound_interest, simple_interest)
10. **`calculate_geometry_2d`** - 2D geometry calculations (distance, slope, circle_area, circle_circumference, triangle_area, rectangle_area, rectangle_perimeter, midpoint)
11. **`calculate_geometry_3d`** - 3D geometry and vector operations (distance_3d, midpoint_3d, vector_magnitude, vector_dot_product, vector_cross_product, vector_angle, sphere_volume, cylinder_volume, cone_volume, rectangular_prism_volume, sphere_surface_area, cylinder_surface_area, cone_surface_area, rectangular_prism_surface_area)
12. **`manipulate_matrices`** - Matrix operations (add, multiply, determinant, transpose)
13. **`financial_calculations`** - Financial and business calculations (compound_interest, simple_interest, present_value, future_value, loan_payment, roi, depreciation, mortgage_payment, break_even, npv, irr)
14. **`computer_science_tools`** - Computer science functions (binary_to_decimal, decimal_to_binary, hex_to_decimal, decimal_to_hex, hash_md5, hash_sha256, big_o_analysis, data_size_convert, ascii_to_char, char_to_ascii, bitwise_and, bitwise_or)
15. **`data_analysis`** - Advanced data analysis functions (z_score, correlation, quartiles, skewness, kurtosis, coefficient_of_variation, outliers_detection, confidence_interval, normalize_data, iqr_analysis)
16. **`utility_functions`** - Utility functions (help, get_constants, validate_input, list_operations, format_number)
