import { NextRequest, NextResponse } from 'next/server';
import { query } from '@/lib/db';

export const dynamic = 'force-dynamic';

export async function GET(request: NextRequest) {
  try {
    const result = await query(
      `SELECT 
        id,
        ticket_number,
        subject,
        description,
        customer_name,
        customer_email,
        category,
        priority,
        status,
        assigned_team,
        assigned_to,
        created_at,
        updated_at,
        resolved_at
      FROM support_tickets 
      ORDER BY 
        CASE priority 
          WHEN 'urgent' THEN 1
          WHEN 'high' THEN 2
          WHEN 'medium' THEN 3
          WHEN 'low' THEN 4
        END,
        created_at DESC`
    );

    return NextResponse.json({
      tickets: result.rows,
      count: result.rowCount,
    });
  } catch (error) {
    console.error('Error fetching tickets:', error);
    return NextResponse.json(
      { error: 'Failed to fetch tickets' },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { subject, description, customer_name, customer_email, category, priority } = body;

    // Get next ticket number
    const maxTicket = await query(
      'SELECT MAX(ticket_number) as max_number FROM support_tickets'
    );
    const nextNumber = (maxTicket.rows[0].max_number || 1000) + 1;

    const result = await query(
      `INSERT INTO support_tickets 
        (ticket_number, subject, description, customer_name, customer_email, category, priority, status)
      VALUES ($1, $2, $3, $4, $5, $6, $7, 'new')
      RETURNING *`,
      [nextNumber, subject, description, customer_name, customer_email, category, priority || 'medium']
    );

    return NextResponse.json({
      ticket: result.rows[0],
    });
  } catch (error) {
    console.error('Error creating ticket:', error);
    return NextResponse.json(
      { error: 'Failed to create ticket' },
      { status: 500 }
    );
  }
}
