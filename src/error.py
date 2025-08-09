from enum import Enum

class DBErrorKind(Enum):
    ConnectionError = "ConnectionError"
    QueryError = "QueryError"

class DBError(Exception):
    """Custom exception for database errors."""
    def __init__(self, message: str, error_kind: DBErrorKind):
        super().__init__(message)
        self.error_kind = error_kind
