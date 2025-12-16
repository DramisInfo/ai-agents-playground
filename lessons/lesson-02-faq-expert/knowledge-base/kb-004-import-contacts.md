# KB-004: Importing Contacts into FlowCRM

**Product:** FlowCRM  
**Category:** Data Management  
**Last Updated:** December 2025  
**Article ID:** KB-004

## Summary
FlowCRM allows you to import large numbers of contacts at once from CSV files, Excel spreadsheets, or other CRM systems. This article covers the import process, file formatting, and troubleshooting.

## Supported Import Formats

- CSV (.csv)
- Excel (.xlsx, .xls)
- Google Sheets (via URL)
- Direct CRM migration (Salesforce, HubSpot, Zoho - contact sales)

## Import Limits

- **Starter Plan:** 1,000 contacts per import
- **Professional Plan:** 10,000 contacts per import
- **Enterprise Plan:** 100,000 contacts per import

Multiple imports can be performed to exceed these limits.

## Step-by-Step Import Process

### 1. Prepare Your Import File

**Required Columns:**
- Email (required - must be unique)
- First Name and Last Name (or Full Name)

**Recommended Columns:**
- Company
- Title
- Phone
- Mobile
- Address
- City
- State
- Zip Code
- Country
- Tags

**Example CSV Format:**
```
Email,First Name,Last Name,Company,Title,Phone
john.doe@example.com,John,Doe,Acme Corp,CEO,555-0100
jane.smith@example.com,Jane,Smith,Tech Inc,CTO,555-0101
```

### 2. Start the Import

1. Log in to FlowCRM
2. Go to **Contacts** → **Import**
3. Click **"Upload File"** or drag and drop your file
4. Wait for file validation

### 3. Map Your Fields

1. Review the automatic field mapping
2. FlowCRM will suggest mappings based on column headers
3. Adjust any incorrect mappings using the dropdowns
4. Map custom fields if needed
5. Click **"Next"**

### 4. Configure Import Options

**Duplicate Handling:**
- **Skip duplicates:** Don't import contacts with existing emails
- **Update existing:** Update existing contacts with new data
- **Create new with suffix:** Add a suffix to duplicate emails (e.g., john.doe+1@example.com)

**Other Options:**
- **Tag all imported contacts:** Add a tag like "Import 2025-12" for tracking
- **Assign owner:** Assign all contacts to a specific user
- **Subscribe to newsletter:** Automatically subscribe contacts to your newsletter
- **Send welcome email:** Send an automated welcome email to new contacts

### 5. Review and Import

1. Review the import summary
2. Check for any validation errors (shown in red)
3. Fix errors or choose to skip invalid rows
4. Click **"Start Import"**

### 6. Monitor Progress

- Import progress will be shown on screen
- Large imports run in the background
- You'll receive an email when complete
- Check **Settings → Import History** for status

## Import Best Practices

### Data Cleaning
- **Remove duplicates** in your file before importing
- **Validate emails** using a tool like NeverBounce
- **Standardize formatting** (phone numbers, addresses)
- **Remove test data** and invalid entries

### Performance Tips
- **Import during off-hours** for faster processing
- **Split large files** into smaller batches (10,000 rows each)
- **Test with a small sample** first (100 contacts)
- **Review results** before importing the full dataset

### Data Security
- **Don't share import files** via email (use secure file transfer)
- **Delete files** from your computer after import
- **Review permissions** of who can import contacts

## Troubleshooting

### "Invalid Email Format" Error
- Emails must follow standard format: user@domain.com
- Remove spaces and special characters
- Check for missing @ symbols or domain extensions

### "Import Failed" Message
**Common causes:**
- File size too large (max 50MB)
- Corrupt file format
- Special characters in column headers
- Exceeded account contact limit

**Solutions:**
- Split file into smaller parts
- Re-export from source system
- Use simple column headers (no spaces or special chars)
- Upgrade plan or remove unused contacts

### Contacts Missing After Import
- Check **Import History** for error details
- Verify duplicate handling settings didn't skip them
- Check if contacts were assigned to another user
- Search by email to locate individual contacts

### Wrong Data in Fields
- Verify field mapping was correct
- Re-import with correct mapping
- Use **Bulk Edit** to fix incorrect data

## Importing from Other CRMs

### Salesforce
1. Export contacts from Salesforce to CSV
2. Download the file
3. Follow standard import process above

### HubSpot
1. Go to Contacts → Export in HubSpot
2. Select "All contacts" and properties
3. Download CSV
4. Import to FlowCRM

### For Large Migrations (10,000+ contacts)
Contact sales@techflowsolutions.com for assisted migration service (Enterprise customers only).

## Post-Import Tasks

After importing:
1. **Review sample contacts** for data quality
2. **Run duplicate detection** (Contacts → Duplicates)
3. **Set up any workflows** for new contacts
4. **Train team** on newly imported data
5. **Create segments** based on import tags

## Related Articles
- KB-003: How to Create Your First Contact
- KB-005: Managing Duplicate Contacts
- KB-006: Contact Custom Fields Setup
- KB-020: FlowCRM Data Limits and Quotas
