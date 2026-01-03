# LangGraph Deep Agents - Setup and Installation

## Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set OpenAI API Key

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Or create a `.env` file:**
```
OPENAI_API_KEY=your-api-key-here
```

### 3. Run Examples

**Quick Start (Interactive):**
```bash
python quick_start.py
```

**View Concepts:**
```bash
python concepts_explained.py
```

**Run Individual Examples:**
```bash
python 01_basic_agent.py
python 02_stateful_agent.py
python 03_reflection_agent.py
# ... etc
```

## File Structure

```
09_deep_agents/
├── README.md                      # Overview and introduction
├── SETUP.md                       # This file - setup instructions
├── requirements.txt               # Python dependencies
├── concepts_explained.py          # Detailed concept explanations
├── quick_start.py                 # Interactive demo launcher
│
├── 01_basic_agent.py             # Basic agent with tools
├── 02_stateful_agent.py          # Persistent state and memory
├── 03_reflection_agent.py        # Self-improvement pattern
├── 04_planning_agent.py          # Plan-and-execute pattern
├── 05_human_in_loop.py           # Human approval workflow
├── 06_multi_agent_system.py     # Multi-agent collaboration
└── 07_advanced_deep_agent.py    # Complete deep agent
```

## Dependencies Explained

- **langgraph**: Core framework for building stateful agents
- **langchain**: LLM orchestration framework
- **langchain-openai**: OpenAI integration for LangChain
- **langchain-core**: Core LangChain abstractions
- **openai**: OpenAI API client
- **python-dotenv**: Environment variable management

## Troubleshooting

### Issue: "Module not found"
**Solution:** Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "OpenAI API key not found"
**Solution:** Set your API key as shown in step 2 above

### Issue: "Rate limit exceeded"
**Solution:** The examples use GPT-4o-mini which is cost-effective. If you hit rate limits:
- Wait a few moments between runs
- Consider upgrading your OpenAI plan
- Reduce the number of iterations in examples

### Issue: "Import errors on Windows"
**Solution:** Make sure you're in the correct directory:
```bash
cd c:\Users\Rakesh\vscode_projects\learning\09_deep_agents
```

## Running in Different Environments

### Jupyter Notebook
You can run these examples in Jupyter by:
1. Converting to notebook format, or
2. Copying code cells into a notebook

### VS Code
1. Open the folder in VS Code
2. Install Python extension
3. Run files directly with F5 or right-click → Run Python File

### Command Line
Simply run: `python <filename>.py`

## Next Steps

1. **Start with concepts:** `python concepts_explained.py`
2. **Try quick start:** `python quick_start.py`
3. **Study examples in order:** 01 → 02 → 03 → ... → 07
4. **Modify and experiment:** Change prompts, add tools, adjust logic
5. **Build your own:** Use these as templates for your projects

## Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

## Tips for Learning

1. **Read the code comments** - Each file has detailed explanations
2. **Run examples multiple times** - See how agents behave differently
3. **Modify parameters** - Change temperatures, models, prompts
4. **Add print statements** - Debug and understand the flow
5. **Combine concepts** - Mix and match patterns for your use case

## Cost Considerations

These examples use **GPT-4o-mini** which is very cost-effective:
- ~$0.15 per 1M input tokens
- ~$0.60 per 1M output tokens

Running all examples should cost less than $0.10 total.

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the code comments in each file
3. Consult the LangGraph documentation
4. Check your OpenAI API key and quota

Happy learning! 🚀
