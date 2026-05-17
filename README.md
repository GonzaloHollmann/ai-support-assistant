# AI Support Assistant - Multi-tasking Text Utility

Este proyecto es un asistente inteligente diseñado para ayudar a agentes de soporte técnico. Recibe preguntas de usuarios y devuelve una respuesta estructurada en JSON que incluye la respuesta sugerida, el nivel de confianza y acciones recomendadas.

## 🚀 Configuración y Ejecución

### 1. Requisitos Previos
- Python 3.8 o superior.
- Una cuenta de OpenAI con API Key.

### 2. Instalación

1. Clonar el repositorio:
   ```bash
   git clone <tu-url-de-github>
   cd ai-support-assistant
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   # En Windows: .\venv\Scripts\activate
   # En Mac/Linux: source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto y agrega tu clave:
```text
OPENAI_API_KEY=tu_clave_aqui
```

### 4. Ejecución

Para realizar una consulta:
```bash
python src/run_query.py
```

Para ejecutar los tests:
```bash
python tests/test_core.py
```

## 📊 Métricas Registradas

El sistema guarda automáticamente en `metrics/metrics.json`:
- Latencia (ms)
- Conteo de tokens (Prompt, Completion y Total)
- Costo estimado en USD.
- Timestamp de la consulta.

## 📄 Reporte Técnico

El reporte técnico que justifica las decisiones de ingeniería del proyecto se encuentra disponible en [`reports/PI_report_en.md`](reports/PI_report_en.md).
