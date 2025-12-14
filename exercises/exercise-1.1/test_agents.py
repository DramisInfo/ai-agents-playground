"""
Automated tests for Exercise 1.1: Build Your First AI Agents

These tests validate that your agents are properly configured and behave appropriately.
Run with: pytest test_agents.py -v
"""

import pytest
import asyncio
from solution import (
    create_chat_client,
    create_customer_service_agent,
    create_data_analyst_agent,
    create_marketing_agent
)


@pytest.fixture(scope="module")
def chat_client():
    """Fixture to create chat client once for all tests."""
    return create_chat_client()


@pytest.fixture(scope="module")
def customer_service_agent(chat_client):
    """Fixture to create customer service agent."""
    return create_customer_service_agent(chat_client)


@pytest.fixture(scope="module")
def data_analyst_agent(chat_client):
    """Fixture to create data analyst agent."""
    return create_data_analyst_agent(chat_client)


@pytest.fixture(scope="module")
def marketing_agent(chat_client):
    """Fixture to create marketing agent."""
    return create_marketing_agent(chat_client)


class TestAgentCreation:
    """Tests for basic agent creation and configuration."""
    
    def test_customer_service_agent_exists(self, customer_service_agent):
        """Test that customer service agent is created."""
        assert customer_service_agent is not None
        
    def test_customer_service_agent_name(self, customer_service_agent):
        """Test that customer service agent has correct name."""
        assert customer_service_agent.name == "CustomerServiceAgent"
        
    def test_customer_service_agent_has_instructions(self, customer_service_agent):
        """Test that customer service agent has instructions."""
        assert customer_service_agent.instructions is not None
        assert len(customer_service_agent.instructions) > 50  # Non-trivial instructions
        
    def test_data_analyst_agent_exists(self, data_analyst_agent):
        """Test that data analyst agent is created."""
        assert data_analyst_agent is not None
        
    def test_data_analyst_agent_name(self, data_analyst_agent):
        """Test that data analyst agent has correct name."""
        assert data_analyst_agent.name == "DataAnalystAgent"
        
    def test_data_analyst_agent_has_instructions(self, data_analyst_agent):
        """Test that data analyst agent has instructions."""
        assert data_analyst_agent.instructions is not None
        assert len(data_analyst_agent.instructions) > 50
        
    def test_marketing_agent_exists(self, marketing_agent):
        """Test that marketing agent is created."""
        assert marketing_agent is not None
        
    def test_marketing_agent_name(self, marketing_agent):
        """Test that marketing agent has correct name."""
        assert marketing_agent.name == "MarketingAgent"
        
    def test_marketing_agent_has_instructions(self, marketing_agent):
        """Test that marketing agent has instructions."""
        assert marketing_agent.instructions is not None
        assert len(marketing_agent.instructions) > 50


class TestCustomerServiceAgent:
    """Tests for customer service agent behavior."""
    
    @pytest.mark.asyncio
    async def test_handles_customer_complaint(self, customer_service_agent):
        """Test that agent responds professionally to complaints."""
        response = await customer_service_agent.run(
            "I'm very frustrated! My order arrived late and damaged."
        )
        
        response_text = response.text.lower()
        
        # Should show empathy
        empathy_words = ["sorry", "apologize", "understand", "frustrating", "inconvenience"]
        assert any(word in response_text for word in empathy_words), \
            "Response should show empathy to customer complaint"
        
        # Should offer solution or next steps
        solution_words = ["help", "resolve", "solution", "fix", "replace", "refund", "contact"]
        assert any(word in response_text for word in solution_words), \
            "Response should offer solution or next steps"
        
    @pytest.mark.asyncio
    async def test_maintains_professional_tone(self, customer_service_agent):
        """Test that agent maintains professional tone."""
        response = await customer_service_agent.run(
            "What are your business hours?"
        )
        
        # Response should be helpful and professional
        assert len(response.text) > 20, "Response should be substantive"
        assert response.text, "Should provide a response"


class TestDataAnalystAgent:
    """Tests for data analyst agent behavior."""
    
    @pytest.mark.asyncio
    async def test_provides_analytical_response(self, data_analyst_agent):
        """Test that agent provides analytical, structured responses."""
        response = await data_analyst_agent.run(
            "What metrics should I track for a website?"
        )
        
        response_text = response.text.lower()
        
        # Should mention data/metrics/analysis concepts
        analytical_words = ["metric", "data", "measure", "track", "analyze", "kpi", "performance"]
        assert any(word in response_text for word in analytical_words), \
            "Response should include analytical terminology"
        
        # Should provide multiple points (structured response)
        assert len(response.text) > 100, "Response should be detailed and structured"
        
    @pytest.mark.asyncio
    async def test_explains_data_concepts(self, data_analyst_agent):
        """Test that agent can explain data concepts clearly."""
        response = await data_analyst_agent.run(
            "Explain correlation vs causation."
        )
        
        # Should provide educational, clear explanation
        assert "correlation" in response.text.lower()
        assert len(response.text) > 80, "Explanation should be detailed"


class TestMarketingAgent:
    """Tests for marketing agent behavior."""
    
    @pytest.mark.asyncio
    async def test_creates_creative_content(self, marketing_agent):
        """Test that agent creates creative marketing content."""
        response = await marketing_agent.run(
            "Write a catchy tagline for a coffee shop."
        )
        
        # Should provide creative output
        assert len(response.text) > 10, "Should provide creative content"
        # Taglines are typically short
        assert len(response.text) < 500, "Tagline should be concise"
        
    @pytest.mark.asyncio
    async def test_generates_marketing_ideas(self, marketing_agent):
        """Test that agent generates marketing ideas."""
        response = await marketing_agent.run(
            "Suggest ways to promote a new mobile app."
        )
        
        response_text = response.text.lower()
        
        # Should include marketing concepts
        marketing_words = [
            "campaign", "promote", "marketing", "advertise", "social media",
            "content", "brand", "audience", "engagement", "strategy"
        ]
        assert any(word in response_text for word in marketing_words), \
            "Response should include marketing concepts"
        
        # Should provide multiple ideas
        assert len(response.text) > 100, "Should provide multiple ideas or details"


class TestInstructionQuality:
    """Tests to verify instruction quality and appropriateness."""
    
    def test_customer_service_instructions_appropriate(self, customer_service_agent):
        """Test that customer service instructions mention key concepts."""
        instructions = customer_service_agent.instructions.lower()
        
        # Should mention customer service concepts
        relevant_concepts = [
            "customer", "service", "help", "support", "assist",
            "professional", "empathy", "solution", "problem"
        ]
        matches = sum(1 for concept in relevant_concepts if concept in instructions)
        assert matches >= 2, \
            f"Instructions should mention customer service concepts (found {matches}/9)"
    
    def test_data_analyst_instructions_appropriate(self, data_analyst_agent):
        """Test that data analyst instructions mention key concepts."""
        instructions = data_analyst_agent.instructions.lower()
        
        # Should mention analytical concepts
        relevant_concepts = [
            "data", "analys", "insight", "metric", "precise",
            "detail", "structure", "explain", "finding"
        ]
        matches = sum(1 for concept in relevant_concepts if concept in instructions)
        assert matches >= 2, \
            f"Instructions should mention analytical concepts (found {matches}/9)"
    
    def test_marketing_instructions_appropriate(self, marketing_agent):
        """Test that marketing instructions mention key concepts."""
        instructions = marketing_agent.instructions.lower()
        
        # Should mention marketing/creative concepts
        relevant_concepts = [
            "marketing", "creative", "content", "persuasive", "engaging",
            "brand", "campaign", "copy", "idea"
        ]
        matches = sum(1 for concept in relevant_concepts if concept in instructions)
        assert matches >= 2, \
            f"Instructions should mention marketing concepts (found {matches}/9)"


def test_suite_info():
    """Print information about the test suite."""
    print("\n" + "="*60)
    print("Exercise 1.1 Test Suite")
    print("="*60)
    print("This test suite validates:")
    print("  ✓ Agent creation with correct names")
    print("  ✓ Presence of non-trivial instructions")
    print("  ✓ Appropriate behavior for each agent type")
    print("  ✓ Quality and relevance of instructions")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
