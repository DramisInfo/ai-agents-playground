# KB-003: How to Create Your First Contact in FlowCRM

**Product:** FlowCRM  
**Category:** Getting Started  
**Last Updated:** December 2025  
**Article ID:** KB-003

## Summary
This article explains how to manually create a contact in FlowCRM, including required fields, optional information, and best practices.

## Prerequisites
- Active FlowCRM account
- User role with contact creation permissions (all roles except "Read Only")

## Step-by-Step Instructions

### Creating a Single Contact

1. **Log in** to your FlowCRM account at app.flowcrm.com

2. **Navigate to Contacts**
   - Click the "Contacts" tab in the main navigation bar
   - Or use the quick search (Ctrl+K or Cmd+K) and type "Contacts"

3. **Start Creating**
   - Click the "+ New Contact" button in the upper right corner
   - The contact creation form will open

4. **Fill in Required Fields**
   - **First Name:** Contact's first name
   - **Last Name:** Contact's last name
   - **Email:** Primary email address (must be unique)

5. **Add Optional Information**
   - **Phone:** Primary phone number
   - **Mobile:** Mobile phone number
   - **Company:** Select existing company or create new
   - **Title:** Job title
   - **Department:** Business department
   - **Address:** Full mailing address
   - **Social Profiles:** LinkedIn, Twitter, etc.
   - **Tags:** Add tags for categorization
   - **Owner:** Assign contact to a team member
   - **Custom Fields:** Any custom fields configured for your account

6. **Save the Contact**
   - Click the "Save" button at the bottom
   - Or press Ctrl+S (Cmd+S on Mac)

7. **Confirmation**
   - You'll see a success message
   - The contact details page will open
   - The contact is now searchable in FlowCRM

## Tips and Best Practices

### Data Quality
- **Always include email:** Required for many features like email tracking and campaigns
- **Use consistent naming:** Capitalize names properly (John Smith, not john smith)
- **Link to companies:** Always associate contacts with their company for better reporting
- **Add tags early:** Use tags like "customer", "prospect", "partner" for easy segmentation

### Smart Features
- **Auto-enrichment:** FlowCRM automatically enriches contact data from public sources after saving
- **Duplicate detection:** If a similar contact exists, you'll see a warning before saving
- **Email validation:** Invalid email addresses will be flagged in real-time

### Keyboard Shortcuts
- **Create new contact:** Ctrl+Shift+C (Cmd+Shift+C on Mac)
- **Save contact:** Ctrl+S (Cmd+S on Mac)
- **Cancel editing:** Esc

## Bulk Contact Creation

For creating multiple contacts at once, see **KB-004: Importing Contacts into FlowCRM**.

## Common Issues

### "Email already exists" Error
This means a contact with that email already exists in your account. Options:
- Search for the existing contact and update it
- Use a different email address
- Contact your admin if you believe this is a duplicate that should be merged

### Contact Not Appearing in List
- **Check filters:** Clear any active filters in the contacts view
- **Check permissions:** Ensure you have permission to view all contacts
- **Search by email:** Use the search bar to find the contact directly
- **Wait for indexing:** New contacts may take 30-60 seconds to appear in search

### Can't Select a Company
- The company must be created first in the Companies section
- Or click "+ New Company" when selecting to create it inline
- Ensure you have permission to create companies

## Related Articles
- KB-001: FlowCRM Product Overview
- KB-004: Importing Contacts into FlowCRM
- KB-005: Managing Duplicate Contacts
- KB-006: Contact Custom Fields Setup
