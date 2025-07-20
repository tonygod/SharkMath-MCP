"""
Test suite for matrix_operations.py module

Tests matrix operations: matrix_add, matrix_multiply, matrix_determinant, matrix_transpose
"""

import asyncio
import json
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import matrix_operations


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestMatrixOperations:
    """Test class for matrix operations."""
    
    def __init__(self):
        self.mcp = MockMCP()
        matrix_operations.register_tools(self.mcp)
    
    # Matrix addition tests
    
    async def test_matrix_add_2x2(self):
        """Test addition of 2x2 matrices."""
        matrix1 = "[[1,2],[3,4]]"
        matrix2 = "[[5,6],[7,8]]"
        result = await self.mcp.tools['matrix_add'](matrix1, matrix2)
        
        # Result should be [[6,8],[10,12]]
        return ("Matrix addition (2×2)" in result and
                "[[6, 8], [10, 12]]" in result)
    
    async def test_matrix_add_3x3(self):
        """Test addition of 3x3 matrices."""
        matrix1 = "[[1,0,2],[0,1,0],[2,0,1]]"
        matrix2 = "[[1,1,1],[1,1,1],[1,1,1]]"
        result = await self.mcp.tools['matrix_add'](matrix1, matrix2)
        
        # Result should be [[2,1,3],[1,2,1],[3,1,2]]
        return ("Matrix addition (3×3)" in result and
                "[[2, 1, 3], [1, 2, 1], [3, 1, 2]]" in result)
    
    async def test_matrix_add_dimension_mismatch(self):
        """Test matrix addition with dimension mismatch."""
        matrix1 = "[[1,2],[3,4]]"
        matrix2 = "[[1,2,3],[4,5,6]]"
        result = await self.mcp.tools['matrix_add'](matrix1, matrix2)
        
        return result.startswith("❌") and "dimensions don't match" in result
    
    async def test_matrix_add_invalid_json(self):
        """Test matrix addition with invalid JSON."""
        matrix1 = "[[1,2],[3,4]"  # Missing closing bracket
        matrix2 = "[[5,6],[7,8]]"
        result = await self.mcp.tools['matrix_add'](matrix1, matrix2)
        
        return result.startswith("❌") and "Invalid matrix format" in result
    
    # Matrix multiplication tests
    
    async def test_matrix_multiply_2x2(self):
        """Test multiplication of 2x2 matrices."""
        matrix1 = "[[1,2],[3,4]]"
        matrix2 = "[[5,6],[7,8]]"
        result = await self.mcp.tools['matrix_multiply'](matrix1, matrix2)
        
        # Result should be [[19,22],[43,50]]
        # [1*5+2*7, 1*6+2*8] = [19, 22]
        # [3*5+4*7, 3*6+4*8] = [43, 50]
        return ("Matrix multiplication (2×2 × 2×2 = 2×2)" in result and
                "[[19, 22], [43, 50]]" in result)
    
    async def test_matrix_multiply_different_dimensions(self):
        """Test multiplication of matrices with compatible dimensions."""
        matrix1 = "[[1,2,3],[4,5,6]]"  # 2x3
        matrix2 = "[[7,8],[9,10],[11,12]]"  # 3x2
        result = await self.mcp.tools['matrix_multiply'](matrix1, matrix2)
        
        # Result should be 2x2
        # [1*7+2*9+3*11, 1*8+2*10+3*12] = [58, 64]
        # [4*7+5*9+6*11, 4*8+5*10+6*12] = [139, 154]
        return ("Matrix multiplication (2×3 × 3×2 = 2×2)" in result and
                "[[58, 64], [139, 154]]" in result)
    
    async def test_matrix_multiply_incompatible_dimensions(self):
        """Test matrix multiplication with incompatible dimensions."""
        matrix1 = "[[1,2],[3,4]]"  # 2x2
        matrix2 = "[[1,2,3],[4,5,6],[7,8,9]]"  # 3x3
        result = await self.mcp.tools['matrix_multiply'](matrix1, matrix2)
        
        return (result.startswith("❌") and 
                "Cannot multiply matrices" in result and
                "Columns of first matrix" in result)
    
    # Matrix determinant tests
    
    async def test_matrix_determinant_1x1(self):
        """Test determinant of 1x1 matrix."""
        matrix = "[[5]]"
        result = await self.mcp.tools['matrix_determinant'](matrix)
        
        return ("Determinant of 1×1 matrix: 5" in result)
    
    async def test_matrix_determinant_2x2(self):
        """Test determinant of 2x2 matrix."""
        matrix = "[[1,2],[3,4]]"
        result = await self.mcp.tools['matrix_determinant'](matrix)
        
        # det = 1*4 - 2*3 = -2
        return ("Determinant of 2×2 matrix: -2" in result)
    
    async def test_matrix_determinant_3x3(self):
        """Test determinant of 3x3 matrix."""
        matrix = "[[1,0,2],[-1,5,0],[0,3,-9]]"
        result = await self.mcp.tools['matrix_determinant'](matrix)
        
        # Using cofactor expansion:
        # det = 1*(5*(-9) - 0*3) - 0*(...) + 2*(-1*3 - 5*0)
        # det = 1*(-45) + 2*(-3) = -45 - 6 = -51
        return ("Determinant of 3×3 matrix: -51" in result)
    
    async def test_matrix_determinant_identity_matrix(self):
        """Test determinant of identity matrix."""
        matrix = "[[1,0,0],[0,1,0],[0,0,1]]"
        result = await self.mcp.tools['matrix_determinant'](matrix)
        
        # Identity matrix has determinant 1
        return ("Determinant of 3×3 matrix: 1" in result)
    
    async def test_matrix_determinant_singular_matrix(self):
        """Test determinant of singular matrix (determinant = 0)."""
        matrix = "[[1,2],[2,4]]"  # Second row is 2 * first row
        result = await self.mcp.tools['matrix_determinant'](matrix)
        
        # det = 1*4 - 2*2 = 0
        return ("Determinant of 2×2 matrix: 0" in result)
    
    async def test_matrix_determinant_non_square(self):
        """Test determinant of non-square matrix."""
        matrix = "[[1,2,3],[4,5,6]]"  # 2x3 matrix
        result = await self.mcp.tools['matrix_determinant'](matrix)
        
        return result.startswith("❌") and "must be square" in result
    
    # Matrix transpose tests
    
    async def test_matrix_transpose_2x2(self):
        """Test transpose of 2x2 matrix."""
        matrix = "[[1,2],[3,4]]"
        result = await self.mcp.tools['matrix_transpose'](matrix)
        
        # Transpose should be [[1,3],[2,4]]
        return ("Matrix transpose (2×2 → 2×2)" in result and
                "[[1, 3], [2, 4]]" in result)
    
    async def test_matrix_transpose_2x3(self):
        """Test transpose of 2x3 matrix."""
        matrix = "[[1,2,3],[4,5,6]]"
        result = await self.mcp.tools['matrix_transpose'](matrix)
        
        # Transpose should be [[1,4],[2,5],[3,6]]
        return ("Matrix transpose (2×3 → 3×2)" in result and
                "[[1, 4], [2, 5], [3, 6]]" in result)
    
    async def test_matrix_transpose_3x2(self):
        """Test transpose of 3x2 matrix."""
        matrix = "[[1,4],[2,5],[3,6]]"
        result = await self.mcp.tools['matrix_transpose'](matrix)
        
        # Transpose should be [[1,2,3],[4,5,6]]
        return ("Matrix transpose (3×2 → 2×3)" in result and
                "[[1, 2, 3], [4, 5, 6]]" in result)
    
    async def test_matrix_transpose_1x4(self):
        """Test transpose of row vector."""
        matrix = "[[1,2,3,4]]"
        result = await self.mcp.tools['matrix_transpose'](matrix)
        
        # Transpose should be [[1],[2],[3],[4]]
        return ("Matrix transpose (1×4 → 4×1)" in result and
                "[[1], [2], [3], [4]]" in result)
    
    # Error handling tests
    
    async def test_matrix_empty(self):
        """Test with empty matrix."""
        matrix = "[]"
        result = await self.mcp.tools['matrix_determinant'](matrix)
        
        return result.startswith("❌") and "cannot be empty" in result
    
    async def test_matrix_non_numeric_values(self):
        """Test with non-numeric matrix values."""
        matrix1 = "[[1,'a'],[3,4]]"
        matrix2 = "[[1,2],[3,4]]"
        result = await self.mcp.tools['matrix_add'](matrix1, matrix2)
        
        return result.startswith("❌") and "non-numeric values" in result
    
    async def test_matrix_inconsistent_row_lengths(self):
        """Test with inconsistent row lengths."""
        matrix = "[[1,2,3],[4,5]]"  # Second row has different length
        result = await self.mcp.tools['matrix_transpose'](matrix)
        
        return result.startswith("❌") and "inconsistent length" in result
