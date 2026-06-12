# Actividad 1 - Docker en Producción

| Aspecto | Desarrollo / Local | Producción |
|----------|----------|----------|
| Imagen base | Puede usarse cualquier imagen | Se prefieren imágenes pequeñas y confiables |
| Usuario del proceso | Frecuentemente root | Usuario no root |
| Persistencia | Datos temporales | Uso de volúmenes |
| Secretos | Variables simples | Secrets gestionados |
| Healthcheck | Generalmente no se usa | Debe estar configurado |
| Restart Policy | No suele configurarse | Debe reiniciarse automáticamente |
| Puertos | Se exponen varios para pruebas | Solo los estrictamente necesarios |
| Filesystem | Lectura y escritura completa | Preferiblemente solo lectura |

## Explicación

Un contenedor que funciona localmente no está listo automáticamente para producción porque en producción se requieren medidas adicionales de seguridad, persistencia de datos, monitoreo, recuperación automática ante fallos y control de acceso.