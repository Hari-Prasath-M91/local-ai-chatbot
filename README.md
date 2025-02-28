# 🤖 An AI Chatbot that runs Locally on your own device

## Overview
This project is a **simple AI chatbot** that runs **entirely on your local machine** using **LangChain, Ollama LLM, and Streamlit**. It allows you to ask questions and receive AI-generated responses in real-time without needing an internet connection after setup.

## Features
- **AI-powered chatbot** for answering user queries
- **Runs locally on your PC** without external API calls
- **Uses LangChain, Ollama LLM, and Streamlit** for a smooth experience
- **Simple and intuitive interface**

## 📖 Index
1. [Installation & Setup](#installation--setup)
    - [Clone the Repository](#1-clone-the-repository)
    - [Set Up a Virtual Environment](#2-set-up-a-virtual-environment-recommended)
    - [Install Dependencies](#3-install-dependencies)
    - [Install and Set Up Ollama](#4-install-and-set-up-ollama)
    - [Set Up Environment Variables](#5-set-up-environment-variables)
    - [Run the Chatbot](#6-run-the-chatbot)
2. [Usage](#usage)
3. [Troubleshooting](#troubleshooting)
4. [License](#license)
5. [Contact](#contact)

## Installation & Setup

### 1. Clone the Repository
First, download the project files to your local machine:
```sh
git clone https://github.com/your-repository-url.git
cd your-repository-folder
```

### 2. Set Up a Virtual Environment (Recommended)
Creating a virtual environment helps keep dependencies organized. Run:
```sh
python -m venv venv

```
Then activate it:
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```

### 3. Install Dependencies
Install the required Python packages:
```sh
pip install -r requirements.txt
```

### 4. Install and Set Up Ollama
Ollama is required to run the chatbot locally. Follow these steps:

1. **Download and Install Ollama**
   - Visit [Ollama’s official website](https://ollama.ai/) and install it for your operating system.

2. **Download the Llama 3.1 Model**
   - Open a terminal or command prompt and run:
   ```sh
   ollama pull llama3.1
   ```
   - This will download the model required for chatbot responses.

### 5. Set Up Environment Variables
The repository includes a `.env.example` file. Copy it and rename it to `.env`, then modify the values as needed:
```sh
cp .env.example .env  # Mac/Linux
copy .env.example .env  # Windows
```
Edit the `.env` file using any text editor and update the necessary configurations.

### 6. Run the Chatbot
Now, you’re ready to start chatting! Simply run:
```sh
streamlit run AI_Chatbot.py
```
This will open the chatbot interface in your web browser.

## Usage

1. Enter your question in the text input box.
2. The chatbot will generate a response using the **Llama 3.1** model.
3. Keep chatting as needed!

## Troubleshooting

- **Missing Dependencies?**
  - Run `pip install -r requirements.txt` again to ensure all packages are installed.

- **Ollama Not Found?**
  - Make sure you installed it correctly and ran `ollama pull llama3.1`.

- **Environment Variables Not Working?**
  - Check your `.env` file and ensure the values are set properly.

## License

This project is licensed under the **GPL-3.0 License** - see the [LICENSE](LICENSE) file for details.

## Contact

If you have questions, suggestions, or issues, please:

- Open an issue on GitHub  
- Feel free to contact me at [hariprasath.m2017@gmail.com](mailto:hariprasath.m2017@gmail.com)
