# Multi-Agent LLM-Based Financial Trading Framework

## Overview

This repository contains a comprehensive multi-agent system for automated financial trading, leveraging Large Language Models (LLMs) to coordinate specialized trading agents. The system implements a sophisticated architecture where multiple AI agents collaborate to analyze market data, make trading decisions, and manage portfolio risk.

## Architecture

### Core Components

1. **Analyst Team**: Market analysis and research agents
2. **Research Team**: Data collection and processing agents  
3. **Trader**: Execution and order management agents
4. **Risk Management**: Portfolio risk assessment and mitigation
5. **Portfolio Management**: Asset allocation and optimization

### Key Features

- **Multi-Agent Coordination**: Blackboard architecture for agent communication
- **LLM Integration**: OpenAI and LangChain-based decision making
- **Real-time Data Processing**: Yahoo Finance, Google News, and Reddit integration
- **Advanced Analytics**: Technical indicators, sentiment analysis, and portfolio optimization
- **Risk Management**: Black-Litterman model and Modern Portfolio Theory implementation
- **CLI Interface**: Rich terminal-based user interface for system interaction

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install dependencies
pip install -e .

# Set up environment variables
export OPENAI_API_KEY="your-api-key"
```

## Usage

### CLI Interface

```bash
# Start the main CLI
tradingagents

# Access specific modules
tradingagents analyst
tradingagents researcher
tradingagents trader
tradingagents risk
tradingagents portfolio
```

### API Endpoints

The system provides REST API endpoints for integration:

- `GET /blackboard` - Retrieve agent messages
- `POST /blackboard` - Send messages to agents
- `GET /blackboard/stats` - System statistics
- `DELETE /blackboard` - Clear message history

## Technical Details

### Dependencies

- **Core ML**: LangChain, OpenAI, NumPy, Pandas
- **Financial Data**: yfinance, stockstats, PRAW (Reddit)
- **UI**: Rich, Typer, Questionary
- **Optimization**: Custom MVO and Black-Litterman implementations

### Data Sources

- **Market Data**: Yahoo Finance API
- **News**: Google News RSS feeds
- **Social Sentiment**: Reddit discussions
- **Technical Indicators**: StockStats library

## Research Contributions

This work demonstrates:

1. **Multi-Agent System Design**: Novel blackboard architecture for financial trading
2. **LLM Integration**: Effective use of language models in quantitative finance
3. **Real-time Decision Making**: Coordinated agent responses to market events
4. **Risk Management**: Advanced portfolio optimization techniques
5. **Scalable Architecture**: Modular design for extensibility

## License

Apache License 2.0

## Citation

If you use this work in your research, please cite:

```bibtex
@software{multi_agent_trading_framework,
  title={Multi-Agent LLM-Based Financial Trading Framework},
  author={Research Team},
  year={2024},
  url={https://github.com/example/research}
}
```

## Contact

For research inquiries: research@example.com
