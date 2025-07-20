# SharkMath Tools Refactoring Plan

## Overview
This document outlines the systematic refactoring of SharkMath from 70+ individual tools to 15-20 consolidated tools using parameter-based routing. This addresses MCP tool registration limits while maintaining functionality and improving maintainability.

## Operating Procedures
**IMPORTANT: Follow these procedures during implementation:**

1. **Phase Confirmation Required**: Never automatically begin implementation of any phase without first confirming that the user is ready to proceed.

2. **Simple Commit Messages**: When committing changes to the repository, always use simple, single-line commit messages. Enhanced multi-line messages with extended characters cause terminal prompt issues requiring CTRL+C to escape.

3. **Module File Management**: Reuse original module filenames (e.g., `arithmetic.py`) instead of creating new "consolidated_" prefixed files. Original modules will be replaced with consolidated versions and obsolete modules cleaned up at the end of each phase.

4. **Test Execution**: Run tests using Python's built-in unittest module, not pytest. Individual test suites: `python Tests/test_calculate_arithmetic.py`. Consolidated tests: `python Tests/test_consolidated_tools.py`. Do not use pytest commands.

5. **Running and Restarting the SharkMath-MCP server**: Prompt the user to restart the MCP server when needed.  The server is managed by the user, so do not start a new server instance unless instructed to do so.

## Current State Analysis
- **Current Tools**: 18 total tools (4 consolidated + 14 individual) - DOWN FROM 70+
- **Consolidated Tools**: 4 major consolidations completed (arithmetic, trigonometry, statistics, unit conversions)
- **Current Test Files**: 152+ tests across consolidated and individual tool test files
- **Current AI Agent Tests**: 60+ test prompts in `mcp_tests.md` (updated for consolidated tools)
- **Issue Resolved**: MCP tool registration limits solved through consolidation
- **Architecture**: Parameter-based routing successfully implemented and tested

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

### **Phase 1: Core Infrastructure Setup - ✅ COMPLETED**
**Objective**: Establish consolidated tool architecture and testing framework

#### Step 1.1: Create Consolidated Tool Template - ✅ COMPLETED
✅ **Created `consolidated_tool_template.py`** - Template for parameter-based routing
✅ **Defined standard parameter patterns** - Consistent interface across all tools
✅ **Created operation mapping dictionaries** - Systematic lookup for all operations
✅ **Implemented standard error handling** - Uniform ✅/❌ response patterns

#### Step 1.2: Create Prototype Tool - ✅ COMPLETED
✅ **Implemented `convert_units` as prototype** - Most complex consolidated tool
✅ **Included all 42 current conversions** - Energy, time, temperature, length, weight, volume
✅ **Added parameter validation** - Ensure robust input handling  
✅ **Tested prototype thoroughly** - Verify all conversions work correctly

#### Step 1.3: Update Testing Infrastructure - ✅ COMPLETED
✅ **Created `Tests/test_consolidated_tools.py`** - New test file for consolidated tools (28 tests passing)
✅ **Updated `Tests/README.md`** - Document new testing approach
✅ **Created consolidated test patterns** - Template for testing multi-function tools
✅ **Implemented parameter validation tests** - Test invalid operations and parameters

**Phase 1 Results:**
- **✅ Tool count reduction proven**: 42 conversion tools → 1 consolidated tool (97.6% reduction)
- **✅ All functionality preserved**: 42 conversions working identically to individual tools
- **✅ Template system established**: Reusable patterns for future consolidation phases
- **✅ Testing framework proven**: 28/28 tests passing with comprehensive validation
- **✅ Architecture validated**: Parameter-based routing works effectively for complex multi-function tools

**Phase 2 Status: ✅ COMPLETED**
- **✅ Step 2.1 Complete**: `calculate_arithmetic` consolidated tool with all arithmetic and power operations (45/45 tests passing)
- **✅ Step 2.2 Complete**: `calculate_trigonometry` consolidated tool with all trigonometric functions (42/42 tests passing)
- **✅ Step 2.3 Complete**: `calculate_statistics` consolidated tool with all statistical operations (37/37 tests passing)
- **✅ Step 2.4 Complete**: Phase 2 cleanup, documentation updates, and file cleanup finished
- **✅ Individual Test Suites**: Dedicated test files per consolidated tool approach fully implemented and working

---

### **Phase 2: Mathematics Core Tools - ✅ COMPLETED**
**Objective**: Consolidate fundamental mathematical operations

#### Step 2.1: Arithmetic Consolidation - ✅ COMPLETED
✅ **Create `calculate_arithmetic`** - Consolidate add, subtract, multiply, divide, power, square, cube, sqrt, cbrt
✅ **Migrate from `arithmetic.py`** - Move logic to consolidated tool
✅ **Update tests** - Created dedicated test suite (`test_calculate_arithmetic.py` with 45/45 tests passing)
✅ **Replace original modules** - Replaced `arithmetic.py` and removed `power_operations.py` with consolidated version
✅ **Verify MCP integration** - Tool registers and functions correctly
✅ **Clean up obsolete files** - Removed temporary consolidated files

#### Step 2.2: Trigonometry Functions - ✅ COMPLETED
✅ **Create `calculate_trigonometry`** - Consolidate sin, cos, tan, asin, acos, atan, atan2 (radians/degrees)
✅ **Replace `trigonometric.py`** - Overwrite with consolidated tool using original filename  
✅ **Update tests** - Create dedicated test suite (`test_calculate_trigonometry.py`) - 42/42 tests passing
✅ **Include angle unit support** - Support both radians and degrees with proper validation

#### Step 2.3: Statistics Functions - ✅ COMPLETED
✅ **Create `calculate_statistics`** - Consolidate mean, median, mode, std_dev, variance, range_stats, percentile
✅ **Replace `stats_operations.py`** - Overwrite with consolidated tool using original filename  
✅ **Update tests** - Create dedicated test suite (`test_calculate_statistics.py`) - 37/37 tests passing
✅ **Include percentile support** - Add percentile calculation with proper interpolation

#### Step 2.4: Phase 2 Cleanup and Documentation - ✅ COMPLETED
✅ **Verify no obsolete modules remain** - Ensured no leftover individual tool files
✅ **Update `sharkmath_server.py`** - Register new consolidated tools, removed obsolete imports
✅ **Clean up legacy test files** - Removed obsolete individual tool tests (test_arithmetic.py, test_power_operations.py, test_trigonometric.py, test_statistics.py)
✅ **Remove obsolete modules** - Removed conversions.py and other duplicate modules
✅ **Update `.github/copilot-instructions.md`** - Document new consolidated tool structure
✅ **Update `Tests/mcp_tests.md`** - Convert test prompts to use consolidated tools
✅ **Update `Tests/mcp_test_expected.md`** - Update expected results for new tool calls (started)
✅ **Update `Tests/README.md`** - Document new individual test suite approach

---

### **Phase 3: Advanced Mathematics Tools**
**Objective**: Consolidate specialized mathematical functions

#### Step 3.1: Logarithmic and Exponential
🔲 **Create `calculate_logarithmic`** - Consolidate ln, log10, log_base, exponential
🔲 **Replace `logarithmic.py`** - Overwrite with consolidated tool using original filename
🔲 **Update tests** - Create dedicated test suite (`test_calculate_logarithmic.py`)
🔲 **Include domain validation** - Ensure proper input validation

#### Step 3.2: Hyperbolic Functions
🔲 **Create `calculate_hyperbolic`** - Consolidate sinh, cosh, tanh
🔲 **Replace `hyperbolic.py`** - Overwrite with consolidated tool using original filename
🔲 **Update tests** - Create dedicated test suite (`test_calculate_hyperbolic.py`)
🔲 **Include overflow protection** - Handle large input values

#### Step 3.3: Precision and Number Theory
🔲 **Create `format_precision`** - Consolidate round, floor, ceiling, truncate, absolute
🔲 **Create `analyze_numbers`** - Consolidate factorial, gcd, lcm, is_prime, prime_factors, is_perfect_square, fibonacci
🔲 **Replace `precision.py` and `number_theory.py`** - Overwrite with consolidated tools
🔲 **Merge `combinatorics.py`** - Integrate into `analyze_numbers` tool
🔲 **Update tests** - Create dedicated test suites for both tools
🔲 **Phase 3 Cleanup** - Verify no obsolete modules remain from precision/number theory consolidation

---

### **Phase 4: Applied Mathematics Tools**
**Objective**: Consolidate application-specific mathematical functions

#### Step 4.1: Equation Solvers
🔲 **Create `solve_equations`** - Consolidate solve_quadratic, compound_interest, linear equations
🔲 **Extract from `advanced_calc.py`** - Split advanced_calc into equation and geometry tools
🔲 **Update tests** - Create dedicated test suite (`test_solve_equations.py`)
🔲 **Include complex number handling** - Handle all solution types

#### Step 4.2: Geometry Tools
🔲 **Create `calculate_geometry_2d`** - Consolidate distance_2d, slope, circle area/circumference, triangle area, rectangle area/perimeter
🔲 **Create `calculate_geometry_3d`** - Consolidate sphere, cylinder, cone, prism calculations
🔲 **Replace `advanced_calc.py`** - Split remaining functions into new geometry modules
🔲 **Update tests** - Create dedicated test suites (`test_calculate_geometry_2d.py`, `test_calculate_geometry_3d.py`)
🔲 **Include all geometric operations** - Comprehensive shape calculations

#### Step 4.3: Matrix Operations
🔲 **Create `manipulate_matrices`** - Consolidate matrix_add, matrix_multiply, matrix_determinant, matrix_transpose
🔲 **Replace `matrix_operations.py`** - Overwrite with consolidated tool using original filename
🔲 **Update tests** - Create dedicated test suite (`test_manipulate_matrices.py`)
🔲 **Include JSON parsing and validation** - Handle matrix input formats
🔲 **Phase 4 Cleanup** - Verify no obsolete modules remain from applied math consolidation

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

#### Step 6.3: Final Integration and Cleanup
🔲 **Update `sharkmath_server.py`** - Register all consolidated tools
🔲 **Final module cleanup** - Verify all obsolete individual tool modules removed
🔲 **Remove temporary files** - Clean up any "consolidated_" prefixed files used during development
🔲 **Create migration guide** - Document transition from individual to consolidated tools
🔲 **Performance testing** - Ensure consolidated tools perform efficiently
🔲 **Final verification** - Confirm no legacy individual tools remain in codebase

---

## Testing Strategy

### **Individual Tool Test Suites Approach**

#### Separate Test Files for Each Consolidated Tool
- **`Tests/test_calculate_arithmetic.py`** - Dedicated test suite for arithmetic operations
- **`Tests/test_calculate_trigonometry.py`** - Dedicated test suite for trigonometric functions  
- **`Tests/test_convert_units.py`** - Dedicated test suite for unit conversions
- **`Tests/test_calculate_statistics.py`** - Dedicated test suite for statistical operations
- **`Tests/test_[tool_name].py`** - Pattern for each consolidated tool

#### Test File Structure Example
```python
# Tests/test_calculate_arithmetic.py
class TestCalculateArithmetic:
    def test_add_operation(self):
        # Test: calculate_arithmetic("add", 5, 3)
        
    def test_divide_by_zero_error(self):
        # Test: calculate_arithmetic("divide", 10, 0)
        
    def test_power_operation(self):
        # Test: calculate_arithmetic("power", base=2, exponent=8)
        
    def test_invalid_operation_error(self):
        # Test: calculate_arithmetic("invalid", 1, 2)
```

### **Test Migration Strategy**

#### Phase A: Create New Consolidated Test Suites
1. **Create individual test files** - One test file per consolidated tool
2. **Implement comprehensive test coverage** - All operations, parameters, and error conditions
3. **Verify test equivalency** - Ensure new tests cover all functionality from original individual tests
4. **Run parallel testing** - Both old and new test suites during transition

#### Phase B: Legacy Test Cleanup  
1. **Cross-reference test coverage** - Map original tests to new consolidated tests
2. **Verify no functionality gaps** - Ensure all edge cases are preserved
3. **Remove obsolete test files** - Clean up original individual tool tests after verification
4. **Update test documentation** - Reflect new testing structure

#### Files Successfully Cleaned Up After Phase 2 Completion
- **✅ `Tests/test_arithmetic.py`** - REMOVED (replaced with `Tests/test_calculate_arithmetic.py`)
- **✅ `Tests/test_trigonometric.py`** - REMOVED (replaced with `Tests/test_calculate_trigonometry.py`)
- **✅ `Tests/test_power_operations.py`** - REMOVED (merged into `Tests/test_calculate_arithmetic.py`)
- **✅ `Tests/test_statistics.py`** - REMOVED (replaced with `Tests/test_calculate_statistics.py`)
- **✅ `conversions.py`** - REMOVED (functionality moved to `convert_units.py`)

#### Files to Clean Up in Future Phases
- **`Tests/test_logarithmic.py`** - Replace with `Tests/test_calculate_logarithmic.py` (Phase 3)
- **`Tests/test_hyperbolic.py`** - Replace with `Tests/test_calculate_hyperbolic.py` (Phase 3)
- **`Tests/test_precision.py`** - Replace with `Tests/test_format_precision.py` (Phase 3)
- **`Tests/test_number_theory.py`** - Replace with `Tests/test_analyze_numbers.py` (Phase 3)
- **`Tests/test_combinatorics.py`** - Merge into `Tests/test_analyze_numbers.py` (Phase 3)
- **`Tests/test_advanced_calc.py`** - Split into geometry and equation solver tests (Phase 4)
- **`Tests/test_matrix_operations.py`** - Replace with `Tests/test_manipulate_matrices.py` (Phase 4)

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
1. **✅ Unit Testing** - Each consolidated tool tested individually with dedicated test suites
2. **✅ Integration Testing** - Verified MCP server registration and execution for all consolidated tools
3. **✅ Regression Testing** - Ensured all original functionality preserved across 152+ tests  
4. **🔲 Performance Testing** - Verify response times under 100ms (to be done in Phase 3+)
5. **🔄 AI Agent Testing** - Updated and executing test prompts (partially completed for consolidated tools)

---

## Documentation Updates

### **Files to Update**

#### Core Documentation
✅ **`.github/copilot-instructions.md`** - Complete rewrite for consolidated architecture (COMPLETED)
🔲 **`README.md`** - Update with new tool structure and usage examples  
🔲 **`sharkmath_enhancement_tasks.md`** - Update to reflect consolidated approach

#### Test Documentation  
✅ **`Tests/README.md`** - Document consolidated testing approach (COMPLETED)
✅ **`Tests/mcp_tests.md`** - Convert all 60+ prompts to consolidated tool format (COMPLETED for major tools)
� **`Tests/mcp_test_expected.md`** - Update expected results for consolidated tools (PARTIALLY COMPLETED)
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
1. **✅ Phase 1 Complete** - Prototype `convert_units` tool working with full test coverage (COMPLETED - 28/28 tests passing, 42 conversions working)
2. **✅ Phase 2 Complete** - Core math tools (arithmetic, trig, stats) consolidated and tested (COMPLETED - 124+ tests passing across 3 consolidated tools)
3. **🔲 Phase 3 Complete** - Advanced math tools consolidated with documentation updated  
4. **🔲 Phase 4 Complete** - Applied math tools working with comprehensive test coverage
5. **🔲 Phase 5 Complete** - All business/CS tools implemented and integrated
6. **🔲 Phase 6 Complete** - Full refactoring complete, all documentation updated, performance validated

---

## Success Criteria

### **Functional Requirements**
- ✅ **Tool count reduced** from 70+ to 18 consolidated tools (4 consolidated + 14 individual)
- ✅ **All functionality preserved** - No loss of mathematical capabilities across 152+ tests
- ✅ **Parameter-based routing** - Clear, unambiguous operation specification implemented
- ✅ **Consistent error handling** - Uniform ✅/❌ response patterns across all consolidated tools
- 🔄 **Performance maintained** - All operations complete within 100ms (verified for consolidated tools, full testing pending)

### **Quality Requirements**  
- ✅ **100% test coverage** - All consolidated tools thoroughly tested (124+ tests for 4 major consolidations)
- ✅ **Documentation completeness** - All consolidated tools and parameters documented
- ✅ **MCP integration** - All consolidated tools register and execute correctly in MCP server

### **Maintenance Requirements**
- ✅ **Reduced complexity** - Easier to add new operations to existing consolidated tools
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
1. **✅ Review and approve** this refactoring plan (COMPLETED)
2. **✅ Create Phase 1 branch** for development work (COMPLETED)
3. **✅ Begin with `consolidated_tool_template.py`** - Establish patterns (COMPLETED)
4. **✅ Implement `convert_units` prototype** - Prove the consolidation approach (COMPLETED)
5. **✅ Set up consolidated testing framework** - Foundation for all testing (COMPLETED)
6. **✅ Complete Phase 2** - Consolidate core mathematical operations (COMPLETED)

### **Next Phase Actions**
1. **Begin Phase 3** - Advanced mathematics tools (logarithmic, hyperbolic, precision, number theory)
2. **Continue documentation updates** - Complete remaining test prompt updates
3. **Performance validation** - Benchmark consolidated tool response times
4. **Consider Phase 4 planning** - Applied mathematics tools preparation

### **Decision Points**
1. **✅ Approve overall approach** - Confirm 18-tool consolidation strategy (APPROVED)
2. **✅ Confirm timeline** - Adjust phases based on available development time (CONFIRMED)
3. **✅ Tool naming conventions** - Finalize naming pattern for consolidated tools (FINALIZED)
4. **✅ Parameter standards** - Use typical/widely-accepted MCP parameter naming and validation patterns (IMPLEMENTED)
5. **🔄 Phase 3 readiness** - Confirm readiness to proceed with advanced mathematics consolidation

This refactoring plan transforms SharkMath from a tool-count-limited system to a scalable, maintainable mathematical toolkit while preserving all functionality and improving the development experience.
