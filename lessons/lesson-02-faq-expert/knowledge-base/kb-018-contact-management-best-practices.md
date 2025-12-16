# KB-018: Contact Management — Best Practices

**Product:** FlowCRM  
**Category:** Data Quality  
**Last Updated:** December 2025  
**Article ID:** KB-018

## Summary
Best practices for organizing and maintaining a healthy contacts database to improve CRM performance and engagement.

## Standardization
- Use consistent name and company fields (e.g., separate first/last names).
- Normalize phone numbers and email addresses.

## Deduplication
- Regularly run deduplication by email and external ID.
- Merge duplicates and preserve activity history when merging.

## Enrichment
- Enrich records with firmographic and demographic data where useful.
- Use third-party connectors for enrichments and keep a record of source.

## Segmentation
- Use tags and custom fields to segment contacts for campaigns and workflows.
- Prefer dynamic lists based on filters (e.g., "active in last 90 days").

## Retention & Cleanup
- Implement a retention policy for stale contacts (e.g., unsubscribe, archive after 24 months of inactivity).
- Archive instead of delete for compliance and auditability.

## Related Articles
- KB-017: Importing CSV — Advanced
- KB-014: Custom Fields and Tags
- KB-016: Automation Workflows
