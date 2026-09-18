from abc import ABC


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁBaseErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class BaseError(Exception, ABC):
    @_mutmut_mutated(mutants_xǁBaseErrorǁ__init____mutmut)
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)
    def xǁBaseErrorǁ__init____mutmut_orig(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)
    def xǁBaseErrorǁ__init____mutmut_1(self, message: str) -> None:
        self._message = None
        super().__init__(self._message)
    def xǁBaseErrorǁ__init____mutmut_2(self, message: str) -> None:
        self._message = message
        super().__init__(None)

    @property
    def message(self) -> str:
        return self._message

mutants_xǁBaseErrorǁ__init____mutmut['_mutmut_orig'] = BaseError.xǁBaseErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseErrorǁ__init____mutmut['xǁBaseErrorǁ__init____mutmut_1'] = BaseError.xǁBaseErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseErrorǁ__init____mutmut['xǁBaseErrorǁ__init____mutmut_2'] = BaseError.xǁBaseErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
