# Copilot Instructions for MCP Python Tutorial Codebase

## Project Overview
This is an MCP server providing comprehensive mathematical tools for solving problems across multiple domains

## Core Architecture

### MCP Server Types
1. **SharkMath Server** (`sharkmath_server.py`) - Mathematical tools

### Key Components
- **FastMCP servers** - All servers use `FastMCP("Server Name")` pattern
- **SharkMath Server** - Comprehensive mathematical calculation server with tools across all mathematical domains

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

### SharkMath Architecture
- **Main server pattern** - `sharkmath_server.py` imports and registers tools from modules
- **Module registration** - Each module has `register_tools(mcp)` function
- **Dual import context** - Handles both direct execution and module imports
- **Parameter-based routing** - Tools use operation parameters to route to specific functions
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
- **Root level** - Mathematical calculation MCP server with parameter-based routing
  - `arithmetic.py` - `calculate_arithmetic` - Basic arithmetic, enhanced expression evaluation with mathematical functions, and power operations
  - **Enhanced Expression Evaluation**: Expression evaluation now supports mathematical functions (sqrt, sin, cos, tan, asin, acos, atan, log, log10, ln, sinh, cosh, tanh, floor, ceil, trunc, abs, round, pow) and constants (pi, e)
  - `trigonometric.py` - `calculate_trigonometry` - Trigonometric functions with radians/degrees support
  - `stats_operations.py` - `calculate_statistics` - Statistical operations and analysis
  - `convert_units.py` - `convert_units` - Unit conversions across multiple measurement types
  - `logarithmic.py` - `calculate_logarithmic` - Logarithmic and exponential functions
  - `hyperbolic.py` - `calculate_hyperbolic` - Hyperbolic functions
  - `precision.py` - `format_precision` - Precision and rounding operations
  - `number_theory.py` - `analyze_numbers` - Number theory and combinatorial functions
  - `solve_equations.py` - `solve_equations` - Equation solving capabilities
  - `calculate_geometry_2d.py` - `calculate_geometry_2d` - 2D geometry calculations
  - `matrix_operations.py` - `manipulate_matrices` - Matrix operations and linear algebra
  - `financial_calculations.py` - `financial_calculations` - Financial and business calculations
  - `computer_science_tools.py` - `computer_science_tools` - Programming and computer science utilities
  - `data_analysis.py` - `data_analysis` - Advanced statistical analysis
  - `utility_functions.py` - `utility_functions` - Helper functions and mathematical constants
- **Tests** - Individual test suites per tool for comprehensive coverage  

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
- **calculate_arithmetic** - Basic arithmetic (add, subtract, multiply, divide), enhanced expression evaluation with mathematical functions, and power operations (square, cube, roots)
  - **Enhanced Expression Evaluation**: Safe expression evaluation with 20+ mathematical functions including sqrt(), sin(), cos(), tan(), log(), ln(), abs(), floor(), ceil(), and mathematical constants (pi, e)

#### **Trigonometric Functions** (`trigonometric.py`)
- **calculate_trigonometry** - Standard trigonometric functions (sin, cos, tan) and inverse functions, with support for both radians and degrees

#### **Statistical Functions** (`stats_operations.py`)
- **calculate_statistics** - Descriptive statistics including central tendency, dispersion measures, and percentile calculations

#### **Unit Conversions** (`convert_units.py`)
- **convert_units** - Comprehensive unit conversions across temperature, length, weight, volume, energy, time, area, speed, pressure, and data

#### **Logarithmic and Exponential Functions** (`logarithmic.py`)
- **calculate_logarithmic** - Natural logarithm, base-10 logarithm, custom base logarithms, and exponential functions with domain validation

#### **Hyperbolic Functions** (`hyperbolic.py`)
- **calculate_hyperbolic** - Hyperbolic sine, cosine, and tangent functions with overflow protection

#### **Precision and Rounding** (`precision.py`)
- **format_precision** - Number formatting including rounding, floor, ceiling, truncation, and absolute value operations

#### **Number Theory and Combinatorics** (`number_theory.py`)
- **analyze_numbers** - Prime number analysis, GCD/LCM calculations, factorial, permutations, combinations, and Fibonacci sequences

#### **Equation Solvers** (`solve_equations.py`)
- **solve_equations** - Quadratic and linear equation solving with support for complex solutions

#### **2D Geometry** (`calculate_geometry_2d.py`)
- **calculate_geometry_2d** - Distance calculations, slope determination, and area/perimeter calculations for basic shapes

#### **Matrix Operations** (`matrix_operations.py`)
- **manipulate_matrices** - Matrix arithmetic including addition, multiplication, determinant calculation, and transposition

#### **Financial Calculations** (`financial_calculations.py`)
- **financial_calculations** - Interest calculations, loan payments, investment analysis, depreciation, and business metrics

#### **Computer Science Tools** (`computer_science_tools.py`)
- **computer_science_tools** - Base conversions, hash functions, algorithm complexity analysis, bitwise operations, and ASCII conversions

#### **Data Analysis** (`data_analysis.py`)
- **data_analysis** - Advanced statistical analysis including correlation, distribution analysis, outlier detection, and data standardization

#### **Utility Functions** (`utility_functions.py`)
- **utility_functions** - Mathematical constants, input validation, help system, and number formatting utilities

## Key Files for Context
- `sharkmath_server.py` - Main mathematical MCP server with tool imports
- `arithmetic.py` - Basic arithmetic and power operations module
- `trigonometric.py` - Trigonometric and inverse trigonometric functions module  
- `stats_operations.py` - Statistical calculations module
- `convert_units.py` - Unit conversion functions across multiple measurement types
- `logarithmic.py` - Logarithmic and exponential functions module
- `hyperbolic.py` - Hyperbolic functions module
- `precision.py` - Rounding and precision utilities module
- `number_theory.py` - Number theory and combinatorial mathematics module
- `solve_equations.py` - Equation solving functions
- `calculate_geometry_2d.py` - 2D geometry calculations
- `matrix_operations.py` - Matrix operations and linear algebra functions
- `financial_calculations.py` - Financial and business calculation functions
- `computer_science_tools.py` - Computer science and programming utility functions
- `data_analysis.py` - Advanced statistical analysis and data science functions
- `utility_functions.py` - Helper functions and mathematical constants
- `sharkmath_tasklist.md` - Development roadmap and task tracking
- `pyproject.toml` - Project dependencies and tooling configuration
- `.vscode/mcp.json` - VS Code MCP server configuration
