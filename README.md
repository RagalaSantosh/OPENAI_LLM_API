# OPENAI_LLM_API
This is a chatbot developed using OpenAI LLM with REST API Integration

**Features:**

1. **OpenAI LLM Integration:** Seamlessly interacts with OpenAI's large language models for chatbot responses. (Specify the LLM you're using, e.g., ChatGPT, Jurassic-1 Jumbo)
2. **REST API with FastAPI:** Provides a user-friendly REST API built with FastAPI, enabling easy integration into various applications.
3. **Topic-Based Generation:** Allows sending topics through the API to guide the chatbot's response generation.

   
**Installation:**

**Prerequisites:**
Python 3.11 or later (https://www.python.org/downloads/)

Clone Repository:
git clone https://github.com/RagalaSantosh/OPENAI_LLM_API.git


**Create Virtual Environment (recommended using Anaconda):**
pip install -r requirements.txt

**Usage:**

**Run the API Server:**
python app.py

1. This will start the FastAPI server, typically on port 8000 by default. You can customize the port by modifying the port parameter in the app.py script.

   
**Send Requests:** Use tools like Postman, cURL, or your preferred HTTP client to send POST requests to the following endpoint:
http://localhost:8000/generate  # Replace with your server's URL if running remotely
or use **calling.py**

**Include a JSON body with the topic key:**

JSON
{
  "topic": "Your desired topic"
}


**Response:** The API will return a JSON response containing the chatbot's generated text based on the provided topic.
