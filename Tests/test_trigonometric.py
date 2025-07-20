"""
Test suite for trigonometric.py module

Tests trigonometric functions: sin, cos, tan, sin_degrees, cos_degrees, tan_degrees, 
asin, acos, atan, atan2
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import trigonometric


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestTrigonometric:
    """Test class for trigonometric functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        trigonometric.register_tools(self.mcp)
    
    # Radian-based trigonometric functions
    
    async def test_sin_zero(self):
        """Test sin(0)."""
        result = await self.mcp.tools['sin'](0)
        expected = "✅ sin(0.0 radians) = 0.0"
        return result == expected
    
    async def test_sin_pi_over_2(self):
        """Test sin(π/2)."""
        result = await self.mcp.tools['sin'](math.pi / 2)
        # sin(π/2) = 1
        return result.startswith("✅ sin(") and "= 1.0" in result
    
    async def test_sin_pi(self):
        """Test sin(π)."""
        result = await self.mcp.tools['sin'](math.pi)
        # sin(π) ≈ 0 (within floating point precision)
        return result.startswith("✅ sin(") and ("= 0.0" in result or "1.2246e-16" in result)
    
    async def test_cos_zero(self):
        """Test cos(0)."""
        result = await self.mcp.tools['cos'](0)
        expected = "✅ cos(0.0 radians) = 1.0"
        return result == expected
    
    async def test_cos_pi_over_2(self):
        """Test cos(π/2)."""
        result = await self.mcp.tools['cos'](math.pi / 2)
        # cos(π/2) ≈ 0
        return result.startswith("✅ cos(") and ("= 0.0" in result or "6.123e-17" in result)
    
    async def test_cos_pi(self):
        """Test cos(π)."""
        result = await self.mcp.tools['cos'](math.pi)
        expected_contains = "= -1.0"
        return result.startswith("✅ cos(") and expected_contains in result
    
    async def test_tan_zero(self):
        """Test tan(0)."""
        result = await self.mcp.tools['tan'](0)
        expected = "✅ tan(0.0 radians) = 0.0"
        return result == expected
    
    async def test_tan_pi_over_4(self):
        """Test tan(π/4)."""
        result = await self.mcp.tools['tan'](math.pi / 4)
        # tan(π/4) = 1
        return result.startswith("✅ tan(") and "= 1.0" in result
    
    async def test_tan_pi_over_2_undefined(self):
        """Test tan(π/2) which should be undefined."""
        result = await self.mcp.tools['tan'](math.pi / 2)
        return result.startswith("❌") and "undefined" in result.lower()
    
    # Degree-based trigonometric functions
    
    async def test_sin_degrees_zero(self):
        """Test sin(0°)."""
        result = await self.mcp.tools['sin_degrees'](0)
        expected = "✅ sin(0.0°) = 0.0"
        return result == expected
    
    async def test_sin_degrees_90(self):
        """Test sin(90°)."""
        result = await self.mcp.tools['sin_degrees'](90)
        expected = "✅ sin(90.0°) = 1.0"
        return result == expected
    
    async def test_sin_degrees_180(self):
        """Test sin(180°)."""
        result = await self.mcp.tools['sin_degrees'](180)
        return result.startswith("✅ sin(180.0°) = 0.0") or "1.2246e-16" in result
    
    async def test_cos_degrees_zero(self):
        """Test cos(0°)."""
        result = await self.mcp.tools['cos_degrees'](0)
        expected = "✅ cos(0.0°) = 1.0"
        return result == expected
    
    async def test_cos_degrees_90(self):
        """Test cos(90°)."""
        result = await self.mcp.tools['cos_degrees'](90)
        return result.startswith("✅ cos(90.0°) = 0.0") or "6.123e-17" in result
    
    async def test_cos_degrees_180(self):
        """Test cos(180°)."""
        result = await self.mcp.tools['cos_degrees'](180)
        expected = "✅ cos(180.0°) = -1.0"
        return result == expected
    
    async def test_tan_degrees_zero(self):
        """Test tan(0°)."""
        result = await self.mcp.tools['tan_degrees'](0)
        expected = "✅ tan(0.0°) = 0.0"
        return result == expected
    
    async def test_tan_degrees_45(self):
        """Test tan(45°)."""
        result = await self.mcp.tools['tan_degrees'](45)
        expected = "✅ tan(45.0°) = 1.0"
        return result == expected
    
    async def test_tan_degrees_90_undefined(self):
        """Test tan(90°) which should be undefined."""
        result = await self.mcp.tools['tan_degrees'](90)
        return result.startswith("❌") and "undefined" in result.lower()
    
    # Inverse trigonometric functions
    
    async def test_asin_zero(self):
        """Test asin(0)."""
        result = await self.mcp.tools['asin'](0)
        expected = "✅ arcsin(0.0) = 0.0 radians"
        return result == expected
    
    async def test_asin_one(self):
        """Test asin(1)."""
        result = await self.mcp.tools['asin'](1)
        # asin(1) = π/2
        return result.startswith("✅ arcsin(1.0) = 1.570")
    
    async def test_asin_invalid_domain(self):
        """Test asin with value outside [-1, 1]."""
        result = await self.mcp.tools['asin'](2)
        return result.startswith("❌") and "domain" in result.lower()
    
    async def test_acos_one(self):
        """Test acos(1)."""
        result = await self.mcp.tools['acos'](1)
        expected = "✅ arccos(1.0) = 0.0 radians"
        return result == expected
    
    async def test_acos_zero(self):
        """Test acos(0)."""
        result = await self.mcp.tools['acos'](0)
        # acos(0) = π/2
        return result.startswith("✅ arccos(0.0) = 1.570")
    
    async def test_acos_invalid_domain(self):
        """Test acos with value outside [-1, 1]."""
        result = await self.mcp.tools['acos'](-2)
        return result.startswith("❌") and "domain" in result.lower()
    
    async def test_atan_zero(self):
        """Test atan(0)."""
        result = await self.mcp.tools['atan'](0)
        expected = "✅ arctan(0.0) = 0.0 radians"
        return result == expected
    
    async def test_atan_one(self):
        """Test atan(1)."""
        result = await self.mcp.tools['atan'](1)
        # atan(1) = π/4
        return result.startswith("✅ arctan(1.0) = 0.785")
    
    async def test_atan2_standard(self):
        """Test atan2(1, 1)."""
        result = await self.mcp.tools['atan2'](1, 1)
        # atan2(1, 1) = π/4
        return result.startswith("✅ atan2(1.0, 1.0) = 0.785")
    
    async def test_atan2_quadrant_ii(self):
        """Test atan2 in quadrant II."""
        result = await self.mcp.tools['atan2'](1, -1)
        # atan2(1, -1) = 3π/4
        return result.startswith("✅ atan2(1.0, -1.0) = 2.356")
    
    async def test_atan2_zero_zero(self):
        """Test atan2(0, 0) special case."""
        result = await self.mcp.tools['atan2'](0, 0)
        expected = "✅ atan2(0.0, 0.0) = 0.0 radians"
        return result == expected
