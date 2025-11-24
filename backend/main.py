from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from Ai_agent import SYSTEM_PROMPT, graph, parse_response

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/")
async def home():
    return {"status": "backend running 🎉"}

@app.post("/ask")
async def askMe(query: Message):

    try:
        inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}

        # FIX: Convert stream → list (prevents infinite block)
        stream_output = list(graph.stream(inputs, stream_mode="updates"))

        # FIX: Proper parse
        tool_called, final_response = parse_response(stream_output)

        if final_response is None:
            final_response = "I'm here with you. Let's talk."

        return {
            "response": final_response,
            "tool_called": tool_called
        }

    except Exception as e:
        return {"error": str(e)}
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
