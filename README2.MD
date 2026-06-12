1. ¿Qué es Git?

Es un sistema de control de versiones distribuido que permite registrar y gestionar cambios en los archivos de un proyecto.

2. ¿Para qué sirve Git?

Para mantener historial de cambios, trabajar con ramas, recuperar versiones anteriores y facilitar el trabajo colaborativo.

3. ¿Qué es un repositorio?

Es una carpeta controlada por Git que almacena los archivos y el historial de cambios del proyecto.

4. ¿Qué es un commit?

Es un registro de cambios acompañado de un mensaje descriptivo.

5. ¿Qué diferencia hay entre git add y git commit?

git add prepara los cambios y git commit los guarda en el historial.

Sobre GitHub

6. ¿Qué es GitHub?

Es una plataforma para alojar repositorios Git en la nube y facilitar la colaboración.

7. ¿Cuál es la diferencia entre Git y GitHub?

Git es la herramienta de control de versiones; GitHub es la plataforma donde se almacenan y comparten los repositorios.

8. ¿Qué es un repositorio remoto?

Es la copia del proyecto almacenada en GitHub.

9. ¿Qué hace git push?

Envía los cambios del repositorio local al remoto.

10. ¿Qué hace git pull?

Descarga e integra cambios del repositorio remoto al local.

Sobre ramas

11. ¿Qué es una rama (branch)?

Es una línea de trabajo independiente dentro del proyecto.

12. ¿Por qué usar ramas?

Para desarrollar cambios sin afectar la rama principal.

13. ¿Qué es merge?

Es la integración de cambios de una rama a otra.

14. ¿Qué comando usaste para crear una rama?

git switch -c feature-home

15. ¿Qué comando usaste para fusionar ramas?

git merge feature-home

Sobre archivos del proyecto

16. ¿Qué es README.md?

Es el archivo principal de documentación del proyecto.

17. ¿Qué es .gitignore?

Es un archivo que indica qué elementos no deben ser versionados.

18. ¿Por qué no se deben subir archivos .env?

Porque pueden contener información sensible como contraseñas o claves.

19. ¿Qué función tiene Dockerfile?

Define las instrucciones para construir una imagen Docker.

20. ¿Qué función tiene compose.yml?

Permite definir y ejecutar varios servicios Docker de forma conjunta.

Sobre DevOps

21. ¿Por qué Git y GitHub son importantes en DevOps?

Porque permiten trazabilidad, colaboración, control de versiones y sirven de base para integración y despliegue continuo.

22. ¿Qué es trazabilidad?

Es la capacidad de conocer quién hizo un cambio, cuándo lo hizo y qué modificó.

23. ¿Qué es integración continua (CI)?

Es la práctica de validar automáticamente los cambios que se integran al proyecto.

24. ¿Qué es despliegue continuo (CD)?

Es la automatización del proceso de publicación de nuevas versiones del software.

Preguntas que suelen hacer para comprobar comprensión

25. ¿Qué pasa si haces git commit sin git add?

Git no incluirá los cambios que no fueron agregados al área de preparación.

26. ¿Qué muestra git status?

El estado actual del repositorio y los archivos modificados.

27. ¿Qué muestra git log --oneline?

Un historial resumido de los commits realizados.

28. ¿Qué diferencia hay entre trabajo local y remoto?

El local está en tu computador y el remoto en GitHub.

29. ¿Cuál fue el flujo de trabajo que utilizaste?

git status → git add → git commit → git push → git pull.

30. ¿Por qué es importante escribir buenos mensajes de commit?

Porque permiten entender claramente qué cambios se realizaron en cada versión.