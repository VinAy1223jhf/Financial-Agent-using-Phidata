from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

MODEL = Ollama(
    model="llama3.1:latest",
    temperature=0.2
)

agent = Agent(
    name="Financial Research Agent",
    role="Analyze stocks using tools and summarize results clearly",
    model=MODEL,
    tools=[
        DuckDuckGo(),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        )
    ],
    instructions=[
        "Always use tools when factual data is needed",
        "Present analyst recommendations in a table",
        "Summarize news in bullet points",
        "Include sources when available"
    ],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response(
    "Summarize analyst recommendations and share the latest news for NVDA",
    stream=True
)
