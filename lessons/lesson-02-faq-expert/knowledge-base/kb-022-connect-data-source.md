# KB-022: Connecting Your First Data Source in FlowAnalytics

**Product:** FlowAnalytics  
**Category:** Getting Started  
**Last Updated:** December 2025  
**Article ID:** KB-022

## Summary
This guide walks you through connecting your first data source to FlowAnalytics, whether it's a database, cloud application, or file.

## Prerequisites
- Active FlowAnalytics account
- Access credentials for your data source
- Network access (if connecting to a private database)

## Choosing Your Data Source Type

FlowAnalytics supports three main categories:

**Databases** - Direct connection to SQL/NoSQL databases  
**Cloud Apps** - OAuth integration with SaaS applications  
**Files** - Upload or link to CSV, Excel, Google Sheets

## Connecting a Database

### Example: PostgreSQL Database

**Step 1: Gather Connection Details**

You'll need:
- **Host:** Database server address (e.g., db.example.com)
- **Port:** Usually 5432 for PostgreSQL
- **Database Name:** The specific database to connect to
- **Username & Password:** Database credentials
- **SSL Mode:** Whether to use SSL (recommended)

**Step 2: Add Data Source**

1. Log in to FlowAnalytics
2. Click **"Data Sources"** in the left sidebar
3. Click **"+ Add Data Source"**
4. Search for "PostgreSQL" or select from database category
5. Click **"Connect"**

**Step 3: Configure Connection**

```
Host: db.example.com
Port: 5432
Database: production_db
Username: analytics_user
Password: ••••••••••••
SSL Mode: Require
```

**Optional Settings:**
- **Connection Name:** Give it a friendly name (e.g., "Production DB")
- **Schema:** Specify schema if not using default (usually 'public')
- **Read-only User:** Recommended for safety

**Step 4: Test Connection**

1. Click **"Test Connection"**
2. Wait for validation (5-10 seconds)
3. If successful, you'll see a green checkmark
4. If failed, see troubleshooting section below

**Step 5: Save Data Source**

1. Click **"Save Data Source"**
2. Optionally select tables to sync immediately
3. Configure sync schedule (hourly, daily, etc.)
4. Click **"Complete Setup"**

### Other Database Types

**MySQL:**
- Port: 3306
- Similar process to PostgreSQL
- May require granting permissions: `GRANT SELECT ON database.* TO 'user'@'%';`

**SQL Server:**
- Port: 1433
- Choose authentication: Windows or SQL Server
- May need to enable TCP/IP protocol

**MongoDB:**
- Connection string format: `mongodb://username:password@host:27017/database`
- Supports replica sets and sharded clusters

## Connecting a Cloud Application

### Example: Google Analytics

**Step 1: Select Application**

1. Click **"+ Add Data Source"**
2. Choose **"Cloud Applications"** category
3. Select **"Google Analytics"**
4. Click **"Connect"**

**Step 2: OAuth Authorization**

1. You'll be redirected to Google login
2. Choose your Google account
3. Review requested permissions
4. Click **"Allow"**
5. You'll be redirected back to FlowAnalytics

**Step 3: Configure Integration**

1. **Select Property:** Choose which GA property to import
2. **Select Views:** Choose specific views (or all)
3. **Date Range:** Historical data to import (last 30 days, 1 year, all)
4. **Metrics:** Choose which metrics to sync

**Step 4: Set Sync Schedule**

- Daily (recommended for GA)
- Every 12 hours
- Every 6 hours
- Real-time (Enterprise only)

**Step 5: Complete Setup**

Click **"Start Sync"** to begin initial data import.

### Other Popular Cloud Apps

**Salesforce:**
- OAuth process similar to Google
- Can sync standard and custom objects
- Supports scheduled exports

**Shopify:**
- Requires admin access to your store
- Syncs orders, customers, products
- Real-time webhook support available

**Stripe:**
- Uses API key authentication
- Syncs transactions, customers, subscriptions
- Historical data available

## Uploading a File

### CSV or Excel File

**Step 1: Upload File**

1. Click **"+ Add Data Source"**
2. Choose **"Upload File"**
3. Drag and drop or click **"Select File"**
4. Supported: CSV, XLSX, XLS (max 100MB)

**Step 2: Configure Import**

**Column Detection:**
- FlowAnalytics auto-detects column names (first row)
- Adjust if needed

**Data Types:**
- Auto-detected: text, number, date
- Click column header to change type
- Important for correct calculations later

**Date Format:**
- Select your date format (MM/DD/YYYY, DD/MM/YYYY, etc.)
- Used for parsing date columns correctly

**Step 3: Import**

1. Name your dataset (e.g., "Sales Data 2025")
2. Click **"Import"**
3. Wait for processing
4. Data source is now available

### Google Sheets

**Step 1: Connect Google Sheets**

1. Click **"+ Add Data Source"**
2. Choose **"Google Sheets"**
3. Authorize Google account (OAuth)

**Step 2: Select Sheet**

1. Browse your Google Drive
2. Select the spreadsheet
3. Choose specific sheet/tab
4. Set header row

**Step 3: Configure Sync**

- **Auto-refresh:** Sync changes automatically
- **Interval:** Every 15 minutes to daily
- **Range:** Specific cell range or entire sheet

Live connection! Changes in Google Sheets reflect in FlowAnalytics automatically.

## Network Configuration

### Connecting to Private Databases

If your database is behind a firewall:

**Option 1: Whitelist FlowAnalytics IPs**

Add these IPs to your firewall allowlist:
```
52.1.123.45
52.1.123.46
52.1.123.47
```

(Get current IPs from Settings → Security)

**Option 2: SSH Tunnel (Enterprise)**

1. Set up SSH server with database access
2. In FlowAnalytics, enable "Use SSH Tunnel"
3. Provide SSH credentials
4. Database traffic routes through secure tunnel

**Option 3: VPN Connection (Enterprise)**

Contact support for VPN setup.

## Data Refresh Settings

After connecting, configure how often data syncs:

**Real-time:**
- Uses webhooks/streaming
- Available for select sources
- Enterprise plan only

**Scheduled:**
- Every 15 minutes (minimum on Professional)
- Hourly
- Every 6/12 hours
- Daily at specific time
- Weekly

**Manual:**
- Refresh on-demand only
- Good for one-time imports

## Troubleshooting Connection Issues

### Database Connection Failed

**Common Errors:**

1. **"Connection timeout"**
   - Database host unreachable
   - Check firewall rules
   - Verify host address is correct
   - Whitelist FlowAnalytics IPs

2. **"Authentication failed"**
   - Wrong username/password
   - User doesn't have access to specified database
   - Grant permissions: `GRANT SELECT ON *.* TO 'user'@'%';`

3. **"SSL required"**
   - Database requires SSL but not configured
   - Change SSL Mode to "Require"

4. **"Database not found"**
   - Database name misspelled
   - User doesn't have access to that database

### Cloud App Authorization Failed

1. **Check permissions:** Ensure your account has admin access
2. **Clear cookies:** Browser cookies may be interfering
3. **Try incognito:** Use private browsing mode
4. **Re-authorize:** Disconnect and reconnect

### File Upload Issues

1. **"File too large"** - Max 100MB. Split file or upgrade to Enterprise
2. **"Invalid format"** - Ensure file is CSV or XLSX (not XLS old format)
3. **"Parsing error"** - Check for special characters, fix file encoding (use UTF-8)

## Next Steps

After connecting your data source:

1. **Explore data:** Browse tables and preview data
2. **Create first dashboard:** See KB-023
3. **Set up data refresh alerts:** Get notified of sync failures
4. **Document your schemas:** Add descriptions to tables/columns

## Related Articles
- KB-020: FlowAnalytics Product Overview
- KB-023: Creating Your First Dashboard
- KB-024: Writing Custom SQL Queries
- KB-025: FlowAnalytics Data Source Connectors List
- KB-026: Troubleshooting Data Sync Issues
