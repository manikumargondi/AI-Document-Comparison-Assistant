from report_generator import generate_docx_report, generate_pdf_report

import streamlit as st
from document_reader import extract_pdf_text
from comparison import compare_documents

st.set_page_config(
    page_title="AI Document Comparison Assistant",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Document Comparison Assistant")
st.write(
    "Upload two PDF documents to summarize their contents "
    "and identify similarities and differences."
)

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Document A")
    file_a = st.file_uploader(
        "Upload the first PDF",
        type=["pdf"],
        key="document_a",
    )

with col_b:
    st.subheader("Document B")
    file_b = st.file_uploader(
        "Upload the second PDF",
        type=["pdf"],
        key="document_b",
    )

if st.button("Compare Documents", type="primary", use_container_width=True):
    if file_a is None or file_b is None:
        st.error("Please upload both PDF documents.")
    elif file_a.name == file_b.name:
        st.error("Please upload two different PDF files.")
    else:
        try:
            with st.spinner("Extracting PDF text..."):
                text_a = extract_pdf_text(file_a)
                text_b = extract_pdf_text(file_b)

            with st.spinner("Comparing documents with AI..."):
                result = compare_documents(text_a, text_b)

            st.session_state["comparison_result"] = result
            st.session_state["document_names"] = (file_a.name, file_b.name)
            st.success("Comparison completed successfully!")

        except ValueError as exc:
            st.error(str(exc))
        except Exception as exc:
            st.error(
                "Something went wrong while comparing the documents. "
                "Check your internet connection and API configuration, "
                "then try again."
            )
            st.exception(exc)

result = st.session_state.get("comparison_result")

if result:
    st.divider()
    st.header("Comparison Results")

    tab_a, tab_b, tab_sim, tab_diff, tab_details, tab_conclusion = st.tabs(
        [
            "Summary A",
            "Summary B",
            "Similarities",
            "Differences",
            "Key Details",
            "Conclusion",
        ]
    )

    with tab_a:
        st.markdown(result["summary_a"])

    with tab_b:
        st.markdown(result["summary_b"])

    with tab_sim:
        st.json(result["similarities"])

    with tab_diff:
        st.json(result["differences"])

    with tab_details:
        st.json(result["key_details"])

    with tab_conclusion:
        st.markdown(result["conclusion"])
        if result["limitations"]:
            st.subheader("Limitations")
            for limitation in result["limitations"]:
                st.write(f"- {limitation}")

    st.divider()
    st.subheader("Download Comparison Report")

    col_docx, col_pdf = st.columns(2)

    with col_docx:
        st.download_button(
            label="Download DOCX Report",
            data=generate_docx_report(result),
            file_name="document_comparison_report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
        )

    with col_pdf:
        st.download_button(
            label="Download PDF Report",
            data=generate_pdf_report(result),
            file_name="document_comparison_report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )