import streamlit as st
import requests

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
DEVELOPER_NAME = "Siswana AI Solutions"  # <--- ENTER YOUR NAME HERE
PAGE_TITLE = "Company Intelligence Portal"
# ---------------------------------------------------------

# 1. Page Configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    layout="centered"
)

# 2. Sidebar with Developer Branding
with st.sidebar:
    st.header("System Status")
    st.info("System Online")
    st.markdown("---")
    st.markdown(f"**Developer:** {DEVELOPER_NAME}")
    st.caption("AI Solutions Architect")

# 3. Main Interface
st.header(PAGE_TITLE)
st.markdown("""
    This tool utilizes an Agentic AI workflow to research companies, 
    analyze business models, and generate strategic summaries.
""")
st.divider()

# 4. Input Section
url_input = st.text_input("Enter Company URL", placeholder="e.g. stripe.com")

# 5. Logic & Execution
if st.button("Generate Analysis", type="primary"):
    if not url_input:
        st.error("Please enter a valid URL to begin the research.")
    else:
        # Professional Loading State
        with st.spinner("Agent is analyzing target infrastructure..."):
            try:
                # ---------------------------------------------------------
                # PASTE YOUR N8N CLOUD WEBHOOK URL BELOW
                webhook_url = "https://my-n8n-bot-25ks.onrender.com/webhook/chat"
                # ---------------------------------------------------------
                
                payload = {"chatInput": f"Research {url_input}"}
                response = requests.post(webhook_url, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Display Results
                    st.success("Analysis Generated Successfully")
                    st.subheader("Executive Summary")
                    st.markdown("---")
                    # Clean output display
                    st.markdown(data.get('output', "No data received."))
                else:
                    st.error(f"Server Error: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Connection Error: {str(e)}")

# 6. Professional Footer
st.markdown("---")
st.caption("© 2025 Automated Research Systems | Confidential Report")
