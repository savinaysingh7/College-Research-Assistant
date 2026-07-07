# College Research Assistant

An AI-powered chatbot built with **Streamlit** and **Anthropic Claude** that helps students with college-related queries.

## Features

- Natural language Q&A for college research
- Clean web UI with Streamlit
- Powered by Claude Haiku 4.5

## Tech Stack

| Component | Technology |
|:---|:---|
| Frontend | Streamlit |
| LLM | Anthropic Claude Haiku 4.5 |
| Framework | LangChain |

## Setup

1. Clone the repo:
```bash
git clone https://github.com/savinaysingh7/College-Research-Assistant.git
cd College-Research-Assistant
```

2. Install dependencies:
```bash
pip install streamlit langchain-anthropic python-dotenv
```

3. Create `.env` file and add your API key:
```env
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

4. Run the app:
```bash
streamlit run main.py
```

## Screenshot

![App Screenshot](https://img.shields.io/badge/Run-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## License

MIT
