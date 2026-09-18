from sqlalchemy.orm import DeclarativeBase


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class OrmBase(DeclarativeBase): ...
