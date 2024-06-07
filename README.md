# AI-Summarizer

A simple web application that uses a custom Llama model specifically tuned for Norwegian text by [RuterNorway](https://huggingface.co/RuterNorway/Llama-2-13b-chat-norwegian). The application allows the user to input text and receive a summarized version.

## Prerequisites

### Ollama

- [Install Ollama](https://ollama.com/)
- Serve Ollama using `ollama serve`

### Custom Ollama Model

- Download the quantized GGUF version of the model from [Hugging Face](https://huggingface.co/jankovicsandras/Llama-2-13b-chat-norwegian-Q5_K_M-GGUF)
- Drag the model file into the `models` folder
- Rename the model file to `llama-2-13b-chat-norwegian.gguf`
- Create a model file:

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

- Create the custom Ollama model by running:

  ```sh
  ollama create llama-nor -f .modelfile
  ```

### Python Dependencies

- Install Python dependencies using:

  ```sh
  pip install -r requirements.txt
  ```

## Running the Application

1. Start the Flask application:

   ```sh
   python main.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

- Enter the text you want to summarize in the "Tekst å summere" field.
- Click the "Summer" button.
- The summarized text will appear in the "Sammendrag" field.

## Demo

[YouTube Demo](https://www.youtube.com/watch?v=x-hK-ZK9J-E)

## References

- [Hugging Face Model](https://huggingface.co/jankovicsandras/Llama-2-13b-chat-norwegian-Q5_K_M-GGUF)
- [Ollama Python Library](https://github.com/ollama/ollama-python)
