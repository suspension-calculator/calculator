# State Actions

## Overview

This directory contains action definitions and action creators for managing state changes in the application. Actions
are the only way to trigger state changes in our Redux-like architecture.

## Action Structure

Each action should follow these key principles:

- Use dataclasses for action definitions
- Include an action type enum
- Provide action creator functions
- Follow proper field ordering in dataclasses

## Basic Action Example

First, define your action types:

```python
from dataclasses import dataclass
from enum import Enum


class ExampleActionType(Enum):
    UPDATE_VALUE = "UPDATE_VALUE"
    RESET_VALUE = "RESET_VALUE"
    SET_ERROR = "SET_ERROR"
```

## Action Class Definition

When creating action classes:

1. Use dataclasses
2. Put required fields BEFORE fields with defaults
3. Add clear docstrings
4. Keep actions focused and single-purpose

```python
@dataclass
class UpdateValueAction:
    """Action to update a specific value"""
    value: int  # Required field first
    type: ExampleActionType = ExampleActionType.UPDATE_VALUE  # Default field last


# ❌ WRONG - Default argument before required argument
@dataclass
class WrongAction:
    """This will raise a TypeError"""
    type: ExampleActionType = ExampleActionType.UPDATE_VALUE  # Default first
    value: int  # Required second
```

## Action Creators

Always provide action creator functions that:

1. Have clear, descriptive names
2. Include type hints
3. Have docstrings explaining their purpose
4. Handle any necessary data transformation

```python
def update_value(value: int) -> UpdateValueAction:
    """Create an action to update the value.

    Args:
        value: The new value to set

    Returns:
        An UpdateValueAction instance
    """
    return UpdateValueAction(value=value)
```

## Complete Example

Here's a complete example showing all the components together:

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional


# 1. Define Action Types
class UserActionType(Enum):
    UPDATE_PROFILE = "UPDATE_PROFILE"
    SET_PREFERENCES = "SET_PREFERENCES"
    LOGOUT = "LOGOUT"


# 2. Define Action Classes
@dataclass
class UpdateProfileAction:
    """Action to update user profile information"""
    username: str
    email: str
    type: UserActionType = UserActionType.UPDATE_PROFILE


@dataclass
class SetPreferencesAction:
    """Action to update user preferences"""
    theme: str
    notifications: bool
    type: UserActionType = UserActionType.SET_PREFERENCES


@dataclass
class LogoutAction:
    """Action to log out the user"""
    type: UserActionType = UserActionType.LOGOUT


# 3. Define Action Creators
def update_profile(username: str, email: str) -> UpdateProfileAction:
    """Create an action to update the user profile"""
    return UpdateProfileAction(username=username, email=email)


def set_preferences(theme: str, notifications: bool) -> SetPreferencesAction:
    """Create an action to set user preferences"""
    return SetPreferencesAction(theme=theme, notifications=notifications)


def logout() -> LogoutAction:
    """Create an action to log out the user"""
    return LogoutAction()
```

## Best Practices

### Do's ✅

1. Keep actions simple and focused
2. Use descriptive names for actions and creators
3. Include proper type hints
4. Add descriptive docstrings
5. Put required fields before optional fields
6. Use action creators instead of direct class instantiation

### Don'ts ❌

1. Don't put default arguments before required arguments
2. Don't include complex logic in action classes
3. Don't mutate action data after creation
4. Don't use actions for side effects
5. Don't include computed values that should be in selectors

## Testing

Actions should be easy to test:

```python
def test_update_profile_action():
    """Test the update profile action creator"""
    # Given
    username = "test_user"
    email = "test@example.com"

    # When
    action = update_profile(username=username, email=email)

    # Then
    assert action.type == UserActionType.UPDATE_PROFILE
    assert action.username == username
    assert action.email == email
```

## Common Pitfalls

1. **Circular Dependencies**
    - Keep action definitions independent of state types
    - Import domain types directly, not through state

2. **Action Bloat**
    - Keep actions focused on a single responsibility
    - Don't include derived data that can be calculated by selectors

3. **Type Safety**
    - Always use type hints
    - Consider using literal types for string constants
    - Use enums for action types

## Directory Structure

actions/
├── __init__.py # Exports all actions
├── navigation.py # Navigation-related actions
├── analysis.py # Analysis-related actions
├── user.py # User-related actions
└── README.md # This documentation
