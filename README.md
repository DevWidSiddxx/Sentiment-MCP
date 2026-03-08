# 🤖 Gradio Sentiment Analysis MCP Server

This is a dual-purpose Sentiment Analysis tool built with **Gradio** and **TextBlob**. It serves both a beautiful web interface for humans and a powerful **Model Context Protocol (MCP)** endpoint for AI models.

## 🚀 Features
- **Human-Friendly**: Clean web UI for manual sentiment testing.
- **AI-Ready**: Exposes a standard MCP tool (`sentiment_analysis`) via SSE.
- **Auto-Documentation**: Generates MCP schemas automatically from Python docstrings.

## 🛠️ Architecture
- **Server**: Gradio (with MCP extension)
- **Engine**: TextBlob (Natural Language Processing)
- **Protocol**: MCP (Model Context Protocol)
- **Deployment**: Vercel/Hugging Face Spaces

## 📦 Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mcp.git
   cd mcp/mcp-sentiment
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   python -m textblob.download_corpora lite
   ```

4. **Run Locally**:
   ```bash
   python app.py
   ```

## 🔌 MCP Usage
The server exposes the following endpoints for AI clients:
- **SSE Connection**: `http://localhost:7860/gradio_api/mcp/sse`
- **Tool Schema**: `http://localhost:7860/gradio_api/mcp/schema`

## 🧪 Testing
| Input | Expected Sentiment |
|-------|-------------------|
| "I love this tool!" | Positive |
| "This is terrible." | Negative |
| "It's 3 PM." | Neutral |

## 🌐 Deployment
This project is configured for easy deployment on **Vercel** or **Hugging Face Spaces**.
- **Vercel**: Uses `vercel.json` and `vercel_app.py`.
- **Hugging Face**: Set up as a Gradio Space.
