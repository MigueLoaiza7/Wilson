# Actividad 6 - Reflexión Final

## ¿Qué diferencia existe entre correr un contenedor y operarlo en producción?

Ejecutar un contenedor significa poner una aplicación en funcionamiento. Operarlo en producción implica además garantizar seguridad, monitoreo, disponibilidad, recuperación ante fallos y mantenimiento continuo.

## ¿Qué medida de seguridad te parece más valiosa y por qué?

La ejecución como usuario no root, porque reduce el impacto de posibles vulnerabilidades y limita los privilegios dentro del contenedor.

## ¿Qué error sería más grave en un despliegue real?

Exponer credenciales o secretos dentro de imágenes, repositorios o archivos de configuración accesibles.

## ¿Qué harías primero para mejorar un contenedor existente?

Revisar la seguridad básica, eliminar privilegios innecesarios, implementar healthchecks y utilizar políticas de reinicio automático.
