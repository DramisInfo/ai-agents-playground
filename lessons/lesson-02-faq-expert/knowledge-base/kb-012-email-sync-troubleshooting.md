# KB-012: Troubleshooting Email Sync Issues

**Product:** FlowCRM  
**Category:** Troubleshooting  
**Last Updated:** December 2025  
**Article ID:** KB-012

## Summary
This article helps diagnose and resolve common problems when email integration or syncing doesn't work as expected.

## Common Issues and Fixes
### 1) Emails Not Appearing in FlowCRM
- **Check connection status:** Settings → Integrations → Email Integration (green check).
- **Verify sync filters:** Ensure labels/folders selected for sync are correct.
- **Re-authorize account:** Disconnect and reconnect provider credentials.

### 2) Duplicate Emails
- **Cause:** Multiple team members syncing the same mailbox or both manual logging and auto-sync.
- **Fix:** Enable "De-duplicate emails" in Settings → Email.

### 3) Tracking Not Recording Opens/Clicks
- **Cause:** Recipient email client blocks images or privacy protection is enabled.
- **Fix:** Rely on click metrics and reply tracking; inform stakeholders about measurement limits.

### 4) Attachments Not Syncing
- **Cause:** Attachment size exceeds plan limits or provider restrictions.
- **Fix:** Increase plan limits (Enterprise) or ask sender to use links to files instead.

### Logging and Diagnostics
- Enable diagnostic logs for a user: Settings → Support → Enable Email Diagnostics.
- Export logs and include timestamps, user ID, and affected messages when contacting support.

## When to Contact Support
- There is an authorization error after re-connecting.
- You observe data loss or inconsistent sync across multiple accounts.
- Diagnostic logs show provider errors (e.g., 401/403 responses) after re-authorization.

## Checklist Before Escalation
1. Confirm provider status (Google/Outlook outage).
2. Re-authorize account.
3. Confirm correct labels/folders are selected.
4. Check plan limits for daily sync.

## Related Articles
- KB-010: Setting Up Email Integration in FlowCRM
- KB-011: Email Tracking and Analytics
- KB-015: FlowCRM Security Best Practices
