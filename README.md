# SharkMath MCP

A comprehensive Model Context Protocol (MCP) server providing 70+ mathematical functions across 12 domains. This MCP server integrates seamlessly with VS Code Copilot and other MCP-compatible clients to provide powerful mathematical computation capabilities.

## 🚀 Features

### 12 Mathematical Domains
- **Arithmetic Operations** - Basic math operations and expression evaluation
- **Power & Root Operations** - Powers, squares, cubes, and nth roots
- **Logarithmic & Exponential** - Natural log, base-10 log, custom base log, exponential
- **Hyperbolic Functions** - sinh, cosh, tanh with overflow protection
- **Statistical Functions** - mean, median, mode, standard deviation, variance
- **Precision & Rounding** - Floor, ceiling, truncation, absolute value
- **Trigonometric Functions** - Complete trig suite with degree/radian support
- **Combinatorial Mathematics** - Factorial, permutations, combinations, Fibonacci
- **Number Theory** - GCD, LCM, prime checking, prime factorization
- **Unit Conversions** - Temperature, length, weight, volume conversions
- **Advanced Calculator** - Quadratic solver, 2D geometry, compound interest
- **Matrix Operations** - Matrix addition, multiplication, determinant, transpose

## 📦 Installation

### Prerequisites
- Python 3.8+
- VS Code with MCP extension support
- `uv` package manager (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SharkMath-MCP.git
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

### Arithmetic Operations
- `add(a, b)` - Addition
- `subtract(a, b)` - Subtraction  
- `multiply(a, b)` - Multiplication
- `divide(a, b)` - Division with zero-division protection
- `calculate(expression)` - Safe expression evaluation

### Statistical Functions
- `mean(numbers)` - Arithmetic mean
- `median(numbers)` - Median value
- `mode(numbers)` - Most frequent value
- `standard_deviation(numbers)` - Standard deviation
- `variance(numbers)` - Variance calculation

### Matrix Operations
- `matrix_add(matrix1, matrix2)` - Matrix addition
- `matrix_multiply(matrix1, matrix2)` - Matrix multiplication
- `matrix_determinant(matrix)` - Determinant calculation
- `matrix_transpose(matrix)` - Matrix transpose

### Unit Conversions
- Temperature: `celsius_to_fahrenheit()`, `fahrenheit_to_celsius()`
- Length: `meters_to_feet()`, `inches_to_centimeters()`
- Weight: `kilograms_to_pounds()`, `pounds_to_kilograms()`
- Volume: `liters_to_gallons()`, `gallons_to_liters()`

*[See complete API documentation for all 70+ functions]*

## 🏗️ Architecture

The project uses a modular architecture with FastMCP:

```
sharkmath_server.py          # Main MCP server
├── arithmetic.py            # Basic operations
├── power_operations.py      # Powers and roots
├── logarithmic.py          # Log and exponential
├── hyperbolic.py           # Hyperbolic functions
├── stats_operations.py     # Statistical functions
├── precision.py            # Rounding utilities
├── trigonometric.py        # Trig functions
├── combinatorics.py        # Combinatorial math
├── number_theory.py        # Number theory
├── conversions.py          # Unit conversions
├── advanced_calc.py        # Advanced calculations
└── matrix_operations.py    # Matrix operations
```

Each module implements:
- Function definitions with proper error handling
- `register_tools(mcp)` function for MCP integration
- Comprehensive input validation
- Consistent return formatting (✅/❌ prefixes)

## 🧪 Testing

Run the comprehensive test suite:

```bash
cd Tests
python test_runner.py
```

Individual module testing:
```bash
python test_arithmetic.py
python test_matrix_operations.py
# ... etc for each module
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-function`)
3. Add your mathematical function to the appropriate module
4. Include comprehensive tests
5. Update documentation
6. Submit a pull request

### Adding New Functions

1. Choose the appropriate module (or create a new one)
2. Implement the function with proper error handling
3. Add the function to the module's `register_tools()` function
4. Import and register in `sharkmath_server.py`
5. Add comprehensive tests

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
- Check the [Tests/TEST_RESULTS.md](Tests/TEST_RESULTS.md) for function validation
- Review [sharkmath_tasklist.md](sharkmath_tasklist.md) for development roadmap

---

**SharkMath MCP** - Empowering AI with comprehensive mathematical capabilities 🦈📊
