# AI Agentic Platform - Orchestrator Service
"""
Multi-agent execution logic, local vs cloud model loader, and prompt fetching.
"""

from typing import Dict, List, Any
import asyncio
from datetime import datetime
import os

# Import LLM libraries
try:
    import ollama
    HAS_OLLAMA = True
except ImportError:
    HAS_OLLAMA = False

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

# Import MCP libraries
try:
    from ..services.mcp_service import mcp_service
    HAS_MCP = True
except ImportError:
    HAS_MCP = False

from ..utils.logging import logger
from ..models import get_db, Agent
from sqlalchemy.orm import Session

class OrchestratorService:
    """Service for orchestrating multi-agent workflows."""
    
    def __init__(self, db_session: Session = None):
        """Initialize the orchestrator with LLM configurations and optional database session."""
        self.db_session = db_session
        self.ollama_client = None
        self.openai_client = None
        self.anthropic_client = None
        
        # Initialize clients based on available libraries and environment variables
        if HAS_OLLAMA:
            ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
            self.ollama_client = ollama.Client(host=ollama_host)
            
        if HAS_OPENAI:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if openai_api_key:
                self.openai_client = OpenAI(api_key=openai_api_key)
                
        if HAS_ANTHROPIC:
            anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
            if anthropic_api_key:
                self.anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)
    
    async def execute_agent_workflow(self, agents: List[Dict], prompt: str) -> Dict[str, Any]:
        """Execute a workflow with multiple agents."""
        try:
            results = {}
            
            # Execute each agent in sequence or parallel based on configuration
            for agent in agents:
                agent_id = agent.get("id")
                agent_config = agent.get("config", {})
                
                # Get the appropriate LLM based on configuration
                llm_type = agent_config.get("llm_type", "ollama")
                model_name = agent_config.get("model_name", "llama3")
                
                # Execute the agent with the prompt
                result = await self._execute_agent(
                    agent_id=agent_id,
                    prompt=prompt,
                    llm_type=llm_type,
                    model_name=model_name
                )
                
                results[agent_id] = result
                
            return {
                "status": "success",
                "results": results,
                "timestamp": asyncio.get_event_loop().time()
            }
            
        except Exception as e:
            logger.error(f"Error executing agent workflow: {str(e)}")
            raise
    
    async def _execute_agent(self, agent_id: str, prompt: str, llm_type: str, model_name: str) -> Dict[str, Any]:
        """Execute a single agent with the given prompt."""
        # Update agent status and last_executed if database session is available
        if self.db_session:
            try:
                agent = self.db_session.query(Agent).filter(Agent.id == agent_id).first()
                if agent:
                    agent.status = "executing"
                    agent.last_executed = datetime.utcnow()
                    self.db_session.commit()
            except Exception as e:
                logger.warning(f"Could not update agent status for {agent_id}: {str(e)}")
        
        try:
            response = None
            
            if llm_type == "ollama" and self.ollama_client:
                # Use Ollama for local LLMs
                response = self.ollama_client.generate(
                    model=model_name,
                    prompt=prompt,
                    stream=False
                )
                
            elif llm_type == "openai" and self.openai_client:
                # Use OpenAI cloud LLMs
                response = self.openai_client.chat.completions.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    stream=False
                )
                
            elif llm_type == "anthropic" and self.anthropic_client:
                # Use Anthropic cloud LLMs
                response = self.anthropic_client.messages.create(
                    model=model_name,
                    max_tokens=1024,
                    messages=[{"role": "user", "content": prompt}]
                )
                
            elif llm_type == "mcp" and HAS_MCP:
                # Use MCP for tool execution
                # This would integrate with the MCP service to execute tools
                response = await self._execute_mcp_tool(prompt)
                
            else:
                # Fallback to a default approach or raise an error
                raise ValueError(f"Unsupported LLM type: {llm_type}")
            
            result = {
                "agent_id": agent_id,
                "prompt": prompt,
                "response": response,
                "timestamp": asyncio.get_event_loop().time()
            }
            
            # Update agent status to active if database session is available
            if self.db_session:
                try:
                    agent = self.db_session.query(Agent).filter(Agent.id == agent_id).first()
                    if agent:
                        agent.status = "active"
                        self.db_session.commit()
                except Exception as e:
                    logger.warning(f"Could not update agent status for {agent_id}: {str(e)}")
            
            return result
            
        except Exception as e:
            # Update agent status to error if database session is available
            if self.db_session:
                try:
                    agent = self.db_session.query(Agent).filter(Agent.id == agent_id).first()
                    if agent:
                        agent.status = "error"
                        self.db_session.commit()
                except Exception as db_e:
                    logger.warning(f"Could not update agent status for {agent_id}: {str(db_e)}")
            
            logger.error(f"Error executing agent {agent_id}: {str(e)}")
            raise
    
    async def _execute_mcp_tool(self, prompt: str) -> Dict[str, Any]:
        """Execute MCP tools based on the prompt."""
        try:
            # This is a placeholder implementation
            # In a real implementation, this would parse the prompt to determine which tools to call
            # and then execute them via the MCP service
            
            # For now, we'll just return a mock response
            result = {
                "status": "success",
                "message": f"MCP tool execution completed for prompt: {prompt[:50]}...",
                "tools_executed": [],
                "timestamp": asyncio.get_event_loop().time()
            }
            
            logger.info(f"Executed MCP tools for prompt: {prompt[:50]}...")
            return result
            
        except Exception as e:
            logger.error(f"Error executing MCP tools: {str(e)}")
            raise
    
    def load_prompt_by_version(self, prompt_id: str, version: str = None) -> Dict[str, Any]:
        """Load a specific version of a prompt."""
        # In a real implementation, this would fetch from the database
        # For now, we'll return a mock response
        return {
            "id": prompt_id,
            "version": version or "1.0",
            "body": f"Prompt content for {prompt_id} (version {version or '1.0'})",
            "tags": [],
            "created_at": "2025-08-27T00:00:00Z"
        }
    
    def fetch_prompts_by_tags(self, tags: List[str]) -> List[Dict[str, Any]]:
        """Fetch prompts by tags."""
        # In a real implementation, this would query the database
        # For now, we'll return mock data
        return [
            {
                "id": f"prompt_{i}",
                "body": f"Prompt content with tag {tag}",
                "version": "1.0",
                "tags": tags,
                "created_at": "2025-08-27T00:00:00Z"
            }
            for i, tag in enumerate(tags)
        ]
    
    async def monitor_performance(self) -> Dict[str, Any]:
        """Monitor agent performance metrics."""
        # In a real implementation, this would collect actual metrics
        return {
            "total_executions": 0,
            "average_response_time": 0.0,
            "success_rate": 1.0,
            "active_agents": 0,
            "timestamp": asyncio.get_event_loop().time()
        }

# Global orchestrator instance
orchestrator = OrchestratorService()