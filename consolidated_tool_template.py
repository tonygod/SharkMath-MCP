"""
Consolidated Tool Template for SharkMath MCP Server
This template provides the standard structure for parameter-based routing tools.
"""

import math
from typing import Dict, Callable, Any, Optional, Union

class ConsolidatedToolTemplate:
    """Base template for consolidated SharkMath tools with parameter-based routing."""
    
    def __init__(self, tool_name: str):
        self.tool_name = tool_name
        self.operations: Dict[str, Callable] = {}
        
    def register_operation(self, operation_name: str, function: Callable):
        """Register an operation with the consolidated tool."""
        self.operations[operation_name] = function
        
    def get_supported_operations(self) -> list:
        """Return list of supported operations."""
        return list(self.operations.keys())
        
    def validate_operation(self, operation: str) -> bool:
        """Check if operation is supported."""
        return operation in self.operations
        
    def format_success_response(self, operation: str, inputs: dict, result: Any) -> str:
        """Format successful operation response."""
        return f"✅ {operation}({', '.join(f'{k}={v}' for k, v in inputs.items())}) = {result}"
        
    def format_error_response(self, error_message: str) -> str:
        """Format error response."""
        return f"❌ {error_message}"
        
    async def execute_operation(self, operation: str, **kwargs) -> str:
        """Execute the specified operation with given parameters."""
        try:
            # Validate operation
            if not self.validate_operation(operation):
                supported = ", ".join(self.get_supported_operations())
                return self.format_error_response(
                    f"Operation '{operation}' not supported. Supported operations: {supported}"
                )
                
            # Execute operation
            result = self.operations[operation](**kwargs)
            return self.format_success_response(operation, kwargs, result)
            
        except TypeError as e:
            return self.format_error_response(f"Invalid parameters for {operation}: {str(e)}")
        except ValueError as e:
            return self.format_error_response(f"Invalid value for {operation}: {str(e)}")
        except ZeroDivisionError:
            return self.format_error_response(f"Division by zero in {operation}")
        except Exception as e:
            return self.format_error_response(f"Error in {operation}: {str(e)}")


class ConversionTool(ConsolidatedToolTemplate):
    """Specialized template for unit conversion tools."""
    
    def __init__(self):
        super().__init__("conversion_tool")
        self.conversion_factors: Dict[str, Dict[str, Union[float, Callable]]] = {}
        
    def register_conversion(self, from_unit: str, to_unit: str, conversion: Union[float, Callable]):
        """Register a conversion factor or function."""
        if from_unit not in self.conversion_factors:
            self.conversion_factors[from_unit] = {}
        self.conversion_factors[from_unit][to_unit] = conversion
        
    def get_conversion_key(self, from_unit: str, to_unit: str) -> str:
        """Generate conversion key for lookup."""
        return f"{from_unit}_to_{to_unit}"
        
    def validate_conversion(self, from_unit: str, to_unit: str) -> bool:
        """Check if conversion is supported."""
        return (from_unit in self.conversion_factors and 
                to_unit in self.conversion_factors[from_unit])
                
    async def convert(self, from_unit: str, to_unit: str, value: float, **kwargs) -> str:
        """Perform unit conversion."""
        try:
            # Input validation
            if not isinstance(value, (int, float)):
                return self.format_error_response(f"Value must be a number, got {type(value).__name__}")
                
            if not self.validate_conversion(from_unit, to_unit):
                return self.format_error_response(
                    f"Conversion from '{from_unit}' to '{to_unit}' not supported"
                )
                
            # Get conversion factor or function
            conversion = self.conversion_factors[from_unit][to_unit]
            
            # Apply conversion
            if callable(conversion):
                result = conversion(value, **kwargs)
            else:
                result = value * conversion
                
            # Format response based on conversion type
            if "time_hours" in kwargs and kwargs["time_hours"] != 1.0:
                return f"✅ {value} {from_unit} × {kwargs['time_hours']} hours = {result} {to_unit}"
            else:
                return f"✅ {value} {from_unit} = {result} {to_unit}"
                
        except Exception as e:
            return self.format_error_response(f"Conversion error: {str(e)}")


# Standard parameter validation functions
def validate_positive(value: float, param_name: str = "value") -> None:
    """Validate that a value is positive."""
    if value < 0:
        raise ValueError(f"{param_name} cannot be negative")
        
def validate_non_zero(value: float, param_name: str = "value") -> None:
    """Validate that a value is not zero."""
    if value == 0:
        raise ValueError(f"{param_name} cannot be zero")
        
def validate_range(value: float, min_val: float, max_val: float, param_name: str = "value") -> None:
    """Validate that a value is within a specified range."""
    if not (min_val <= value <= max_val):
        raise ValueError(f"{param_name} must be between {min_val} and {max_val}")
        
def validate_angle_unit(angle_unit: str) -> None:
    """Validate angle unit parameter."""
    valid_units = ["radians", "degrees"]
    if angle_unit not in valid_units:
        raise ValueError(f"angle_unit must be one of {valid_units}")

# Standard mathematical operations for reuse
def safe_divide(a: float, b: float) -> float:
    """Perform division with zero check."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def safe_sqrt(value: float) -> float:
    """Perform square root with domain check."""
    if value < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(value)

def safe_log(value: float, base: Optional[float] = None) -> float:
    """Perform logarithm with domain check."""
    if value <= 0:
        raise ValueError("Logarithm domain error: value must be positive")
    if base is not None:
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        return math.log(value) / math.log(base)
    return math.log(value)

# Example usage and testing functions
if __name__ == "__main__":
    # Example of how to use the template
    print("Consolidated Tool Template loaded successfully!")
    print("This template provides:")
    print("- ConsolidatedToolTemplate: Base class for parameter-based routing")
    print("- ConversionTool: Specialized class for unit conversions")  
    print("- Validation functions: Standard parameter validation")
    print("- Mathematical utilities: Safe mathematical operations")
