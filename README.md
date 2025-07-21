# SharkMath MCP

A comprehensive Model Context Protocol (MCP) server providing 150+ mathematical functions consolidated into 15 powerful tools across all mathematical domains. This MCP server integrates seamlessly with VS Code Copilot and other MCP-compatible clients to provide powerful mathematical computation capabilities through parameter-based routing.

## 🚀 Features

### 15 Consolidated Mathematical Tools
- **`calculate_arithmetic`** - Basic arithmetic operations, expression evaluation, and power operations
- **`calculate_trigonometry`** - Complete trigonometric and inverse functions with degree/radian support
- **`calculate_statistics`** - Statistical operations including central tendency, dispersion, and percentiles
- **`convert_units`** - Universal unit converter supporting 80+ conversions across all measurement types
- **`calculate_logarithmic`** - Logarithmic and exponential functions with domain validation
- **`calculate_hyperbolic`** - Hyperbolic functions with overflow protection
- **`format_precision`** - Number formatting including rounding, floor, ceiling, and absolute value
- **`analyze_numbers`** - Number theory and combinatorial mathematics (primes, GCD, LCM, factorial, etc.)
- **`solve_equations`** - Equation solvers for quadratic and linear equations
- **`calculate_geometry_2d`** - 2D geometry calculations for distance, slope, areas, and perimeters
- **`manipulate_matrices`** - Matrix operations including addition, multiplication, determinant, and transpose
- **`financial_calculations`** - Financial and business calculations including interest, loans, and investment analysis
- **`computer_science_tools`** - Programming utilities including base conversions, hash functions, and algorithm analysis
- **`data_analysis`** - Advanced statistical analysis including correlation, distribution analysis, and outlier detection
- **`utility_functions`** - Helper functions providing mathematical constants, validation, and operation help

## 📦 Installation

### Prerequisites
- Python 3.8+
- VS Code with MCP extension support
- `uv` package manager (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/tonygod/SharkMath-MCP.git
cd SharkMath-MCP
```

2. Install dependencies:
```bash
uv venv mcp-env
source mcp-env/bin/activate  # On Windows: mcp-env\Scripts\activate
uv pip install mcp fastmcp
```

3. Run the MCP server:
```bash
uv run sharkmath_server.py
```

## 🔧 VS Code Integration

Configure the MCP server in your VS Code settings (`.vscode/mcp.json`):

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

## 📚 API Reference

SharkMath uses **parameter-based routing** where each consolidated tool accepts an `operation` parameter to specify the desired function.

### Arithmetic Operations - `calculate_arithmetic`
- `operation="add"` - Addition: `a + b`
- `operation="subtract"` - Subtraction: `a - b`
- `operation="multiply"` - Multiplication: `a * b`
- `operation="divide"` - Division with zero-division protection: `a / b`
- `operation="calculate"` - **Enhanced expression evaluation with 20+ mathematical functions**
  - **Basic Functions**: `sqrt()`, `pow()`, `abs()`, `round()`
  - **Trigonometric**: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`
  - **Logarithmic**: `log()`, `log10()`, `ln()` (natural log alias)
  - **Hyperbolic**: `sinh()`, `cosh()`, `tanh()`
  - **Rounding**: `floor()`, `ceil()`, `trunc()`
  - **Constants**: `pi`, `e`
  - **Examples**: `sqrt(25)`, `sin(pi/2)`, `log(e)`, `sqrt((5-0)^2 + (12-0)^2)`
- `operation="power"` - Exponentiation: `base^exponent`
- `operation="square"` - Square: `n²`
- `operation="cube"` - Cube: `n³`
- `operation="square_root"` - Square root: `√n`

### Statistical Functions - `calculate_statistics`
- `operation="mean"` - Arithmetic mean
- `operation="median"` - Median value
- `operation="mode"` - Most frequent value
- `operation="standard_deviation"` - Standard deviation
- `operation="variance"` - Variance calculation
- `operation="range_stats"` - Min, max, and range
- `operation="percentile"` - Percentile calculation (requires percentile parameter)

### Trigonometric Functions - `calculate_trigonometry`
- `operation="sin"` - Sine function
- `operation="cos"` - Cosine function
- `operation="tan"` - Tangent function
- `operation="asin"` - Inverse sine (arcsine)
- `operation="acos"` - Inverse cosine (arccosine)
- `operation="atan"` - Inverse tangent (arctangent)
- `operation="atan2"` - Two-argument arctangent (requires x and y parameters)

### Matrix Operations - `manipulate_matrices`
- `operation="add"` - Matrix addition
- `operation="multiply"` - Matrix multiplication
- `operation="determinant"` - Determinant calculation
- `operation="transpose"` - Matrix transpose

### Unit Conversions - `convert_units`
- **Energy**: watts, kilowatts, horsepower, joules, calories, btu
- **Temperature**: celsius, fahrenheit
- **Length**: meters, feet, inches, centimeters, kilometers, miles
- **Weight**: kilograms, pounds
- **Volume**: liters, gallons
- **Time**: seconds, minutes, hours, days, weeks, months, years
- **Area**: square_meters, square_feet, acres, hectares
- **Speed**: mps, kmh, mph, knots
- **Pressure**: pascals, atmospheres, psi, bar
- **Data**: bytes, kilobytes, megabytes, gigabytes, terabytes

### Financial Calculations - `financial_calculations`
- `operation="compound_interest"` - Compound interest calculation
- `operation="simple_interest"` - Simple interest calculation
- `operation="present_value"` - Present value calculation
- `operation="future_value"` - Future value calculation
- `operation="loan_payment"` - Monthly loan payment
- `operation="roi"` - Return on investment
- `operation="mortgage_payment"` - Mortgage payment calculation

**📖 [Complete API Documentation](Docs/API_DOCUMENTATION.md)** - Full reference for all tools and operations

## 🏗️ Architecture

The project uses a **consolidated tool architecture** with parameter-based routing and FastMCP:

```
sharkmath_server.py          # Main MCP server (15 consolidated tools)
├── arithmetic.py            # calculate_arithmetic (arithmetic + power operations + 20+ math functions)
├── trigonometric.py         # calculate_trigonometry (trig + inverse trig functions)
├── stats_operations.py      # calculate_statistics (statistical operations + percentiles)
├── convert_units.py         # convert_units (80+ unit conversions)
├── logarithmic.py           # calculate_logarithmic (log + exponential functions)
├── hyperbolic.py            # calculate_hyperbolic (hyperbolic functions)
├── precision.py             # format_precision (rounding + precision utilities)
├── number_theory.py         # analyze_numbers (number theory + combinatorics)
├── solve_equations.py       # solve_equations (quadratic + linear solvers)
├── calculate_geometry_2d.py # calculate_geometry_2d (2D geometry calculations)
├── matrix_operations.py     # manipulate_matrices (matrix operations)
├── financial_calculations.py # financial_calculations (financial + business calcs)
├── computer_science_tools.py # computer_science_tools (CS + programming utilities)
├── data_analysis.py         # data_analysis (advanced statistical analysis)
└── utility_functions.py     # utility_functions (constants + validation + help)
```

### Consolidated Tool Pattern
Each module implements parameter-based routing:
- **Single tool registration** with `operation` parameter
- **Function routing** based on operation parameter value
- **Comprehensive error handling** with ✅/❌ prefixes
- **Input validation** specific to each mathematical operation
- **Consistent return formatting** across all operations

### Key Architecture Benefits
- **Reduced tool count**: 70+ individual tools → 15 consolidated tools
- **Improved maintainability**: Logical grouping of related functions
- **Better performance**: Single tool registration per domain
- **Enhanced usability**: Intuitive parameter-based operation selection
- **MCP compatibility**: Avoids tool registration limits

## 🧪 Testing

Run the comprehensive test suite:

```bash
cd Tests
python test_runner.py
```

### Individual Consolidated Tool Testing
Each consolidated tool has its own dedicated test suite:
```bash
python test_calculate_arithmetic.py      # 45+ arithmetic operation tests
python test_calculate_trigonometry.py    # 42+ trigonometric function tests
python test_calculate_statistics.py      # 37+ statistical operation tests
python test_convert_units.py             # 51+ unit conversion tests
python test_manipulate_matrices.py       # 31+ matrix operation tests
python test_financial_calculations.py    # 31+ financial calculation tests
python test_computer_science_tools.py    # 41+ CS utility tests
python test_data_analysis.py             # 36+ advanced analysis tests
# ... and more for each consolidated tool
```

### Test Coverage
- **500+ individual tests** across all consolidated tools
- **Parameter validation testing** for all operation types
- **Error condition testing** with comprehensive edge case coverage
- **Integration testing** with MCP server registration verification
- **Regression testing** ensuring all original functionality preserved

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-function`)
3. Add your mathematical function to the appropriate module
4. Include comprehensive tests
5. Update documentation
6. Submit a pull request

### Adding New Functions

1. Choose the appropriate consolidated tool module
2. Add your operation to the module's operation routing dictionary
3. Implement the function with proper error handling and validation
4. Add comprehensive test coverage to the tool's test suite
5. Update documentation with the new operation parameter

### Example: Adding a New Operation
```python
# In arithmetic.py - adding a new operation
def calculate_arithmetic(operation: str, a: float = None, b: float = None, ...):
    operations = {
        "add": lambda: a + b,
        "subtract": lambda: a - b,
        "new_operation": lambda: your_new_function(a, b),  # Add here
        # ... other operations
    }
    
    if operation not in operations:
        return f"❌ Unsupported operation: {operation}"
    
    try:
        result = operations[operation]()
        return f"✅ {operation.title()} result: {result}"
    except Exception as e:
        return f"❌ Error in {operation}: {str(e)}"
```

## 📋 Requirements

- Python 3.8+
- MCP (Model Context Protocol)
- FastMCP framework

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on the Model Context Protocol (MCP) framework
- Uses FastMCP for efficient server implementation
- Inspired by the need for comprehensive mathematical tools in AI workflows

## 📞 Support

- Create an issue for bug reports or feature requests
- Check the [Tests/](Tests/) directory for comprehensive function validation
- Review [Docs/sharkmath_tools_refactor.md](Docs/Archive/sharkmath_tools_refactor.md) for architecture details
- All 15 consolidated tools with 150+ operations are thoroughly tested and documented

---

**SharkMath MCP** - Empowering AI with comprehensive mathematical capabilities through efficient consolidated tools 🦈📊
