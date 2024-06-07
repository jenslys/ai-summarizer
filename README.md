# AI-Summarizer

A simple web application that uses a custom Llama model specifically tuned for Norwegian text by [RuterNorway](https://huggingface.co/RuterNorway/Llama-2-13b-chat-norwegian). The application allows the user to input text and receive a summarized version.

## Prerequisites

### Ollama

- [Install Ollama](https://ollama.com/)
- Serve Ollama using `ollama serve`

### Custom Ollama Model

1. **Download the Model**:
   - Download the quantized GGUF version of the model from [Hugging Face](https://huggingface.co/jankovicsandras/Llama-2-13b-chat-norwegian-Q5_K_M-GGUF)
   - Drag the model file into the `models` folder
   - Rename the model file to `llama-2-13b-chat-norwegian.gguf`

2. **Create a Model File**:
   - Create a model file with the following content:

     ```sh
     # set the base model 
     FROM llama-2-13b-chat-norwegian.gguf

     # Set custom parameter values
     PARAMETER temperature 0.7

     # Define stop tokens to ensure proper parsing of sections
     PARAMETER stop  </>
     PARAMETER stop  </>
     PARAMETER stop  </>
     PARAMETER stop <|reserved_special_token|>

     # Set the model template to handle summarization
     TEMPLATE """
     {{ if .System }} </system>
     {{ .System }}{{ end }}
     {{ if .Prompt }} </user>
     {{ .Prompt }}{{ end }}
     </assistant>
     {{ .Response }}
     """

     SYSTEM Du er en erfaren journalist. Svar med en kort og nøyaktig oppsummering av informasjonen som er gitt.
     ```

3. **Create the Custom Ollama Model**:
   - Run the following command to create the custom model:

     ```sh
     ollama create llama-nor -f .modelfile
     ```

### Python Dependencies

- Install Python dependencies using:

  ```sh
  pip install -r requirements.txt
  ```

## Running the Application

1. **Start the Flask Application**:

   ```sh
   python main.py
   ```

2. **Open the Web Application**:
   - Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

- Enter the text you want to summarize in the "Tekst å summere" field.
- Click the "Summer" button.
- The summarized text will appear in the "Sammendrag" field.

## Architecture

### Overview

The application consists of the following components:

1. **Frontend**: A simple HTML form where users can input text and receive the summarized output.
2. **Backend**: A Flask server that handles requests from the frontend and interacts with the Ollama model.
3. **Model**: A custom Llama model fine-tuned for Norwegian text summarization.

### Data Flow

1. **User Input**: The user enters text into the input field on the web page.
2. **Request Handling**: The frontend sends the input text to the Flask backend via an HTTP POST request.
3. **Model Interaction**: The Flask server processes the input and sends it to the Ollama model for summarization.
4. **Response Handling**: The Ollama model returns the summarized text to the Flask server.
5. **Display Output**: The Flask server sends the summarized text back to the frontend, where it is displayed to the user.

## Demo

[YouTube Demo](https://www.youtube.com/watch?v=x-hK-ZK9J-E)

## References

- [RuterNorway/Llama-2-13b-chat-norwegian](https://huggingface.co/RuterNorway/Llama-2-13b-chat-norwegian)
  - [Quantized GGUF Model](https://huggingface.co/jankovicsandras/Llama-2-13b-chat-norwegian-Q5_K_M-GGUF)
- [Ollama Python Library](https://github.com/ollama/ollama-python)
