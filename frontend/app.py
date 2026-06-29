# frontend/app.py
import streamlit as st
# Import the cleaner communication tool from your utils directory
from utils.api_client import send_query_to_backend

st.set_page_config(page_title="Support Hub", page_icon="🤖", layout="wide")

st.title("🤖 Customer Support AI Assistant")
st.markdown("Welcome to the production dashboard. Navigate using the sidebar menu on the left.")
st.markdown("---")

left_col, right_col = st.columns([3, 2])

with left_col:
    st.subheader("📥 Enter Customer Interaction(sg)")
    user_message = st.text_area("Type your message here:", placeholder="e.g., Change my billing address on file.", height=150)
    submit_btn = st.button("Run Live Assistant Pipeline", type="primary")

with right_col:
    st.subheader("🤖 S.G's Live Assistant Insights")
    if submit_btn and user_message.strip():
        with st.spinner("Streaming data packets to pipeline..."):
            # Call your utility helper
            api_response = send_query_to_backend(user_message)
            
            if "error" in api_response:
                st.error(api_response["error"])
            else:
                st.metric(label="🎯 Captured Intent Tag", value=str(api_response.get("intent")))
                st.info(f"**Cleaned Processing Input:** {api_response.get('cleaned')}")
                st.json(api_response)