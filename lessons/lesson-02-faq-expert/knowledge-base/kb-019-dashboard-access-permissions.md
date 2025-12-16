# KB-019: Dashboard Access & Permissions Troubleshooting

**Product:** FlowCRM  
**Category:** Troubleshooting / Access  
**Last Updated:** December 2025  
**Article ID:** KB-019

## Summary
This article helps diagnose and resolve issues related to accessing the FlowCRM dashboard, including login errors, SSO problems, role-based access, browser issues, and session errors.

## Common Symptoms
- Users see a "Permission Denied" message when opening the dashboard
- Dashboard loads partially or shows a blank page
- Users cannot access specific dashboards or widgets
- Intermittent login failures after SSO

## Quick Checklist
1. Confirm user account exists and is active (Settings → Users).
2. Check assigned role and team (Admin or Manager expected for dashboard access).
3. Verify SSO configuration and Identity Provider (IdP) logs if SSO is used.
4. Try a different browser or incognito window to rule out cache/cookies.
5. Check for IP restriction policies or session timeouts.

## Diagnosing Dashboard Access Issues
### 1) Permission Denied or Missing Dashboard Elements
- Verify role permissions: Settings → Users & Roles → [Role] → Dashboard access and Reports permissions.
- If a custom role is used, ensure the role includes access to the specific dashboard and its underlying data sources.
- Confirm the user is assigned to the team or territory that the dashboard filters by.

### 2) SSO / SAML / OAuth Problems
- Check IdP status (Okta, Azure AD, Google Workspace) for recent authentication errors.
- Verify assertion consumer service (ACS) URL and entity ID match values in FlowCRM SSO settings.
- Re-synchronize SAML certificates if recently rotated.
- Use IdP login logs to find specific error codes and time stamps.

### 3) Blank Page / Partial Load
- Clear browser cache and disable extensions (ad blockers, privacy plugins) that may block scripts.
- Check browser console for errors (F12 → Console) and capture screenshots for support.
- Ensure your browser is up-to-date and supported (Chrome, Firefox, Edge latest stable versions).

### 4) Session or Cookie Issues
- Confirm cookies are enabled and not blocked by browser settings.
- For 401/403 on existing sessions, try logging out and logging back in.
- If using a proxy or corporate VPN, test from a direct network to narrow root cause.

### 5) IP Restrictions & Whitelisting
- Check tenant Security settings for IP allowlists that could block the user's current IP.
- If needed, add the user's IP temporarily while investigating.

## Reproducing & Gathering Evidence to Escalate
If the issue persists after the above checks, collect the following for support escalation:
- User ID and email
- Timestamp of failed attempts (UTC)
- Browser name and version
- Screenshots of errors or console logs
- IdP logs (if SSO) or authentication error messages
- Any recent changes to roles, SSO configuration, or security settings

## Temporary Workarounds
- Assign the user a temporary Admin or Manager role to verify if the issue is permission-related.
- Ask the user to try an incognito window or another browser.
- Bypass IP restrictions for the user IP temporarily.

## Preventive Best Practices
- Use role templates for standard access to avoid misconfigurations.
- Monitor IdP certificate expiry and rotate before expiry.
- Document dashboard ownership and filters to speed troubleshooting.

## Related Articles
- KB-013: User Roles & Permissions
- KB-015: FlowCRM Security Best Practices
- KB-023: Password & Account Recovery
