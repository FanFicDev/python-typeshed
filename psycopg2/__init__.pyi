from typing import Any, Iterable, Sequence, Optional

Row = Sequence[Any]

class cursor:
	def __init__(self, name: Optional[str] = None) -> None:
		self.rowcount: int
		...
	def __enter__(self) -> 'cursor': ...
	def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
	def __iter__(self) -> Any: ...
	def execute(self, sql: str, parms: Iterable[Any] = None) -> None: ...
	def fetchone(self) -> Optional[Row]: ...
	def fetchall(self) -> Iterable[Row]: ...
	def close(self) -> None: ...

class connection:
	def __enter__(self) -> 'connection': ...
	def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
	def cursor(self, name: Optional[str] = None) -> cursor: ...
	def commit(self) -> None: ...
	def close(self) -> None: ...

def connect(target: str) -> connection: ...
