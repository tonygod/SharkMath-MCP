"""
Comprehensive test suite for computer_science_tools consolidated tool.

This test suite covers all computer science operations including:
- Base conversions (binary, octal, decimal, hexadecimal)
- Hash functions (MD5, SHA-1, SHA-256)
- Big O complexity analysis
- Data type size information
- Bitwise operations (AND, OR, XOR, NOT)
- Bit shift operations (left, right)
- ASCII/Character conversions

Each test validates both successful calculations and error handling.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from computer_science_tools import (
        _base_conversion, _hash_function, _big_o_analysis, _data_size,
        _bitwise_and, _bitwise_or, _bitwise_xor, _bitwise_not,
        _bit_shift_left, _bit_shift_right, _ascii_to_char, _char_to_ascii
    )
except ImportError:
    print("Warning: Could not import computer_science_tools functions directly")


class TestComputerScienceTools(unittest.TestCase):
    """Test suite for consolidated computer science tools."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sample_text = "Hello World"
        
    def test_base_conversion_decimal_to_binary(self):
        """Test decimal to binary conversion."""
        result = _base_conversion(value=42, from_base=10, to_base=2)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Output: 101010 (binary)", result)
        self.assertIn("Decimal equivalent: 42", result)
        
    def test_base_conversion_binary_to_decimal(self):
        """Test binary to decimal conversion."""
        result = _base_conversion(value=1010, from_base=2, to_base=10)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Output: 10 (decimal)", result)
        self.assertIn("Decimal equivalent: 10", result)
        
    def test_base_conversion_decimal_to_hex(self):
        """Test decimal to hexadecimal conversion."""
        result = _base_conversion(value=255, from_base=10, to_base=16)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Output: FF (hexadecimal)", result)
        self.assertIn("Decimal equivalent: 255", result)
        
    def test_base_conversion_octal_to_decimal(self):
        """Test octal to decimal conversion."""
        result = _base_conversion(value=77, from_base=8, to_base=10)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Output: 63 (decimal)", result)
        self.assertIn("Decimal equivalent: 63", result)
        
    def test_base_conversion_missing_params(self):
        """Test base conversion with missing parameters."""
        result = _base_conversion(value=None, from_base=10, to_base=2)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_base_conversion_invalid_base(self):
        """Test base conversion with invalid base."""
        result = _base_conversion(value=10, from_base=3, to_base=2)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("Supported bases", result)
        
    def test_base_conversion_invalid_binary(self):
        """Test base conversion with invalid binary digits."""
        result = _base_conversion(value=1029, from_base=2, to_base=10)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("Invalid binary number", result)
        
    def test_base_conversion_invalid_octal(self):
        """Test base conversion with invalid octal digits."""
        result = _base_conversion(value=89, from_base=8, to_base=10)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("Invalid octal number", result)
        
    def test_hash_function_md5(self):
        """Test MD5 hash generation."""
        result = _hash_function(text="hello", hash_algorithm="md5")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("MD5 Hash:", result)
        self.assertIn("5d41402abc4b2a76b9719d911017c592", result)
        
    def test_hash_function_sha1(self):
        """Test SHA-1 hash generation."""
        result = _hash_function(text="test", hash_algorithm="sha1")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("SHA-1 Hash:", result)
        self.assertIn("Length: 40 characters", result)
        
    def test_hash_function_sha256(self):
        """Test SHA-256 hash generation."""
        result = _hash_function(text="password", hash_algorithm="sha256")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("SHA-256 Hash:", result)
        self.assertIn("Length: 64 characters", result)
        
    def test_hash_function_missing_params(self):
        """Test hash function with missing parameters."""
        result = _hash_function(text=None, hash_algorithm="md5")
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_hash_function_invalid_algorithm(self):
        """Test hash function with invalid algorithm."""
        result = _hash_function(text="test", hash_algorithm="invalid")
        self.assertTrue(result.startswith("❌"))
        self.assertIn("Supported hash algorithms", result)
        
    def test_big_o_analysis_linear_search(self):
        """Test Big O analysis for linear search."""
        result = _big_o_analysis(algorithm="linear_search", input_size=1000)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Complexity: O(n)", result)
        self.assertIn("Estimated Operations: 1,000", result)
        
    def test_big_o_analysis_binary_search(self):
        """Test Big O analysis for binary search."""
        result = _big_o_analysis(algorithm="binary_search", input_size=1024)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Complexity: O(log n)", result)
        self.assertIn("Estimated Operations: 10", result)
        
    def test_big_o_analysis_bubble_sort(self):
        """Test Big O analysis for bubble sort."""
        result = _big_o_analysis(algorithm="bubble_sort", input_size=100)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Complexity: O(n²)", result)
        self.assertIn("Estimated Operations: 10,000", result)
        
    def test_big_o_analysis_no_input_size(self):
        """Test Big O analysis without input size."""
        result = _big_o_analysis(algorithm="merge_sort", input_size=None)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Complexity: O(n log n)", result)
        self.assertIn("Provide input_size", result)
        
    def test_big_o_analysis_invalid_algorithm(self):
        """Test Big O analysis with invalid algorithm."""
        result = _big_o_analysis(algorithm="invalid_sort", input_size=None)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("Supported algorithms", result)
        
    def test_big_o_analysis_large_input(self):
        """Test Big O analysis with very large input size."""
        result = _big_o_analysis(algorithm="linear_search", input_size=2000000)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("too large", result)
        
    def test_data_size_int(self):
        """Test data size for integer type."""
        result = _data_size(data_type="int")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Size: 4 bytes (32 bits)", result)
        self.assertIn("Integer (32-bit)", result)
        
    def test_data_size_float(self):
        """Test data size for float type."""
        result = _data_size(data_type="float")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Size: 4 bytes (32 bits)", result)
        self.assertIn("Single precision", result)
        
    def test_data_size_double(self):
        """Test data size for double type."""
        result = _data_size(data_type="double")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Size: 8 bytes (64 bits)", result)
        self.assertIn("Double precision", result)
        
    def test_data_size_string(self):
        """Test data size for string type."""
        result = _data_size(data_type="string")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Size: variable", result)
        self.assertIn("Depends on length", result)
        
    def test_data_size_invalid_type(self):
        """Test data size with invalid type."""
        result = _data_size(data_type="invalid_type")
        self.assertTrue(result.startswith("❌"))
        self.assertIn("Supported data types", result)
        
    def test_bitwise_and_operation(self):
        """Test bitwise AND operation."""
        result = _bitwise_and(operand1=12, operand2=10)  # 1100 & 1010 = 1000 = 8
        self.assertTrue(result.startswith("✅"))
        self.assertIn("12 (0b1100)", result)
        self.assertIn("10 (0b1010)", result)
        self.assertIn("= 8 (0b1000)", result)
        
    def test_bitwise_or_operation(self):
        """Test bitwise OR operation."""
        result = _bitwise_or(operand1=12, operand2=10)  # 1100 | 1010 = 1110 = 14
        self.assertTrue(result.startswith("✅"))
        self.assertIn("12 (0b1100)", result)
        self.assertIn("10 (0b1010)", result)
        self.assertIn("= 14 (0b1110)", result)
        
    def test_bitwise_xor_operation(self):
        """Test bitwise XOR operation."""
        result = _bitwise_xor(operand1=12, operand2=10)  # 1100 ^ 1010 = 0110 = 6
        self.assertTrue(result.startswith("✅"))
        self.assertIn("12 (0b1100)", result)
        self.assertIn("10 (0b1010)", result)
        self.assertIn("= 6 (0b110)", result)
        
    def test_bitwise_not_operation(self):
        """Test bitwise NOT operation."""
        result = _bitwise_not(value=15)  # ~00001111 = 11110000 = 240 (8-bit)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("~ 15 (00001111)", result)
        self.assertIn("= 240 (11110000)", result)
        
    def test_bitwise_and_missing_params(self):
        """Test bitwise AND with missing parameters."""
        result = _bitwise_and(operand1=None, operand2=10)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_bitwise_negative_operand(self):
        """Test bitwise operation with negative operand."""
        result = _bitwise_and(operand1=-5, operand2=10)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("non-negative integers", result)
        
    def test_bitwise_not_out_of_range(self):
        """Test bitwise NOT with value out of 8-bit range."""
        result = _bitwise_not(value=256)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("between 0 and 255", result)
        
    def test_bit_shift_left(self):
        """Test left bit shift operation."""
        result = _bit_shift_left(value=5, bit_position=2)  # 5 << 2 = 20
        self.assertTrue(result.startswith("✅"))
        self.assertIn("5 << 2", result)
        self.assertIn("= 20", result)
        self.assertIn("5 × 2^2 = 20", result)
        
    def test_bit_shift_right(self):
        """Test right bit shift operation."""
        result = _bit_shift_right(value=20, bit_position=2)  # 20 >> 2 = 5
        self.assertTrue(result.startswith("✅"))
        self.assertIn("20 >> 2", result)
        self.assertIn("= 5", result)
        self.assertIn("20 ÷ 2^2 = 5", result)
        
    def test_bit_shift_missing_params(self):
        """Test bit shift with missing parameters."""
        result = _bit_shift_left(value=None, bit_position=2)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_bit_shift_invalid_position(self):
        """Test bit shift with invalid position."""
        result = _bit_shift_left(value=5, bit_position=50)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("between 0 and 32", result)
        
    def test_ascii_to_char_printable(self):
        """Test ASCII to character conversion for printable character."""
        result = _ascii_to_char(value=65)  # 'A'
        self.assertTrue(result.startswith("✅"))
        self.assertIn("ASCII Code: 65", result)
        self.assertIn("Character: 'A'", result)
        self.assertIn("Hex: 0x41", result)
        
    def test_ascii_to_char_control(self):
        """Test ASCII to character conversion for control character."""
        result = _ascii_to_char(value=10)  # Line feed
        self.assertTrue(result.startswith("✅"))
        self.assertIn("ASCII Code: 10", result)
        self.assertIn("non-printable control character", result)
        
    def test_ascii_to_char_out_of_range(self):
        """Test ASCII to character with out-of-range value."""
        result = _ascii_to_char(value=200)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("between 0 and 127", result)
        
    def test_char_to_ascii_printable(self):
        """Test character to ASCII conversion for printable character."""
        result = _char_to_ascii(text="A")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Character: 'A'", result)
        self.assertIn("ASCII Code: 65", result)
        self.assertIn("Hex: 0x41", result)
        
    def test_char_to_ascii_multiple_chars(self):
        """Test character to ASCII with multiple characters."""
        result = _char_to_ascii(text="AB")
        self.assertTrue(result.startswith("❌"))
        self.assertIn("exactly one character", result)
        
    def test_char_to_ascii_non_ascii(self):
        """Test character to ASCII with non-ASCII character."""
        result = _char_to_ascii(text="ñ")
        self.assertTrue(result.startswith("❌"))
        self.assertIn("not standard ASCII", result)
        

if __name__ == '__main__':
    print("Running Computer Science Tools Tests...")
    print("=" * 60)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestComputerScienceTools)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print(f"\nFailures:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
            
    if result.errors:
        print(f"\nErrors:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun) * 100
    print(f"\nSuccess Rate: {success_rate:.1f}%")
