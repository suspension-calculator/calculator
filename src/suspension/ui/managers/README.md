# UI Managers

This directory contains manager classes that handle UI state and logic using Qt's native patterns, providing clean
separation of concerns and performant state management.

## Design Patterns

Managers in this directory follow these patterns:

- Utilize Qt's signals/slots for immediate UI updates
- Handle state persistence using QSettings
- Provide clear, type-safe interfaces
- Keep UI logic separate from calculation/business logic

## Manager Types

### Navigation Manager

Handles navigation state including:

- Tree view state management
- Page/view tracking
- Navigation history
- Layout preferences

### Theme Manager

Handles application theming:

- System theme integration
- Theme switching
- Component styling
- Theme persistence

### Layout Manager

Handles window/widget layouts:

- Panel configurations
- Window state
- Split view management
- Layout persistence

### Plot Manager (Planned)

Will handle:

- Plot configurations
- Real-time updates
- Data caching
- Export functionality

## Best Practices

1. Use Qt's signal/slot mechanism for state updates
2. Cache expensive calculations using py-memoize
3. Persist state appropriately using QSettings
4. Maintain clear type hints and documentation
5. Keep managers focused and single-purpose

## Testing

Managers should be:

1. Easily testable in isolation
2. Have clear dependencies
3. Use mockable interfaces
4. Support state verification

## State Persistence

- Use QSettings for UI state
- Cache calculation results appropriately
- Handle configuration import/export