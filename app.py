"""
SATVAM.AI
Provenance-first, context-aware knowledge intelligence
for regulated case management workflows (Appian-aligned)

Author: Ganesh T N Bhushan
"""

import streamlit as st
from dataclasses import dataclass
from typing import List, Dict


# Page Configuration

st.set_page_config(
    page_title="SATVAM.AI",
    page_icon="🛡️",
    layout="centered"
)


# Domain Models

@dataclass
class CaseContext:
    case_type: str
    jurisdiction: str
    amount: int


@dataclass
class KnowledgeSource:
    title: str
    source: str
    reference: str
    content: str



# Mock Knowledge Base

KNOWLEDGE_BASE: Dict[str, List[KnowledgeSource]] = {
    "Insurance Claim": [
        KnowledgeSource(
            title="IRDAI Claim Settlement Timelines",
            source="IRDAI Regulations, 2016",
            reference="Section 12",
            content=(
                "All insurance claims must be settled within 30 days "
                "after receipt of the final required document."
            )
        ),
        KnowledgeSource(
            title="High-Value Claim Inspection Requirement",
            source="Standard Insurance Policy",
            reference="Page 18",
            content=(
                "Claims exceeding ₹2,00,000 require mandatory field inspection "
                "by an authorized surveyor."
            )
        )
    ],
    "Government Benefit Approval": [
        KnowledgeSource(
            title="Income Eligibility Verification",
            source="Ministry of Rural Development Guidelines",
            reference="Clause 7.3",
            content=(
                "Income eligibility must be verified using state revenue records "
                "and Aadhaar-based authentication."
            )
        )
    ],
    "Regulatory Compliance Review": [
        KnowledgeSource(
            title="Record Retention Policy",
            source="State Compliance Manual",
            reference="Section 4.2",
            content=(
                "All compliance-related documents must be retained for a minimum "
                "period of 8 years for audit purposes."
            )
        )
    ]
}

# Core SATVAM

def retrieve_relevant_knowledge(case: CaseContext) -> List[KnowledgeSource]:
    """
    Retrieval-first approach:
    Selects knowledge strictly based on case type.
    No free-form generation to minimize hallucination risk.
    """
    return KNOWLEDGE_BASE.get(case.case_type, [])


def generate_grounded_insights(
    case: CaseContext,
    sources: List[KnowledgeSource]
) -> Dict:
    """
    Generates a structured, explainable response
    grounded entirely in retrieved sources.
    """
    insights = []
    citations = []

    for src in sources:
        insights.append(f"- {src.content}")
        citations.append(
            f"{src.title} | {src.source} ({src.reference})"
        )

    return {
        "insights": insights,
        "citations": citations
    }



# UI Layer (Appian-like Case Screen)

st.title("SATVAM.AI")
st.caption(
    "Provenance-first AI for compliance-critical case decisions"
)

st.divider()

st.subheader("Active Case Context")

case_type = st.selectbox(
    "Case Type",
    [
        "Insurance Claim",
        "Government Benefit Approval",
        "Regulatory Compliance Review"
    ]
)

jurisdiction = st.selectbox(
    "Jurisdiction / State",
    [
        "Tamil Nadu",
        "Karnataka",
        "Maharashtra",
        "Kerala",
        "Delhi"
    ]
)

amount = st.number_input(
    "Claim / Benefit Amount (₹)",
    min_value=0,
    step=5000
)

case_context = CaseContext(
    case_type=case_type,
    jurisdiction=jurisdiction,
    amount=amount
)

st.divider()

# SATVAM Output

if st.button("Get Verified Policy Insights"):

    st.subheader("SATVAM.AI – Recommended Knowledge")

    retrieved_sources = retrieve_relevant_knowledge(case_context)
    result = generate_grounded_insights(case_context, retrieved_sources)

    if not retrieved_sources:
        st.warning("No relevant knowledge found for this case context.")
    else:
        st.markdown("### Key Policy Insights")
        for insight in result["insights"]:
            st.write(insight)

        st.markdown("### Source Citations")
        for cite in result["citations"]:
            st.write(f"• {cite}")

        st.success(
            "All insights are fully grounded in source documents "
            "and suitable for audit and compliance review."
        )

st.divider()


# Footer

st.caption(
    "SATVAM.AI | Designed for Appian-style, regulated enterprise workflows"
)
