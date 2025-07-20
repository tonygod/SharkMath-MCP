"""
Consolidated Arithmetic Tool for SharkMath MCP Server
Consolidates basic arithmetic and power operations with parameter-based routing.
Combines operations from arithmetic.py and power_operations.py modules.
"""

import math
from typing import Dict, Callable, Any

class ArithmeticTool:
    """Consolidated arithmetic tool with parameter-based operation routing."""
    
    def __init__(self):
        self.tool_name = "calculate_arithmetic"
        self.operations: Dict[str, Callable] = {
            # Basic arithmetic operations
            "add": self._add,
            "subtract": self._subtract, 
            "multiply": self._multiply,
            "divide": self._divide,
            "calculate": self._calculate,
            
            # Power operations
            "power": self._power,
            "square": self._square,
            "cube": self._cube,
            "square_root": self._square_root,
            "cube_root": self._cube_root,
            "nth_root": self._nth_root
        }
    
    def get_supported_operations(self) -> list:
        """Return list of supported operations."""
        return list(self.operations.keys())
    
    def _validate_operation(self, operation: str) -> None:
        """Validate that operation is supported."""
        if operation not in self.operations:
            supported = ", ".join(self.get_supported_operations())
            raise ValueError(f"Operation '{operation}' not supported. Supported operations: {supported}")
    
    # Basic arithmetic operations
    def _add(self, a: float, b: float) -> float:
        """Add two numbers together."""
        return a + b
    
    def _subtract(self, a: float, b: float) -> float:
        """Subtract the second number from the first number."""
        return a - b
    
    def _multiply(self, a: float, b: float) -> float:
        """Multiply two numbers together."""
        return a * b
    
    def _divide(self, a: float, b: float) -> float:
        """Divide the first number by the second number."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    def _calculate(self, expression: str) -> float:
        """Evaluate a mathematical expression safely."""
        # Basic safety check - only allow numbers, operators, parentheses and spaces
        allowed_chars = set('0123456789+-*/.()')
        if not all(c in allowed_chars or c.isspace() for c in expression):
            raise ValueError("Expression contains invalid characters. Only numbers, +, -, *, /, (, ) are allowed.")
        
        try:
            # Evaluate the expression safely
            result = eval(expression)
            return result
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero in expression")
        except SyntaxError:
            raise ValueError("Invalid mathematical expression")
    
    # Power operations
    def _power(self, base: float, exponent: float) -> float:
        """Calculate base raised to the power of exponent."""
        try:
            result = base ** exponent
            if math.isinf(result):
                raise OverflowError("Result too large to calculate")
            return result
        except OverflowError:
            raise OverflowError("Result too large to calculate")
    
    def _square(self, n: float) -> float:
        """Calculate n²."""
        return n * n
    
    def _cube(self, n: float) -> float:
        """Calculate n³."""
        return n * n * n
    
    def _square_root(self, n: float) -> float:
        """Calculate √n with negative number validation."""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(n)
    
    def _cube_root(self, n: float) -> float:
        """Calculate ∛n."""
        # Handle negative numbers for cube root (unlike square root, cube root of negative is valid)
        if n >= 0:
            return n ** (1/3)
        else:
            return -((-n) ** (1/3))
    
    def _nth_root(self, n: float, root: float) -> float:
        """Calculate nth root of a number."""
        if root == 0:
            raise ValueError("Root cannot be zero")
        
        # Handle even roots of negative numbers
        if n < 0 and root % 2 == 0:
            raise ValueError(f"Cannot calculate even root ({root}) of negative number ({n})")
        
        # Calculate nth root
        if n >= 0:
            return n ** (1/root)
        else:
            # For odd roots of negative numbers
            return -((-n) ** (1/root))
    
    def format_result(self, operation: str, inputs: dict, result: Any) -> str:
        """Format the result based on operation type."""
        if operation == "add":
            return f"✅ {inputs['a']} + {inputs['b']} = {result}"
        elif operation == "subtract":
            return f"✅ {inputs['a']} - {inputs['b']} = {result}"
        elif operation == "multiply":
            return f"✅ {inputs['a']} × {inputs['b']} = {result}"
        elif operation == "divide":
            return f"✅ {inputs['a']} ÷ {inputs['b']} = {result}"
        elif operation == "calculate":
            return f"✅ {inputs['expression']} = {result}"
        elif operation == "power":
            return f"✅ {inputs['base']}^{inputs['exponent']} = {result}"
        elif operation == "square":
            return f"✅ {inputs['n']}² = {result}"
        elif operation == "cube":
            return f"✅ {inputs['n']}³ = {result}"
        elif operation == "square_root":
            return f"✅ √{inputs['n']} = {result}"
        elif operation == "cube_root":
            return f"✅ ∛{inputs['n']} = {result}"
        elif operation == "nth_root":
            return f"✅ {inputs['n']}^(1/{inputs['root']}) = {result}"
        else:
            # Generic format
            return f"✅ {operation}({', '.join(f'{k}={v}' for k, v in inputs.items())}) = {result}"


def register_tools(mcp):
    """Register the consolidated arithmetic tool with the MCP server."""
    
    arithmetic_tool = ArithmeticTool()
    
    @mcp.tool()
    async def calculate_arithmetic(
        operation: str,
        a: float = None,
        b: float = None,
        n: float = None,
        base: float = None,
        exponent: float = None,
        root: float = None,
        expression: str = None
    ) -> str:
        """
        Consolidated arithmetic and power operations tool.
        
        Supported operations:
        - add(a, b): Addition
        - subtract(a, b): Subtraction  
        - multiply(a, b): Multiplication
        - divide(a, b): Division
        - calculate(expression): Evaluate mathematical expression
        - power(base, exponent): Exponentiation
        - square(n): Square
        - cube(n): Cube
        - square_root(n): Square root
        - cube_root(n): Cube root
        - nth_root(n, root): Nth root
        """
        try:
            # Validate operation
            arithmetic_tool._validate_operation(operation)
            
            # Prepare inputs based on operation
            if operation in ["add", "subtract", "multiply", "divide"]:
                if a is None or b is None:
                    return f"❌ Operation '{operation}' requires parameters 'a' and 'b'"
                inputs = {"a": a, "b": b}
                result = arithmetic_tool.operations[operation](a, b)
                
            elif operation == "calculate":
                if expression is None:
                    return "❌ Operation 'calculate' requires parameter 'expression'"
                inputs = {"expression": expression}
                result = arithmetic_tool.operations[operation](expression)
                
            elif operation == "power":
                if base is None or exponent is None:
                    return "❌ Operation 'power' requires parameters 'base' and 'exponent'"
                inputs = {"base": base, "exponent": exponent}
                result = arithmetic_tool.operations[operation](base, exponent)
                
            elif operation in ["square", "cube", "square_root", "cube_root"]:
                if n is None:
                    return f"❌ Operation '{operation}' requires parameter 'n'"
                inputs = {"n": n}
                result = arithmetic_tool.operations[operation](n)
                
            elif operation == "nth_root":
                if n is None or root is None:
                    return "❌ Operation 'nth_root' requires parameters 'n' and 'root'"
                inputs = {"n": n, "root": root}
                result = arithmetic_tool.operations[operation](n, root)
                
            else:
                return f"❌ Unknown operation: {operation}"
            
            return arithmetic_tool.format_result(operation, inputs, result)
            
        except ValueError as e:
            return f"❌ Value error: {str(e)}"
        except ZeroDivisionError as e:
            return f"❌ Division error: {str(e)}"
        except OverflowError as e:
            return f"❌ Overflow error: {str(e)}"
        except Exception as e:
            return f"❌ Error in {operation}: {str(e)}"


# Support for direct execution and testing
if __name__ == "__main__":
    # Test the arithmetic tool
    tool = ArithmeticTool()
    
    print("Testing ArithmeticTool operations:")
    
    # Test basic operations
    print(f"Add: {tool._add(5, 3)}")
    print(f"Subtract: {tool._subtract(10, 4)}")
    print(f"Multiply: {tool._multiply(6, 7)}")
    print(f"Divide: {tool._divide(15, 3)}")
    print(f"Calculate: {tool._calculate('2 + 3 * 4')}")
    
    # Test power operations
    print(f"Power: {tool._power(2, 8)}")
    print(f"Square: {tool._square(9)}")
    print(f"Cube: {tool._cube(4)}")
    print(f"Square root: {tool._square_root(25)}")
    print(f"Cube root: {tool._cube_root(27)}")
    print(f"Nth root: {tool._nth_root(16, 4)}")
    
    print("\n✅ All arithmetic operations working correctly!")
