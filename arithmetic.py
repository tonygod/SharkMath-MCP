"""
Arithmetic operations module for SharkMath MCP server.
Contains basic mathematical operations: addition, subtraction, multiplication, division.
"""

def register_tools(mcp):
    """Register all arithmetic tools with the MCP server."""
    
    @mcp.tool()
    async def add(a: float, b: float) -> str:
        """Add two numbers together."""
        try:
            result = a + b
            return f"✅ {a} + {b} = {result}"
        except Exception as e:
            return f"❌ Error performing addition: {str(e)}"

    @mcp.tool()
    async def subtract(a: float, b: float) -> str:
        """Subtract the second number from the first number."""
        try:
            result = a - b
            return f"✅ {a} - {b} = {result}"
        except Exception as e:
            return f"❌ Error performing subtraction: {str(e)}"

    @mcp.tool()
    async def multiply(a: float, b: float) -> str:
        """Multiply two numbers together."""
        try:
            result = a * b
            return f"✅ {a} × {b} = {result}"
        except Exception as e:
            return f"❌ Error performing multiplication: {str(e)}"

    @mcp.tool()
    async def divide(a: float, b: float) -> str:
        """Divide the first number by the second number."""
        try:
            if b == 0:
                return "❌ Error: Cannot divide by zero!"
            
            result = a / b
            return f"✅ {a} ÷ {b} = {result}"
        except Exception as e:
            return f"❌ Error performing division: {str(e)}"

    @mcp.tool()
    async def calculate(expression: str) -> str:
        """Evaluate a mathematical expression safely. Supports +, -, *, / and parentheses."""
        try:
            # Basic safety check - only allow numbers, operators, parentheses and spaces
            allowed_chars = set('0123456789+-*/.()')
            if not all(c in allowed_chars or c.isspace() for c in expression):
                return "❌ Error: Expression contains invalid characters. Only numbers, +, -, *, /, (, ) are allowed."
            
            # Evaluate the expression safely
            result = eval(expression)
            return f"✅ {expression} = {result}"
        except ZeroDivisionError:
            return "❌ Error: Division by zero in expression!"
        except SyntaxError:
            return "❌ Error: Invalid mathematical expression!"
        except Exception as e:
            return f"❌ Error evaluating expression: {str(e)}"
