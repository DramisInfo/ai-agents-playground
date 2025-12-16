-- TechFlow Solutions Database Initialization
-- Creates the base schema and tables used across multiple lessons

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm"; -- For text search
CREATE EXTENSION IF NOT EXISTS "vector"; -- For embeddings and RAG (pgvector)

-- Support Tickets (Lessons 1, 2, 3)
CREATE TABLE IF NOT EXISTS support_tickets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    ticket_number INTEGER UNIQUE NOT NULL,
    subject VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    customer_email VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'new',
    priority VARCHAR(20) DEFAULT 'medium',
    category VARCHAR(100),
    assigned_team VARCHAR(100),
    assigned_to VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP
);

-- Seed support tickets with realistic data
INSERT INTO support_tickets (ticket_number, subject, description, customer_name, customer_email, category, priority, status, created_at) VALUES
(1247, 'How do I reset my password?', 'I forgot my password and the reset link is not working. Can you help?', 'John Smith', 'john.smith@example.com', 'Account', 'medium', 'new', NOW() - INTERVAL '15 minutes'),
(1248, 'API returning 500 errors', 'Our production API integration is returning 500 errors since this morning. This is blocking our customers.', 'Sarah Johnson', 'sarah.j@techcorp.com', 'Technical', 'urgent', 'new', NOW() - INTERVAL '5 minutes'),
(1249, 'How to integrate webhooks?', 'I want to set up webhooks for order notifications. Where can I find the documentation?', 'Mike Chen', 'mike.chen@startup.io', 'Technical', 'low', 'new', NOW() - INTERVAL '30 minutes'),
(1250, 'Billing question about invoice #4521', 'I received invoice #4521 but the amount seems incorrect. Can you review?', 'Emily Davis', 'emily.d@company.com', 'Billing', 'medium', 'new', NOW() - INTERVAL '10 minutes'),
(1251, 'How do I export my data?', 'I need to export all my data for compliance reasons. What format is available?', 'Robert Wilson', 'r.wilson@business.com', 'Account', 'low', 'new', NOW() - INTERVAL '45 minutes'),
(1252, 'Connection timeout errors', 'Getting intermittent connection timeout errors when uploading large files (>100MB).', 'Lisa Anderson', 'lisa.a@enterprise.com', 'Technical', 'high', 'new', NOW() - INTERVAL '20 minutes'),
(1253, 'What is your refund policy?', 'I purchased the annual plan but need to cancel. What is your refund policy?', 'David Brown', 'david.brown@email.com', 'Sales', 'low', 'new', NOW() - INTERVAL '35 minutes'),
(1254, 'How to add team members?', 'I need to add 5 new team members to our account. How do I do this?', 'Jennifer Lee', 'jlee@company.org', 'Account', 'medium', 'new', NOW() - INTERVAL '8 minutes'),
(1255, 'Feature request: Dark mode', 'Would love to see a dark mode option in the dashboard. Any plans for this?', 'Tom Harris', 'tharris@dev.com', 'Feature Request', 'low', 'new', NOW() - INTERVAL '50 minutes'),
(1256, 'Cannot access dashboard - urgent!', 'Dashboard is showing a blank page after login. This is urgent as we have a client demo in 30 minutes!', 'Amanda White', 'awhite@critical.com', 'Technical', 'urgent', 'new', NOW() - INTERVAL '3 minutes');

-- Customer Leads (Lesson 4)
CREATE TABLE IF NOT EXISTS sales_leads (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_name VARCHAR(255) NOT NULL,
    contact_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    industry VARCHAR(100),
    company_size VARCHAR(50),
    status VARCHAR(50) DEFAULT 'new',
    research_data JSONB,
    proposal_generated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Code Review Requests (Lesson 5)
CREATE TABLE IF NOT EXISTS code_reviews (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    repository VARCHAR(255) NOT NULL,
    pull_request_number INTEGER NOT NULL,
    author VARCHAR(100) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    review_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

-- Onboarding Sessions (Lesson 6)
CREATE TABLE IF NOT EXISTS onboarding_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    developer_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    progress_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Invoices (Lesson 7)
CREATE TABLE IF NOT EXISTS invoices (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_number VARCHAR(50) UNIQUE NOT NULL,
    vendor_name VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    due_date DATE,
    status VARCHAR(50) DEFAULT 'pending',
    extracted_data JSONB,
    validated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP
);

-- Research Reports (Lesson 8)
CREATE TABLE IF NOT EXISTS research_reports (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'in_progress',
    research_data JSONB,
    analysis_data JSONB,
    report_content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

-- HR Questions (Lesson 9)
CREATE TABLE IF NOT EXISTS hr_questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    employee_name VARCHAR(255) NOT NULL,
    question TEXT NOT NULL,
    category VARCHAR(100),
    answer TEXT,
    escalated BOOLEAN DEFAULT FALSE,
    status VARCHAR(50) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP
);

-- Agent Metrics (Lessons 10, 11, 12)
CREATE TABLE IF NOT EXISTS agent_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    agent_name VARCHAR(100) NOT NULL,
    metric_type VARCHAR(50) NOT NULL,
    metric_value JSONB NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Agent Audit Log (Lesson 11)
CREATE TABLE IF NOT EXISTS agent_audit_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    agent_name VARCHAR(100) NOT NULL,
    user_id VARCHAR(100),
    action VARCHAR(100) NOT NULL,
    details JSONB,
    ip_address INET,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Knowledge Base Documents (Lesson 2)
CREATE TABLE IF NOT EXISTS kb_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    filename VARCHAR(500) NOT NULL,
    filepath VARCHAR(1000) NOT NULL UNIQUE,
    title VARCHAR(500),
    content_type VARCHAR(100),
    file_size INTEGER,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    indexed_at TIMESTAMP
);

-- Knowledge Base Chunks with Embeddings (Lesson 2)
CREATE TABLE IF NOT EXISTS kb_chunks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL REFERENCES kb_documents(id) ON DELETE CASCADE,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    embedding vector(768), -- Ollama nomic-embed-text embeddings are 768 dimensions
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(document_id, chunk_index)
);

-- Create indexes for better performance
CREATE INDEX idx_tickets_status ON support_tickets(status);
CREATE INDEX idx_tickets_created ON support_tickets(created_at DESC);
CREATE INDEX idx_leads_status ON sales_leads(status);
CREATE INDEX idx_invoices_status ON invoices(status);
CREATE INDEX idx_metrics_agent ON agent_metrics(agent_name, timestamp DESC);
CREATE INDEX idx_audit_agent ON agent_audit_log(agent_name, timestamp DESC);

-- Indexes for knowledge base
CREATE INDEX idx_kb_documents_filepath ON kb_documents(filepath);
CREATE INDEX idx_kb_chunks_document ON kb_chunks(document_id);
-- Vector similarity search index (using HNSW algorithm)
CREATE INDEX idx_kb_chunks_embedding ON kb_chunks USING hnsw (embedding vector_cosine_ops);

-- Success message
DO $$
BEGIN
    RAISE NOTICE 'TechFlow database initialized successfully!';
END $$;
