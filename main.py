import ollama
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Initialize the Flask application
app = Flask(__name__)

# Initialize SocketIO with the Flask app
socketio = SocketIO(app)


# Define the route for the root URL
@app.route("/")
def index():
    # Render the index.html template when the root URL is accessed
    return render_template("index.html")


# Define the event handler for the "summarize" event
@socketio.on("summarize")
def handle_summarization(json):
    # Extract the text to be summarized from the incoming JSON data
    text = json["text"]

    # Start a streaming chat with the custom Llama model
    stream = ollama.chat(
        model="llama-nor:latest",  # Specify the model to use
        messages=[{"role": "user", "content": text}],  # Provide the user message
        stream=True,  # Enable streaming responses
    )

    # Iterate over the streaming response chunks
    for chunk in stream:
        # Emit each chunk of the response back to the client
        emit("response", {"content": chunk["message"]["content"]})


# Run the Flask application with SocketIO support
if __name__ == "__main__":
    socketio.run(app, debug=True)
