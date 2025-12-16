# KB-015: FlowCRM Security Best Practices

**Product:** FlowCRM  
**Category:** Security  
**Last Updated:** December 2025  
**Article ID:** KB-015

## Summary
Security best practices to protect your CRM data, users, and integrations.

## Account & Access
- Enforce **SSO** (SAML/OAuth) for enterprise tenants.
- Enable **2FA** for all Admins.
- Use role-based access control and least privilege.

## Data Protection
- Data encrypted in transit (TLS) and at rest (AES-256).
- Use field-level encryption for sensitive PII.
- Regularly export and back up critical data.

## Integrations & API
- Rotate API keys periodically.
- Use service accounts for automated integrations.
- Restrict webhooks to trusted IPs and validate signatures.

## Auditing & Monitoring
- Enable audit logs for critical actions (user creation, permission changes, data exports).
- Monitor failed login attempts and unusual API usage.

## Incident Response
- Have a contact point for security incidents.
- Revoke compromised credentials immediately and rotate keys.
- Communicate with affected stakeholders per compliance requirements (GDPR/CCPA).

## Compliance
- FlowCRM provides compliance controls for GDPR and CCPA. For enterprise customers, request a DPA and security questionnaire.

## Related Articles
- KB-013: User Roles & Permissions
- KB-019: Dashboard Access & Permissions Troubleshooting
- KB-023: Password & Account Recovery
- KB-010: Setting Up Email Integration in FlowCRM
- KB-012: Troubleshooting Email Sync Issues
