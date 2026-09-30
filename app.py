import streamlit as st

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.markdown(
    """
    Welcome to **LegalEase**.

    Generate a draft legal document using AI by providing the
    document type, parties, terms, and effective date.
    """
)

st.divider()

document_type = st.selectbox(
    "Document Type",
    [
        "Non-Disclosure Agreement",
        "Rental Agreement",
        "Employment Agreement",
        "Service Agreement",
        "Partnership Agreement",
        "General Legal Agreement"
    ]
)

parties = st.text_area(
    "Parties",
    placeholder="Example: ABC Technologies Pvt. Ltd. and XYZ Solutions"
)

terms = st.text_area(
    "Terms and Conditions",
    placeholder="Enter the important terms and conditions..."
)

effective_date = st.date_input(
    "Effective Date"
)

if st.button("Generate Legal Document", type="primary"):
    st.success("LegalEase interface is working!")
    st.subheader("📄 Generated Legal Document")

document_text = f"""
NON-DISCLOSURE AGREEMENT

Effective Date: {effective_date}

PARTIES
{parties}

TERMS AND CONDITIONS
{terms}

CONFIDENTIALITY
The parties agree to keep all confidential business information private
and shall not disclose such information to third parties without written
permission.

SIGNATURES

For the First Party:
Name: ______________________
Signature: __________________
Date: ______________________


For the Second Party:
Name: ______________________
Signature: __________________
Date: ______________________
"""

st.text_area(
    "Preview / Edit Document",
    document_text,
    height=600
)

st.download_button(
    label="📥 Download as TXT",
    data=document_text,
    file_name="LegalEase_Document.txt",
    mime="text/plain"
)
    
st.write("### Document Details")

if st.session_state.get("generated_document"):
    st.text_area(
        "Generated Legal Document",
        st.session_state["generated_document"],
        height=500
    )
    st.write(f"**Document Type:** {document_type}")
    st.write(f"**Parties:** {parties}")
    st.write(f"**Effective Date:** {effective_date}")

    if terms:
        st.write("**Terms:**")
        st.write(terms)

st.divider()

st.caption(
    "LegalEase generates drafts for informational purposes only. "
    "Review important legal documents with a qualified legal professional."
)