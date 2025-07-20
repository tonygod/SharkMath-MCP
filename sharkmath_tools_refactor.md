# SharkMath Tools Refactoring Plan

## Overview
This document outlines the systematic refactoring of SharkMath from 70+ individual tools to 15-20 consolidated tools using parameter-based routing. This addresses MCP tool registration limits while maintaining functionality and improving maintainability.

## Current State Analysis
- **Current Tools**: 70+ individual MCP tools across 12 modules
- **Current Test Files**: 45 tests across 4 working test files
- **Current AI Agent Tests**: 60+ test prompts in `mcp_tests.md`
- **Issue**: MCP tool registration limits prevent enabling all tools simultaneously
- **Solution**: Consolidate related operations into multi-function tools with parameter-based routing

---

## Target Architecture

### **Consolidated Tool Structure (18 tools total)**

| Tool Name | Current Functions | Parameters | Description |
|-----------|-------------------|------------|-------------|
| `convert_units` | 42 conversion functions | from_unit, to_unit, value, time_hours | Universal unit converter |
| `calculate_arithmetic` | 9 arithmetic functions | operation, a, b | Basic math operations |
| `calculate_trigonometry` | 10 trig functions | function, value, angle_unit | Trig and inverse trig |
| `calculate_statistics` | 14 stats functions | operation, numbers, percentile | Statistical operations |
| `calculate_logarithmic` | 4 log functions | operation, value, base | Log and exponential |
| `calculate_hyperbolic` | 3 hyperbolic functions | function, value | Hyperbolic functions |
| `format_precision` | 5 precision functions | operation, value, places | Rounding and precision |
| `analyze_numbers` | 8 number theory functions | operation, value, second_value | Prime, GCD, LCM, factorial |
| `solve_equations` | 4 equation solvers | equation_type, a, b, c, extra_params | Quadratic, compound interest |
| `calculate_geometry_2d` | 6 2D geometry functions | operation, params | Distance, slope, area, perimeter |
| `calculate_geometry_3d` | 6 3D geometry functions | operation, params | Volume, surface area |
| `manipulate_matrices` | 4 matrix operations | operation, matrix1, matrix2 | Matrix math operations |
| `financial_calculations` | 11 financial functions | operation, principal, rate, time, params | Investment and business calc |
| `computer_science_tools` | 9 CS functions | operation, value, params | Base conversions, algorithms |
| `advanced_mathematics` | 8 advanced functions | operation, params | Complex operations |
| `data_analysis` | 8 advanced stats functions | operation, data, params | Advanced statistical analysis |
| `enhanced_conversions` | 20 new conversion functions | from_unit, to_unit, value, params | Area, speed, pressure, data |
| `utility_functions` | 5 helper functions | operation, params | Validation, constants, help |

---

## Refactoring Phases

### **Phase 1: Core Infrastructure Setup**
**Objective**: Establish consolidated tool architecture and testing framework

#### Step 1.1: Create Consolidated Tool Template
🔲 **Create `consolidated_tool_template.py`** - Template for parameter-based routing
🔲 **Define standard parameter patterns** - Consistent interface across all tools
🔲 **Create operation mapping dictionaries** - Systematic lookup for all operations
🔲 **Implement standard error handling** - Uniform ✅/❌ response patterns

#### Step 1.2: Create Prototype Tool
🔲 **Implement `convert_units` as prototype** - Most complex consolidated tool
🔲 **Include all 42 current conversions** - Energy, time, temperature, length, weight, volume
🔲 **Add parameter validation** - Ensure robust input handling  
🔲 **Test prototype thoroughly** - Verify all conversions work correctly

#### Step 1.3: Update Testing Infrastructure
🔲 **Create `Tests/test_consolidated_tools.py`** - New test file for consolidated tools
🔲 **Update `Tests/README.md`** - Document new testing approach
🔲 **Create consolidated test patterns** - Template for testing multi-function tools
🔲 **Implement parameter validation tests** - Test invalid operations and parameters

---

### **Phase 2: Mathematics Core Tools**
**Objective**: Consolidate fundamental mathematical operations

#### Step 2.1: Arithmetic Consolidation
🔲 **Create `calculate_arithmetic`** - Consolidate add, subtract, multiply, divide, power, square, cube, sqrt, cbrt
🔲 **Migrate from `arithmetic.py`** - Move logic to consolidated tool
🔲 **Update tests** - Convert 9 individual tests to parameter-based tests
🔲 **Verify MCP integration** - Ensure tool registers and functions correctly

#### Step 2.2: Trigonometry Consolidation
🔲 **Create `calculate_trigonometry`** - Consolidate all 10 trig functions with angle unit support
🔲 **Migrate from `trigonometric.py`** - Include sin, cos, tan, asin, acos, atan, atan2 with degree/radian handling
🔲 **Update tests** - Convert trig tests to consolidated format
🔲 **Add angle unit validation** - Ensure proper degree/radian handling

#### Step 2.3: Statistics Consolidation  
🔲 **Create `calculate_statistics`** - Consolidate mean, median, mode, std_dev, variance, range
🔲 **Migrate from `statistics.py`** - Include all current statistical operations
🔲 **Update tests** - Convert statistical tests to parameter-based format
🔲 **Add data validation** - Ensure proper comma-separated input handling

#### Step 2.4: Update Documentation
🔲 **Update `.github/copilot-instructions.md`** - Document new consolidated tool structure
🔲 **Update `Tests/mcp_tests.md`** - Convert test prompts to use consolidated tools
🔲 **Update `Tests/mcp_test_expected.md`** - Update expected results for new tool calls
🔲 **Update `Tests/README.md`** - Document testing approach for consolidated tools

---

### **Phase 3: Advanced Mathematics Tools**
**Objective**: Consolidate specialized mathematical functions

#### Step 3.1: Logarithmic and Exponential
🔲 **Create `calculate_logarithmic`** - Consolidate ln, log10, log_base, exponential
🔲 **Migrate from `logarithmic.py`** - Include domain validation
🔲 **Update tests** - Convert log/exp tests to consolidated format

#### Step 3.2: Hyperbolic Functions
🔲 **Create `calculate_hyperbolic`** - Consolidate sinh, cosh, tanh
🔲 **Migrate from `hyperbolic.py`** - Include overflow protection
🔲 **Update tests** - Convert hyperbolic tests to consolidated format

#### Step 3.3: Precision and Number Theory
🔲 **Create `format_precision`** - Consolidate round, floor, ceiling, truncate, absolute
🔲 **Create `analyze_numbers`** - Consolidate factorial, gcd, lcm, is_prime, prime_factors, is_perfect_square, fibonacci
🔲 **Migrate from `precision.py` and `number_theory.py`** - Include all validation logic
🔲 **Update tests** - Convert precision and number theory tests

---

### **Phase 4: Applied Mathematics Tools**
**Objective**: Consolidate application-specific mathematical functions

#### Step 4.1: Equation Solvers
🔲 **Create `solve_equations`** - Consolidate solve_quadratic, compound_interest, linear equations
🔲 **Migrate from `advanced_calc.py`** - Include complex number handling
🔲 **Update tests** - Convert equation solver tests

#### Step 4.2: Geometry Tools
🔲 **Create `calculate_geometry_2d`** - Consolidate distance_2d, slope, circle area/circumference, triangle area, rectangle area/perimeter
🔲 **Create `calculate_geometry_3d`** - Consolidate sphere, cylinder, cone, prism calculations
🔲 **Migrate from `advanced_calc.py`** - Include all geometric operations
🔲 **Update tests** - Convert geometry tests to consolidated format

#### Step 4.3: Matrix Operations
🔲 **Create `manipulate_matrices`** - Consolidate matrix_add, matrix_multiply, matrix_determinant, matrix_transpose
🔲 **Migrate from `matrix_operations.py`** - Include JSON parsing and validation
🔲 **Update tests** - Convert matrix tests to consolidated format

---

### **Phase 5: Business and Computer Science Tools**
**Objective**: Consolidate specialized domain tools

#### Step 5.1: Financial Calculations
🔲 **Create `financial_calculations`** - Consolidate compound_interest, simple_interest, PV, FV, loan payments, ROI, depreciation
🔲 **Migrate from `advanced_calc.py` and new financial functions** - Include business calculation logic
🔲 **Update tests** - Create comprehensive financial calculation tests

#### Step 5.2: Computer Science Tools
🔲 **Create `computer_science_tools`** - Consolidate base conversions, algorithm helpers, hash functions
🔲 **Implement new CS functions** - Binary, hex, octal conversions, Big O calculations
🔲 **Create tests** - Comprehensive CS function testing

#### Step 5.3: Data Analysis Tools
🔲 **Create `data_analysis`** - Consolidate percentile, quartiles, correlation, z_score, skewness, kurtosis
🔲 **Implement advanced statistical functions** - Beyond basic statistics
🔲 **Create tests** - Advanced statistics testing

---

### **Phase 6: Enhanced Conversions and Utilities**
**Objective**: Complete the consolidation with remaining functions

#### Step 6.1: Enhanced Conversions
🔲 **Expand `convert_units`** - Add area, speed, pressure, data conversions (total 62 conversions)
🔲 **Alternatively create `enhanced_conversions`** - Separate tool for new conversion categories
🔲 **Update tests** - Include all new conversion types

#### Step 6.2: Utility Functions
🔲 **Create `utility_functions`** - Help system, constants, validation helpers
🔲 **Implement helper operations** - Mathematical constants, input validation, operation help
🔲 **Create tests** - Utility function testing

#### Step 6.3: Final Integration
🔲 **Update `sharkmath_server.py`** - Register all consolidated tools
🔲 **Create migration guide** - Document transition from individual to consolidated tools
🔲 **Performance testing** - Ensure consolidated tools perform efficiently

---

## Testing Strategy

### **Consolidated Tool Testing Approach**

#### Test File Structure
```python
# Tests/test_consolidated_tools.py
class TestConsolidatedTools:
    def test_convert_units_energy(self):
        # Test: convert_units("watts", "kilowatts", 1500)
        
    def test_convert_units_invalid_operation(self):
        # Test: convert_units("invalid", "units", 100)
        
    def test_calculate_arithmetic_operations(self):
        # Test: calculate_arithmetic("add", 5, 3)
        
    def test_calculate_arithmetic_invalid_operation(self):
        # Test: calculate_arithmetic("invalid", 1, 2)
```

#### AI Agent Test Updates
```markdown
# Tests/mcp_tests.md - Updated format
### 1. Unit Conversions
**Test 1.1 - Energy Conversion**
**Prompt**: "Convert 1500 watts to kilowatts"
**Expected MCP Tool**: `convert_units`
**Parameters**: from_unit="watts", to_unit="kilowatts", value=1500
**Test ID**: CONV_ENERGY_001

**Test 1.2 - Arithmetic Operation**  
**Prompt**: "Add 47 and 293"
**Expected MCP Tool**: `calculate_arithmetic` 
**Parameters**: operation="add", a=47, b=293
**Test ID**: ARITH_ADD_001
```

### **Testing Phases**
1. **Unit Testing** - Each consolidated tool tested individually
2. **Integration Testing** - Verify MCP server registration and execution
3. **Regression Testing** - Ensure all original functionality preserved
4. **Performance Testing** - Verify response times under 100ms
5. **AI Agent Testing** - Update and execute all test prompts

---

## Documentation Updates

### **Files to Update**

#### Core Documentation
🔲 **`.github/copilot-instructions.md`** - Complete rewrite for consolidated architecture
🔲 **`README.md`** - Update with new tool structure and usage examples  
🔲 **`sharkmath_enhancement_tasks.md`** - Update to reflect consolidated approach

#### Test Documentation  
🔲 **`Tests/README.md`** - Document consolidated testing approach
🔲 **`Tests/mcp_tests.md`** - Convert all 60+ prompts to consolidated tool format
🔲 **`Tests/mcp_test_expected.md`** - Update expected results for consolidated tools
🔲 **`Tests/TEST_RESULTS.md`** - Document consolidated tool test results

#### New Documentation
🔲 **`TOOL_REFERENCE.md`** - Complete reference for all consolidated tool parameters
🔲 **`ARCHITECTURE.md`** - Document the consolidated tool architecture and design decisions

### **Documentation Standards**
- **Consistent parameter documentation** - All tools follow same parameter description format
- **Usage examples** - Each tool includes multiple usage examples  
- **Error handling documentation** - Document all error conditions and responses

---

## Implementation Milestones

### **Milestone Checkpoints**
1. **Phase 1 Complete** - Prototype `convert_units` tool working with full test coverage
2. **Phase 2 Complete** - Core math tools (arithmetic, trig, stats) consolidated and tested
3. **Phase 3 Complete** - Advanced math tools consolidated with documentation updated  
4. **Phase 4 Complete** - Applied math tools working with comprehensive test coverage
5. **Phase 5 Complete** - All business/CS tools implemented and integrated
6. **Phase 6 Complete** - Full refactoring complete, all documentation updated, performance validated

---

## Success Criteria

### **Functional Requirements**
- ✅ **Tool count reduced** from 70+ to 18 consolidated tools
- ✅ **All functionality preserved** - No loss of mathematical capabilities
- ✅ **Parameter-based routing** - Clear, unambiguous operation specification
- ✅ **Consistent error handling** - Uniform ✅/❌ response patterns
- ✅ **Performance maintained** - All operations complete within 100ms

### **Quality Requirements**  
- ✅ **100% test coverage** - All consolidated tools thoroughly tested
- ✅ **Documentation completeness** - All tools and parameters documented
- ✅ **MCP integration** - All tools register and execute correctly in MCP server

### **Maintenance Requirements**
- ✅ **Reduced complexity** - Easier to add new operations to existing tools
- ✅ **Centralized logic** - Related operations share validation and error handling
- ✅ **Clear architecture** - Tool organization follows logical mathematical domains
- ✅ **Extensibility** - Easy to add new mathematical domains as additional consolidated tools

---

## Risk Mitigation

### **Technical Risks**
1. **Parameter complexity** - Risk: Consolidated tools become too complex to maintain
   - *Mitigation*: Maintain clear parameter patterns, comprehensive documentation
   
2. **Performance degradation** - Risk: Parameter routing adds overhead
   - *Mitigation*: Use efficient dictionary lookups, performance testing at each phase
   
3. **User experience impact** - Risk: Users prefer individual tools
   - *Mitigation*: Focus on clear parameter interface design and comprehensive documentation

### **Project Risks**
1. **Scope creep** - Risk: Adding new functionality during refactoring
   - *Mitigation*: Focus on consolidation first, enhancements in separate phases
   
2. **Testing gaps** - Risk: Missing edge cases during consolidation  
   - *Mitigation*: Comprehensive test coverage, systematic regression testing
   
3. **Documentation debt** - Risk: Documentation falls behind implementation
   - *Mitigation*: Update documentation as part of each phase, not as afterthought

---

## Next Steps

### **Immediate Actions**
1. **Review and approve** this refactoring plan
2. **Create Phase 1 branch** for development work
3. **Begin with `consolidated_tool_template.py`** - Establish patterns
4. **Implement `convert_units` prototype** - Prove the consolidation approach
5. **Set up consolidated testing framework** - Foundation for all testing

### **Decision Points**
1. **✅ Approve overall approach** - Confirm 18-tool consolidation strategy (APPROVED)
2. **✅ Confirm timeline** - Adjust phases based on available development time (CONFIRMED)
3. **✅ Tool naming conventions** - Finalize naming pattern for consolidated tools (FINALIZED, may adjust as needed)
4. **Parameter standards** - Use typical/widely-accepted MCP parameter naming and validation patterns

This refactoring plan transforms SharkMath from a tool-count-limited system to a scalable, maintainable mathematical toolkit while preserving all functionality and improving the development experience.
