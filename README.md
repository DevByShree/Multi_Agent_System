#  Multi Agent Research System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-4A90D9?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google%20Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)

**An intelligent multi-agent AI system that autonomously researches any topic, scrapes the web, and generates a structured, critic-reviewed research report — all in one pipeline.**

[🔗 View on GitHub](https://github.com/DevByShree/Multi_Agent_System) · [🐛 Report Bug](https://github.com/DevByShree/Multi_Agent_System/issues) · [✨ Request Feature](https://github.com/DevByShree/Multi_Agent_System/issues)

</div>

---

##  Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Environment Setup](#-environment-setup)
- [Usage](#-usage)
- [Example Workflow](#-example-workflow)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

##  About the Project

The **Multi Agent Research System** is an autonomous AI research pipeline built using **LangChain**, **LangGraph**, and **Google Gemini**. Instead of relying on a single AI call, this system breaks down the research process into **four specialized AI agents** — each responsible for a distinct phase of the workflow.

> Think of it as a small AI team: one searches the web, one reads the pages, one writes the report, and one critiques and improves it.

This project showcases the power of **agentic AI architectures** for real-world use cases like automated research, content generation, and information synthesis.

---

##  Features

-  **Automated Web Search** — Finds the most relevant and recent URLs for any research topic
-  **Deep Content Extraction** — Scrapes and cleans full-page content from multiple sources
-  **Structured Report Generation** — Produces a well-organized research report using an LLM
-  **Critic-Driven Refinement** — Automatically reviews and improves the report for quality
-  **Modular Agent Architecture** — Each agent is independently defined and easy to extend
-  **LangGraph Orchestration** — Agents are connected in a stateful, graph-based pipeline
-  **Google Gemini Powered** — Uses Gemini's advanced language understanding for generation

---

##  How It Works

The system runs a sequential multi-agent pipeline where each agent hands off its output to the next:

```
User Query
    │
    ▼
┌─────────────────────┐
│    Search Agent   │  ──► Finds relevant URLs using web search
└─────────────────────┘
    │
    ▼
┌─────────────────────┐
│    Reader Agent   │  ──► Scrapes and extracts content from each URL
└─────────────────────┘
    │
    ▼
┌─────────────────────┐
│     Writer Agent  │  ──► Generates a structured research report
└─────────────────────┘
    │
    ▼
┌─────────────────────┐
│    Critic Agent   │  ──► Reviews, critiques, and refines the report
└─────────────────────┘
    │
    ▼
 Final Research Report
```

###  Search Agent
Accepts a user query and searches the web to retrieve a list of the most relevant and up-to-date URLs on the topic.

###  Reader Agent
Takes each URL returned by the Search Agent, scrapes the full page content using **BeautifulSoup** and **Requests**, and extracts clean, meaningful text for analysis.

###  Writer Agent
Processes all extracted content and uses **Google Gemini** via **LangChain** to generate a well-structured, coherent research report with sections, key findings, and summaries.

###  Critic Agent
Reviews the generated report for accuracy, completeness, tone, and structure — then outputs an improved final version with corrections and enhancements applied.

---

##  Tech Stack

| Technology | Purpose |
|---|---|
|  **Python 3.10+** | Core programming language |
|  **LangChain** | LLM integration and chain management |
|  **LangGraph** | Multi-agent graph orchestration |
|  **Google Gemini API** | Large language model for generation |
|  **BeautifulSoup4** | HTML parsing and content extraction |
|  **Requests** | HTTP requests for web scraping |
|  **python-dotenv** | Secure environment variable management |

---

##  Project Structure

```
Multi_Agent_System/
│
├── agents/
│   ├── search_agent.py        # Handles web search and URL retrieval
│   ├── reader_agent.py        # Scrapes and extracts content from URLs
│   ├── writer_agent.py        # Generates structured research report
│   └── critic_agent.py        # Reviews and refines the report
│
├── graph/
│   └── pipeline.py            # LangGraph pipeline connecting all agents
│
├── utils/
│   └── helpers.py             # Shared utility functions
│
├── .env                       # API keys and environment variables (not committed)
├── .env.example               # Example env file for reference
├── main.py                    # Entry point — run the full pipeline
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

##  Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/DevByShree/Multi_Agent_System.git
cd Multi_Agent_System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Setup

Create a `.env` file in the root directory and add the following:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> **How to get your Gemini API key:**
> 1. Go to [Google AI Studio](https://aistudio.google.com/)
> 2. Sign in with your Google account
> 3. Click **"Get API Key"** and copy it
> 4. Paste it in your `.env` file

 **Never commit your `.env` file.** It's already listed in `.gitignore` for safety.

---

##  Usage

Once installed and configured, run the system with:

```bash
python main.py
```

You'll be prompted to enter a research topic:

```
Enter your research topic: Artificial Intelligence in Healthcare 2024
```

The pipeline will then:
1. Search the web for relevant sources
2. Scrape and read the content
3. Write a structured report
4. Critique and improve it

The final report will be displayed in the terminal and/or saved to an output file.

---

##  Example Workflow

**Input:**
```
Topic: "Impact of Large Language Models on Software Development"
```

**Step 1 — Search Agent Output:**
```
Found URLs:
  → https://example.com/llms-in-software-dev
  → https://techblog.com/ai-coding-tools-2024
  → https://research.org/llm-impact-study
```

**Step 2 — Reader Agent Output:**
```
Extracted content from 3 sources...
Total content: ~8,400 words of clean text
```

**Step 3 — Writer Agent Output:**
```
## Research Report: Impact of LLMs on Software Development

### Introduction
Large Language Models (LLMs) have rapidly transformed...

### Key Findings
1. Developer productivity has increased by...
2. Common use cases include code generation...

### Conclusion
...
```

**Step 4 — Critic Agent Output:**
```
 Report reviewed. Improvements applied:
  - Strengthened the introduction
  - Added missing citations context
  - Improved conclusion clarity

[Final improved report generated]
```

---

##  Future Improvements

- [ ]  Save final reports as `.pdf` or `.md` files automatically
- [ ]  Add a simple web UI using **Streamlit** or **Gradio**
- [ ]  Support additional LLMs (OpenAI GPT-4, Claude, Mistral)
- [ ]  Add memory so agents can reference previous research sessions
- [ ]  Include citation tracking and source reliability scoring
- [ ]  Dockerize the project for easy deployment
- [ ]  Add unit tests for each agent module

---

##  Author

<div align="center">

**Shree Joshi**

[![GitHub](https://img.shields.io/badge/GitHub-DevByShree-181717?style=for-the-badge&logo=github)](https://github.com/DevByShree)

*3rd Year B.Tech CSE Student | AI/ML Enthusiast | Building cool stuff with LLMs*

</div>

---

<div align="center">




</div>
