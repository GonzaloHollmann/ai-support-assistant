import json

def test_json_structure():
    """Prueba que el formato que definimos sea el correcto."""
    # Simulamos una respuesta del modelo
    sample_response = '{"answer": "Hola", "confidence": 0.9, "recommended_actions": ["test"]}'
    
    try:
        data = json.loads(sample_response)
        # Verificamos que existan las llaves que pide nuestro "contrato"
        assert "answer" in data
        assert "confidence" in data
        assert "recommended_actions" in data
        print("✅ Test de estructura JSON: PASADO")
    except Exception as e:
        print(f"❌ Test de estructura JSON: FALLÓ ({e})")

if __name__ == "__main__":
    print("Ejecutando pruebas...")
    test_json_structure()