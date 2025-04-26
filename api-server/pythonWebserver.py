from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary in-memory storage
messages = []

# Endpoints

# GET    127.0.0.1:8000/messages                // Return a list of all messages
@app.get("/messages")
def get_messages():
    return messages

#POST   127.0.0.1:8000/messages                // Create a new message
@app.post("/messages")
def create_message(message: str):
    messages.append({"id": len(messages) + 1, "message": message})
    return {"status": "Message created"}

#PUT    127.0.0.1:8000/messages/:message_id    // Update an existing message
@app.put("/messages/{message_id}")
def update_message(message_id: int, new_message: str):
    for m in messages:
        if m["id"] == message_id:
            m["message"] = new_message
            return {"status": "Message updated"}
    return {"error": "Message not found"}

#DELETE 127.0.0.1:8000/messages/:message_id    // Delete an existing message
@app.delete("/messages/{message_id}")
def delete_message(message_id: int):
    global messages
    messages = [m for m in messages if m["id"] != message_id]
    return {"status": "Message deleted"}



# Run Uvicorn if this file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("pythonWebserver:app", host="127.0.0.1", port=8000, reload=True)