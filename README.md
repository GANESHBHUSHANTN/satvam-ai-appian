# SATVAM.AI

**SATVAM.AI** is a provenance-first, context-aware AI system designed to assist agents handling high-stakes, regulated casework on platforms like **Appian**.

It proactively surfaces **relevant policies, regulations, and SOPs** based on live case context — with **verifiable citations** to ensure compliance and auditability.

---

##  Problem Statement

In regulated industries such as insurance and government services, agents must frequently consult:
- Government regulations
- Internal SOPs
- Policy documents (PDFs)

These documents are fragmented across systems, forcing agents to manually search outside their workflow. This leads to:
- High average handling time (AHT)
- Compliance errors
- Missed policy updates

---

##  Solution Overview

SATVAM.AI acts as a **Just-in-Time Knowledge Copilot** that:
1. Understands the active case context
2. Retrieves only the relevant document sections
3. Generates grounded insights
4. Displays **source-backed citations**

All without leaving the Appian workflow.

---

##  How It Works (High Level)

1. Policy and regulatory documents are indexed
2. Case data (type, location, amount) is used as context
3. Relevant document chunks are retrieved
4. AI generates a concise, grounded summary
5. Each output links back to its source document

---

##  Prototype UI

The prototype includes a lightweight UI that simulates an Appian case screen:
- Case type selection
- Jurisdiction input
- Claim / benefit amount
- Provenance-backed policy insights

This demonstrates feasibility and user experience, not full production deployment.

---

## India-Specific Context

This demo is contextualized for **Indian regulated workflows**, including:
- IRDAI insurance guidelines
- Government benefit approval processes
- State-level compliance considerations

---

##  Tech Stack

- Python
- Streamlit (UI)
- Conceptual RAG architecture
- Document-based policy retrieval (mocked for prototype)

---

#
