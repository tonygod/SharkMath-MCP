"""
Consolidated Trigonometric Functions for SharkMath MCP Server
Consolidates all trigonometric operations into a single parameter-based tool.
"""
import math

class TrigonometryTool:
    """Consolidated trigonometry calculator with parameter-based routing."""
    
    @staticmethod
    def _validate_angle_unit(angle_unit: str) -> None:
        """Validate angle unit parameter."""
        if angle_unit not in ["radians", "degrees"]:
            raise ValueError(f"angle_unit must be 'radians' or 'degrees', got '{angle_unit}'")
    
    @staticmethod
    def _validate_domain_range(value: float, min_val: float, max_val: float, function_name: str) -> None:
        """Validate input is within valid domain range."""
        if value < min_val or value > max_val:
            raise ValueError(f"{function_name} domain is [{min_val}, {max_val}]. Input {value} is out of range!")
    
    @staticmethod
    def _check_tan_undefined(angle: float, angle_unit: str) -> bool:
        """Check if tangent is undefined at the given angle."""
        if angle_unit == "degrees":
            normalized = angle % 180
            return abs(normalized - 90) < 1e-10
        else:  # radians
            normalized = angle % math.pi
            return abs(normalized - math.pi/2) < 1e-10
    
    @staticmethod
    def _format_result(value: float, operation: str, input_val: float, angle_unit: str = None, second_val: float = None) -> str:
        """Format result with appropriate units and precision."""
        if operation in ["sin", "cos", "tan"]:
            unit_symbol = "°" if angle_unit == "degrees" else " rad"
            return f"✅ {operation}({input_val}{unit_symbol}) = {value}"
        elif operation in ["asin", "acos", "atan"]:
            degrees_result = math.degrees(value)
            return f"✅ arc{operation[1:]}({input_val}) = {value} rad = {degrees_result}°"
        elif operation == "atan2":
            degrees_result = math.degrees(value)
            return f"✅ atan2({input_val}, {second_val}) = {value} rad = {degrees_result}°"
        else:
            return f"✅ {operation}({input_val}) = {value}"
    
    @staticmethod
    def calculate(operation: str, angle: float = None, angle_unit: str = "radians", 
                 value: float = None, y: float = None, x: float = None) -> str:
        """
        Calculate trigonometric functions with parameter-based routing.
        
        Args:
            operation: The trigonometric operation to perform
                - "sin", "cos", "tan": Basic trigonometric functions
                - "asin", "acos", "atan": Inverse trigonometric functions  
                - "atan2": Two-argument arctangent
            angle: Input angle for basic trig functions
            angle_unit: "radians" or "degrees" for angle input (default: "radians")
            value: Input value for inverse trig functions
            y, x: Input values for atan2 function
            
        Returns:
            Formatted result string with ✅ success or ❌ error prefix
        """
        try:
            if operation in ["sin", "cos", "tan"]:
                if angle is None:
                    return f"❌ Error: {operation} requires 'angle' parameter"
                
                TrigonometryTool._validate_angle_unit(angle_unit)
                
                # Check for undefined tangent values
                if operation == "tan" and TrigonometryTool._check_tan_undefined(angle, angle_unit):
                    unit_desc = "90° + n*180°" if angle_unit == "degrees" else "π/2 + nπ rad"
                    return f"❌ Error: Tangent is undefined at {angle} ({unit_desc})"
                
                # Convert to radians if needed
                angle_rad = math.radians(angle) if angle_unit == "degrees" else angle
                
                # Calculate the function
                if operation == "sin":
                    result = math.sin(angle_rad)
                elif operation == "cos":
                    result = math.cos(angle_rad)
                elif operation == "tan":
                    result = math.tan(angle_rad)
                    # Check for very large results near undefined values
                    if abs(result) > 1e10:
                        unit_symbol = "°" if angle_unit == "degrees" else " rad"
                        return f"⚠️ tan({angle}{unit_symbol}) = {result} (very large, near undefined)"
                
                return TrigonometryTool._format_result(result, operation, angle, angle_unit)
                
            elif operation in ["asin", "acos", "atan"]:
                if value is None:
                    return f"❌ Error: {operation} requires 'value' parameter"
                
                # Domain validation for asin and acos
                if operation in ["asin", "acos"]:
                    TrigonometryTool._validate_domain_range(value, -1.0, 1.0, f"arc{operation[1:]}")
                
                # Calculate inverse trig function
                if operation == "asin":
                    result = math.asin(value)
                elif operation == "acos":
                    result = math.acos(value)
                elif operation == "atan":
                    result = math.atan(value)
                
                return TrigonometryTool._format_result(result, operation, value)
                
            elif operation == "atan2":
                if y is None or x is None:
                    return f"❌ Error: atan2 requires both 'y' and 'x' parameters"
                
                if x == 0 and y == 0:
                    return "❌ Error: atan2(0,0) is undefined!"
                
                result = math.atan2(y, x)
                return TrigonometryTool._format_result(result, operation, y, second_val=x)
                
            else:
                return f"❌ Error: Operation '{operation}' is not supported. Supported: sin, cos, tan, asin, acos, atan, atan2"
                
        except ValueError as e:
            return f"❌ Error: {str(e)}"
        except Exception as e:
            return f"❌ Error calculating {operation}: {str(e)}"

def register_tools(mcp):
    """Register consolidated trigonometry tool with the MCP server."""
    
    @mcp.tool()
    async def calculate_trigonometry(
        operation: str,
        angle: float = None,
        angle_unit: str = "radians",
        value: float = None,
        y: float = None,
        x: float = None
    ) -> str:
        """
        Calculate trigonometric and inverse trigonometric functions.
        
        This consolidated tool handles all trigonometric operations:
        - Basic functions: sin, cos, tan (with angle in radians or degrees)
        - Inverse functions: asin, acos, atan (returns radians and degrees)
        - Two-argument: atan2 (requires y and x parameters)
        
        Parameters:
        - operation: sin, cos, tan, asin, acos, atan, or atan2
        - angle: Input angle for basic trig functions
        - angle_unit: "radians" or "degrees" for angle input (default: radians)
        - value: Input value for inverse trig functions (must be in [-1,1] for asin/acos)
        - y, x: Coordinates for atan2 function
        
        Examples:
        - calculate_trigonometry("sin", angle=1.57, angle_unit="radians")
        - calculate_trigonometry("cos", angle=90, angle_unit="degrees") 
        - calculate_trigonometry("asin", value=0.5)
        - calculate_trigonometry("atan2", y=1, x=1)
        """
        return TrigonometryTool.calculate(operation, angle, angle_unit, value, y, x)

# Support direct execution for testing
if __name__ == "__main__":
    # Test cases for verification
    test_cases = [
        # Basic trigonometry in radians
        ("sin", {"angle": math.pi/2}),
        ("cos", {"angle": 0}),
        ("tan", {"angle": math.pi/4}),
        
        # Basic trigonometry in degrees  
        ("sin", {"angle": 90, "angle_unit": "degrees"}),
        ("cos", {"angle": 0, "angle_unit": "degrees"}),
        ("tan", {"angle": 45, "angle_unit": "degrees"}),
        
        # Inverse trigonometry
        ("asin", {"value": 1}),
        ("acos", {"value": 0}),
        ("atan", {"value": 1}),
        ("atan2", {"y": 1, "x": 1}),
        
        # Error cases
        ("tan", {"angle": 90, "angle_unit": "degrees"}),  # Undefined
        ("asin", {"value": 2}),  # Out of domain
        ("invalid", {"angle": 1}),  # Invalid operation
    ]
    
    print("Testing Consolidated Trigonometry Tool:")
    print("=" * 50)
    
    for operation, params in test_cases:
        result = TrigonometryTool.calculate(operation, **params)
        print(f"{operation}({params}): {result}")
        print()
