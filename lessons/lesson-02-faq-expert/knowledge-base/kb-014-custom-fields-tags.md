# KB-014: Custom Fields and Tags

**Product:** FlowCRM  
**Category:** Configuration  
**Last Updated:** December 2025  
**Article ID:** KB-014

## Summary
Custom fields and tags help you capture tailored information for contacts, companies, and deals. This article explains field types, tag usage, and how to import/export custom fields.

## Field Types
- **Text:** Short string values
- **Long text:** Notes and descriptions
- **Number:** Numeric values for scoring
- **Date:** For events and deadlines
- **Single choice / Multi choice:** Dropdown or multi-select
- **Boolean:** True/False

## Creating Custom Fields
1. Settings → Data Model → Custom Fields
2. Select entity (Contact, Company, Deal)
3. Choose field type and validation rules
4. Save and optionally add to forms and views

## Using Tags
- Tags are lightweight labels used for segmentation (e.g., "VIP", "beta", "churn-risk").
- Add tags on contact record or via bulk operations.
- Use tags in filters and automation workflows.

## Import/Export Notes
- When importing, map CSV columns to custom fields by name.
- Export includes custom fields; ensure you have export permissions.

## Best Practices
- Use clear naming conventions (prefix, e.g., "cf_" for custom fields used by integrations).
- Avoid too many fields; prefer tags and related objects when appropriate.

## Related Articles
- KB-003: Create Your First Contact
- KB-017: Importing CSV — Advanced
