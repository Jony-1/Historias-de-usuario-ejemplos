## Historia de Usuario 3: Optimización del Rendimiento
**Título:** Optimización de rendimiento en consultas de base de datos.

**Descripción:**  
Como analista de rendimiento,  
quiero optimizar el tiempo de respuesta de las consultas más utilizadas,  
para garantizar un mejor rendimiento del sistema y la satisfacción del usuario.

**Criterios de aceptación:**
1. Identificar las consultas más lentas usando herramientas como APM (Application Performance Monitoring), logs de base de datos o índices de uso.
2. Proponer optimizaciones como el uso de índices, particionamiento o reducción del volumen de datos procesados.
3. Implementar optimizaciones y validar que las consultas optimizadas mejoran al menos un 20% su tiempo de respuesta en un entorno de pruebas.
4. Medir el impacto general del rendimiento del sistema después de los cambios mediante herramientas como JMeter o Locust.

**Notas técnicas:**
- Validar que las optimizaciones no impacten otras consultas relacionadas ni afecten la consistencia de los datos.
- En el caso de consultas sobre grandes volúmenes de datos, considerar estrategias de cacheo.

**Tareas relacionadas:**
- Crear scripts automatizados para ejecutar pruebas de rendimiento antes y después de las optimizaciones.
- Implementar un dashboard con métricas de tiempo de respuesta en Grafana o Kibana.
