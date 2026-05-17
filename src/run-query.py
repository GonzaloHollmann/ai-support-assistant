import os
import time
import json
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_prompt():
    """Lee el prompt usando una ruta absoluta para evitar errores de ubicación."""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(base_path, "prompts", "main_prompt.txt")
    
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("⚠️ Advertencia: No se encontró main_prompt.txt, usando prompt básico.")
        return "Responde siempre en formato JSON con los campos: answer, confidence, recommended_actions."

def check_moderation(text):
    """
    BONUS: Verifica si el texto es seguro.
    Retorna True si el contenido es inapropiado.
    """
    response = client.moderations.create(input=text)
    return response.results[0].flagged

def save_metrics(metrics_dict):
    """Guarda las métricas asegurando que la carpeta exista en la raíz."""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    metrics_dir = os.path.join(base_path, "metrics")
    os.makedirs(metrics_dir, exist_ok=True)
    
    file_path = os.path.join(metrics_dir, "metrics.json")
    metrics_dict["timestamp"] = datetime.now().isoformat()
    
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except: data = []
    
    data.append(metrics_dict)
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"\n✅ Métricas guardadas en {file_path}")

def get_assistant_response(user_question):
    # Moderación (Seguridad)
    if check_moderation(user_question):
        return {"error": "Contenido inapropiado detectado."}, {"status": "blocked"}

    # Configuración y llamada
    start_time = time.time() 
    system_prompt = load_prompt()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ],
        temperature=0.7
    )
    end_time = time.time()
    
    # Procesamiento
    raw_content = response.choices[0].message.content
    try:
        content_json = json.loads(raw_content)
    except json.JSONDecodeError:
        content_json = {"error": "Invalid JSON response"}

    # Métricas
    metrics = {
        "latency_ms": (end_time - start_time) * 1000,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
        "estimated_cost_usd": (response.usage.prompt_tokens / 1_000_000 * 0.15) + 
                              (response.usage.completion_tokens / 1_000_000 * 0.60)
    }

    return content_json, metrics

if __name__ == "__main__":
    print("--- Bienvenido al Asistente de Soporte (AI) ---")
    print("Escribe 'salir' para terminar.\n")

    while True:
        pregunta_usuario = input("Haz tu pregunta: ")
        
        if pregunta_usuario.lower() in ["salir", "exit", "quit"]:
            print("¡Hasta luego!")
            break

        if not pregunta_usuario.strip():
            continue

        print("Procesando...")
        resultado, metriz = get_assistant_response(pregunta_usuario)
        
        print("\n--- RESPUESTA ---")
        print(json.dumps(resultado, indent=4, ensure_ascii=False))
        
        if "status" not in metriz:
            save_metrics(metriz)
            print(f"Latencia: {metriz['latency_ms']:.2f}ms | Costo: ${metriz['estimated_cost_usd']:.6f}")
        else:
            print("⚠️ La consulta fue bloqueada por seguridad.")
        print("-" * 30)