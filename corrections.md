- En general no quiero que cada módulo tenga un comentario al inicio. Quitar esto si está en alguna
especificación de skill o subagent y registralo como convención.
- En test_acceptance validar solo el status code
- Mirar si uso pytest-bdd para los test de aceptación
- No hace falta importar from __future__ import annotations
- Nombres de tests más descriptivos, que expresen el comportamiento validado. Registrarlo
como convención
- Los nombres de los test que empiecen con 'should'. Registrarlo como convención
- Usar object mothers. Registrar convención
- En los test unitarios del router no veo que esté mockeando el caso de uso, está usando la implementación real
- Los nombres de los casos de uso son <modulo><acción>