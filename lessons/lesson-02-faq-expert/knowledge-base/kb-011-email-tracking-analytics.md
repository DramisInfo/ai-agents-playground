# KB-011: Email Tracking and Analytics

**Product:** FlowCRM  
**Category:** Analytics  
**Last Updated:** December 2025  
**Article ID:** KB-011

## Summary
Email Tracking and Analytics lets you measure open rates, click rates, reply times, and campaign effectiveness directly inside FlowCRM. This article explains how tracking works, key metrics to monitor, and how to use the analytics dashboard.

## How Tracking Works
- FlowCRM embeds a small tracking pixel in HTML emails to detect opens.
- Link clicks are tracked by redirecting through the FlowCRM tracker for analytics purposes.
- Replies are detected by threading and inbound email parsing.

## Key Metrics
- **Open Rate:** Percentage of recipients who opened the email.
- **Click Rate:** Percentage who clicked at least one link.
- **Reply Rate:** Percentage who replied to the email.
- **Average Reply Time:** Mean time between sent and first reply.
- **Bounce Rate:** Emails that couldn't be delivered.

## Analytics Dashboard
1. Navigate to **Analytics → Emails** in FlowCRM.
2. Select timeframe (7/30/90 days or custom range).
3. Filter by campaign, sender, team, or tag.
4. Click a campaign to view open/click trends and top-performing links.

## Campaign Tracking
- Create a campaign in **Marketing → Campaigns** and send via FlowCRM or connect your mail tool.
- Ensure tracking is enabled in the campaign settings.

## Limitations & Privacy
- Open tracking depends on images being loaded; privacy features and clients (e.g., Apple Mail Privacy Protection) may reduce accuracy.
- Use link tracking with caution for privacy-sensitive recipients.

## Best Practices
- A/B test subject lines and CTAs to improve open/click rates.
- Use short, actionable subject lines.
- Segment lists by engagement to boost deliverability.

## Related Articles
- KB-010: Setting Up Email Integration in FlowCRM
- KB-012: Troubleshooting Email Sync Issues
- KB-015: FlowCRM Security Best Practices
