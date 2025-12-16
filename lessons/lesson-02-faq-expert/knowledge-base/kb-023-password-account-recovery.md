# KB-023: Password & Account Recovery

**Product:** FlowCRM  
**Category:** Account Management  
**Last Updated:** December 2025  
**Article ID:** KB-023

## Summary
This article explains how users can reset passwords, recover access when 2FA devices are lost, and what admins can do to unlock or reset accounts.

## Forgot Password Flow
1. On the login page, click **"Forgot password?"**
2. Enter the email associated with the account
3. Check inbox (and spam folder) for a password reset email
4. Click the reset link and create a new password (link expires after 1 hour by default)

If the reset email doesn't arrive:
- Confirm the account email is correct and active
- Check spam/junk folders and any routing rules
- Contact an Admin to resend/reset if email delivery is blocked

## Password Policy
- Minimum length: 12 characters
- Must include at least one uppercase, one lowercase, one digit, and one special character
- Passwords cannot be reused within the last 12 iterations

## SSO / Identity Provider (IdP) Notes
- If your tenant uses SSO (SAML/OAuth), the password reset must be performed via your IdP (Okta, Azure AD, Google Workspace).
- In SSO setups, the FlowCRM password is not used; contact your Identity team for resets.

## 2FA / MFA Lost Device
- Users should keep backup codes stored securely when enabling 2FA.
- If a device is lost and backup codes are unavailable, an admin can perform a 2FA reset:
  1. Admin navigates to **Settings → Users**
  2. Locate user and click **"Reset 2FA"**
  3. User will be prompted to re-enroll MFA on next login

## Account Locked Out
- Repeated failed attempts may lock accounts temporarily (configurable: e.g., 15 minutes). An admin can unlock a user immediately by editing the user's status.

## Admin Reset Procedures
- Admins can reset passwords for users (if not SSO-managed) by going to Settings → Users → [User] → Reset Password.
- Ensure the user changes the temporary password after first login.
- For SSO tenants, admins should coordinate with the IdP admin.

## Security Considerations
- Verify user identity on sensitive resets using multi-factor verification (email + phone call) for high-risk accounts.
- Log all admin-performed resets in the audit log for compliance.

## Related Articles
- KB-013: User Roles & Permissions
- KB-015: FlowCRM Security Best Practices
- KB-019: Dashboard Access & Permissions Troubleshooting
