import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="AI Lead Researcher", page_icon="🕵️")

# Title
st.title("🕵️ AI Lead Researcher")
st.markdown("Enter a company URL to generate a business analysis.")

# Input
url_input = st.text_input("Company URL (e.g., stripe.com)", "")

# Button
if st.button("Research"):
    if not url_input:
        st.warning("Please enter a URL.")
    else:
        with st.spinner("Agent is visiting the website and analyzing... (This takes about 20s)"):
            try:
                # ---------------------------------------------------------
                # PASTE YOUR N8N WEBHOOK URL BELOW INSIDE THE QUOTES
                webhook_url = "https://your-n8n-app.onrender.com/webhook/chat"
                # ---------------------------------------------------------
                
                # We send the user's input as "chatInput" because the Agent expects that
                payload = {"chatInput": f"Research {url_input}"}
                
                response = requests.post(webhook_url, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("Analysis Complete!")
                    # We display the text that came back from n8n
                    st.markdown(data.get('output', "No output received."))
                else:
                    st.error(f"Error: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect: {e}")

# Footer
st.markdown("---")
st.caption("Powered by n8n Agentic AI")
