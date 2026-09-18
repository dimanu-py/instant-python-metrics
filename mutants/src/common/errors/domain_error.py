from common.errors.base_error import BaseError


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DomainError(BaseError): ...
