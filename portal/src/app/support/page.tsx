'use client';

import { useState, useEffect } from 'react';
import { Clock, AlertCircle, User, Mail, Tag, ChevronDown, Search, Filter, Sparkles, Zap } from 'lucide-react';
import { supportTeams, knowledgeBase } from '@/lib/mockData';
import { formatDistanceToNow } from 'date-fns';

interface Ticket {
  id: string;
  ticket_number: number;
  subject: string;
  customer_name: string;
  customer_email: string;
  category: string;
  priority: 'low' | 'medium' | 'high' | 'urgent';
  status: 'new' | 'open' | 'pending' | 'resolved';
  description: string;
  created_at: string;
  assigned_to?: string;
}

export default function SupportPage() {
  const [tickets, setTickets] = useState<Ticket[]>([]);
  const [selectedTicket, setSelectedTicket] = useState<Ticket | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [response, setResponse] = useState('');
  const [selectedTeam, setSelectedTeam] = useState('');
  const [showKnowledgeBase, setShowKnowledgeBase] = useState(false);
  const [loading, setLoading] = useState(true);
  const [aiEnabled, setAiEnabled] = useState(false);
  const [aiResponse, setAiResponse] = useState<any>(null);
  const [aiLoading, setAiLoading] = useState(false);

  useEffect(() => {
    fetchTickets();
    checkAiStatus();
  }, []);

  const checkAiStatus = async () => {
    try {
      const res = await fetch('http://localhost:8001/health');
      const data = await res.json();
      setAiEnabled(data.ai_enabled === true);
    } catch (error) {
      console.error('Error checking AI status:', error);
      setAiEnabled(false);
    }
  };

  const fetchTickets = async () => {
    try {
      const res = await fetch('/api/tickets');
      const data = await res.json();
      setTickets(data.tickets || []);
    } catch (error) {
      console.error('Error fetching tickets:', error);
    } finally {
      setLoading(false);
    }
  };

  const getAiResponse = async (ticket: Ticket) => {
    setAiLoading(true);
    setAiResponse(null);
    try {
      const res = await fetch('http://localhost:8001/ticket', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question: ticket.description,
          user_email: ticket.customer_email
        })
      });
      const data = await res.json();
      setAiResponse(data);
    } catch (error) {
      console.error('Error getting AI response:', error);
    } finally {
      setAiLoading(false);
    }
  };

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'urgent': return 'bg-red-100 text-red-800';
      case 'high': return 'bg-orange-100 text-orange-800';
      case 'medium': return 'bg-yellow-100 text-yellow-800';
      case 'low': return 'bg-green-100 text-green-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const handleResponse = () => {
    if (!selectedTicket || !response) return;
    
    // Simulate slow manual process
    alert('Sending response... (In reality, this would take 2-5 minutes to compose and send)');
    setResponse('');
  };

  const handleRouting = async () => {
    if (!selectedTicket || !selectedTeam) return;
    
    try {
      await fetch(`/api/tickets/${selectedTicket.id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ assigned_team: selectedTeam }),
      });
      
      alert(`Routing to ${supportTeams.find(t => t.id === selectedTeam)?.name}...\n\nNote: Manual routing often results in 40% misrouted tickets that need to be re-assigned.`);
      setSelectedTeam('');
      fetchTickets();
    } catch (error) {
      console.error('Error routing ticket:', error);
    }
  };

  const searchKnowledgeBase = () => {
    if (!searchQuery) return;
    setShowKnowledgeBase(true);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center justify-between mb-2">
          <h1 className="text-3xl font-bold text-gray-900">Support Dashboard</h1>
          {aiEnabled && (
            <div className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg">
              <Sparkles className="h-5 w-5" />
              <span className="font-semibold">AI Enabled</span>
            </div>
          )}
        </div>
        <p className="text-gray-600">
          {aiEnabled 
            ? 'AI-powered support - Average response time: 1.2 seconds' 
            : 'Manual ticket management - Average response time: 45 minutes'}
        </p>
        
        <div className="mt-4 grid grid-cols-4 gap-4">
          <div className={aiEnabled ? 'bg-green-50 p-4 rounded-lg' : 'bg-red-50 p-4 rounded-lg'}>
            <p className={`text-sm font-medium ${aiEnabled ? 'text-green-600' : 'text-red-600'}`}>Open Tickets</p>
            <p className={`text-2xl font-bold ${aiEnabled ? 'text-green-700' : 'text-red-700'}`}>
              {tickets.filter(t => t.status === 'new').length}
            </p>
          </div>
          <div className={aiEnabled ? 'bg-green-50 p-4 rounded-lg' : 'bg-yellow-50 p-4 rounded-lg'}>
            <p className={`text-sm font-medium ${aiEnabled ? 'text-green-600' : 'text-yellow-600'}`}>Avg. Response Time</p>
            <p className={`text-2xl font-bold ${aiEnabled ? 'text-green-700' : 'text-yellow-700'}`}>
              {aiEnabled ? '1.2s' : '45 min'}
            </p>
          </div>
          <div className={aiEnabled ? 'bg-green-50 p-4 rounded-lg' : 'bg-orange-50 p-4 rounded-lg'}>
            <p className={`text-sm font-medium ${aiEnabled ? 'text-green-600' : 'text-orange-600'}`}>
              {aiEnabled ? 'Accuracy' : 'Misrouted Today'}
            </p>
            <p className={`text-2xl font-bold ${aiEnabled ? 'text-green-700' : 'text-orange-700'}`}>
              {aiEnabled ? '92%' : '8 (40%)'}
            </p>
          </div>
          <div className={aiEnabled ? 'bg-blue-50 p-4 rounded-lg' : 'bg-purple-50 p-4 rounded-lg'}>
            <p className={`text-sm font-medium ${aiEnabled ? 'text-blue-600' : 'text-purple-600'}`}>
              {aiEnabled ? 'Auto-Resolved' : 'Manual Searches'}
            </p>
            <p className={`text-2xl font-bold ${aiEnabled ? 'text-blue-700' : 'text-purple-700'}`}>
              {aiEnabled ? '184' : '127'}
            </p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-6">
        {/* Ticket List */}
        <div className="col-span-1 bg-white rounded-lg shadow-md p-6">
          <h2 className="text-xl font-bold mb-4">Ticket Queue</h2>
          {loading ? (
            <div className="text-center py-12">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-techflow-primary mx-auto"></div>
              <p className="text-gray-500 mt-4">Loading tickets...</p>
            </div>
          ) : (
            <div className="space-y-2 max-h-[600px] overflow-y-auto">
              {tickets.map((ticket) => (
                <div
                  key={ticket.id}
                  onClick={() => setSelectedTicket(ticket)}
                  className={`p-4 border rounded-lg cursor-pointer hover:bg-gray-50 transition-colors ${
                    selectedTicket?.id === ticket.id ? 'border-techflow-primary bg-blue-50' : 'border-gray-200'
                  }`}
                >
                  <div className="flex items-start justify-between mb-2">
                    <span className="font-medium text-sm text-gray-900">#{ticket.ticket_number}</span>
                    <span className={`text-xs px-2 py-1 rounded-full ${getPriorityColor(ticket.priority)}`}>
                      {ticket.priority}
                    </span>
                  </div>
                  <p className="text-sm font-medium text-gray-900 mb-1">{ticket.subject}</p>
                  <p className="text-xs text-gray-500">{ticket.customer_name}</p>
                  <div className="flex items-center text-xs text-gray-400 mt-2">
                    <Clock className="h-3 w-3 mr-1" />
                    {formatDistanceToNow(new Date(ticket.created_at), { addSuffix: true })}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Ticket Detail & Response */}
        <div className="col-span-2 space-y-6">
          {selectedTicket ? (
            <>
              {/* Ticket Details */}
              <div className="bg-white rounded-lg shadow-md p-6">
                <div className="flex items-start justify-between mb-4">
                  <div>
                    <h2 className="text-2xl font-bold text-gray-900 mb-2">#{selectedTicket.ticket_number}: {selectedTicket.subject}</h2>
                    <div className="flex items-center gap-4 text-sm text-gray-600">
                      <div className="flex items-center">
                        <User className="h-4 w-4 mr-1" />
                        {selectedTicket.customer_name}
                      </div>
                      <div className="flex items-center">
                        <Mail className="h-4 w-4 mr-1" />
                        {selectedTicket.customer_email}
                      </div>
                      <div className="flex items-center">
                        <Tag className="h-4 w-4 mr-1" />
                        {selectedTicket.category}
                      </div>
                    </div>
                  </div>
                  <span className={`px-3 py-1 rounded-full text-sm font-medium ${getPriorityColor(selectedTicket.priority)}`}>
                    {selectedTicket.priority}
                  </span>
                </div>
                
                <div className="bg-gray-50 p-4 rounded-lg">
                  <p className="text-gray-800">{selectedTicket.description}</p>
                </div>
              </div>

              {/* AI Response Section */}
              {aiEnabled && (
                <div className="bg-gradient-to-br from-blue-50 to-purple-50 rounded-lg shadow-md p-6 border-2 border-blue-200">
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="text-lg font-bold flex items-center gap-2">
                      <Sparkles className="h-5 w-5 text-blue-600" />
                      AI-Powered Instant Response
                    </h3>
                    <button
                      onClick={() => getAiResponse(selectedTicket)}
                      disabled={aiLoading}
                      className="px-4 py-2 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg hover:from-blue-600 hover:to-purple-700 disabled:opacity-50 flex items-center gap-2"
                    >
                      {aiLoading ? (
                        <>
                          <div className="animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"></div>
                          Processing...
                        </>
                      ) : (
                        <>
                          <Zap className="h-4 w-4" />
                          Get AI Answer
                        </>
                      )}
                    </button>
                  </div>

                  {aiResponse && (
                    <div className="space-y-4">
                      <div className="bg-white p-4 rounded-lg border border-blue-200">
                        <div className="flex items-center justify-between mb-2">
                          <span className="text-sm font-medium text-blue-600">AI Generated Response:</span>
                          <div className="flex items-center gap-4 text-xs text-gray-500">
                            <span>⚡ {aiResponse.metrics.response_time_seconds}s</span>
                            <span>✓ {Math.round(aiResponse.metrics.accuracy_score * 100)}% accuracy</span>
                          </div>
                        </div>
                        <div className="text-gray-800 whitespace-pre-wrap">{aiResponse.answer}</div>
                      </div>
                      
                      <div className="flex gap-2">
                        <button
                          onClick={() => {
                            setResponse(aiResponse.answer);
                            alert('AI response copied to compose field! You can review and send it.');
                          }}
                          className="flex-1 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"
                        >
                          Use This Response
                        </button>
                        <button
                          onClick={() => alert('Response sent instantly!')}
                          className="flex-1 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                        >
                          Send Immediately
                        </button>
                      </div>
                    </div>
                  )}

                  {!aiResponse && !aiLoading && (
                    <p className="text-sm text-gray-600">
                      Click "Get AI Answer" to instantly generate a response using context-aware AI. 
                      Response time: <span className="font-bold text-blue-600">~1 second</span> with 
                      <span className="font-bold text-blue-600"> 92% accuracy</span>.
                    </p>
                  )}
                </div>
              )}

              {/* Manual Knowledge Base Search */}
              {!aiEnabled && (
                <div className="bg-white rounded-lg shadow-md p-6">
                  <h3 className="text-lg font-bold mb-4">📚 Manual Knowledge Base Search</h3>
                  <p className="text-sm text-gray-600 mb-4">
                    You need to manually search through 500+ KB articles to find relevant information...
                </p>
                
                <div className="flex gap-2 mb-4">
                  <input
                    type="text"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    placeholder="Search knowledge base manually..."
                    className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-techflow-primary text-gray-900"
                  />
                  <button
                    onClick={searchKnowledgeBase}
                    className="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 flex items-center gap-2"
                  >
                    <Search className="h-4 w-4" />
                    Search
                  </button>
                </div>

                {showKnowledgeBase && (
                  <div className="space-y-2">
                    {knowledgeBase
                      .filter(kb => 
                        kb.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                        kb.content.toLowerCase().includes(searchQuery.toLowerCase())
                      )
                      .map(kb => (
                        <div key={kb.id} className="p-3 bg-gray-50 rounded border border-gray-200">
                          <p className="font-medium text-sm">{kb.title}</p>
                          <p className="text-xs text-gray-600 mt-1">{kb.content}</p>
                        </div>
                      ))}
                  </div>
                )}
              </div>
              )}

              {/* Manual Response */}
              {!aiEnabled && (
                <div className="bg-white rounded-lg shadow-md p-6">
                  <h3 className="text-lg font-bold mb-4">✍️ Compose Response Manually</h3>
                  <p className="text-sm text-gray-600 mb-4">
                    Average time to compose: 5-10 minutes per ticket
                  </p>
                <textarea
                  value={response}
                  onChange={(e) => setResponse(e.target.value)}
                  placeholder="Type your response here... (no suggestions, no templates, all manual)"
                  rows={6}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-techflow-primary mb-4"
                />
                <button
                  onClick={handleResponse}
                  disabled={!response}
                  className="px-6 py-2 bg-techflow-primary text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
                >
                  Send Response (Manual)
                </button>
              </div>
              )}

              {/* Manual Routing */}
              {!aiEnabled && (
                <div className="bg-white rounded-lg shadow-md p-6">
                  <h3 className="text-lg font-bold mb-4">🎯 Manual Routing</h3>
                  <p className="text-sm text-gray-600 mb-4">
                    40% of tickets are misrouted and need reassignment...
                  </p>
                  
                  <div className="flex gap-2">
                    <select
                      value={selectedTeam}
                      onChange={(e) => setSelectedTeam(e.target.value)}
                      className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-techflow-primary"
                    >
                      <option value="">Select team to route to...</option>
                      {supportTeams.map(team => (
                        <option key={team.id} value={team.id}>{team.name}</option>
                      ))}
                    </select>
                    <button
                      onClick={handleRouting}
                      disabled={!selectedTeam}
                      className="px-6 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
                    >
                      Route Ticket
                    </button>
                  </div>
                </div>
              )}
            </>
          ) : (
            <div className="bg-white rounded-lg shadow-md p-12 text-center">
              <AlertCircle className="h-16 w-16 text-gray-400 mx-auto mb-4" />
              <p className="text-gray-600">Select a ticket from the queue to view details and respond</p>
            </div>
          )}
        </div>
      </div>

      {/* Status Notice */}
      {aiEnabled ? (
        <div className="bg-gradient-to-r from-green-50 to-blue-50 border-l-4 border-green-500 p-6 rounded-lg">
          <h3 className="text-lg font-semibold text-green-900 mb-2 flex items-center gap-2">
            <Sparkles className="h-5 w-5" />
            AI Improvements Active
          </h3>
          <ul className="space-y-1 text-green-800 text-sm">
            <li>• ✅ Instant AI-generated responses (1.2s vs 5-10 minutes)</li>
            <li>• ✅ Automatic knowledge base search with context understanding</li>
            <li>• ✅ Intelligent routing with 92% accuracy (vs 60% manual)</li>
            <li>• ✅ AI suggests responses and templates automatically</li>
            <li>• ✅ Average response time: 1.2 seconds (78% faster than manual)</li>
            <li>• ✅ Agents handle 400+ tickets daily without burnout</li>
          </ul>
          <div className="mt-4 p-4 bg-white rounded-lg border border-green-200">
            <p className="text-sm font-semibold text-gray-900">Business Impact:</p>
            <div className="mt-2 grid grid-cols-3 gap-4 text-xs">
              <div>
                <p className="text-gray-600">Time Saved</p>
                <p className="text-lg font-bold text-green-600">15 hrs/week</p>
              </div>
              <div>
                <p className="text-gray-600">Cost Reduction</p>
                <p className="text-lg font-bold text-green-600">50%</p>
              </div>
              <div>
                <p className="text-gray-600">Customer Satisfaction</p>
                <p className="text-lg font-bold text-green-600">↑ 35%</p>
              </div>
            </div>
          </div>
        </div>
      ) : (
        <div className="bg-red-50 border-l-4 border-red-500 p-6 rounded-lg">
          <h3 className="text-lg font-semibold text-red-900 mb-2">Current Pain Points</h3>
          <ul className="space-y-1 text-red-800 text-sm">
            <li>• Every response must be manually composed (5-10 min each)</li>
            <li>• Must manually search 500-page knowledge base for each ticket</li>
            <li>• 40% of tickets misrouted to wrong team (wastes 10+ hours/week)</li>
            <li>• No automated suggestions or templates</li>
            <li>• Average response time: 45 minutes (customers expect &lt;5 minutes)</li>
            <li>• Support agents handling 200+ tickets daily, causing burnout</li>
          </ul>
        </div>
      )}
    </div>
  );
}
