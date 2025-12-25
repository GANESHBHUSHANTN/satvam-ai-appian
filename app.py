import streamlit as st

# SATVAM.AI – India Context Demo
st.set_page_config(page_title="SATVAM.AI", layout="centered")

st.title("SATVAM.AI")
st.caption("Provenance-first, context-aware knowledge intelligence for Indian regulated workflows")

st.divider()
# Case Context Input (Appian-like)
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

st.divider()
# SATVAM Output Simulation
if st.button("Get Verified Policy Insights"):

    st.subheader("SATVAM.AI – Suggested Knowledge")

    # Example logic (mocked but problem-aligned)
    if case_type == "Insurance Claim":
        st.markdown("### Relevant Insurance Policy Clauses")
        st.write(
            "- Claims above ₹2,00,000 require mandatory field inspection report.\n"
            "- Natural disaster claims must follow IRDAI disaster claim guidelines.\n"
            "- Settlement timelines must not exceed 30 days post document submission."
        )

        st.markdown("**Sources:**")
        st.write(
            "• IRDAI Health & General Insurance Regulations, 2016 – Section 12\n"
            "• Standard Motor/Property Policy Document – Page 18"
        )

    elif case_type == "Government Benefit Approval":
        st.markdown("### Applicable Government Guidelines")
        st.write(
            "- Income eligibility must be verified through state revenue records.\n"
            "- Aadhaar-based verification is mandatory.\n"
            "- Benefits above ₹50,000 require district-level approval."
        )

        st.markdown("**Sources:**")
        st.write(
            "• Ministry of Rural Development Guidelines – Clause 7.3\n"
            "• State Government G.O – Page 6"
        )

    else:
        st.markdown("### Compliance & Regulatory Checks")
        st.write(
            "- Ensure adherence to state-specific compliance norms.\n"
            "- Documentation retention period: minimum 8 years.\n"
            "- Escalation required for high-risk cases."
        )

        st.markdown("**Sources:**")
        st.write(
            "• Applicable State Compliance Manual – Section 4.2\n"
            "• Internal SOP – Page 11"
        )

    st.success("All insights are provenance-backed and audit-ready.")

st.divider()

# Footer (Enterprise Tone)
st.caption(
    "SATVAM.AI | Built for compliance-first, high-stakes decision workflows in India"
)

