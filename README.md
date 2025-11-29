# LLM Analysis - Autonomous Quiz Solver Agent

An intelligent autonomous agent that solves multi-step data science quizzes using LangGraph and Google's Gemini 2.5 Flash model.

## Features

- **Web Scraping**: Playwright-based rendering for JavaScript-heavy pages
- **Code Execution**: Dynamically generates and runs Python code
- **File Handling**: Downloads and processes PDFs, CSVs, images
- **Data Analysis**: Statistical analysis and ML model integration
- **Self-healing**: Automatically installs required packages
- **Docker Ready**: Containerized for easy deployment

## Quick Start

### Prerequisites
- Python 3.12+
- Docker (optional)
- Google Gemini API Key

### Installation

```bash
# Clone and install
git clone https://github.com/divyanshu1602-alt/Tds_project_2.git
cd Tds_project_2
pip install -e .
playwright install chromium



EMAIL=your.email@example.com
SECRET=your_secret_string
GOOGLE_API_KEY=your_gemini_api_key


python -m tdsproject2.main


docker build -t llm-analysis-agent .
docker run -p 7860:7860 \
  -e EMAIL="your@email.com" \
  -e SECRET="your_secret" \
  -e GOOGLE_API_KEY="your_key" \
  llm-analysis-agent
