from database import get_all_messages, create_message, update_message, delete_message


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


app = FastAPI()

# Enable CORS to allow the frontend server to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the structure of incoming request bodies for creating/updating messages
class MessageIn(BaseModel):
    content: str


# Endpoints
# GET    127.0.0.1:8000/messages                // Return a list of all messages
@app.get("/messages")
def get_messages():
    return get_all_messages()

#POST   127.0.0.1:8000/messages                // Create a new message
@app.post("/messages")
def create_message_endpoint(message: MessageIn):
    message_id = create_message(message.content)
    return {"status": "Message created", "id": message_id}

#PUT    127.0.0.1:8000/messages/:message_id    // Update an existing message
@app.put("/messages/{message_id}")
def update_message_endpoint(message_id: int, message: MessageIn):
    rows_updated = update_message(message_id, message.content)
    if rows_updated == 0:
        return {"error": "Message not found"}
    return {"status": "Message updated"}

#DELETE 127.0.0.1:8000/messages/:message_id    // Delete an existing message
@app.delete("/messages/{message_id}")
def delete_message_endpoint(message_id: int):
    rows_deleted = delete_message(message_id)
    if rows_deleted == 0:
        return {"error": "Message not found"}
    return {"status": "Message deleted"}



# Run Uvicorn if this file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("pythonWebserver:app", host="127.0.0.1", port=8000, reload=True)