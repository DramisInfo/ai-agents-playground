# KB-005: Managing Duplicate Contacts in FlowCRM

**Product:** FlowCRM  
**Category:** Data Management  
**Last Updated:** December 2025  
**Article ID:** KB-005

## Summary
This article explains how to identify, merge, and prevent duplicate contacts in FlowCRM to maintain clean, accurate data.

## How FlowCRM Detects Duplicates

FlowCRM uses multiple criteria to identify potential duplicates:
- **Exact email match** (highest confidence)
- **Similar names + same company**
- **Phone number match**
- **Fuzzy name matching** (e.g., "John Smith" vs "J Smith")

## Finding Duplicate Contacts

### Automatic Duplicate Detection

1. Navigate to **Contacts → Duplicates** tab
2. FlowCRM automatically scans for duplicates daily
3. Review the list of potential duplicate pairs
4. Each pair shows:
   - Match confidence (High, Medium, Low)
   - Matching fields
   - Last activity date for each contact
   - Number of associated deals/activities

### Manual Duplicate Search

1. Go to **Contacts** list
2. Use the search bar to find similar contacts
3. Look for duplicate indicators (⚠️ icon)
4. Click "Find Duplicates" next to any contact

## Merging Duplicate Contacts

### Step-by-Step Merge Process

1. **Select Duplicate Pair**
   - Go to **Contacts → Duplicates**
   - Click **"Review"** on a duplicate pair

2. **Choose Master Record**
   - Select which contact to keep as the primary
   - The master record will retain its Contact ID
   - This is important for external integrations

3. **Select Fields to Keep**
   - Review side-by-side comparison
   - Choose which data to keep for each field
   - Can mix and match from both records
   - **Pro tip:** Keep the most complete/recent data

4. **Review Associated Data**
   - Deals, activities, and notes from both contacts will be merged
   - Email history will be combined
   - Tags will be combined (duplicates removed)
   - File attachments will be moved to master record

5. **Confirm and Merge**
   - Click **"Merge Contacts"**
   - Review the confirmation dialog
   - Click **"Confirm Merge"**

6. **Result**
   - The duplicate contact is deleted
   - All data is consolidated in the master record
   - Activity log notes the merge
   - The action can be undone within 30 days

## Preventing Duplicate Contacts

### Enable Duplicate Prevention

1. Go to **Settings → Data Quality**
2. Toggle on **"Duplicate Prevention"**
3. Configure prevention rules:
   - **Block exact email duplicates** (recommended)
   - **Warn on similar names**
   - **Warn on matching phone numbers**

### Browser Extension

Install the FlowCRM Chrome extension for duplicate warnings:
- Alerts you when creating a contact that might be a duplicate
- Shows existing contact details before you save
- One-click merge option
- Available in Chrome Web Store

### Import Settings

When importing contacts:
- Choose **"Skip duplicates"** to prevent new duplicates
- Or **"Update existing"** to refresh existing contact data
- See KB-004 for detailed import options

## Best Practices

### Data Entry Guidelines
- **Always search first** before creating a new contact
- **Use consistent email formats** (avoid aliases like email+tag@domain.com)
- **Standardize company names** (e.g., "IBM" not "I.B.M." or "International Business Machines")
- **Verify before saving** using the duplicate warning system

### Regular Maintenance
- **Review duplicates weekly** in high-volume accounts
- **Set up duplicate alerts** (Settings → Notifications)
- **Train team members** on duplicate prevention
- **Run duplicate scans** after bulk imports

### When to Keep "Duplicates"
Sometimes what appears as duplicates are actually different people:
- Same name, different companies
- Same email domain, different individuals
- Personal vs. work email for same person (use "Related Contacts" feature instead)

## Undoing a Merge

If you merged contacts by mistake:

1. Go to the merged contact's detail page
2. Click **Activity** tab
3. Find the merge event
4. Click **"Undo Merge"** (available for 30 days)
5. Confirm the action

**Note:** All changes made after the merge will be lost when undoing.

## Bulk Merge Operations

For merging many duplicates at once (Professional & Enterprise plans):

1. Go to **Contacts → Duplicates**
2. Select multiple duplicate pairs (checkbox)
3. Click **"Bulk Merge"**
4. Choose merge strategy:
   - **Keep oldest contact** (preserves original Contact ID)
   - **Keep newest contact** (preserves recent data)
   - **Keep most complete** (keeps record with most filled fields)
5. Review summary
6. Click **"Merge All Selected"**

**Warning:** Bulk merges cannot be undone. Always test with a small batch first.

## API and Integration Considerations

When merging contacts:
- **External IDs are preserved** from the master record
- **Webhooks are triggered** for contact.merged events
- **Integration mappings** should point to the master record
- **Old contact ID** becomes inactive and redirects to master

Update your integrations after large merge operations.

## Common Issues

### "Cannot Merge: Different Companies"
Contacts at different companies usually shouldn't be merged. If they're actually the same person:
1. First update one contact's company
2. Then perform the merge

### "Merge Failed" Error
**Common causes:**
- One contact is involved in an active workflow
- External integration has locked the contact
- You don't have permission to merge contacts

**Solution:** Contact your admin or wait for workflows to complete.

### Too Many Duplicates
If you have thousands of duplicates:
1. Contact support for assisted cleanup (Enterprise)
2. Export all contacts, clean externally, then re-import
3. Use the API for programmatic merging

## Related Articles
- KB-003: How to Create Your First Contact
- KB-004: Importing Contacts into FlowCRM
- KB-006: Contact Custom Fields Setup
- KB-030: FlowCRM Data Quality Best Practices
