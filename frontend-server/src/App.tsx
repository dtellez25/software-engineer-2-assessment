import { useState, useEffect } from 'react'
import './App.css'

// Define the message structure (id and message content)
type Message = {
  id: number;
  message: string;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [message, setMessage] = useState<string>("")
  const [error, setError] = useState<boolean>(false)

  // Fetch the initial message list from the api server
  useEffect(() => {
    const fetchMessages = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/messages')
        const data = await response.json()
        setMessages(data)
      } catch (err) {
        console.error('Error fetching messages:', err)
        setError(true)
      }
    }

    fetchMessages()
  }, [])

  // Submit a new message
  const submitMessage = async () => {
    if (message.trim() === "") {
      setError(true)
      return
    }

    try {
      const response = await fetch('http://127.0.0.1:8000/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: message }),
      })

      if (response.ok) {
        setError(false)
        setMessage("") // Clear input
        const updatedMessages = await (await fetch('http://127.0.0.1:8000/messages')).json()
        setMessages(updatedMessages)
      } else {
        setError(true)
      }
    } catch (err) {
      console.error('Error submitting message:', err)
      setError(true)
    }
  }

  // Delete a message by id
  const deleteMessage = async (id: number) => {
    try {
      await fetch(`http://127.0.0.1:8000/messages/${id}`, {
        method: 'DELETE',
      })
      const updatedMessages = await (await fetch('http://127.0.0.1:8000/messages')).json()
      setMessages(updatedMessages)
    } catch (err) {
      console.error('Error deleting message:', err)
    }
  }

  // Move a message up in the list
  const moveMessageUp = (id: number) => {
    const idx = messages.findIndex(m => m.id === id)
    if (idx > 0) {
      const newMessages = [...messages]
      ;[newMessages[idx], newMessages[idx - 1]] = [newMessages[idx - 1], newMessages[idx]]
      setMessages(newMessages)
    }
  }

  // Move a message down in the list
  const moveMessageDown = (id: number) => {
    const idx = messages.findIndex(m => m.id === id)
    if (idx < messages.length - 1) {
      const newMessages = [...messages]
      ;[newMessages[idx], newMessages[idx + 1]] = [newMessages[idx + 1], newMessages[idx]]
      setMessages(newMessages)
    }
  }

  return (
    <div className="container">
      <div className="messages">
        <h3>Messages</h3>
        <ol>
          {messages.map(msg => (
            <li className="message" key={msg.id}>
              <div className="button-group">
                <button onClick={() => deleteMessage(msg.id)}>❌</button>
                <div className="button-column-group">
                  <button onClick={() => moveMessageUp(msg.id)}>🔼</button>
                  <button onClick={() => moveMessageDown(msg.id)}>🔽</button>
                </div>
              </div>
              {msg.message}
            </li>
          ))}
        </ol>
      </div>
      <div className="form">
        <h3>Submit a new message</h3>
        <div className="input-group">
          <input value={message} onChange={(e) => setMessage(e.target.value)} />
          <button onClick={submitMessage}>submit</button>
          <p style={{ color: "hotPink", visibility: error ? "visible" : "hidden" }}>
            Message cannot be empty
          </p>
        </div>
      </div>
    </div>
  )
}

export default App
