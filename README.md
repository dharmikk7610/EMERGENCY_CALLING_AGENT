# 🚨 Emergency Calling AI Agent  
AI-powered agent that detects emergency intent from user conversations and automatically triggers a Twilio-based emergency call, while using OpenAI/Ollama models + RAG system for safe & contextual responses.

---

##Features:::::

  1. **Emergency Detection Agent**
- Uses LLM (OpenAI/Ollama) + RAG context to detect:
  - Danger situation
  - Panic text
  - Suicidal intent
  - Immediate help requests
- If detected → activates `emergency_call_tool()`.

 2. **Twilio Emergency Call Trigger**
- Automatically places a call to a pre-configured emergency contact or helpline.
- Secure: Only activated when **agent decides** based on rules.
- Uses Twilio Voice API.

 3. **Mental Health & Friendly Chat Tool**
- Uses a custom `@tool`:
```python
@tool
def ask_mental_health_specialist(prompt: str) -> str:
    return query_ollama(prompt)
