import streamlit as st
from config import settings
from services.document_service import DocumentService
from services.legal_service import LegalService

class DashboardUI:
    def __init__(self):
        st.title(settings.APP_TITLE)
        st.caption(settings.APP_SUBTITLE)
        st.write("---")

    def render_sidebar(self) -> str:
        with st.sidebar:
            st.header("🔑 Authentication & Setup")
            api_key = st.text_input("Enter OpenAI API Key", type="password", help="Type 'test-key' for simulation mode.")
            st.info("**Architecture:** Modular MVC Model Architecture.")
        return api_key

    def render_body(self, api_key: str):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📁 Upload Departmental Notice")
            uploaded_file = st.file_uploader("Upload Notice or Assessment Order (PDF)", type=["pdf"])
            
            scn_text = ""
            if uploaded_file:
                with st.spinner("Extracting text locally..."):
                    scn_text = DocumentService.extract_text(uploaded_file)
                    st.success("Text extracted successfully!")
                    with st.expander("👁️ Preview Text"):
                        st.text(scn_text[:500] + "\n...")
                        
        with col2:
            st.subheader("🤖 Agentic Legal Analysis")
            if not api_key:
                st.warning("Please configure your API credentials in the sidebar.")
            elif uploaded_file and api_key:
                if st.button("🚀 Analyze Notice & Generate Draft"):
                    with st.spinner("Running legal orchestration chain..."):
                        try:
                            output = LegalService.analyze_notice(scn_text, api_key)
                            st.success("Execution Complete!")
                            st.markdown(output)
                        except Exception as e:
                            st.error(str(e))
