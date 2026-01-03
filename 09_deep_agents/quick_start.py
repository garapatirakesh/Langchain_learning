"""
Quick Start Guide for LangGraph Deep Agents

Run this file to see a quick demo of all the concepts!
"""

import os
import sys

# Check if OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    print("="*60)
    print("⚠️  OPENAI_API_KEY not found!")
    print("="*60)
    print("\nPlease set your OpenAI API key:")
    print("  Windows: $env:OPENAI_API_KEY='your-key-here'")
    print("  Linux/Mac: export OPENAI_API_KEY='your-key-here'")
    print("\nOr create a .env file with:")
    print("  OPENAI_API_KEY=your-key-here")
    print("="*60)
    sys.exit(1)


def main():
    """Run quick demos of all concepts"""
    
    print("\n" + "="*60)
    print("LANGGRAPH DEEP AGENTS - QUICK START")
    print("="*60)
    print("\nThis will demonstrate all 7 deep agent concepts:")
    print("1. Basic Agent with Tools")
    print("2. Stateful Agent with Memory")
    print("3. Reflection Agent")
    print("4. Planning Agent")
    print("5. Human-in-the-Loop Agent")
    print("6. Multi-Agent System")
    print("7. Advanced Deep Agent")
    print("\n" + "="*60)
    
    choice = input("\nWhich demo would you like to run? (1-7, or 'all'): ").strip()
    
    if choice == "1":
        print("\n🤖 Running Basic Agent Demo...")
        from basic_agent import run_agent
        run_agent("What's the weather in Tokyo, Japan?")
    
    elif choice == "2":
        print("\n🧠 Running Stateful Agent Demo...")
        from stateful_agent import run_conversation
        run_conversation()
    
    elif choice == "3":
        print("\n🔄 Running Reflection Agent Demo...")
        from reflection_agent import run_reflection_agent
        run_reflection_agent("Explain quantum computing in simple terms")
    
    elif choice == "4":
        print("\n📋 Running Planning Agent Demo...")
        from planning_agent import run_planning_agent
        run_planning_agent("How to build a REST API with Python")
    
    elif choice == "5":
        print("\n👤 Running Human-in-the-Loop Demo...")
        from human_in_loop import run_with_programmatic_approval
        run_with_programmatic_approval(
            "Update the production database schema",
            auto_approve=False
        )
    
    elif choice == "6":
        print("\n👥 Running Multi-Agent System Demo...")
        from multi_agent_system import run_multi_agent_system
        run_multi_agent_system("Benefits of microservices architecture")
    
    elif choice == "7":
        print("\n🚀 Running Advanced Deep Agent Demo...")
        from advanced_deep_agent import run_deep_agent
        run_deep_agent("Compare SQL and NoSQL databases")
    
    elif choice.lower() == "all":
        print("\n🎯 Running ALL demos sequentially...\n")
        
        print("\n" + "="*60)
        print("DEMO 1: BASIC AGENT")
        print("="*60)
        from basic_agent import run_agent
        run_agent("Calculate 25 * 4")
        
        print("\n" + "="*60)
        print("DEMO 2: STATEFUL AGENT")
        print("="*60)
        from stateful_agent import run_conversation
        run_conversation()
        
        print("\n" + "="*60)
        print("DEMO 3: REFLECTION AGENT")
        print("="*60)
        from reflection_agent import run_reflection_agent
        run_reflection_agent("Write a haiku about coding")
        
        print("\n" + "="*60)
        print("DEMO 4: PLANNING AGENT")
        print("="*60)
        from planning_agent import run_planning_agent
        run_planning_agent("Steps to deploy a web application")
        
        print("\n" + "="*60)
        print("DEMO 5: HUMAN-IN-THE-LOOP")
        print("="*60)
        from human_in_loop import run_with_programmatic_approval
        run_with_programmatic_approval("Delete old log files", auto_approve=True)
        
        print("\n" + "="*60)
        print("DEMO 6: MULTI-AGENT SYSTEM")
        print("="*60)
        from multi_agent_system import run_multi_agent_system
        run_multi_agent_system("Advantages of cloud computing")
        
        print("\n" + "="*60)
        print("DEMO 7: ADVANCED DEEP AGENT")
        print("="*60)
        from advanced_deep_agent import run_deep_agent
        run_deep_agent("Explain the concept of deep agents")
        
        print("\n" + "="*60)
        print("✅ ALL DEMOS COMPLETED!")
        print("="*60)
    
    else:
        print("\n❌ Invalid choice. Please run again and select 1-7 or 'all'")
        return
    
    print("\n" + "="*60)
    print("✅ Demo completed!")
    print("="*60)
    print("\nNext steps:")
    print("- Review the code in each file to understand the concepts")
    print("- Modify the examples to experiment with different scenarios")
    print("- Check README.md for detailed explanations")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
