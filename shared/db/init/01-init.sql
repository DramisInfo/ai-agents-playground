-- TechFlow Solutions Database Initialization
-- Creates the base schema and tables used across multiple lessons

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm"; -- For text search

-- Support Tickets (Lessons 1, 2, 3)
CREATE TABLE IF NOT EXISTS support_tickets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    ticket_number VARCHAR(20) UNIQUE NOT NULL,
    subject VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'open',
    priority VARCHAR(20) DEFAULT 'medium',
    category VARCHAR(100),
    assigned_team VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP
);

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

-- Create indexes for better performance
CREATE INDEX idx_tickets_status ON support_tickets(status);
CREATE INDEX idx_tickets_created ON support_tickets(created_at DESC);
CREATE INDEX idx_leads_status ON sales_leads(status);
CREATE INDEX idx_invoices_status ON invoices(status);
CREATE INDEX idx_metrics_agent ON agent_metrics(agent_name, timestamp DESC);
CREATE INDEX idx_audit_agent ON agent_audit_log(agent_name, timestamp DESC);

-- Insert sample data for testing
INSERT INTO support_tickets (ticket_number, subject, description, category, priority) VALUES
    ('TICKET-001', 'How do I reset my password?', 'I forgot my password and need to reset it.', 'account', 'high'),
    ('TICKET-002', 'API documentation request', 'Where can I find the API documentation?', 'documentation', 'medium'),
    ('TICKET-003', 'Billing question', 'I have a question about my last invoice.', 'billing', 'medium')
ON CONFLICT (ticket_number) DO NOTHING;

-- Success message
DO $$
BEGIN
    RAISE NOTICE 'TechFlow database initialized successfully!';
END $$;
