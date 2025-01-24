# State Selectors

## Overview

This directory contains state selectors that provide efficient, memoized access to the application state. We use
the `py-memoize` library to cache selector results and prevent unnecessary recalculations.

## Memoization Profiles

We provide three different caching profiles for different use cases:

### STABLE_CACHE

- **Update After:** 5 seconds
- **Expire After:** 30 seconds
- **Max Items:** 100
- **Use Case:** For selectors that access structural or configuration data that changes infrequently
- **Example Use Cases:**
    - Navigation structure
    - Configuration settings
    - Static data mappings

```python
@create_selector(**STABLE_CACHE)
def select_navigation_items(state: ApplicationState) -> Dict[str, NavigationItem]:
    return state.ui.navigation.items
```

### DYNAMIC_CACHE

- **Update After:** 1 second
- **Expire After:** 5 seconds
- **Max Items:** 100
- **Use Case:** For selectors that access frequently changing UI state
- **Example Use Cases:**
    - Selected items
    - Active elements
    - UI visibility states

```python
@create_selector(**DYNAMIC_CACHE)
def select_selected_item_id(state: ApplicationState) -> Optional[str]:
    return state.ui.navigation.selected_item_id
```

### CALCULATION_CACHE

- **Update After:** 100ms
- **Expire After:** 1 second
- **Max Items:** 50
- **Use Case:** For computationally expensive calculations that need near-immediate updates
- **Example Use Cases:**
    - Plot calculations
    - Complex data transformations
    - Real-time computations

```python
@create_selector(**CALCULATION_CACHE)
def calculate_plot_data(state: ApplicationState) -> PlotData:
    # Complex calculations here
    return plot_data
```

## When to Use Memoization

### Do Memoize

- Complex calculations that are expensive to compute
- Filtering operations on large collections
- Data transformations that are used by multiple components
- Selectors that combine multiple pieces of state
- Calculations that feed into visualizations or plots

### Don't Memoize

- Simple boolean checks
- Direct state access without transformation
- Selectors that are only used once
- Very frequently changing values where cache invalidation overhead might exceed benefits

## Creating a New Selector

1. **Determine the Caching Profile**
    - How often does the data change?
    - How expensive is the computation?
    - How critical is immediate update reflection?

2. **Apply the Appropriate Decorator**

```python
from .utils import create_selector, STABLE_CACHE, DYNAMIC_CACHE, CALCULATION_CACHE


# For structural data
@create_selector(**STABLE_CACHE)
def select_structural_data(state: ApplicationState) -> StructuralData:
    return complex_transformation(state.data)


# For UI state
@create_selector(**DYNAMIC_CACHE)
def select_ui_state(state: ApplicationState) -> UiState:
    return state.ui.current_state


# For heavy calculations
@create_selector(**CALCULATION_CACHE)
def calculate_complex_data(state: ApplicationState) -> ComplexData:
    return expensive_calculation(state.data)
```

## Best Practices

1. **Pure Functions**
    - Selectors should be pure functions
    - Output should depend only on input parameters
    - No side effects

2. **Type Hints**
    - Always include proper type hints
    - Makes selector usage clearer
    - Helps catch errors early

3. **Documentation**
    - Include docstrings explaining the selector's purpose
    - Document any complex transformations
    - Note any performance considerations

4. **Performance Considerations**
    - Consider memory usage when setting max_items
    - Balance update_after and expire_after times
    - Monitor cache hit rates in production

5. **Composition**
    - Break complex selectors into smaller, reusable pieces
    - Use selector composition for complex derivations

```python
@create_selector(**DYNAMIC_CACHE)
def select_derived_data(state: ApplicationState) -> DerivedData:
    base_data = select_base_data(state)
    return transform(base_data)
```

## Testing

- Test selectors with different state configurations
- Verify memoization is working as expected
- Test edge cases and boundary conditions
- Consider cache invalidation scenarios

## Example Implementation

```python
from typing import Dict, Optional
from ..types.application import ApplicationState
from ..types.navigation import NavigationItem
from .utils import create_selector, STABLE_CACHE


@create_selector(**STABLE_CACHE)
def select_navigation_items(
        state: ApplicationState
) -> Dict[str, NavigationItem]:
    """
    Select all navigation items from the state.
    Uses STABLE_CACHE as the structure changes infrequently.
    
    Args:
        state: The application state
        
    Returns:
        Dictionary of navigation items keyed by ID
    """
    return state.ui.navigation.items
```

## Common Pitfalls

1. **Over-memoization**
    - Don't memoize simple operations
    - Consider the overhead of cache management

2. **Cache Invalidation**
    - Be aware of when caches need to be invalidated
    - Consider dependencies between selectors

3. **Memory Usage**
    - Monitor cache sizes in production
    - Adjust max_items based on usage patterns

4. **Update Timing**
    - Balance between responsiveness and performance
    - Consider user experience when setting timing parameters