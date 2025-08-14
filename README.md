# AI News & Research Tracker with Agentic AI

## Project Overview

An automated AI news and research tracker that uses LangChain, LangGraph, RAG, and agentic AI to fetch policy-safe content, organize it into Technical and General lanes, summarize trends with citations, and let users explore them through explanations, runnable code examples, comparisons, and timelines, all in a clean UI.

Users can easily add links they want to extract data from and get an overview of daily or weekly based on the data. RAG and chatbot are right next to the summary ready for questions. The chatbot uses RAG based on user questions and includes citations. Whatever is missing from source, it can web search it in which it will notify the user and use ChatGPT's web search capability.

## Key Features

### **Universal Link Support**
- Add any link (RSS, articles, blogs, papers, social media)
- Automatic link type detection and content extraction
- Choose immediate processing or add to weekly batch
- Smart content validation and quality assessment

### **Agentic AI System**
- **Content Analysis Agent**: Intelligently classifies and analyzes content
- **Trend Discovery Agent**: Identifies patterns and emerging trends
- **RAG Query Agent**: Answers questions using your knowledge base
- **Live Agent**: Interactive chatbot with memory and context

### **Smart Content Organization**
- **Technical Lane**: AI/tech, programming, research papers
- **General Lane**: Business, politics, general news
- **Automatic Classification**: AI determines content type with confidence scoring
- **Trend Cards**: Beautiful summaries with citations and key insights

### 🔍 **RAG + Web Search Integration**
- **RAG First**: Always tries to answer from your knowledge base
- **Web Search Fallback**: Fills gaps with latest information from the web
- **User Notification**: Clearly shows when web search is used
- **Citation Tracking**: Proper attribution for all sources

### 💻 **Code Generation & Analysis**
- **Auto-Lab**: Generate runnable code examples (≤35 lines)
- **Technical Insights**: Code samples tied to technical topics
- **Safety Validation**: Ensures generated code is safe and appropriate
- **PyTorch/Transformers**: Focus on modern AI/ML frameworks

### 📈 **Trend Analysis & Visualization**
- **Daily Summaries**: Instant overview of today's content
- **Weekly Reports**: Comprehensive Monday summaries
- **Trend Comparisons**: Compare different trends and topics
- **Timeline Evolution**: See how keywords evolve week-to-week

### 🎯 **Interactive Chatbot Interface**
- **Conversation Memory**: Remembers context and user preferences
- **Intent Recognition**: Understands what users are asking for
- **Tool Integration**: Routes to appropriate tools automatically
- **Citation Display**: Shows sources for all information

## Architecture

### **Backend (FastAPI)**
- **LangGraph Workflows**: Orchestrates all AI agents and processes
- **Agentic AI Pipeline**: Multiple specialized AI workers
- **RAG System**: Vector database with semantic search
- **Content Pipeline**: Automated ingestion and processing

### **Frontend (Streamlit)**
- **Clean, Modern UI**: Easy-to-use interface for all features
- **Real-time Updates**: Live agent status and processing progress
- **Interactive Dashboard**: Trend cards, summaries, and controls
- **Chatbot Interface**: Conversational AI with full context

### **Data Layer**
- **SQLite Database**: Local storage for articles, sources, and metadata
- **FAISS/Chroma**: Vector database for AI embeddings and search
- **Memory Systems**: Conversation and agent memory management

## Tech Stack

### **Core AI/ML**
- **OpenAI**: Primary LLM provider with web search capability
- **LangChain**: Framework for building AI agents
- **LangGraph**: Workflow orchestration and state management
- **Hugging Face**: Free alternative models and embeddings

### **Backend & Database**
- **FastAPI**: Modern, fast Python web framework
- **SQLAlchemy**: Database ORM and management
- **SQLite**: Local database (free, lightweight)
- **FAISS/Chroma**: Vector database for embeddings

### **Content Processing**
- **Trafilatura**: AI-enhanced content extraction (primary)
- **Readability-lxml**: AI-powered content detection
- **Boilerpipe3**: ML-based content cleaning
- **Newspaper3k**: Article extraction and processing
- **Feedparser**: RSS feed processing
- **PyPDF2**: PDF content extraction

### **Frontend**
- **Streamlit**: Python-based web interface (free)
- **Interactive Components**: Charts, tables, and chat interface

### **Development & Deployment**
- **Python 3.9+**: Modern Python with async support
- **GitHub Actions**: Automated testing and deployment
- **Docker**: Containerization (optional)

## Getting Started

### **Prerequisites**
- Python 3.9 or higher
- OpenAI API key (required for primary functionality)
- Git for version control

### **Installation**
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `env.example` to `.env` and add your OpenAI API key
5. Run the setup script: `./scripts/setup.sh`

### **Running the Application**
1. **Backend**: `python main.py` (starts FastAPI server)
2. **Frontend**: `streamlit run streamlit_app.py` (starts Streamlit interface)
3. **Access**: Open browser to Streamlit URL

## Project Structure

```
ai_news_trends/
├── main.py                          # FastAPI backend entry point
├── streamlit_app.py                 # Streamlit frontend interface
├── requirements.txt                 # Python dependencies
├── env.example                      # Environment variables template
├── scripts/                         # Setup and utility scripts
├── src/                            # Source code
│   ├── agents/                     # AI agents using LangGraph
│   │   ├── content_analysis_agent.py    # Content classification
│   │   ├── trend_discovery_agent.py     # Trend detection
│   │   ├── rag_query_agent.py           # RAG operations
│   │   ├── live_agent.py                # Interactive chatbot
│   │   └── agent_manager.py             # Agent coordination
│   ├── services/                    # Core services
│   │   ├── content_fetcher.py           # Universal link handling
│   │   ├── link_validator.py            # Link testing & validation
│   │   ├── flexible_processor.py        # Processing options
│   │   ├── content_classifier.py        # AI classification
│   │   ├── rag_service.py               # Vector database & search
│   │   ├── content_pipeline.py          # Main orchestration
│   │   └── scheduler.py                 # Automated processing
│   ├── tools/                       # Specialized AI tools
│   │   ├── retrieval/                   # Retrieval tools
│   │   ├── analysis/                    # Analysis tools
│   │   └── generation/                  # Generation tools
│   ├── memory/                       # AI memory systems
│   ├── planning/                     # Task planning & reasoning
│   ├── dags/                         # LangGraph workflows
│   ├── database/                     # Data models & connections
│   └── api/                          # FastAPI routes
├── data/                            # Data storage
├── docs/                            # Documentation
└── tests/                           # Test suite
```

## Usage

### **Adding Content Sources**
1. Use the "Add Any Link" interface in the Streamlit app
2. Paste any URL (RSS, article, blog, paper, etc.)
3. Choose processing option: immediate, weekly, or custom schedule
4. System automatically detects content type and processes accordingly

### **Daily/Weekly Processing**
- **Daily**: Automatic processing of new content from all sources
- **Weekly**: Comprehensive Monday reports with trend analysis
- **Custom**: Set your own processing schedule for specific sources

### **Interacting with the Chatbot**
1. Ask questions about any content in your knowledge base
2. Get explanations with proper citations
3. Request code examples for technical topics
4. Compare trends and see timelines
5. System automatically uses web search when RAG is insufficient

### **Exploring Trends**
- **Technical Trend Cards**: AI/tech developments and insights
- **General Trend Cards**: Business, politics, and general news
- **Weekly Reports**: Comprehensive summaries with cross-over highlights
- **Interactive Comparisons**: Compare different trends and topics

## Configuration

### **Environment Variables**
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `DATABASE_URL`: Database connection string
- `PROCESSING_FREQUENCY`: Default processing schedule
- `WEB_SEARCH_ENABLED`: Enable/disable web search fallback

### **Processing Options**
- **Immediate**: Process single links right now
- **Weekly**: Add to Monday's batch processing
- **Custom**: Set specific schedules for different sources
- **Monitor**: Check for updates periodically

## Development Status

This project is currently in the **planning and structure phase**. All file structures, TODOs, and architecture are in place. The next phase involves implementing the actual code based on the comprehensive TODO documentation in each file.

## License

[Add your license information here]
