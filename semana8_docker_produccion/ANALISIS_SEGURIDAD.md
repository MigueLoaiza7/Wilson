# Actividad 4 - Análisis de Riesgos de Seguridad

## 10. Riesgo de usar latest

El uso de la etiqueta latest puede generar comportamientos inesperados porque la imagen puede cambiar con el tiempo. Esto dificulta reproducir el mismo entorno y puede introducir errores o vulnerabilidades sin previo aviso.

## 11. Riesgo de privileged: true

La opción privileged otorga permisos elevados al contenedor, aumentando significativamente el riesgo de que una vulnerabilidad afecte al sistema anfitrión.

## 12. Riesgo de almacenar contraseñas en variables visibles

Las credenciales pueden quedar expuestas en archivos de configuración, repositorios o registros, comprometiendo la seguridad del sistema.

## 13. Riesgo de montar docker.sock

Permite que un contenedor controle Docker en el host, lo que puede dar acceso a recursos críticos y elevar privilegios.

## 14. Mejoras recomendadas

* Utilizar versiones específicas de imágenes.
* Ejecutar los contenedores como usuario no root.
* Utilizar Docker Secrets para datos sensibles.
* Evitar privileged: true salvo casos excepcionales.
* Evitar montajes innecesarios de docker.sock.
* Exponer únicamente los puertos requeridos.
* Aplicar healthchecks y restart policies.
