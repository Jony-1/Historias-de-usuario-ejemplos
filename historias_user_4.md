## Historia de Usuario 4: Mejora de Seguridad
**Título:** Implementación de autenticación multifactorial (MFA).

**Descripción:**  
Como administrador de seguridad,  
quiero implementar autenticación multifactor en el sistema,  
para proteger la información sensible de los usuarios contra accesos no autorizados.

**Criterios de aceptación:**
1. Permitir que los usuarios habiliten y gestionen la autenticación multifactor desde su perfil.
2. Integrar métodos de autenticación como aplicaciones de autenticación (Google Authenticator, Authy) y mensajes SMS.
3. Validar el MFA en todas las rutas protegidas antes de permitir el acceso.
4. Proveer un mecanismo de recuperación en caso de pérdida del dispositivo MFA, como preguntas de seguridad o un correo de emergencia.

**Notas técnicas:**
- Usar bibliotecas como `django-mfa2` o `Auth0` (según el stack) para implementar MFA de manera eficiente.
- Asegurarse de que los códigos de autenticación cumplan con estándares de generación segura (TOTP).

**Tareas relacionadas:**
- Escribir documentación para usuarios finales sobre cómo configurar MFA.
- Realizar pruebas de vulnerabilidad para garantizar que MFA no pueda ser omitido.
