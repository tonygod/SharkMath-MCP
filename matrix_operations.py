"""
Matrix Operations Module for SharkMath MCP Server

This module provides matrix operations and linear algebra functions including:
- Matrix addition and multiplication
- Matrix determinant calculation
- Matrix transpose operation

All functions follow the SharkMath error handling standards with ✅/❌ prefixes.
Matrix input format: JSON string representing 2D array, e.g., "[[1,2],[3,4]]"
"""

import json
from typing import Union


def register_tools(mcp):
    """Register all matrix operation tools with the MCP server."""
    
    @mcp.tool()
    async def matrix_add(matrix1: Union[str, list], matrix2: Union[str, list]) -> str:
        """
        Add two matrices of the same dimensions.
        
        Args:
            matrix1: JSON string or list representing first matrix, e.g., "[[1,2],[3,4]]" or [[1,2],[3,4]]
            matrix2: JSON string or list representing second matrix, e.g., "[[5,6],[7,8]]" or [[5,6],[7,8]]
            
        Returns:
            String with the resulting matrix or error message
        """
        try:
            # Parse input matrices - handle both string and list inputs
            try:
                if isinstance(matrix1, str):
                    m1 = json.loads(matrix1)
                else:
                    m1 = matrix1
                    
                if isinstance(matrix2, str):
                    m2 = json.loads(matrix2)
                else:
                    m2 = matrix2
            except json.JSONDecodeError as e:
                return f"❌ Invalid matrix format. Use JSON format like [[1,2],[3,4]]. Error: {str(e)}"
            
            # Validate matrices are 2D lists
            if not isinstance(m1, list) or not isinstance(m2, list):
                return "❌ Matrices must be 2D arrays (lists of lists)"
            
            if not all(isinstance(row, list) for row in m1) or not all(isinstance(row, list) for row in m2):
                return "❌ Matrices must be 2D arrays (lists of lists)"
            
            # Check dimensions
            if len(m1) == 0 or len(m2) == 0:
                return "❌ Matrices cannot be empty"
            
            if len(m1) != len(m2):
                return f"❌ Matrix dimensions don't match: {len(m1)}×? vs {len(m2)}×?"
            
            if len(m1[0]) != len(m2[0]):
                return f"❌ Matrix dimensions don't match: ?×{len(m1[0])} vs ?×{len(m2[0])}"
            
            # Validate consistent row lengths
            for i, row in enumerate(m1):
                if len(row) != len(m1[0]):
                    return f"❌ Matrix1 row {i} has inconsistent length: {len(row)} vs {len(m1[0])}"
                if not all(isinstance(x, (int, float)) for x in row):
                    return f"❌ Matrix1 contains non-numeric values in row {i}"
            
            for i, row in enumerate(m2):
                if len(row) != len(m2[0]):
                    return f"❌ Matrix2 row {i} has inconsistent length: {len(row)} vs {len(m2[0])}"
                if not all(isinstance(x, (int, float)) for x in row):
                    return f"❌ Matrix2 contains non-numeric values in row {i}"
            
            # Perform matrix addition
            result = []
            for i in range(len(m1)):
                row = []
                for j in range(len(m1[0])):
                    row.append(m1[i][j] + m2[i][j])
                result.append(row)
            
            # Format result
            rows, cols = len(result), len(result[0])
            result_str = json.dumps(result)
            return f"✅ Matrix addition ({rows}×{cols}):\n   Result: {result_str}"
            
        except Exception as e:
            return f"❌ Error performing matrix addition: {str(e)}"

    @mcp.tool()
    async def matrix_multiply(matrix1: Union[str, list], matrix2: Union[str, list]) -> str:
        """
        Multiply two matrices (matrix1 × matrix2).
        For multiplication to be valid, the number of columns in matrix1 must equal the number of rows in matrix2.
        
        Args:
            matrix1: JSON string or list representing first matrix, e.g., "[[1,2],[3,4]]" or [[1,2],[3,4]]
            matrix2: JSON string or list representing second matrix, e.g., "[[5,6],[7,8]]" or [[5,6],[7,8]]
            
        Returns:
            String with the resulting matrix or error message
        """
        try:
            # Parse input matrices - handle both string and list inputs
            try:
                if isinstance(matrix1, str):
                    m1 = json.loads(matrix1)
                else:
                    m1 = matrix1
                    
                if isinstance(matrix2, str):
                    m2 = json.loads(matrix2)
                else:
                    m2 = matrix2
            except json.JSONDecodeError as e:
                return f"❌ Invalid matrix format. Use JSON format like [[1,2],[3,4]]. Error: {str(e)}"
            
            # Validate matrices are 2D lists
            if not isinstance(m1, list) or not isinstance(m2, list):
                return "❌ Matrices must be 2D arrays (lists of lists)"
            
            if not all(isinstance(row, list) for row in m1) or not all(isinstance(row, list) for row in m2):
                return "❌ Matrices must be 2D arrays (lists of lists)"
            
            # Check dimensions
            if len(m1) == 0 or len(m2) == 0:
                return "❌ Matrices cannot be empty"
            
            # Validate consistent row lengths and numeric values
            for i, row in enumerate(m1):
                if len(row) != len(m1[0]):
                    return f"❌ Matrix1 row {i} has inconsistent length: {len(row)} vs {len(m1[0])}"
                if not all(isinstance(x, (int, float)) for x in row):
                    return f"❌ Matrix1 contains non-numeric values in row {i}"
            
            for i, row in enumerate(m2):
                if len(row) != len(m2[0]):
                    return f"❌ Matrix2 row {i} has inconsistent length: {len(row)} vs {len(m2[0])}"
                if not all(isinstance(x, (int, float)) for x in row):
                    return f"❌ Matrix2 contains non-numeric values in row {i}"
            
            # Check multiplication compatibility
            m1_rows, m1_cols = len(m1), len(m1[0])
            m2_rows, m2_cols = len(m2), len(m2[0])
            
            if m1_cols != m2_rows:
                return f"❌ Cannot multiply matrices: {m1_rows}×{m1_cols} × {m2_rows}×{m2_cols}. Columns of first matrix ({m1_cols}) must equal rows of second matrix ({m2_rows})"
            
            # Perform matrix multiplication
            result = []
            for i in range(m1_rows):
                row = []
                for j in range(m2_cols):
                    # Calculate dot product of row i from m1 and column j from m2
                    dot_product = sum(m1[i][k] * m2[k][j] for k in range(m1_cols))
                    row.append(dot_product)
                result.append(row)
            
            # Format result
            result_str = json.dumps(result)
            return f"✅ Matrix multiplication ({m1_rows}×{m1_cols} × {m2_rows}×{m2_cols} = {m1_rows}×{m2_cols}):\n   Result: {result_str}"
            
        except Exception as e:
            return f"❌ Error performing matrix multiplication: {str(e)}"

    @mcp.tool()
    async def matrix_determinant(matrix: Union[str, list]) -> str:
        """
        Calculate the determinant of a square matrix.
        Supports matrices up to reasonable size using recursive expansion.
        
        Args:
            matrix: JSON string or list representing square matrix, e.g., "[[1,2],[3,4]]" or [[1,2],[3,4]]
            
        Returns:
            String with the determinant value or error message
        """
        try:
            # Parse input matrix - handle both string and list inputs
            try:
                if isinstance(matrix, str):
                    m = json.loads(matrix)
                else:
                    m = matrix
            except json.JSONDecodeError as e:
                return f"❌ Invalid matrix format. Use JSON format like [[1,2],[3,4]]. Error: {str(e)}"
            
            # Validate matrix is 2D list
            if not isinstance(m, list):
                return "❌ Matrix must be a 2D array (list of lists)"
            
            if not all(isinstance(row, list) for row in m):
                return "❌ Matrix must be a 2D array (list of lists)"
            
            # Check if matrix is non-empty and square
            if len(m) == 0:
                return "❌ Matrix cannot be empty"
            
            n = len(m)
            for i, row in enumerate(m):
                if len(row) != n:
                    return f"❌ Matrix must be square. Row {i} has length {len(row)} but expected {n}"
                if not all(isinstance(x, (int, float)) for x in row):
                    return f"❌ Matrix contains non-numeric values in row {i}"
            
            # Calculate determinant using recursive expansion
            def calc_determinant(matrix):
                size = len(matrix)
                
                # Base cases
                if size == 1:
                    return matrix[0][0]
                
                if size == 2:
                    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                
                # Recursive case: expand along first row
                det = 0
                for col in range(size):
                    # Create minor matrix (remove row 0 and current column)
                    minor = []
                    for row in range(1, size):
                        minor_row = []
                        for c in range(size):
                            if c != col:
                                minor_row.append(matrix[row][c])
                        minor.append(minor_row)
                    
                    # Calculate cofactor and add to determinant
                    cofactor = matrix[0][col] * calc_determinant(minor)
                    if col % 2 == 1:
                        cofactor = -cofactor
                    det += cofactor
                
                return det
            
            # Check for reasonable matrix size (to prevent excessive computation)
            if n > 10:
                return f"❌ Matrix too large for determinant calculation. Maximum supported size is 10×10, got {n}×{n}"
            
            determinant = calc_determinant(m)
            
            return f"✅ Determinant of {n}×{n} matrix: {determinant}"
            
        except Exception as e:
            return f"❌ Error calculating matrix determinant: {str(e)}"

    @mcp.tool()
    async def matrix_transpose(matrix: Union[str, list]) -> str:
        """
        Calculate the transpose of a matrix (swap rows and columns).
        
        Args:
            matrix: JSON string or list representing matrix, e.g., "[[1,2,3],[4,5,6]]" or [[1,2,3],[4,5,6]]
            
        Returns:
            String with the transposed matrix or error message
        """
        try:
            # Parse input matrix - handle both string and list inputs
            try:
                if isinstance(matrix, str):
                    m = json.loads(matrix)
                else:
                    m = matrix
            except json.JSONDecodeError as e:
                return f"❌ Invalid matrix format. Use JSON format like [[1,2],[3,4]]. Error: {str(e)}"
            
            # Validate matrix is 2D list
            if not isinstance(m, list):
                return "❌ Matrix must be a 2D array (list of lists)"
            
            if not all(isinstance(row, list) for row in m):
                return "❌ Matrix must be a 2D array (list of lists)"
            
            # Check if matrix is non-empty
            if len(m) == 0:
                return "❌ Matrix cannot be empty"
            
            # Validate consistent row lengths and numeric values
            cols = len(m[0])
            for i, row in enumerate(m):
                if len(row) != cols:
                    return f"❌ Matrix row {i} has inconsistent length: {len(row)} vs {cols}"
                if not all(isinstance(x, (int, float)) for x in row):
                    return f"❌ Matrix contains non-numeric values in row {i}"
            
            # Calculate transpose
            rows = len(m)
            transpose = []
            for col in range(cols):
                new_row = []
                for row in range(rows):
                    new_row.append(m[row][col])
                transpose.append(new_row)
            
            # Format result
            result_str = json.dumps(transpose)
            return f"✅ Matrix transpose ({rows}×{cols} → {cols}×{rows}):\n   Result: {result_str}"
            
        except Exception as e:
            return f"❌ Error calculating matrix transpose: {str(e)}"


# Support for direct execution (testing)
if __name__ == "__main__":
    print("Matrix Operations Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
