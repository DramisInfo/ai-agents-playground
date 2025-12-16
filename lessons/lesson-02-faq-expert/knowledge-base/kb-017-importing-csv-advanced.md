# KB-017: Importing CSV — Advanced

**Product:** FlowCRM  
**Category:** Data Import  
**Last Updated:** December 2025  
**Article ID:** KB-017

## Summary
Advanced tips for importing large CSV files, resolving mapping issues, and avoiding duplicates.

## Pre-import Checklist
- Clean the data (remove empty rows, normalize emails, phone formats).
- Ensure column headers are descriptive (e.g., "first_name" rather than "fn").
- Split very large files (>50k rows) into smaller batches.

## Mapping and Field Matching
- Use the preview step to map CSV headers to FlowCRM fields.
- Save mapping templates for recurring imports.

## Duplicate Handling
- Choose deduplication strategy: by email, by external ID, or by name+company.
- Use the "match confidence" threshold for fuzzy matching.

## Importing Attachments
- Attachments must be accessible via public URL columns.
- The import process will download and attach files to the record (respecting size limits).

## Error Handling
- Import job provides a failure report with row-level errors.
- Re-upload only the failed rows after fixing issues.

## Large Imports & Performance
- Use the API for very large or automated imports.
- Schedule imports during off-peak hours to reduce contention.

## Related Articles
- KB-003: Create Your First Contact
- KB-014: Custom Fields and Tags
