# src/suspension/state/persistence/exceptions.py


class PersistenceError(Exception):
    """Base exception for persistence-related errors"""

    pass


class FileFormatError(PersistenceError):
    """Error for invalid or unsupported file formats"""

    pass


class SerializationError(PersistenceError):
    """Error during serialization/deserialization"""

    pass


class ValidationError(PersistenceError):
    """Error during data validation"""

    pass
