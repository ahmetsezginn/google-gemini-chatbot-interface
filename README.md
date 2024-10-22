
# Google Gemini Chatbot Interface

This project is a Python-based interface to interact with the Google Gemini API. The interface allows users to upload files to Gemini. It also lets them initialize a chat session and send messages to the AI.

## Features
- **File Upload**: Easily upload files to the Gemini API for chat context.
- **Chat Initialization**: Configure a chat session with adjustable parameters like temperature and token limits.
- **Chat Interaction**: Send messages to the Gemini API and receive responses directly in the console.

## Getting Started

Follow these steps to set up the project and start interacting with the Google Gemini API.

### Prerequisites

Before you begin, ensure you have the following installed on your machine:
- Python 3.x
- Virtual environment tool (venv)
- A valid API key for the Google Gemini API.

### 1. Get Your Google Gemini API Key

To use this project, you need an API key from Google for the Gemini API. Follow these steps to obtain your API key:

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. If you don't already have a project, create a new one.
3. In the sidebar, navigate to "APIs & Services" > "Credentials."
4. Click on "Create Credentials" and select "API key."
5. Copy the API key that is generated. You'll need this to interact with the Gemini API.

### 2. Clone the Repository

First, clone the repository to your local machine:

```bash
# Clone the repository
git clone https://github.com/your-username/gemini-chatbot-interface.git
cd gemini-chatbot-interface
```

### 3. Set Up a Virtual Environment

It's recommended to use a virtual environment to keep your project dependencies isolated. You can create and activate it with the following commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 4. Install Dependencies

Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

### 5. Set Up Your API Key

You need to set your Google Gemini API key as an environment variable. You can do this by running the following command in your terminal:

```bash
export GENAI_API_KEY='your_api_key_here'
```

On Windows, use:

```bash
set GENAI_API_KEY='your_api_key_here'
```

Alternatively, you can directly replace the `self.api_key` in the `Model` class with your API key.

### 6. Running the Project

After setting up the environment and dependencies, you can run the chatbot interface:

```bash
python main.py
```

This will initiate a chat session with the Gemini API, and you'll be able to interact with it by sending messages.

### Example: Uploading a File

To upload a file to the Gemini API, you can modify the `upload_to_gemini` method and provide the correct file paths. The file will be available for use in your chat sessions.

## Contributing

Feel free to fork this project and contribute! Pull requests are welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Requirements

### `requirements.txt`
```
google-generativeai
```
