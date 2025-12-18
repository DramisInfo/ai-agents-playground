'use client';

import { useState, useEffect } from 'react';
import { Search, Sparkles, Clock, BookOpen, FileText, Zap, TrendingUp } from 'lucide-react';

interface FAQResponse {
  question: string;
  answer: string;
  mode: string;
  sources?: Array<{
    title: string;
    filename: string;
    similarity: number;
  }>;
  matched_faq?: string;
  match_count?: number;
  confidence?: string;
  search_time?: number;
  generation_time?: number;
  response_time?: number;
  total_time?: number;
}

export default function FAQPage() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState<FAQResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [aiEnabled, setAiEnabled] = useState(false);
  const [stats, setStats] = useState<any>(null);

  useEffect(() => {
    checkAiStatus();
    fetchStats();
  }, []);

  const checkAiStatus = async () => {
    try {
      const res = await fetch('http://localhost:8002/health');
      const data = await res.json();
      setAiEnabled(data.ai_enabled === true);
    } catch (error) {
      console.error('Error checking AI status:', error);
      setAiEnabled(false);
    }
  };

  const fetchStats = async () => {
    try {
      const res = await fetch('http://localhost:8002/stats');
      const data = await res.json();
      setStats(data);
    } catch (error) {
      console.error('Error fetching stats:', error);
    }
  };

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setResponse(null);

    try {
      const res = await fetch('http://localhost:8002/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: question.trim() })
      });

      if (!res.ok) {
        throw new Error('Failed to get answer');
      }

      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error('Error asking question:', error);
      alert('Error getting answer. Make sure the FAQ Expert service is running.');
    } finally {
      setLoading(false);
    }
  };

  const sampleQuestions = [
    "How much does FlowCRM cost?",
    "How do I import contacts from a CSV file?",
    "What are the steps to integrate my email?",
    "How can I reset my password?",
    "Tell me about user roles and permissions",
    "How do I handle duplicate contacts?",
    "What is FlowAnalytics?",
    "How do I create custom fields?"
  ];


  return (
    <div className="space-y-6">
      {/* Header with AI Status */}
      <div className="bg-white shadow rounded-lg p-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
              <BookOpen className="h-7 w-7 text-blue-600" />
              FAQ Expert
              {aiEnabled && <Sparkles className="h-5 w-5 text-yellow-500" />}
            </h1>
            <p className="text-sm text-gray-600 mt-1">
              Lesson 2: RAG-Powered Knowledge Search
            </p>
          </div>
          <div className="text-right">
            <div className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${
              aiEnabled 
                ? 'bg-green-100 text-green-800' 
                : 'bg-gray-100 text-gray-800'
            }`}>
              {aiEnabled ? (
                <>
                  <Sparkles className="h-4 w-4 mr-1" />
                  AI-RAG Enabled
                </>
              ) : (
                <>
                  <Zap className="h-4 w-4 mr-1" />
                  Manual Mode
                </>
              )}
            </div>
            <p className="text-xs text-gray-500 mt-1">
              Feature Flag: ENABLE_AI_FAQ_RAG
            </p>
          </div>
        </div>
      </div>

      {/* Stats Cards */}
      {stats && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-white shadow rounded-lg p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Accuracy</p>
                <p className="text-2xl font-bold text-gray-900">
                  {stats.typical_metrics?.accuracy || 'N/A'}
                </p>
              </div>
              <TrendingUp className={`h-8 w-8 ${aiEnabled ? 'text-green-500' : 'text-orange-500'}`} />
            </div>
          </div>

          <div className="bg-white shadow rounded-lg p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Coverage</p>
                <p className="text-2xl font-bold text-gray-900">
                  {stats.typical_metrics?.coverage || 'N/A'}
                </p>
              </div>
              <BookOpen className={`h-8 w-8 ${aiEnabled ? 'text-blue-500' : 'text-gray-500'}`} />
            </div>
          </div>

          <div className="bg-white shadow rounded-lg p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Response Time</p>
                <p className="text-2xl font-bold text-gray-900">
                  {stats.typical_metrics?.response_time || 'N/A'}
                </p>
              </div>
              <Clock className={`h-8 w-8 ${aiEnabled ? 'text-purple-500' : 'text-green-500'}`} />
            </div>
          </div>
        </div>
      )}

      {/* Question Input */}
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-lg font-semibold mb-4">Ask a Question</h2>
        
        <div className="space-y-4">
          <div className="flex gap-2">
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && askQuestion()}
              placeholder="Type your question here..."
              className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
            <button
              onClick={askQuestion}
              disabled={loading || !question.trim()}
              className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed flex items-center gap-2"
            >
              {loading ? (
                <>
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
                  Processing...
                </>
              ) : (
                <>
                  <Search className="h-4 w-4" />
                  Ask
                </>
              )}
            </button>
          </div>

          {/* Sample Questions */}
          <div>
            <p className="text-sm text-gray-600 mb-2">Try these sample questions:</p>
            <div className="flex flex-wrap gap-2">
              {sampleQuestions.map((q, idx) => (
                <button
                  key={idx}
                  onClick={() => setQuestion(q)}
                  className="px-3 py-1 text-sm bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-full transition-colors"
                >
                  {q}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Response */}
      {response && (
        <div className="bg-white shadow rounded-lg p-6">
          <div className="flex items-start justify-between mb-4">
            <h2 className="text-lg font-semibold">Answer</h2>
            <div className="flex items-center gap-4 text-sm text-gray-600">
              {response.total_time && (
                <span className="flex items-center gap-1">
                  <Clock className="h-4 w-4" />
                  {response.total_time}s
                </span>
              )}
              {response.response_time && (
                <span className="flex items-center gap-1">
                  <Clock className="h-4 w-4" />
                  {response.response_time}s
                </span>
              )}
            </div>
          </div>

          {/* Question */}
          <div className="mb-4 p-3 bg-gray-50 rounded-lg">
            <p className="text-sm font-medium text-gray-700">Question:</p>
            <p className="text-gray-900">{response.question}</p>
          </div>

          {/* Answer */}
          <div className="mb-4 p-4 bg-blue-50 rounded-lg">
            <p className="text-sm font-medium text-gray-700 mb-2">Answer:</p>
            <p className="text-gray-900 whitespace-pre-wrap">{response.answer}</p>
          </div>

          {/* Metadata */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
            <div className="p-3 bg-gray-50 rounded">
              <p className="text-xs text-gray-600">Mode</p>
              <p className="font-semibold text-gray-900">{response.mode}</p>
            </div>

            {response.confidence && (
              <div className="p-3 bg-gray-50 rounded">
                <p className="text-xs text-gray-600">Confidence</p>
                <p className="font-semibold text-gray-900">{response.confidence}</p>
              </div>
            )}

            {response.match_count !== undefined && (
              <div className="p-3 bg-gray-50 rounded">
                <p className="text-xs text-gray-600">Keyword Matches</p>
                <p className="font-semibold text-gray-900">{response.match_count}</p>
              </div>
            )}

            {response.search_time && (
              <div className="p-3 bg-gray-50 rounded">
                <p className="text-xs text-gray-600">Search Time</p>
                <p className="font-semibold text-gray-900">{response.search_time}s</p>
              </div>
            )}

            {response.generation_time && (
              <div className="p-3 bg-gray-50 rounded">
                <p className="text-xs text-gray-600">Generation Time</p>
                <p className="font-semibold text-gray-900">{response.generation_time}s</p>
              </div>
            )}
          </div>

          {/* Sources (for AI mode) */}
          {response.sources && response.sources.length > 0 && (
            <div className="border-t pt-4">
              <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2">
                <FileText className="h-4 w-4" />
                Sources
              </h3>
              <div className="space-y-2">
                {response.sources.map((source, idx) => (
                  <div key={idx} className="flex items-center justify-between p-3 bg-gray-50 rounded">
                    <div>
                      <p className="font-medium text-gray-900">{source.title}</p>
                      <p className="text-sm text-gray-600">{source.filename}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-sm font-semibold text-blue-600">
                        {(source.similarity * 100).toFixed(1)}%
                      </p>
                      <p className="text-xs text-gray-500">similarity</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}



          {/* Matched FAQ (for manual mode) */}
          {response.matched_faq && response.matched_faq !== 'none' && (
            <div className="border-t pt-4">
              <h3 className="text-sm font-semibold text-gray-700 mb-2">Matched FAQ</h3>
              <div className="p-3 bg-gray-50 rounded">
                <p className="font-mono text-sm text-gray-900">{response.matched_faq}</p>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Mode Comparison */}
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-lg font-semibold mb-4">Mode Comparison</h2>
        
        <div className="grid md:grid-cols-2 gap-6">
          {/* Manual Mode */}
          <div className="border border-gray-200 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-3">
              <Zap className="h-5 w-5 text-gray-600" />
              <h3 className="font-semibold">Manual Keyword Search</h3>
            </div>
            <ul className="space-y-2 text-sm text-gray-700">
              <li className="flex items-start gap-2">
                <span className="text-orange-500">✗</span>
                <span>40-50% accuracy</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-orange-500">✗</span>
                <span>Limited to ~10 predefined FAQs</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-orange-500">✗</span>
                <span>No semantic understanding</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-500">✓</span>
                <span>Fast (~0.1s response)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-orange-500">✗</span>
                <span>Requires exact keyword matches</span>
              </li>
            </ul>
          </div>

          {/* AI-RAG Mode */}
          <div className="border border-blue-200 rounded-lg p-4 bg-blue-50">
            <div className="flex items-center gap-2 mb-3">
              <Sparkles className="h-5 w-5 text-blue-600" />
              <h3 className="font-semibold text-blue-900">AI-RAG Mode</h3>
            </div>
            <ul className="space-y-2 text-sm text-gray-700">
              <li className="flex items-start gap-2">
                <span className="text-green-500">✓</span>
                <span><strong>90%+ accuracy</strong></span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-500">✓</span>
                <span>Full knowledge base coverage (18 docs)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-500">✓</span>
                <span>Semantic search with embeddings</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-500">✓</span>
                <span>Natural language understanding</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-500">✓</span>
                <span>Source citations with confidence</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
          <p className="text-sm text-yellow-800">
            <strong>💡 Try toggling the feature flag:</strong> Set <code className="bg-yellow-100 px-2 py-1 rounded">ENABLE_AI_FAQ_RAG=true</code> in your .env file and restart the service to see the difference!
          </p>
        </div>
      </div>
    </div>
  );
}
