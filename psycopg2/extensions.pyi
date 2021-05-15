import psycopg2
from typing import Type, Callable, TypeVar, Any, Optional, Sequence, Union

class AsIs:
	def __init__(self, sql: Union[str, int]) -> None:
		...

T = TypeVar('T')
def register_adapter(t: Type[T], adapter: Callable[[T], AsIs]) -> None:
	...

class QuotedString:
	def getquoted(self) -> bytes:
		...

def adapt(obj: Any) -> QuotedString:
	...

class _Caster:
	...

Caster = Callable[[Optional[str], psycopg2.cursor], Optional[T]]
def new_type(oids: Sequence[int], name: str, caster: Caster) -> _Caster:
	...

def register_type(caster: _Caster) -> None:
	...

