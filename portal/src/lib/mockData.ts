// Mock ticket data - simulating the daily support queue
export interface Ticket {
  id: string;
  number: number;
  subject: string;
  customer: string;
  email: string;
  category: string;
  priority: 'low' | 'medium' | 'high' | 'urgent';
  status: 'new' | 'open' | 'pending' | 'resolved';
  description: string;
  createdAt: Date;
  assignedTo?: string;
}

export const mockTickets: Ticket[] = [
  {
    id: '1',
    number: 1247,
    subject: 'How do I reset my password?',
    customer: 'John Smith',
    email: 'john.smith@example.com',
    category: 'Account',
    priority: 'medium',
    status: 'new',
    description: 'I forgot my password and the reset link is not working. Can you help?',
    createdAt: new Date(Date.now() - 1000 * 60 * 15), // 15 min ago
  },
  {
    id: '2',
    number: 1248,
    subject: 'API returning 500 errors',
    customer: 'Sarah Johnson',
    email: 'sarah.j@techcorp.com',
    category: 'Technical',
    priority: 'urgent',
    status: 'new',
    description: 'Our production API integration is returning 500 errors since this morning. This is blocking our customers.',
    createdAt: new Date(Date.now() - 1000 * 60 * 5), // 5 min ago
  },
  {
    id: '3',
    number: 1249,
    subject: 'How to integrate webhooks?',
    customer: 'Mike Chen',
    email: 'mike.chen@startup.io',
    category: 'Technical',
    priority: 'low',
    status: 'new',
    description: 'I want to set up webhooks for order notifications. Where can I find the documentation?',
    createdAt: new Date(Date.now() - 1000 * 60 * 30), // 30 min ago
  },
  {
    id: '4',
    number: 1250,
    subject: 'Billing question about invoice #4521',
    customer: 'Emily Davis',
    email: 'emily.d@company.com',
    category: 'Billing',
    priority: 'medium',
    status: 'new',
    description: 'I received invoice #4521 but the amount seems incorrect. Can you review?',
    createdAt: new Date(Date.now() - 1000 * 60 * 10), // 10 min ago
  },
  {
    id: '5',
    number: 1251,
    subject: 'How do I export my data?',
    customer: 'Robert Wilson',
    email: 'r.wilson@business.com',
    category: 'Account',
    priority: 'low',
    status: 'new',
    description: 'I need to export all my data for compliance reasons. What format is available?',
    createdAt: new Date(Date.now() - 1000 * 60 * 45), // 45 min ago
  },
  {
    id: '6',
    number: 1252,
    subject: 'Connection timeout errors',
    customer: 'Lisa Anderson',
    email: 'lisa.a@enterprise.com',
    category: 'Technical',
    priority: 'high',
    status: 'new',
    description: 'Getting intermittent connection timeout errors when uploading large files (>100MB).',
    createdAt: new Date(Date.now() - 1000 * 60 * 20), // 20 min ago
  },
  {
    id: '7',
    number: 1253,
    subject: 'What is your refund policy?',
    customer: 'David Brown',
    email: 'david.brown@email.com',
    category: 'Sales',
    priority: 'low',
    status: 'new',
    description: 'I purchased the annual plan but need to cancel. What is your refund policy?',
    createdAt: new Date(Date.now() - 1000 * 60 * 35), // 35 min ago
  },
  {
    id: '8',
    number: 1254,
    subject: 'How to add team members?',
    customer: 'Jennifer Lee',
    email: 'jlee@company.org',
    category: 'Account',
    priority: 'medium',
    status: 'new',
    description: 'I need to add 5 new team members to our account. How do I do this?',
    createdAt: new Date(Date.now() - 1000 * 60 * 8), // 8 min ago
  },
  {
    id: '9',
    number: 1255,
    subject: 'Feature request: Dark mode',
    customer: 'Tom Harris',
    email: 'tharris@dev.com',
    category: 'Feature Request',
    priority: 'low',
    status: 'new',
    description: 'Would love to see a dark mode option in the dashboard. Any plans for this?',
    createdAt: new Date(Date.now() - 1000 * 60 * 50), // 50 min ago
  },
  {
    id: '10',
    number: 1256,
    subject: 'Cannot access dashboard - urgent!',
    customer: 'Amanda White',
    email: 'awhite@critical.com',
    category: 'Technical',
    priority: 'urgent',
    status: 'new',
    description: 'Dashboard is showing a blank page after login. This is urgent as we have a client demo in 30 minutes!',
    createdAt: new Date(Date.now() - 1000 * 60 * 3), // 3 min ago
  },
];

export const supportTeams = [
  { id: 'tier1', name: 'Tier 1 Support' },
  { id: 'tier2', name: 'Tier 2 Support' },
  { id: 'technical', name: 'Technical Team' },
  { id: 'billing', name: 'Billing Team' },
  { id: 'sales', name: 'Sales Team' },
  { id: 'engineering', name: 'Engineering Team' },
];

export const knowledgeBase = [
  {
    id: 'kb1',
    title: 'How to reset your password',
    category: 'Account',
    content: '1. Go to login page\n2. Click "Forgot Password"\n3. Enter your email\n4. Check email for reset link\n5. Link expires in 1 hour',
  },
  {
    id: 'kb2',
    title: 'Webhook Integration Guide',
    category: 'Technical',
    content: 'Webhooks can be configured in Settings > Integrations. Supported events: order.created, order.updated, payment.processed',
  },
  {
    id: 'kb3',
    title: 'Data Export Process',
    category: 'Account',
    content: 'Go to Settings > Data Export. Available formats: CSV, JSON, XML. Export will be emailed within 24 hours.',
  },
  {
    id: 'kb4',
    title: 'Refund Policy',
    category: 'Sales',
    content: '30-day money-back guarantee on annual plans. Pro-rated refunds for cancellations within first 90 days.',
  },
  {
    id: 'kb5',
    title: 'Adding Team Members',
    category: 'Account',
    content: 'Settings > Team > Add Member. Enter email addresses. They will receive invite links valid for 7 days.',
  },
];
