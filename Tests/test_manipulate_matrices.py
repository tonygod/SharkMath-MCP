"""
Test suite for manipulate_matrices consolidated tool.
Tests matrix operations including addition, multiplication, determinant, and transpose.

Run with: python Tests/test_manipulate_matrices.py
"""

import unittest
import sys
import os
import json

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matrix_operations import register_tools


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestManipulateMatrices(unittest.TestCase):
    """Test cases for manipulate_matrices consolidated tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp = MockMCP()
        register_tools(self.mock_mcp)
        self.manipulate_matrices = self.mock_mcp.tools['manipulate_matrices']
    
    # Matrix Addition Tests
    async def test_matrix_add_2x2(self):
        """Test 2x2 matrix addition."""
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        result = await self.manipulate_matrices("add", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("✅ Matrix addition (2×2)", result)
        self.assertIn("[[6, 8], [10, 12]]", result)
    
    async def test_matrix_add_3x3(self):
        """Test 3x3 matrix addition."""
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        result = await self.manipulate_matrices("add", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("✅ Matrix addition (3×3)", result)
        self.assertIn("[[10, 10, 10], [10, 10, 10], [10, 10, 10]]", result)
    
    async def test_matrix_add_json_strings(self):
        """Test matrix addition with JSON string inputs."""
        matrix1_str = '[[1,2],[3,4]]'
        matrix2_str = '[[5,6],[7,8]]'
        result = await self.manipulate_matrices("add", matrix1=matrix1_str, matrix2=matrix2_str)
        self.assertIn("✅ Matrix addition (2×2)", result)
        self.assertIn("[[6, 8], [10, 12]]", result)
    
    async def test_matrix_add_mismatched_dimensions(self):
        """Test matrix addition with mismatched dimensions."""
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[1, 2, 3], [4, 5, 6]]
        result = await self.manipulate_matrices("add", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("❌ Matrix dimensions don't match", result)
    
    async def test_matrix_add_empty_matrix(self):
        """Test matrix addition with empty matrix."""
        matrix1 = []
        matrix2 = [[1, 2]]
        result = await self.manipulate_matrices("add", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("❌ Matrices cannot be empty", result)
    
    async def test_matrix_add_inconsistent_rows(self):
        """Test matrix addition with inconsistent row lengths."""
        matrix1 = [[1, 2], [3, 4, 5]]  # Inconsistent row length
        matrix2 = [[1, 2], [3, 4]]
        result = await self.manipulate_matrices("add", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("❌ Matrix1 row 1 has inconsistent length", result)
    
    async def test_matrix_add_non_numeric(self):
        """Test matrix addition with non-numeric values."""
        matrix1 = [[1, "a"], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        result = await self.manipulate_matrices("add", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("❌ Matrix1 contains non-numeric values", result)
    
    async def test_matrix_add_missing_parameters(self):
        """Test matrix addition with missing parameters."""
        result = await self.manipulate_matrices("add", matrix1=[[1, 2]])
        self.assertIn("❌ Matrix addition requires parameters: matrix1, matrix2", result)
    
    # Matrix Multiplication Tests
    async def test_matrix_multiply_2x2(self):
        """Test 2x2 matrix multiplication."""
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        result = await self.manipulate_matrices("multiply", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("✅ Matrix multiplication (2×2 × 2×2 = 2×2)", result)
        self.assertIn("[[19, 22], [43, 50]]", result)  # [1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]
    
    async def test_matrix_multiply_3x2_2x3(self):
        """Test 3×2 × 2×3 matrix multiplication."""
        matrix1 = [[1, 2], [3, 4], [5, 6]]  # 3×2
        matrix2 = [[7, 8, 9], [10, 11, 12]]  # 2×3
        result = await self.manipulate_matrices("multiply", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("✅ Matrix multiplication (3×2 × 2×3 = 3×3)", result)
        # Expected: [[1*7+2*10, 1*8+2*11, 1*9+2*12], [3*7+4*10, 3*8+4*11, 3*9+4*12], [5*7+6*10, 5*8+6*11, 5*9+6*12]]
        self.assertIn("[[27, 30, 33], [61, 68, 75], [95, 106, 117]]", result)
    
    async def test_matrix_multiply_incompatible_dimensions(self):
        """Test matrix multiplication with incompatible dimensions."""
        matrix1 = [[1, 2, 3], [4, 5, 6]]  # 2×3
        matrix2 = [[1, 2], [3, 4]]  # 2×2 (incompatible: 3 ≠ 2)
        result = await self.manipulate_matrices("multiply", matrix1=matrix1, matrix2=matrix2)
        self.assertIn("❌ Cannot multiply matrices: 2×3 × 2×2", result)
        self.assertIn("Columns of first matrix (3) must equal rows of second matrix (2)", result)
    
    async def test_matrix_multiply_json_strings(self):
        """Test matrix multiplication with JSON string inputs."""
        matrix1_str = '[[1,2],[3,4]]'
        matrix2_str = '[[2,0],[1,2]]'
        result = await self.manipulate_matrices("multiply", matrix1=matrix1_str, matrix2=matrix2_str)
        self.assertIn("✅ Matrix multiplication (2×2 × 2×2 = 2×2)", result)
        self.assertIn("[[4, 4], [10, 8]]", result)  # [[1*2+2*1, 1*0+2*2], [3*2+4*1, 3*0+4*2]]
    
    async def test_matrix_multiply_missing_parameters(self):
        """Test matrix multiplication with missing parameters."""
        result = await self.manipulate_matrices("multiply", matrix1=[[1, 2]])
        self.assertIn("❌ Matrix multiplication requires parameters: matrix1, matrix2", result)
    
    # Matrix Determinant Tests
    async def test_matrix_determinant_1x1(self):
        """Test determinant of 1×1 matrix."""
        matrix = [[5]]
        result = await self.manipulate_matrices("determinant", matrix=matrix)
        self.assertIn("✅ Determinant of 1×1 matrix: 5", result)
    
    async def test_matrix_determinant_2x2(self):
        """Test determinant of 2×2 matrix."""
        matrix = [[1, 2], [3, 4]]
        result = await self.manipulate_matrices("determinant", matrix=matrix)
        self.assertIn("✅ Determinant of 2×2 matrix: -2", result)  # 1*4 - 2*3 = -2
    
    async def test_matrix_determinant_3x3(self):
        """Test determinant of 3×3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = await self.manipulate_matrices("determinant", matrix=matrix)
        self.assertIn("✅ Determinant of 3×3 matrix: 0", result)  # This matrix is singular
    
    async def test_matrix_determinant_3x3_nonsingular(self):
        """Test determinant of 3×3 non-singular matrix."""
        matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        result = await self.manipulate_matrices("determinant", matrix=matrix)
        self.assertIn("✅ Determinant of 3×3 matrix: 1", result)
    
    async def test_matrix_determinant_json_string(self):
        """Test determinant with JSON string input."""
        matrix_str = '[[2,3],[1,4]]'
        result = await self.manipulate_matrices("determinant", matrix=matrix_str)
        self.assertIn("✅ Determinant of 2×2 matrix: 5", result)  # 2*4 - 3*1 = 5
    
    async def test_matrix_determinant_non_square(self):
        """Test determinant of non-square matrix."""
        matrix = [[1, 2, 3], [4, 5, 6]]  # 2×3 matrix
        result = await self.manipulate_matrices("determinant", matrix=matrix)
        self.assertIn("❌ Matrix must be square. Row 0 has length 3 but expected 2", result)
    
    async def test_matrix_determinant_too_large(self):
        """Test determinant of matrix that's too large."""
        # Create an 11×11 matrix
        matrix = [[i*j for j in range(11)] for i in range(11)]
        result = await self.manipulate_matrices("determinant", matrix=matrix)
        self.assertIn("❌ Matrix too large for determinant calculation. Maximum supported size is 10×10, got 11×11", result)
    
    async def test_matrix_determinant_missing_parameter(self):
        """Test determinant with missing parameter."""
        result = await self.manipulate_matrices("determinant")
        self.assertIn("❌ Matrix determinant requires parameter: matrix", result)
    
    # Matrix Transpose Tests
    async def test_matrix_transpose_2x2(self):
        """Test transpose of 2×2 matrix."""
        matrix = [[1, 2], [3, 4]]
        result = await self.manipulate_matrices("transpose", matrix=matrix)
        self.assertIn("✅ Matrix transpose (2×2 → 2×2)", result)
        self.assertIn("[[1, 3], [2, 4]]", result)
    
    async def test_matrix_transpose_2x3(self):
        """Test transpose of 2×3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = await self.manipulate_matrices("transpose", matrix=matrix)
        self.assertIn("✅ Matrix transpose (2×3 → 3×2)", result)
        self.assertIn("[[1, 4], [2, 5], [3, 6]]", result)
    
    async def test_matrix_transpose_3x2(self):
        """Test transpose of 3×2 matrix."""
        matrix = [[1, 2], [3, 4], [5, 6]]
        result = await self.manipulate_matrices("transpose", matrix=matrix)
        self.assertIn("✅ Matrix transpose (3×2 → 2×3)", result)
        self.assertIn("[[1, 3, 5], [2, 4, 6]]", result)
    
    async def test_matrix_transpose_1x3(self):
        """Test transpose of 1×3 matrix (row vector)."""
        matrix = [[1, 2, 3]]
        result = await self.manipulate_matrices("transpose", matrix=matrix)
        self.assertIn("✅ Matrix transpose (1×3 → 3×1)", result)
        self.assertIn("[[1], [2], [3]]", result)
    
    async def test_matrix_transpose_json_string(self):
        """Test transpose with JSON string input."""
        matrix_str = '[[1,2,3],[4,5,6]]'
        result = await self.manipulate_matrices("transpose", matrix=matrix_str)
        self.assertIn("✅ Matrix transpose (2×3 → 3×2)", result)
        self.assertIn("[[1, 4], [2, 5], [3, 6]]", result)
    
    async def test_matrix_transpose_missing_parameter(self):
        """Test transpose with missing parameter."""
        result = await self.manipulate_matrices("transpose")
        self.assertIn("❌ Matrix transpose requires parameter: matrix", result)
    
    # Error Handling Tests
    async def test_invalid_json_format(self):
        """Test invalid JSON format."""
        result = await self.manipulate_matrices("add", matrix1="invalid_json", matrix2="[[1,2]]")
        self.assertIn("❌ Invalid matrix format", result)
        self.assertIn("Use JSON format like [[1,2],[3,4]]", result)
    
    async def test_non_2d_list(self):
        """Test non-2D list input."""
        result = await self.manipulate_matrices("add", matrix1="[1,2,3]", matrix2="[[1,2]]")
        self.assertIn("❌ Matrices must be 2D arrays (lists of lists)", result)
    
    async def test_invalid_operation(self):
        """Test invalid operation."""
        result = await self.manipulate_matrices("invalid_operation", matrix=[[1, 2]])
        self.assertIn("❌ Invalid operation 'invalid_operation'", result)
        self.assertIn("Valid operations: add, multiply, determinant, transpose", result)
    
    async def test_empty_operation(self):
        """Test empty operation."""
        result = await self.manipulate_matrices("", matrix=[[1, 2]])
        self.assertIn("❌ Invalid operation", result)


def run_async_test(coro):
    """Helper to run async test functions."""
    import asyncio
    return asyncio.run(coro)


if __name__ == '__main__':
    # Create test suite with async support
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test methods
    test_instance = TestManipulateMatrices()
    test_instance.setUp()
    
    test_methods = [
        'test_matrix_add_2x2',
        'test_matrix_add_3x3',
        'test_matrix_add_json_strings',
        'test_matrix_add_mismatched_dimensions',
        'test_matrix_add_empty_matrix',
        'test_matrix_add_inconsistent_rows',
        'test_matrix_add_non_numeric',
        'test_matrix_add_missing_parameters',
        'test_matrix_multiply_2x2',
        'test_matrix_multiply_3x2_2x3',
        'test_matrix_multiply_incompatible_dimensions',
        'test_matrix_multiply_json_strings',
        'test_matrix_multiply_missing_parameters',
        'test_matrix_determinant_1x1',
        'test_matrix_determinant_2x2',
        'test_matrix_determinant_3x3',
        'test_matrix_determinant_3x3_nonsingular',
        'test_matrix_determinant_json_string',
        'test_matrix_determinant_non_square',
        'test_matrix_determinant_too_large',
        'test_matrix_determinant_missing_parameter',
        'test_matrix_transpose_2x2',
        'test_matrix_transpose_2x3',
        'test_matrix_transpose_3x2',
        'test_matrix_transpose_1x3',
        'test_matrix_transpose_json_string',
        'test_matrix_transpose_missing_parameter',
        'test_invalid_json_format',
        'test_non_2d_list',
        'test_invalid_operation',
        'test_empty_operation'
    ]
    
    print("Running manipulate_matrices consolidated tool tests...")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for method_name in test_methods:
        try:
            method = getattr(test_instance, method_name)
            run_async_test(method())
            print(f"✅ {method_name}")
            passed += 1
        except Exception as e:
            print(f"❌ {method_name}: {str(e)}")
            failed += 1
    
    print("=" * 50)
    print(f"Tests passed: {passed}")
    print(f"Tests failed: {failed}")
    print(f"Total tests: {passed + failed}")
    
    if failed == 0:
        print("✅ All manipulate_matrices tests passed!")
    else:
        print(f"❌ {failed} test(s) failed")
