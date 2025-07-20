# SharkMath Server Enhancement Tasks

## Current Implementation Status
✅ **Basic Arithmetic Operations**
- `add(a, b)` - Addition of two numbers
- `subtract(a, b)` - Subtraction (a - b)
- `multiply(a, b)` - Multiplication of two numbers
- `divide(a, b)` - Division with zero-division protection
- `calculate(expression)` - Safe evaluation of mathematical expressions

## Phase 0: Refactor Current Implementation (Priority Task)
✅ **Create `arithmetic.py`** - Move existing basic operations
✅ **Create `__init__.py`** - Initialize SharkMath as a Python package
✅ **Refactor `sharkmath_server.py`** - Convert to modular import structure
✅ **Test refactored server** - Ensure all existing functionality works
✅ **Update MCP configuration** - Verify VS Code integration still works

---

## File Structure and Modular Organization

### Proposed File Structure
```
SharkMath/
├── sharkmath_server.py          # Main MCP server with imports
├── arithmetic.py                # Basic arithmetic operations
├── power_operations.py          # Power and root functions
├── logarithmic.py              # Logarithmic and exponential functions
├── trigonometric.py            # Trig and inverse trig functions
├── hyperbolic.py               # Hyperbolic functions
├── statistics.py               # Statistical calculations
├── combinatorics.py            # Factorials, permutations, combinations
├── number_theory.py            # Prime numbers, GCD, LCM functions
├── precision.py                # Rounding and precision utilities
├── conversions.py              # Unit conversion functions
├── advanced_calc.py            # Quadratic solver, geometry, finance
├── matrix_operations.py        # Matrix calculations (advanced)
└── __init__.py                 # Package initialization
```

### Implementation Strategy
1. **Move existing functions** from `sharkmath_server.py` to `arithmetic.py`
2. **Update main server** to import and register tools from modules
3. **Each module** follows consistent error handling and naming patterns
4. **Maintain single MCP server** that aggregates all tools

### Main Server Pattern
```python
# sharkmath_server.py
from mcp.server.fastmcp import FastMCP
from . import arithmetic, power_operations, logarithmic
# ... import other modules

mcp = FastMCP("SharkMath Server")

# Register tools from each module
arithmetic.register_tools(mcp)
power_operations.register_tools(mcp)
logarithmic.register_tools(mcp)
# ... register other modules

if __name__ == "__main__":
    import asyncio
    asyncio.run(mcp.run())
```

### Module Pattern
```python
# Example: arithmetic.py
def register_tools(mcp):
    @mcp.tool()
    async def add(a: float, b: float) -> str:
        """Add two numbers together."""
        # ... implementation
    
    @mcp.tool()
    async def subtract(a: float, b: float) -> str:
        """Subtract the second number from the first number."""
        # ... implementation
```

---

## Phase 1: Power and Root Operations
**File: `power_operations.py`**
✅ **power(base, exponent)** - Calculate base raised to the power of exponent
✅ **square(n)** - Calculate n²
✅ **cube(n)** - Calculate n³
✅ **square_root(n)** - Calculate √n with negative number validation
✅ **cube_root(n)** - Calculate ∛n
✅ **nth_root(n, root)** - Calculate nth root of a number
🔲 **UPDATE DOCUMENTATION**: Add power/root functions to copilot-instructions.md
🔲 **PHASE 1 COMPLETE**: Mark when both implementation AND documentation are done

## Phase 2: Logarithmic Functions
**File: `logarithmic.py`**
✅ **natural_log(n)** - Calculate ln(n) with domain validation
✅ **log_base_10(n)** - Calculate log₁₀(n)
✅ **log_base(n, base)** - Calculate log_base(n) with custom base
✅ **exponential(n)** - Calculate e^n
✅ **Update copilot-instructions.md** - Add phase documentation after completion

## Phase 3: Trigonometric Functions
**File: `trigonometric.py`**
✅ **sin(angle_radians)** - Sine function
✅ **cos(angle_radians)** - Cosine function
✅ **tan(angle_radians)** - Tangent function with π/2 validation
✅ **sin_degrees(angle_degrees)** - Sine with degree input
✅ **cos_degrees(angle_degrees)** - Cosine with degree input
✅ **tan_degrees(angle_degrees)** - Tangent with degree input
🔲 **UPDATE DOCUMENTATION**: Add trigonometric functions to copilot-instructions.md
🔲 **PHASE 3 COMPLETE**: Mark when both implementation AND documentation are done

## Phase 4: Inverse Trigonometric Functions
**File: `trigonometric.py` (combined with Phase 3)**
✅ **asin(value)** - Arcsine with domain validation [-1, 1]
✅ **acos(value)** - Arccosine with domain validation [-1, 1]
✅ **atan(value)** - Arctangent
✅ **atan2(y, x)** - Two-argument arctangent
🔲 **UPDATE DOCUMENTATION**: Add inverse trig functions to copilot-instructions.md
🔲 **PHASE 4 COMPLETE**: Mark when both implementation AND documentation are done

## Phase 5: Hyperbolic Functions
**File: `hyperbolic.py`**
✅ **sinh(x)** - Hyperbolic sine
✅ **cosh(x)** - Hyperbolic cosine
✅ **tanh(x)** - Hyperbolic tangent
✅ **UPDATE DOCUMENTATION**: Add hyperbolic functions to copilot-instructions.md
✅ **PHASE 5 COMPLETE**: Mark when both implementation AND documentation are done

## Phase 6: Statistical Functions
**File: `statistics.py`**
✅ **mean(numbers)** - Calculate arithmetic mean of a list
✅ **median(numbers)** - Calculate median of a list
✅ **mode(numbers)** - Calculate mode of a list
✅ **standard_deviation(numbers)** - Calculate standard deviation
✅ **variance(numbers)** - Calculate variance
✅ **range_stats(numbers)** - Calculate min, max, and range
⚠️ **Update copilot-instructions.md** - Add phase documentation after completion

## Phase 7: Combinatorics and Factorials
**File: `combinatorics.py`**
✅ **factorial(n)** - Calculate n! with non-negative integer validation
✅ **permutation(n, r)** - Calculate P(n,r) = n!/(n-r)!
✅ **combination(n, r)** - Calculate C(n,r) = n!/(r!(n-r)!)
✅ **fibonacci(n)** - Calculate nth Fibonacci number
✅ **Update copilot-instructions.md** - Add phase documentation after completion

## Phase 8: Number Theory Functions
**File: `number_theory.py`**
✅ **gcd(a, b)** - Greatest common divisor
✅ **lcm(a, b)** - Least common multiple
✅ **is_prime(n)** - Check if number is prime
✅ **prime_factors(n)** - List prime factors of a number
✅ **is_perfect_square(n)** - Check if number is a perfect square
✅ **UPDATE DOCUMENTATION**: Add number theory functions to copilot-instructions.md
✅ **PHASE 8 COMPLETE**: Mark when both implementation AND documentation are done

## Phase 9: Rounding and Precision
**File: `precision.py`**
✅ **round_to_decimal(n, places)** - Round to specified decimal places
✅ **floor(n)** - Floor function (round down)
✅ **ceiling(n)** - Ceiling function (round up)
✅ **truncate(n)** - Truncate decimal part
✅ **absolute(n)** - Absolute value
⚠️ **Update copilot-instructions.md** - Add phase documentation after completion

## Phase 10: Unit Conversions
**File: `conversions.py`**
✅ **degrees_to_radians(degrees)** - Convert degrees to radians
✅ **radians_to_degrees(radians)** - Convert radians to degrees
✅ **celsius_to_fahrenheit(celsius)** - Temperature conversion
✅ **fahrenheit_to_celsius(fahrenheit)** - Temperature conversion
✅ **meters_to_feet(meters)** - Length conversion
✅ **feet_to_meters(feet)** - Length conversion
✅ **inches_to_centimeters(inches)** - Length conversion
✅ **centimeters_to_inches(centimeters)** - Length conversion
✅ **kilometers_to_miles(kilometers)** - Distance conversion
✅ **miles_to_kilometers(miles)** - Distance conversion
✅ **kilograms_to_pounds(kilograms)** - Weight conversion
✅ **pounds_to_kilograms(pounds)** - Weight conversion
✅ **liters_to_gallons(liters)** - Volume conversion
✅ **gallons_to_liters(gallons)** - Volume conversion
✅ **UPDATE DOCUMENTATION**: Add inches/cm conversions to copilot-instructions.md
✅ **PHASE 10 COMPLETE**: Mark when both implementation AND documentation are done

## Phase 11: Advanced Calculator Features
**File: `advanced_calc.py`**
✅ **solve_quadratic(a, b, c)** - Solve ax² + bx + c = 0
✅ **distance_2d(x1, y1, x2, y2)** - Distance between two 2D points
✅ **slope(x1, y1, x2, y2)** - Slope between two points
✅ **compound_interest(principal, rate, time, compounds_per_year)** - Financial calculation
✅ **UPDATE DOCUMENTATION**: Add Phase 11 functions to copilot-instructions.md
✅ **PHASE 11 COMPLETE**: Mark when both implementation AND documentation are done

## Phase 12: Matrix Operations (Advanced)
**File: `matrix_operations.py`**
✅ **matrix_add(matrix1, matrix2)** - Add two matrices
✅ **matrix_multiply(matrix1, matrix2)** - Multiply two matrices
✅ **matrix_determinant(matrix)** - Calculate determinant
✅ **matrix_transpose(matrix)** - Transpose a matrix
✅ **UPDATE DOCUMENTATION**: Add Phase 12 functions to copilot-instructions.md
✅ **PHASE 12 COMPLETE**: Mark when both implementation AND documentation are done

---

## Implementation Guidelines

### Error Handling Standards
- Use ✅ prefix for successful results
- Use ❌ prefix for error messages
- Validate input domains (e.g., positive numbers for square root)
- Handle special cases (e.g., division by zero, invalid domains)

### Function Signatures
```python
@mcp.tool()
async def function_name(param: type, ...) -> str:
    """Clear description of what the function does."""
    try:
        # Input validation
        # Calculation
        return f"✅ result_description"
    except SpecificError as e:
        return f"❌ Specific error message"
    except Exception as e:
        return f"❌ Error performing operation: {str(e)}"
```

### Testing Strategy
- Test each function with valid inputs
- Test edge cases and invalid inputs
- Verify error messages are descriptive
- Test integration with VS Code Copilot chat

### Dependencies to Add
- `math` - For mathematical functions
- `statistics` - For statistical operations
- `fractions` - For exact fraction calculations
- `decimal` - For high-precision decimal arithmetic

---

## Priority Order
1. **Phase 0** (Refactor) - **MUST DO FIRST** - Convert to modular structure
2. **Phase 1** (Power/Root) - Most commonly used advanced functions
3. **Phase 6** (Statistics) - Useful for data analysis
4. **Phase 9** (Rounding) - Essential utility functions
5. **Phase 3** (Trigonometry) - Core mathematical functions
6. **Phase 7** (Combinatorics) - Useful for probability/counting
7. **Phases 2,4,5** (Logs/Inverse Trig/Hyperbolic) - Advanced mathematical functions
8. **Phases 8,10,11** (Number Theory/Conversions/Advanced) - Specialized functions
9. **Phase 12** (Matrix) - Most complex, implement last

## Success Criteria
- Each function follows MCP tool patterns
- Comprehensive error handling and input validation
- Clear, descriptive return messages
- Integration with existing VS Code MCP configuration
- Maintains educational value for MCP learning
