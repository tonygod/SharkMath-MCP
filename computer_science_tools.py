"""
Computer Science Tools Module for SharkMath MCP Server

This module provides consolidated computer science and programming-related functions including:
- Base conversions (binary, octal, hexadecimal, decimal)
- Hash functions (MD5, SHA-1, SHA-256)
- Algorithm complexity analysis helpers
- Data structure size calculations
- Bitwise operations
- Character encoding conversions
- Big O notation helpers

All functions follow the SharkMath error handling standards with ✅/❌ prefixes.
This is a consolidated tool using parameter-based routing.
"""

import hashlib
import math
from typing import Optional


def register_tools(mcp):
    """Register consolidated computer science tools with the MCP server."""
    
    @mcp.tool()
    async def computer_science_tools(
        operation: str,
        value: Optional[int] = None,
        text: Optional[str] = None,
        from_base: Optional[int] = None,
        to_base: Optional[int] = None,
        algorithm: Optional[str] = None,
        input_size: Optional[int] = None,
        hash_algorithm: Optional[str] = None,
        bit_position: Optional[int] = None,
        operand1: Optional[int] = None,
        operand2: Optional[int] = None,
        data_type: Optional[str] = None
    ) -> str:
        """
        Perform various computer science and programming calculations.
        
        Args:
            operation: Type of operation - "base_conversion", "hash_function", "big_o_analysis",
                      "data_size", "bitwise_and", "bitwise_or", "bitwise_xor", "bitwise_not",
                      "bit_shift_left", "bit_shift_right", "ascii_to_char", "char_to_ascii"
            value: Integer value for base conversions, bitwise operations, ASCII conversions
            text: String value for hash functions and character operations
            from_base: Source base for conversions (2, 8, 10, 16)
            to_base: Target base for conversions (2, 8, 10, 16)
            algorithm: Algorithm name for Big O analysis
            input_size: Input size for complexity calculations
            hash_algorithm: Hash algorithm type ("md5", "sha1", "sha256")
            bit_position: Bit position for shift operations
            operand1: First operand for bitwise operations
            operand2: Second operand for bitwise operations
            data_type: Data type for size calculations ("int", "float", "char", "bool")
            
        Returns:
            String with calculation results and explanations
        """
        
        # Define valid operations
        valid_operations = {
            "base_conversion": _base_conversion,
            "hash_function": _hash_function,
            "big_o_analysis": _big_o_analysis,
            "data_size": _data_size,
            "bitwise_and": _bitwise_and,
            "bitwise_or": _bitwise_or,
            "bitwise_xor": _bitwise_xor,
            "bitwise_not": _bitwise_not,
            "bit_shift_left": _bit_shift_left,
            "bit_shift_right": _bit_shift_right,
            "ascii_to_char": _ascii_to_char,
            "char_to_ascii": _char_to_ascii
        }
        
        # Validate operation
        if operation not in valid_operations:
            valid_ops = ", ".join(valid_operations.keys())
            return f"❌ Invalid operation '{operation}'. Valid operations: {valid_ops}"
        
        try:
            # Route to appropriate function
            return valid_operations[operation](
                value=value, text=text, from_base=from_base, to_base=to_base,
                algorithm=algorithm, input_size=input_size, hash_algorithm=hash_algorithm,
                bit_position=bit_position, operand1=operand1, operand2=operand2,
                data_type=data_type
            )
            
        except Exception as e:
            return f"❌ Error in {operation}: {str(e)}"


def _base_conversion(value: Optional[int], from_base: Optional[int], to_base: Optional[int], **kwargs) -> str:
    """
    Convert numbers between different bases (2, 8, 10, 16).
    """
    if value is None or from_base is None or to_base is None:
        return "❌ Base conversion requires parameters: value, from_base, to_base"
    
    # Validate bases
    valid_bases = [2, 8, 10, 16]
    if from_base not in valid_bases or to_base not in valid_bases:
        return f"❌ Supported bases: {valid_bases}"
    
    # Input validation
    if value < 0:
        return "❌ Value cannot be negative for base conversion"
    
    try:
        # Convert to decimal first (if not already)
        if from_base == 10:
            decimal_value = value
        elif from_base == 2:
            # Validate binary digits
            if any(digit not in '01' for digit in str(value)):
                return "❌ Invalid binary number - only 0 and 1 allowed"
            decimal_value = int(str(value), 2)
        elif from_base == 8:
            # Validate octal digits
            if any(digit not in '01234567' for digit in str(value)):
                return "❌ Invalid octal number - only digits 0-7 allowed"
            decimal_value = int(str(value), 8)
        elif from_base == 16:
            # For hex, value should be string but we'll handle int input
            decimal_value = int(str(value), 16)
        
        # Convert from decimal to target base
        if to_base == 10:
            result = str(decimal_value)
            base_name = "decimal"
        elif to_base == 2:
            result = bin(decimal_value)[2:]  # Remove '0b' prefix
            base_name = "binary"
        elif to_base == 8:
            result = oct(decimal_value)[2:]  # Remove '0o' prefix
            base_name = "octal"
        elif to_base == 16:
            result = hex(decimal_value)[2:].upper()  # Remove '0x' prefix, uppercase
            base_name = "hexadecimal"
            
        # Base names for display
        base_names = {2: "binary", 8: "octal", 10: "decimal", 16: "hexadecimal"}
        
        return (f"✅ Base Conversion:\n"
               f"   Input: {value} ({base_names[from_base]})\n"
               f"   Output: {result} ({base_name})\n"
               f"   Decimal equivalent: {decimal_value}")
        
    except ValueError as e:
        return f"❌ Invalid number format for base {from_base}: {str(e)}"


def _hash_function(text: Optional[str], hash_algorithm: Optional[str], **kwargs) -> str:
    """
    Generate hash values for text using various algorithms.
    """
    if text is None or hash_algorithm is None:
        return "❌ Hash function requires parameters: text, hash_algorithm"
    
    # Validate hash algorithm
    valid_algorithms = ["md5", "sha1", "sha256"]
    if hash_algorithm.lower() not in valid_algorithms:
        return f"❌ Supported hash algorithms: {valid_algorithms}"
    
    try:
        # Encode text to bytes
        text_bytes = text.encode('utf-8')
        
        # Generate hash based on algorithm
        algorithm = hash_algorithm.lower()
        if algorithm == "md5":
            hash_obj = hashlib.md5(text_bytes)
            hash_name = "MD5"
        elif algorithm == "sha1":
            hash_obj = hashlib.sha1(text_bytes)
            hash_name = "SHA-1"
        elif algorithm == "sha256":
            hash_obj = hashlib.sha256(text_bytes)
            hash_name = "SHA-256"
        
        hex_digest = hash_obj.hexdigest()
        
        return (f"✅ {hash_name} Hash:\n"
               f"   Input: \"{text}\"\n"
               f"   Hash: {hex_digest}\n"
               f"   Length: {len(hex_digest)} characters\n"
               f"   Algorithm: {hash_name}")
        
    except Exception as e:
        return f"❌ Error generating {hash_algorithm.upper()} hash: {str(e)}"


def _big_o_analysis(algorithm: Optional[str], input_size: Optional[int] = None, **kwargs) -> str:
    """
    Analyze algorithm complexity and estimate operations for given input size.
    """
    if algorithm is None:
        return "❌ Big O analysis requires parameter: algorithm"
    
    # Define common algorithm complexities
    complexities = {
        "linear_search": ("O(n)", lambda n: n),
        "binary_search": ("O(log n)", lambda n: math.log2(n) if n > 0 else 0),
        "bubble_sort": ("O(n²)", lambda n: n * n),
        "merge_sort": ("O(n log n)", lambda n: n * math.log2(n) if n > 0 else 0),
        "quick_sort": ("O(n log n)", lambda n: n * math.log2(n) if n > 0 else 0),
        "selection_sort": ("O(n²)", lambda n: n * n),
        "insertion_sort": ("O(n²)", lambda n: n * n),
        "heap_sort": ("O(n log n)", lambda n: n * math.log2(n) if n > 0 else 0),
        "constant_time": ("O(1)", lambda n: 1),
        "factorial": ("O(n!)", lambda n: math.factorial(min(n, 10)))  # Limit for safety
    }
    
    # Validate algorithm
    if algorithm.lower() not in complexities:
        valid_algorithms = ", ".join(complexities.keys())
        return f"❌ Supported algorithms: {valid_algorithms}"
    
    algorithm_key = algorithm.lower()
    complexity_notation, complexity_func = complexities[algorithm_key]
    
    # Calculate operations if input size provided
    if input_size is not None:
        if input_size < 0:
            return "❌ Input size cannot be negative"
        if input_size > 1000000:  # Limit for safety
            return "❌ Input size too large (max: 1,000,000)"
        
        try:
            operations = complexity_func(input_size)
            if operations > 10**12:  # Very large number
                operations_str = f"{operations:.2e}"
            else:
                operations_str = f"{operations:,.0f}"
                
            return (f"✅ Big O Analysis:\n"
                   f"   Algorithm: {algorithm.replace('_', ' ').title()}\n"
                   f"   Complexity: {complexity_notation}\n"
                   f"   Input Size: {input_size:,}\n"
                   f"   Estimated Operations: {operations_str}")
        except (ValueError, OverflowError):
            return f"❌ Cannot calculate operations for input size {input_size} with complexity {complexity_notation}"
    else:
        return (f"✅ Big O Analysis:\n"
               f"   Algorithm: {algorithm.replace('_', ' ').title()}\n"
               f"   Complexity: {complexity_notation}\n"
               f"   (Provide input_size for operation count estimate)")


def _data_size(data_type: Optional[str], **kwargs) -> str:
    """
    Show typical data type sizes in bytes.
    """
    if data_type is None:
        return "❌ Data size requires parameter: data_type"
    
    # Common data type sizes (in bytes)
    type_sizes = {
        "bool": (1, "Boolean value"),
        "char": (1, "Single character (ASCII)"),
        "short": (2, "Short integer"),
        "int": (4, "Integer (32-bit)"),
        "long": (8, "Long integer (64-bit)"),
        "float": (4, "Single precision floating point"),
        "double": (8, "Double precision floating point"),
        "pointer": (8, "Memory address (64-bit system)"),
        "string": ("variable", "Depends on length and encoding")
    }
    
    # Validate data type
    if data_type.lower() not in type_sizes:
        valid_types = ", ".join(type_sizes.keys())
        return f"❌ Supported data types: {valid_types}"
    
    data_type_key = data_type.lower()
    size, description = type_sizes[data_type_key]
    
    if isinstance(size, int):
        bits = size * 8
        return (f"✅ Data Type Size:\n"
               f"   Type: {data_type.upper()}\n"
               f"   Size: {size} bytes ({bits} bits)\n"
               f"   Description: {description}")
    else:
        return (f"✅ Data Type Size:\n"
               f"   Type: {data_type.upper()}\n"
               f"   Size: {size}\n"
               f"   Description: {description}")


def _bitwise_and(operand1: Optional[int], operand2: Optional[int], **kwargs) -> str:
    """
    Perform bitwise AND operation.
    """
    if operand1 is None or operand2 is None:
        return "❌ Bitwise AND requires parameters: operand1, operand2"
    
    if operand1 < 0 or operand2 < 0:
        return "❌ Operands must be non-negative integers"
    
    result = operand1 & operand2
    
    return (f"✅ Bitwise AND:\n"
           f"   {operand1} ({bin(operand1)})\n"
           f" & {operand2} ({bin(operand2)})\n"
           f" = {result} ({bin(result)})")


def _bitwise_or(operand1: Optional[int], operand2: Optional[int], **kwargs) -> str:
    """
    Perform bitwise OR operation.
    """
    if operand1 is None or operand2 is None:
        return "❌ Bitwise OR requires parameters: operand1, operand2"
    
    if operand1 < 0 or operand2 < 0:
        return "❌ Operands must be non-negative integers"
    
    result = operand1 | operand2
    
    return (f"✅ Bitwise OR:\n"
           f"   {operand1} ({bin(operand1)})\n"
           f" | {operand2} ({bin(operand2)})\n"
           f" = {result} ({bin(result)})")


def _bitwise_xor(operand1: Optional[int], operand2: Optional[int], **kwargs) -> str:
    """
    Perform bitwise XOR operation.
    """
    if operand1 is None or operand2 is None:
        return "❌ Bitwise XOR requires parameters: operand1, operand2"
    
    if operand1 < 0 or operand2 < 0:
        return "❌ Operands must be non-negative integers"
    
    result = operand1 ^ operand2
    
    return (f"✅ Bitwise XOR:\n"
           f"   {operand1} ({bin(operand1)})\n"
           f" ^ {operand2} ({bin(operand2)})\n"
           f" = {result} ({bin(result)})")


def _bitwise_not(value: Optional[int], **kwargs) -> str:
    """
    Perform bitwise NOT operation (limited to 8 bits for readability).
    """
    if value is None:
        return "❌ Bitwise NOT requires parameter: value"
    
    if value < 0 or value > 255:
        return "❌ Value must be between 0 and 255 (8-bit)"
    
    # Calculate NOT for 8-bit representation
    result = (~value) & 0xFF  # Mask to 8 bits
    
    return (f"✅ Bitwise NOT (8-bit):\n"
           f" ~ {value} ({bin(value)[2:].zfill(8)})\n"
           f" = {result} ({bin(result)[2:].zfill(8)})")


def _bit_shift_left(value: Optional[int], bit_position: Optional[int], **kwargs) -> str:
    """
    Perform left bit shift operation.
    """
    if value is None or bit_position is None:
        return "❌ Bit shift left requires parameters: value, bit_position"
    
    if value < 0:
        return "❌ Value must be non-negative"
    
    if bit_position < 0 or bit_position > 32:
        return "❌ Bit position must be between 0 and 32"
    
    result = value << bit_position
    
    return (f"✅ Left Bit Shift:\n"
           f"   {value} << {bit_position}\n"
           f"   {value} ({bin(value)}) << {bit_position}\n"
           f" = {result} ({bin(result)})\n"
           f"   Equivalent to: {value} × 2^{bit_position} = {value * (2**bit_position)}")


def _bit_shift_right(value: Optional[int], bit_position: Optional[int], **kwargs) -> str:
    """
    Perform right bit shift operation.
    """
    if value is None or bit_position is None:
        return "❌ Bit shift right requires parameters: value, bit_position"
    
    if value < 0:
        return "❌ Value must be non-negative"
    
    if bit_position < 0 or bit_position > 32:
        return "❌ Bit position must be between 0 and 32"
    
    result = value >> bit_position
    
    return (f"✅ Right Bit Shift:\n"
           f"   {value} >> {bit_position}\n"
           f"   {value} ({bin(value)}) >> {bit_position}\n"
           f" = {result} ({bin(result)})\n"
           f"   Equivalent to: {value} ÷ 2^{bit_position} = {value // (2**bit_position)}")


def _ascii_to_char(value: Optional[int], **kwargs) -> str:
    """
    Convert ASCII code to character.
    """
    if value is None:
        return "❌ ASCII to char requires parameter: value"
    
    if value < 0 or value > 127:
        return "❌ ASCII value must be between 0 and 127"
    
    try:
        char = chr(value)
        # Handle non-printable characters
        if value < 32:
            char_description = f"'{char}' (non-printable control character)"
        elif value == 127:
            char_description = "'DEL' (delete character)"
        else:
            char_description = f"'{char}'"
        
        return (f"✅ ASCII to Character:\n"
               f"   ASCII Code: {value}\n"
               f"   Character: {char_description}\n"
               f"   Binary: {bin(value)}\n"
               f"   Hex: 0x{value:02X}")
        
    except ValueError as e:
        return f"❌ Cannot convert ASCII code {value}: {str(e)}"


def _char_to_ascii(text: Optional[str], **kwargs) -> str:
    """
    Convert character to ASCII code.
    """
    if text is None:
        return "❌ Char to ASCII requires parameter: text"
    
    if len(text) != 1:
        return "❌ Text must be exactly one character"
    
    char = text[0]
    ascii_value = ord(char)
    
    if ascii_value > 127:
        return f"❌ Character '{char}' is not standard ASCII (code: {ascii_value})"
    
    # Handle non-printable characters
    if ascii_value < 32:
        char_description = f"'{char}' (non-printable control character)"
    elif ascii_value == 127:
        char_description = "'DEL' (delete character)"
    else:
        char_description = f"'{char}'"
    
    return (f"✅ Character to ASCII:\n"
           f"   Character: {char_description}\n"
           f"   ASCII Code: {ascii_value}\n"
           f"   Binary: {bin(ascii_value)}\n"
           f"   Hex: 0x{ascii_value:02X}")


# Support for direct execution (testing)
if __name__ == "__main__":
    print("Computer Science Tools Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
