export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { question, user_email } = body;

    // Check if AI support bot is enabled
    const aiEnabled = process.env.ENABLE_AI_SUPPORT_BOT === 'true';
    
    // If support-bot service is available, forward the request
    if (aiEnabled) {
      try {
        const response = await fetch('http://support-bot:8001/ticket', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question, user_email }),
        });
        
        if (response.ok) {
          const data = await response.json();
          return Response.json(data);
        }
      } catch (error) {
        console.error('Support bot service unavailable:', error);
        // Fall through to mock response
      }
    }

    // Mock response for when service is unavailable or disabled
    return Response.json({
      ticket_id: `TICKET-${Math.random().toString(36).substr(2, 8).toUpperCase()}`,
      question,
      answer: 'This is a mock response. Start the support-bot service to see real AI-powered responses.',
      mode: aiEnabled ? 'ai' : 'manual',
      metrics: {
        response_time_seconds: aiEnabled ? 1.2 : 5.5,
        accuracy_score: aiEnabled ? 0.92 : 0.65,
      },
    });
  } catch (error) {
    console.error('Error processing support ticket:', error);
    return Response.json(
      { error: 'Failed to process ticket' },
      { status: 500 }
    );
  }
}

export async function GET() {
  try {
    // Check if support bot service is available
    const aiEnabled = process.env.ENABLE_AI_SUPPORT_BOT === 'true';
    
    if (aiEnabled) {
      try {
        const response = await fetch('http://support-bot:8001/metrics');
        if (response.ok) {
          const data = await response.json();
          return Response.json(data);
        }
      } catch (error) {
        console.error('Support bot metrics unavailable:', error);
      }
    }

    // Return mock metrics
    return Response.json({
      summary: {
        total_tickets: 0,
        by_mode: { manual: 0, ai: 0 },
      },
      message: 'Start the support-bot service to see real metrics',
    });
  } catch (error) {
    console.error('Error fetching metrics:', error);
    return Response.json(
      { error: 'Failed to fetch metrics' },
      { status: 500 }
    );
  }
}
