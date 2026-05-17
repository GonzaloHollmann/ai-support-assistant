# Project Report: AI Support Assistant

## 1. Architecture Overview
The application follows a modular design separating the core logic (`run_query.py`), the prompt templates (`prompts/`), and the observability layer (`metrics/`). It uses OpenAI's `gpt-4o-mini` model for its balance between low latency and cost-effectiveness.

## 2. Prompt Engineering Technique
We implemented **Few-Shot Prompting**. 
- **Why?** LLMs can sometimes be unpredictable with JSON schemas. By providing explicit examples of "Question -> JSON Output", we anchor the model to the desired structure and tone.
- **Results:** This eliminated formatting errors and ensured the "confidence" and "recommended_actions" fields remained consistent.

## 3. Metrics & Performance
During testing, the average performance observed was:
- **Average Latency:** ~1200ms - 2500ms.
- **Average Cost:** < $0.0001 USD per request.
- **Tokens:** Most interactions stayed under 400 tokens.

## 4. Safety & Moderation
A **Moderation Layer** was added using OpenAI's Moderation API. This ensures that any adversarial prompt (e.g., hate speech or dangerous instructions) is blocked before reaching the LLM, protecting the system and reducing unnecessary costs.

## 5. Trade-offs and Future Improvements
- **Trade-off:** We chose `gpt-4o-mini` over `gpt-4o` to prioritize speed and cost, which is ideal for a high-volume support environment.
- **Improvement:** In a production environment, we would implement **RAG (Retrieval-Augmented Generation)** to connect the assistant to a real database of products and orders.
