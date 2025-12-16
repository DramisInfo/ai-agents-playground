# KB-010: Setting Up Email Integration in FlowCRM

**Product:** FlowCRM  
**Category:** Configuration  
**Last Updated:** December 2025  
**Article ID:** KB-010

## Summary
Email integration allows FlowCRM to sync your emails, track opens and clicks, and log conversations automatically. This article covers setup for Gmail and Outlook.

## Prerequisites
- FlowCRM Professional or Enterprise plan
- Admin or user permissions
- Gmail or Microsoft 365/Outlook account

## Supported Email Providers
- Gmail (Google Workspace)
- Microsoft Outlook / Office 365
- Microsoft Exchange Server 2016+

## Gmail Integration Setup

### Step 1: Connect Gmail

1. Log in to FlowCRM
2. Go to **Settings → Integrations**
3. Find **Email Integration** section
4. Click **"Connect Gmail"**
5. Choose your Google account
6. Review requested permissions
7. Click **"Allow"**

### Step 2: Configure Sync Settings

**Sync Direction:**
- **One-way (Gmail → FlowCRM):** Emails visible in FlowCRM only
- **Two-way:** Emails sync both ways (recommended)

**What to Sync:**
- **All emails:** Every email syncs to FlowCRM
- **Specific labels:** Only emails with certain labels (e.g., "CRM")
- **Contacts only:** Only emails to/from CRM contacts

**Sync Frequency:**
- Real-time (requires browser extension)
- Every 5 minutes
- Every 15 minutes
- Every hour

### Step 3: Install Browser Extension (Optional)

For real-time sync and email sidebar:
1. Visit Chrome Web Store
2. Search for "FlowCRM for Gmail"
3. Click **"Add to Chrome"**
4. Log in with your FlowCRM credentials
5. The extension appears in Gmail's right sidebar

## Outlook / Office 365 Integration

### Step 1: Connect Outlook

1. Go to **Settings → Integrations**
2. Click **"Connect Outlook"**
3. Sign in with your Microsoft account
4. Approve permissions
5. Wait for connection confirmation

### Step 2: Configure Sync Settings

Similar to Gmail, choose:
- **Folders to sync** (instead of labels)
- **Sync direction**
- **Sync frequency**

### Step 3: Install Outlook Add-in (Optional)

1. Open Outlook
2. Go to **Get Add-ins**
3. Search for "FlowCRM"
4. Click **"Add"**
5. The add-in appears in your email toolbar

## Email Tracking Features

Once integrated, FlowCRM tracks:
- **Email opens:** See when recipients open your emails
- **Link clicks:** Track which links are clicked
- **Reply time:** Measure response times
- **Email thread history:** Full conversation context

Enable tracking:
- Check **"Track this email"** before sending
- Or enable automatic tracking in Settings

## Managing Synced Emails

### Viewing Emails in FlowCRM

1. Open any contact record
2. Click the **"Emails"** tab
3. See all email conversations
4. Click to expand full email thread

### Logging Emails Manually

For emails not automatically synced:
1. Forward the email to save@your-account.flowcrm.com
2. Or use the browser extension's "Log Email" button

### Excluding Emails from Sync

To prevent sensitive emails from syncing:
- Add label "No-CRM" (Gmail) or move to excluded folder (Outlook)
- Or BCC privacy@your-account.flowcrm.com to exclude specific emails

## Troubleshooting

### Emails Not Syncing

**Check these items:**
1. **Connection status:** Settings → Integrations (should show green checkmark)
2. **Sync settings:** Verify correct folders/labels are selected
3. **Permissions:** Re-authorize if needed
4. **Quota limits:** Check if you've exceeded email sync limits

**Common causes:**
- Email provider revoked access
- Changed email password (need to reconnect)
- Exceeded sync limit (10,000 emails/day on Professional)

### "Authorization Error"

**Fix:**
1. Go to Settings → Integrations
2. Click **"Disconnect"** next to email integration
3. Wait 30 seconds
4. Click **"Connect"** again
5. Re-authorize with email provider

### Duplicate Emails Appearing

**Causes:**
- Multiple team members have the same email synced
- Email was manually logged and also auto-synced

**Solution:**
- Settings → Email → Enable "De-duplicate emails"
- Remove manual log if auto-sync is working

### Tracking Not Working

**Requirements for tracking:**
- Recipient must allow images in emails
- Tracking pixel may be blocked by privacy tools
- Some email clients block tracking

**Note:** Open tracking has ~60-70% accuracy due to privacy features in modern email clients.

## Email Sync Limits

**Professional Plan:**
- 10,000 emails synced per day
- 100,000 total emails stored
- 50 MB attachment limit

**Enterprise Plan:**
- Unlimited email sync
- Unlimited storage
- 100 MB attachment limit

## Security and Privacy

- All emails encrypted in transit (TLS)
- Emails stored encrypted at rest (AES-256)
- Access controlled by FlowCRM permissions
- Audit logs track who views emails
- Compliant with GDPR, CCPA

## Best Practices

1. **Choose selective sync** to reduce noise (only sync labeled/folder emails)
2. **Train your team** on which emails to sync
3. **Use automatic BCC** to log sent emails (available in settings)
4. **Review sync weekly** to ensure it's working correctly
5. **Clean up old emails** periodically to stay within limits

## Related Articles
- KB-001: FlowCRM Product Overview
- KB-011: Email Tracking and Analytics
- KB-012: Troubleshooting Email Sync Issues
- KB-015: FlowCRM Security Best Practices
