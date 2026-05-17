# Reporte de Proyecto: AI Support Assistant

## 1. Arquitectura general
La aplicación sigue un diseño modular que separa la lógica principal (`run_query.py`), las plantillas de prompts (`prompts/`) y la capa de observabilidad (`metrics/`). Utiliza el modelo `gpt-4o-mini` de OpenAI por su equilibrio entre baja latencia y costo-eficiencia.

## 2. Técnica de prompt engineering
Se implementó **Few-Shot Prompting**.

- **¿Por qué?** Los LLMs pueden ser impredecibles con esquemas JSON. Al proveer ejemplos explícitos de "Pregunta → JSON", se ancla el modelo a la estructura y tono deseados.
- **Resultados:** Se eliminaron los errores de formato y los campos `confidence` y `recommended_actions` se mantuvieron consistentes.

## 3. Métricas y rendimiento
- **Latencia promedio:** ~1.2–2.5s
- **Costo por solicitud:** < $0.0001 USD
- **Tokens por interacción:** < 400 tokens

## 4. Seguridad y moderación
Se agregó una **capa de moderación** utilizando la API de Moderación de OpenAI. Esto garantiza que cualquier prompt adversarial (por ejemplo, discurso de odio o instrucciones peligrosas) sea bloqueado antes de llegar al LLM, protegiendo el sistema y reduciendo costos innecesarios.

## 5. Compromisos y mejoras futuras
- **Compromiso adoptado:** Se eligió `gpt-4o-mini` sobre `gpt-4o` para priorizar velocidad y costo, ideal para entornos de soporte de alto volumen.
- **Mejora planificada:** En producción se implementaría **RAG (Generación Aumentada por Recuperación)** para conectar el asistente a una base de datos real de productos y pedidos.
