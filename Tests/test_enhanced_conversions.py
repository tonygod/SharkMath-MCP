"""
Test suite for enhanced convert_units.py module - Phase 6 additions

Tests new unit conversion functions added in Phase 6:
- Area conversions: square_meters, square_feet, acres, hectares
- Speed conversions: mps, kmh, mph, knots  
- Pressure conversions: pascals, atmospheres, psi, bar
- Data conversions: bytes, kilobytes, megabytes, gigabytes, terabytes, petabytes, bits
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import convert_units


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestEnhancedConversions:
    """Test class for Phase 6 enhanced unit conversion functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        convert_units.register_tools(self.mcp)
    
    # Area conversion tests
    
    async def test_square_meters_to_square_feet(self):
        """Test square meters to square feet conversion."""
        result = await self.mcp.tools['convert_units']("square_meters", "square_feet", 1)
        return "10.7639 square_feet" in result
    
    async def test_square_feet_to_square_meters(self):
        """Test square feet to square meters conversion."""
        result = await self.mcp.tools['convert_units']("square_feet", "square_meters", 10.7639)
        return "1.0 square_meters" in result
    
    async def test_hectares_to_acres(self):
        """Test hectares to acres conversion."""
        result = await self.mcp.tools['convert_units']("hectares", "acres", 1)
        return "2.47105 acres" in result
    
    async def test_acres_to_hectares(self):
        """Test acres to hectares conversion."""
        result = await self.mcp.tools['convert_units']("acres", "hectares", 2.47105)
        return "1.0 hectares" in result
    
    async def test_square_meters_to_hectares(self):
        """Test square meters to hectares conversion."""
        result = await self.mcp.tools['convert_units']("square_meters", "hectares", 10000)
        return "1.0 hectares" in result
    
    async def test_hectares_to_square_meters(self):
        """Test hectares to square meters conversion."""
        result = await self.mcp.tools['convert_units']("hectares", "square_meters", 1)
        return "10000" in result  # Allow both "10000" and "10000.0"
    
    async def test_acres_to_square_feet(self):
        """Test acres to square feet conversion."""
        result = await self.mcp.tools['convert_units']("acres", "square_feet", 1)
        return "43560" in result  # Allow both "43560" and "43560.0"
    
    async def test_square_feet_to_acres(self):
        """Test square feet to acres conversion."""
        result = await self.mcp.tools['convert_units']("square_feet", "acres", 43560)
        return "1.0 acres" in result
    
    # Speed conversion tests
    
    async def test_mps_to_kmh(self):
        """Test meters per second to kilometers per hour conversion."""
        result = await self.mcp.tools['convert_units']("mps", "kmh", 1)
        return "3.6 kmh" in result
    
    async def test_kmh_to_mps(self):
        """Test kilometers per hour to meters per second conversion."""
        result = await self.mcp.tools['convert_units']("kmh", "mps", 3.6)
        return "1.0 mps" in result
    
    async def test_mps_to_mph(self):
        """Test meters per second to miles per hour conversion."""
        result = await self.mcp.tools['convert_units']("mps", "mph", 1)
        return "2.23694 mph" in result
    
    async def test_mph_to_mps(self):
        """Test miles per hour to meters per second conversion."""
        result = await self.mcp.tools['convert_units']("mph", "mps", 2.23694)
        return "1.0 mps" in result
    
    async def test_kmh_to_mph(self):
        """Test kilometers per hour to miles per hour conversion."""
        result = await self.mcp.tools['convert_units']("kmh", "mph", 100)
        return "62.137" in result  # Allow for floating point precision
    
    async def test_mph_to_kmh(self):
        """Test miles per hour to kilometers per hour conversion."""
        result = await self.mcp.tools['convert_units']("mph", "kmh", 62.1371)
        return "100.0 kmh" in result
    
    async def test_knots_to_mps(self):
        """Test nautical knots to meters per second conversion."""
        result = await self.mcp.tools['convert_units']("knots", "mps", 1)
        return "0.514444 mps" in result
    
    async def test_mps_to_knots(self):
        """Test meters per second to nautical knots conversion."""
        result = await self.mcp.tools['convert_units']("mps", "knots", 0.514444)
        return "1.0 knots" in result
    
    async def test_knots_to_mph(self):
        """Test nautical knots to miles per hour conversion."""
        result = await self.mcp.tools['convert_units']("knots", "mph", 1)
        return "1.15078 mph" in result
    
    async def test_mph_to_knots(self):
        """Test miles per hour to nautical knots conversion."""
        result = await self.mcp.tools['convert_units']("mph", "knots", 1.15078)
        return "1.0 knots" in result
    
    async def test_knots_to_kmh(self):
        """Test nautical knots to kilometers per hour conversion."""
        result = await self.mcp.tools['convert_units']("knots", "kmh", 1)
        return "1.852 kmh" in result
    
    async def test_kmh_to_knots(self):
        """Test kilometers per hour to nautical knots conversion."""
        result = await self.mcp.tools['convert_units']("kmh", "knots", 1.852)
        return "1.0 knots" in result
    
    # Pressure conversion tests
    
    async def test_pascals_to_atmospheres(self):
        """Test pascals to atmospheres conversion."""
        result = await self.mcp.tools['convert_units']("pascals", "atmospheres", 101325)
        return "1.0 atmospheres" in result
    
    async def test_atmospheres_to_pascals(self):
        """Test atmospheres to pascals conversion."""
        result = await self.mcp.tools['convert_units']("atmospheres", "pascals", 1)
        return "101325 pascals" in result
    
    async def test_pascals_to_psi(self):
        """Test pascals to pounds per square inch conversion."""
        result = await self.mcp.tools['convert_units']("pascals", "psi", 6895)
        return "1.0 psi" in result
    
    async def test_psi_to_pascals(self):
        """Test pounds per square inch to pascals conversion."""
        result = await self.mcp.tools['convert_units']("psi", "pascals", 1)
        return "6895 pascals" in result
    
    async def test_pascals_to_bar(self):
        """Test pascals to bar conversion."""
        result = await self.mcp.tools['convert_units']("pascals", "bar", 100000)
        return "1.0 bar" in result
    
    async def test_bar_to_pascals(self):
        """Test bar to pascals conversion."""
        result = await self.mcp.tools['convert_units']("bar", "pascals", 1)
        return "100000 pascals" in result
    
    async def test_atmospheres_to_psi(self):
        """Test atmospheres to pounds per square inch conversion."""
        result = await self.mcp.tools['convert_units']("atmospheres", "psi", 1)
        return "14.696 psi" in result
    
    async def test_psi_to_atmospheres(self):
        """Test pounds per square inch to atmospheres conversion."""
        result = await self.mcp.tools['convert_units']("psi", "atmospheres", 14.696)
        return "1.0 atmospheres" in result
    
    async def test_atmospheres_to_bar(self):
        """Test atmospheres to bar conversion."""
        result = await self.mcp.tools['convert_units']("atmospheres", "bar", 1)
        return "1.01325 bar" in result
    
    async def test_bar_to_atmospheres(self):
        """Test bar to atmospheres conversion."""
        result = await self.mcp.tools['convert_units']("bar", "atmospheres", 1.01325)
        return "1.0 atmospheres" in result
    
    # Data conversion tests
    
    async def test_bits_to_bytes(self):
        """Test bits to bytes conversion."""
        result = await self.mcp.tools['convert_units']("bits", "bytes", 8)
        return "1.0 bytes" in result
    
    async def test_bytes_to_bits(self):
        """Test bytes to bits conversion."""
        result = await self.mcp.tools['convert_units']("bytes", "bits", 1)
        return "8 bits" in result
    
    async def test_bytes_to_kilobytes(self):
        """Test bytes to kilobytes conversion."""
        result = await self.mcp.tools['convert_units']("bytes", "kilobytes", 1024)
        return "1.0 kilobytes" in result
    
    async def test_kilobytes_to_bytes(self):
        """Test kilobytes to bytes conversion."""
        result = await self.mcp.tools['convert_units']("kilobytes", "bytes", 1)
        return "1024 bytes" in result
    
    async def test_kilobytes_to_megabytes(self):
        """Test kilobytes to megabytes conversion."""
        result = await self.mcp.tools['convert_units']("kilobytes", "megabytes", 1024)
        return "1.0 megabytes" in result
    
    async def test_megabytes_to_kilobytes(self):
        """Test megabytes to kilobytes conversion."""
        result = await self.mcp.tools['convert_units']("megabytes", "kilobytes", 1)
        return "1024 kilobytes" in result
    
    async def test_megabytes_to_gigabytes(self):
        """Test megabytes to gigabytes conversion."""
        result = await self.mcp.tools['convert_units']("megabytes", "gigabytes", 1024)
        return "1.0 gigabytes" in result
    
    async def test_gigabytes_to_megabytes(self):
        """Test gigabytes to megabytes conversion."""
        result = await self.mcp.tools['convert_units']("gigabytes", "megabytes", 1)
        return "1024 megabytes" in result
    
    async def test_gigabytes_to_terabytes(self):
        """Test gigabytes to terabytes conversion."""
        result = await self.mcp.tools['convert_units']("gigabytes", "terabytes", 1024)
        return "1.0 terabytes" in result
    
    async def test_terabytes_to_gigabytes(self):
        """Test terabytes to gigabytes conversion."""
        result = await self.mcp.tools['convert_units']("terabytes", "gigabytes", 1)
        return "1024 gigabytes" in result
    
    async def test_terabytes_to_petabytes(self):
        """Test terabytes to petabytes conversion."""
        result = await self.mcp.tools['convert_units']("terabytes", "petabytes", 1024)
        return "1.0 petabytes" in result
    
    async def test_petabytes_to_terabytes(self):
        """Test petabytes to terabytes conversion."""
        result = await self.mcp.tools['convert_units']("petabytes", "terabytes", 1)
        return "1024 terabytes" in result
    
    async def test_bytes_to_megabytes(self):
        """Test bytes to megabytes conversion."""
        result = await self.mcp.tools['convert_units']("bytes", "megabytes", 1048576)  # 1024 * 1024
        return "1.0 megabytes" in result
    
    async def test_megabytes_to_bytes(self):
        """Test megabytes to bytes conversion."""
        result = await self.mcp.tools['convert_units']("megabytes", "bytes", 1)
        return "1048576 bytes" in result
    
    async def test_bytes_to_gigabytes(self):
        """Test bytes to gigabytes conversion."""
        result = await self.mcp.tools['convert_units']("bytes", "gigabytes", 1073741824)  # 1024^3
        return "1.0 gigabytes" in result
    
    async def test_gigabytes_to_bytes(self):
        """Test gigabytes to bytes conversion."""
        result = await self.mcp.tools['convert_units']("gigabytes", "bytes", 1)
        return "1073741824 bytes" in result
    
    # Validation tests for new units
    
    async def test_negative_area_validation(self):
        """Test validation for negative area values."""
        result = await self.mcp.tools['convert_units']("square_meters", "square_feet", -5)
        return "❌ Area cannot be negative" in result
    
    async def test_negative_speed_validation(self):
        """Test validation for negative speed values."""
        result = await self.mcp.tools['convert_units']("mps", "kmh", -10)
        return "❌ Speed cannot be negative" in result
    
    async def test_negative_pressure_validation(self):
        """Test validation for negative pressure values."""
        result = await self.mcp.tools['convert_units']("pascals", "atmospheres", -1000)
        return "❌ Pressure cannot be negative" in result
    
    async def test_negative_data_validation(self):
        """Test validation for negative data size values."""
        result = await self.mcp.tools['convert_units']("bytes", "kilobytes", -512)
        return "❌ Data size cannot be negative" in result
    
    async def test_unsupported_conversion_error(self):
        """Test error handling for unsupported conversions."""
        result = await self.mcp.tools['convert_units']("invalid_unit", "another_invalid", 10)
        return "❌ Conversion from 'invalid_unit' to 'another_invalid' not supported" in result


async def run_enhanced_conversion_tests():
    """Run all enhanced conversion tests."""
    tester = TestEnhancedConversions()
    
    test_methods = [method for method in dir(tester) if method.startswith('test_')]
    passed = 0
    failed = 0
    
    print("🧪 Running Enhanced Conversion Tests (Phase 6)...")
    print("=" * 60)
    
    for test_method in test_methods:
        try:
            test_func = getattr(tester, test_method)
            result = await test_func()
            if result:
                print(f"✅ {test_method}")
                passed += 1
            else:
                print(f"❌ {test_method}")
                failed += 1
        except Exception as e:
            print(f"💥 {test_method}: {str(e)}")
            failed += 1
    
    print("=" * 60)
    print(f"📊 Enhanced Conversion Test Results:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📈 Success Rate: {(passed/(passed+failed)*100):.1f}%")
    
    return passed, failed


if __name__ == "__main__":
    print("Testing Enhanced Convert Units Tool (Phase 6 additions):")
    asyncio.run(run_enhanced_conversion_tests())
