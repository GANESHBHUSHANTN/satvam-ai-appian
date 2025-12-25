# SATVAM.AI – System Architecture

SATVAM.AI follows a retrieval-first AI design suitable for regulated workflows.

## Components

1. **Case Context Layer**
   - Receives structured data from Appian cases

2. **Knowledge Index**
   - Policy PDFs
   - Regulations
   - SOP documents

3. **Retrieval Engine**
   - Matches case context to relevant document sections

4. **AI Reasoning Layer**
   - Generates grounded summaries
   - No free-form hallucinations

5. **UI Layer**
   - Displays insights with citations inside workflow

This architecture ensures explainability and compliance readiness.
