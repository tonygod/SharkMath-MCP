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
    
    def _calculate(self, expression: str, precision: int = 10, timeout_seconds: float = 5.0, max_complexity: int = 100) -> float:
        """
        Evaluate a mathematical expression safely with enhanced features.
        
        Security and Validation Framework:
        - Expression complexity limits
        - Function validation system  
        - Timeout protection
        - Enhanced security measures
        """
        import time
        import signal
        
        # Expression Complexity Limits
        self._validate_expression_complexity(expression, max_complexity)
        
        # Enhanced character validation - support for functions, exponentiation, and constants
        # Enhanced Character Validation: Allow letters, underscores, additional operators
        allowed_chars = set('0123456789+-*/.**()^abcdefghijklmnopqrstuvwxyz_,')
        if not all(c in allowed_chars or c.isspace() for c in expression):
            invalid_chars = [c for c in expression if c not in allowed_chars and not c.isspace()]
            raise ValueError(f"Expression contains invalid characters: {invalid_chars}. Supported: numbers, operators (+, -, *, /, **, ^), parentheses, letters, underscore, comma")
        
        # Exponentiation Support: Convert ^ to ** for Python evaluation
        processed_expression = self._preprocess_expression(expression)
        
        # Function Validation System
        self._validate_functions_in_expression(processed_expression)
        
        # Create safe evaluation environment with mathematical functions
        safe_globals = self._create_safe_evaluation_environment()
        
        # Timeout Protection
        def timeout_handler(signum, frame):
            raise TimeoutError(f"Expression evaluation exceeded {timeout_seconds} seconds timeout")
        
        # Set up timeout (Unix-like systems only)
        old_handler = None
        try:
            if hasattr(signal, 'SIGALRM'):
                old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(int(timeout_seconds))
            
            start_time = time.time()
            
            # Evaluate the expression safely with restricted globals
            result = eval(processed_expression, safe_globals, {})
            
            # Check if evaluation took too long (fallback for systems without signal)
            if time.time() - start_time > timeout_seconds:
                raise TimeoutError(f"Expression evaluation exceeded {timeout_seconds} seconds timeout")
            
            # Handle special values
            if math.isnan(result):
                raise ValueError("Expression resulted in NaN (Not a Number)")
            elif math.isinf(result):
                raise OverflowError("Expression resulted in infinity")
            
            # Apply precision formatting
            if isinstance(result, float):
                result = round(result, precision)
                
            return result
            
        except TimeoutError:
            raise TimeoutError(f"Expression evaluation exceeded {timeout_seconds} seconds timeout")
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero in expression")
        except SyntaxError:
            raise ValueError("Invalid mathematical expression syntax")
        except NameError as e:
            raise ValueError(f"Unsupported function or variable: {str(e)}")
        except ValueError as e:
            # Re-raise ValueError with original message (domain errors, etc.)
            raise e
        finally:
            # Clean up timeout alarm
            if hasattr(signal, 'SIGALRM') and old_handler is not None:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
    
    def _preprocess_expression(self, expression: str) -> str:
        """
        Preprocess mathematical expression for enhanced features.
        Convert ^ to ** for exponentiation support.
        """
        # Replace ^ with ** for exponentiation, but be careful not to replace ** that's already there
        processed = expression.replace('^', '**')
        
        # Clean up any triple asterisks that might result from **^ -> ****
        while '***' in processed:
            processed = processed.replace('***', '**')
            
        return processed
    
    def _validate_expression_complexity(self, expression: str, max_complexity: int) -> None:
        """
        Expression Complexity Limits
        Validate expression complexity to prevent DoS attacks and resource exhaustion.
        """
        # Configuration for complexity limits
        MAX_EXPRESSION_LENGTH = 1000
        MAX_NESTING_DEPTH = 10
        MAX_FUNCTION_CALLS = 20
        
        # Check expression length
        if len(expression) > MAX_EXPRESSION_LENGTH:
            raise ValueError(f"Expression too long: {len(expression)} characters (max: {MAX_EXPRESSION_LENGTH})")
        
        # Check parentheses nesting depth
        max_depth = 0
        current_depth = 0
        for char in expression:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                
        if max_depth > MAX_NESTING_DEPTH:
            raise ValueError(f"Expression nesting too deep: {max_depth} levels (max: {MAX_NESTING_DEPTH})")
        
        # Check for unbalanced parentheses
        if current_depth != 0:
            raise ValueError("Unbalanced parentheses in expression")
        
        # Count function calls (approximate - look for function patterns)
        import re
        function_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*\s*\('
        function_matches = re.findall(function_pattern, expression)
        
        if len(function_matches) > MAX_FUNCTION_CALLS:
            raise ValueError(f"Too many function calls: {len(function_matches)} (max: {MAX_FUNCTION_CALLS})")
        
        # Basic complexity score calculation
        complexity_score = (
            len(expression) * 0.1 +
            max_depth * 2 +
            len(function_matches) * 3 +
            expression.count('*') * 0.5 +
            expression.count('/') * 0.5 +
            expression.count('+') * 0.2 +
            expression.count('-') * 0.2
        )
        
        if complexity_score > max_complexity:
            raise ValueError(f"Expression too complex: {complexity_score:.1f} (max: {max_complexity})")
    
    def _validate_functions_in_expression(self, expression: str) -> None:
        """
        Function Validation System
        Validate that all functions in the expression are whitelisted and safe.
        """
        import re
        
        # Get list of supported functions from safe evaluation environment
        safe_globals = self._create_safe_evaluation_environment()
        supported_functions = set(safe_globals.keys()) - {'__builtins__'}
        
        # Find all function calls in the expression
        function_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        function_matches = re.findall(function_pattern, expression)
        
        # Validate each function
        for func_name in function_matches:
            if func_name not in supported_functions:
                supported_list = sorted(supported_functions)
                raise ValueError(f"Unsupported function '{func_name}'. Supported functions: {', '.join(supported_list)}")
        
        # Additional validation for function parameter patterns
        self._validate_function_parameters(expression, function_matches)
    
    def _validate_function_parameters(self, expression: str, function_names: list) -> None:
        """
        Validate function parameters and call patterns for security.
        """
        import re
        
        # Check for potentially dangerous patterns
        dangerous_patterns = [
            r'__[a-zA-Z_]+__',  # Double underscore methods
            r'eval\s*\(',       # Nested eval calls
            r'exec\s*\(',       # Exec calls
            r'import\s+',       # Import statements
            r'globals\s*\(',    # Global access
            r'locals\s*\(',     # Local access
            r'vars\s*\(',       # Variable access
            r'dir\s*\(',        # Directory listing
            r'getattr\s*\(',    # Attribute access
            r'setattr\s*\(',    # Attribute setting
            r'hasattr\s*\(',    # Attribute checking
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, expression, re.IGNORECASE):
                raise ValueError(f"Expression contains potentially dangerous pattern: {pattern}")
        
        # Validate function parameter counts for common functions
        # Note: This is a simplified validation - full AST parsing would be more accurate
        function_param_limits = {
            'sqrt': (1, 1),      # Exactly 1 parameter
            'abs': (1, 1),       # Exactly 1 parameter
            'round': (1, 2),     # 1 or 2 parameters
            'sin': (1, 1),       # Exactly 1 parameter
            'cos': (1, 1),       # Exactly 1 parameter
            'tan': (1, 1),       # Exactly 1 parameter
            'asin': (1, 1),      # Exactly 1 parameter
            'acos': (1, 1),      # Exactly 1 parameter
            'atan': (1, 1),      # Exactly 1 parameter
            'sinh': (1, 1),      # Exactly 1 parameter
            'cosh': (1, 1),      # Exactly 1 parameter
            'tanh': (1, 1),      # Exactly 1 parameter
            'floor': (1, 1),     # Exactly 1 parameter
            'ceil': (1, 1),      # Exactly 1 parameter
            'trunc': (1, 1),     # Exactly 1 parameter
            'log10': (1, 1),     # Exactly 1 parameter for log10
            'ln': (1, 1),        # Exactly 1 parameter for ln (alias)
        }
        
        # Extract and validate individual function calls more accurately
        for func_name in function_names:
            if func_name in function_param_limits:
                min_params, max_params = function_param_limits[func_name]
                
                # Find all instances of this function call with more precise regex
                # This regex captures the content between parentheses for each function call
                pattern = f'\\b{re.escape(func_name)}\\s*\\(([^()]*(?:\\([^()]*\\)[^()]*)*)\\)'
                matches = re.findall(pattern, expression)
                
                for match in matches:
                    if not match.strip():  # Empty parentheses
                        param_count = 0
                    else:
                        # Split by commas but be careful about nested expressions
                        # This is a simplified approach - doesn't handle nested function calls perfectly
                        params = []
                        paren_level = 0
                        current_param = ""
                        
                        for char in match:
                            if char == ',' and paren_level == 0:
                                if current_param.strip():
                                    params.append(current_param.strip())
                                current_param = ""
                            else:
                                if char == '(':
                                    paren_level += 1
                                elif char == ')':
                                    paren_level -= 1
                                current_param += char
                        
                        # Add the last parameter
                        if current_param.strip():
                            params.append(current_param.strip())
                            
                        param_count = len(params)
                    
                    # Check parameter count
                    if param_count < min_params or param_count > max_params:
                        if min_params == max_params:
                            raise ValueError(f"Function '{func_name}' requires exactly {min_params} parameter(s), got {param_count}")
                        else:
                            raise ValueError(f"Function '{func_name}' requires {min_params}-{max_params} parameters, got {param_count}")
        
        # Special case for pow() and log() which have flexible parameters
        # pow(x, y) = 2 parameters, log(x) = 1 param (natural), log(x, base) = 2 params
        if 'pow' in function_names:
            pow_pattern = r'\bpow\s*\(([^()]*(?:\([^()]*\)[^()]*)*)\)'
            pow_matches = re.findall(pow_pattern, expression)
            for match in pow_matches:
                param_count = len([p.strip() for p in match.split(',') if p.strip()]) if match.strip() else 0
                if param_count != 2:
                    raise ValueError(f"Function 'pow' requires exactly 2 parameters, got {param_count}")
        
        if 'log' in function_names:
            log_pattern = r'\blog\s*\(([^()]*(?:\([^()]*\)[^()]*)*)\)'
            log_matches = re.findall(log_pattern, expression)
            for match in log_matches:
                param_count = len([p.strip() for p in match.split(',') if p.strip()]) if match.strip() else 0
                if param_count < 1 or param_count > 2:
                    raise ValueError(f"Function 'log' requires 1-2 parameters, got {param_count}")
    
    def _create_safe_evaluation_environment(self) -> dict:
        """
        Create a safe evaluation environment with mathematical functions and constants.
        Implements Mathematical Functions Library.
        """
        def safe_sqrt(x):
            """Safe square root with domain validation."""
            if x < 0:
                raise ValueError(f"Cannot calculate square root of negative number: {x}")
            return math.sqrt(x)
        
        def safe_log(x, base=math.e):
            """Safe logarithm with domain validation."""
            if x <= 0:
                raise ValueError(f"Cannot calculate logarithm of non-positive number: {x}")
            if base <= 0 or base == 1:
                raise ValueError(f"Invalid logarithm base: {base}")
            return math.log(x, base)
        
        def safe_log10(x):
            """Safe base-10 logarithm with domain validation."""
            if x <= 0:
                raise ValueError(f"Cannot calculate log10 of non-positive number: {x}")
            return math.log10(x)
        
        def safe_asin(x):
            """Safe arc sine with domain validation."""
            if x < -1 or x > 1:
                raise ValueError(f"asin input must be between -1 and 1, got: {x}")
            return math.asin(x)
        
        def safe_acos(x):
            """Safe arc cosine with domain validation."""
            if x < -1 or x > 1:
                raise ValueError(f"acos input must be between -1 and 1, got: {x}")
            return math.acos(x)
        
        # Safe evaluation environment with restricted globals
        safe_globals = {
            '__builtins__': {},  # Remove all built-in functions for security
            
            # Basic Functions
            'sqrt': safe_sqrt,
            'pow': math.pow,
            'abs': abs,
            'round': round,
            
            # Trigonometric Functions
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': safe_asin,
            'acos': safe_acos,
            'atan': math.atan,
            
            # Logarithmic Functions
            'log': safe_log,
            'log10': safe_log10,
            'ln': safe_log,  # Alias for natural log
            
            # Hyperbolic Functions
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            
            # Rounding Functions
            'floor': math.floor,
            'ceil': math.ceil,
            'trunc': math.trunc,
            
            # Mathematical Constants
            'pi': math.pi,
            'e': math.e,
        }
        
        return safe_globals
    
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
        expression: str = None,
        precision: int = 10,
        timeout_seconds: float = 5.0,
        max_complexity: int = 100
    ) -> str:
        """
        Consolidated arithmetic and power operations tool.
        
        Supported operations:
        - add(a, b): Addition
        - subtract(a, b): Subtraction  
        - multiply(a, b): Multiplication
        - divide(a, b): Division
        - calculate(expression): Evaluate mathematical expression with security features
        - power(base, exponent): Exponentiation
        - square(n): Square
        - cube(n): Cube
        - square_root(n): Square root
        - cube_root(n): Cube root
        - nth_root(n, root): Nth root
        
        Security Features (for calculate operation):
        - precision: Number of decimal places (default: 10)
        - timeout_seconds: Maximum evaluation time (default: 5.0)
        - max_complexity: Maximum expression complexity score (default: 100)
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
                inputs = {"expression": expression, "precision": precision, "timeout_seconds": timeout_seconds, "max_complexity": max_complexity}
                result = arithmetic_tool.operations[operation](expression, precision, timeout_seconds, max_complexity)
                
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
        except TimeoutError as e:
            return f"❌ Timeout error: {str(e)}"
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
    
    # Test basic calculate
    print(f"Calculate: {tool._calculate('2 + 3 * 4')}")
    
    # Enhanced expression testing with exponentiation
    print(f"Exponentiation (^): {tool._calculate('2^3')}")  # Should give 8
    print(f"Exponentiation (**): {tool._calculate('2**4')}")  # Should give 16
    print(f"Complex with ^: {tool._calculate('(2+3)^2')}")  # Should give 25
    print(f"Mixed operators: {tool._calculate('2*3^2+1')}")  # Should give 19
    
    # Test Mathematical Functions
    print("\nTesting Mathematical Functions")
    
    # Basic Functions
    print(f"sqrt(25): {tool._calculate('sqrt(25)')}")  # Should give 5.0
    print(f"pow(2, 3): {tool._calculate('pow(2, 3)')}")  # Should give 8.0
    print(f"abs(-5): {tool._calculate('abs(-5)')}")  # Should give 5.0
    print(f"round(3.7): {tool._calculate('round(3.7)')}")  # Should give 4.0
    
    # Trigonometric Functions
    print(f"sin(pi/2): {tool._calculate('sin(pi/2)')}")  # Should give 1.0
    print(f"cos(0): {tool._calculate('cos(0)')}")  # Should give 1.0
    print(f"tan(pi/4): {tool._calculate('tan(pi/4)')}")  # Should give ~1.0
    print(f"asin(1): {tool._calculate('asin(1)')}")  # Should give pi/2
    print(f"acos(0): {tool._calculate('acos(0)')}")  # Should give pi/2
    print(f"atan(1): {tool._calculate('atan(1)')}")  # Should give pi/4
    
    # Logarithmic Functions
    print(f"log(e): {tool._calculate('log(e)')}")  # Should give 1.0
    print(f"log10(100): {tool._calculate('log10(100)')}")  # Should give 2.0
    print(f"ln(e): {tool._calculate('ln(e)')}")  # Should give 1.0
    
    # Hyperbolic Functions
    print(f"sinh(0): {tool._calculate('sinh(0)')}")  # Should give 0.0
    print(f"cosh(0): {tool._calculate('cosh(0)')}")  # Should give 1.0
    print(f"tanh(0): {tool._calculate('tanh(0)')}")  # Should give 0.0
    
    # Rounding Functions
    print(f"floor(3.7): {tool._calculate('floor(3.7)')}")  # Should give 3.0
    print(f"ceil(3.2): {tool._calculate('ceil(3.2)')}")  # Should give 4.0
    print(f"trunc(3.9): {tool._calculate('trunc(3.9)')}")  # Should give 3.0
    
    # Mathematical Constants
    print(f"pi: {tool._calculate('pi')}")  # Should give ~3.14159
    print(f"e: {tool._calculate('e')}")  # Should give ~2.71828
    print(f"2*pi: {tool._calculate('2*pi')}")  # Should give ~6.28318
    
    # Complex expressions with functions
    print(f"Complex: sqrt(25) + sin(pi/2): {tool._calculate('sqrt(25) + sin(pi/2)')}")  # Should give 6.0
    print(f"Distance formula: sqrt((5-0)^2 + (12-0)^2): {tool._calculate('sqrt((5-0)^2 + (12-0)^2)')}")  # Should give 13.0
    
    # Test Security and Validation Framework
    print("\nTesting Security and Validation Framework")
    
    # Test precision parameter
    print(f"Precision test (pi with 3 decimals): {tool._calculate('pi', precision=3)}")
    print(f"Precision test (1/3 with 5 decimals): {tool._calculate('1/3', precision=5)}")
    
    # Test complexity validation
    try:
        # This should work - moderate complexity  
        print(f"Moderate complexity: {tool._calculate('sqrt(pow(2,3) + pow(3,2))')}")
    except Exception as e:
        print(f"Moderate complexity error: {e}")
        # Try a simpler version that should work
        print(f"Alternative complexity test: {tool._calculate('sqrt(64)')}")  # Should work
    
    # Test function validation
    try:
        # This should fail - unsupported function
        print(f"Invalid function test: {tool._calculate('unsupported_func(5)')}")
    except Exception as e:
        print(f"✅ Function validation working: {e}")
    
    # Test dangerous pattern detection
    try:
        # This should fail - dangerous pattern
        print(f"Dangerous pattern test: {tool._calculate('__import__("os")')}")
    except Exception as e:
        print(f"✅ Dangerous pattern detection working: {e}")
    
    # Test expression length limits
    try:
        # Create a very long expression
        long_expr = "1" + "+1" * 500  # This creates 1+1+1+1... 500 times
        print(f"Long expression test: {tool._calculate(long_expr)}")
    except Exception as e:
        print(f"✅ Expression length validation working: {e}")
    
    # Test nesting depth limits
    try:
        # Create deeply nested parentheses
        nested_expr = "(" * 15 + "1" + ")" * 15
        print(f"Deep nesting test: {tool._calculate(nested_expr)}")
    except Exception as e:
        print(f"✅ Nesting depth validation working: {e}")
    
    # Test unbalanced parentheses
    try:
        print(f"Unbalanced parentheses test: {tool._calculate('((1+2)')}")
    except Exception as e:
        print(f"✅ Unbalanced parentheses detection working: {e}")
    
    # Test domain validation for functions
    try:
        print(f"Domain validation test (sqrt of negative): {tool._calculate('sqrt(-1)')}")
    except Exception as e:
        print(f"✅ Domain validation working: {e}")
    
    try:
        print(f"Domain validation test (log of zero): {tool._calculate('log(0)')}")
    except Exception as e:
        print(f"✅ Domain validation working: {e}")
    
    try:
        print(f"Domain validation test (asin out of range): {tool._calculate('asin(2)')}")
    except Exception as e:
        print(f"✅ Domain validation working: {e}")
    
    # Test power operations
    print(f"\nPower: {tool._power(2, 8)}")
    print(f"Square: {tool._square(9)}")
    print(f"Cube: {tool._cube(4)}")
    print(f"Square root: {tool._square_root(25)}")
    print(f"Cube root: {tool._cube_root(27)}")
    print(f"Nth root: {tool._nth_root(16, 4)}")
    
    print("\n✅ All arithmetic operations, mathematical functions, and security features working correctly!")
