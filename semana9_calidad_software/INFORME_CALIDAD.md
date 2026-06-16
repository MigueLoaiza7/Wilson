# Informe de Calidad de Software - Semana 09

## 1. Identificación de la Funcionalidad

| Campo | Información |
|---------|---------|
| Historia de Usuario | HU-03 Solicitar turno virtual |
| Prioridad MoSCoW | Must Have |
| Proceso relacionado | Gestión de turnos virtuales |
| Diagrama asociado | BPMN Solicitar Turno |
| Función analizada | registrarTurno() |

## 2. Función Analizada

```javascript
function registrarTurno(datos) {
  if (!datos.nombre) {
    return "Nombre obligatorio";
  }

  if (!datos.documento) {
    return "Documento obligatorio";
  }

  if (!datos.servicio) {
    return "Servicio obligatorio";
  }

  return "Turno registrado";
}
```

## 3. Complejidad Ciclomática

| Elemento | Cantidad |
|---------|---------|
| Decisiones if | 3 |
| Decisiones else if | 0 |
| Ciclos for / while | 0 |
| switch / case | 0 |
| catch | 0 |
| Total decisiones | 3 |
| Complejidad total | 4 |

### Interpretación

La complejidad ciclomática es 4 porque existen tres decisiones (if) dentro de la función.

Fórmula:

Complejidad = Decisiones + 1

Complejidad = 3 + 1 = 4

## 4. Casos de Prueba

| Caso | Entrada | Camino probado | Resultado esperado |
|---------|---------|---------|---------|
| CP-01 | Sin nombre | Primer if | Nombre obligatorio |
| CP-02 | Sin documento | Segundo if | Documento obligatorio |
| CP-03 | Sin servicio | Tercer if | Servicio obligatorio |
| CP-04 | Datos completos | Camino exitoso | Turno registrado |

## 5. Cobertura Esperada

| Tipo de Cobertura | Resultado |
|---------|---------|
| Líneas | 100% |
| Funciones | 100% |
| Ramas | 100% |
| Sentencias | 100% |

### Explicación

Los casos de prueba propuestos permiten recorrer todos los caminos posibles de la función.

## 6. Registro de Deuda Técnica

| Hallazgo | Tipo de deuda | Riesgo | Acción sugerida |
|---------|---------|---------|---------|
| Validaciones simples | Calidad | Errores de entrada | Mejorar validaciones |
| No existen pruebas automáticas | Calidad | Fallos futuros | Implementar pruebas |
| Mensajes repetidos | Mantenimiento | Difícil actualización | Centralizar mensajes |

## 7. Análisis Estático Simulado

| Herramienta | Hallazgo | Severidad | Acción recomendada |
|---------|---------|---------|---------|
| ESLint | Cadenas repetidas | Baja | Usar constantes |
| SonarQube | Falta de pruebas unitarias | Media | Implementar pruebas |
| Semgrep | Validaciones insuficientes | Media | Mejorar validaciones |

## 8. Acciones de Mejora

1. Implementar pruebas unitarias.
2. Validar formatos de documento.
3. Centralizar mensajes de error.
4. Registrar eventos importantes.
5. Mejorar manejo de excepciones.

## 9. Conclusión Técnica

La funcionalidad Solicitar Turno Virtual presenta una complejidad ciclomática baja (4), permitiendo un mantenimiento sencillo. Los casos de prueba cubren todos los caminos lógicos identificados. Se detectaron oportunidades de mejora relacionadas con pruebas automatizadas, validaciones y mantenibilidad del código.