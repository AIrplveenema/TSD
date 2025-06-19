
import streamlit as st
import requests

# Function to send query to Flask API
def send_query(ip, port, query):
    url = f"http://{ip}:{port}/search"
    payload = {"query": query}
    response = requests.post(url, json=payload)
    return response.json()

# Streamlit UI
st.title("AI Query Interface")

ip = st.text_input("Server IP Address", "127.0.0.1")
port = st.text_input("Server Port", "5000")
query = st.text_area("Your Query")

if st.button("Send Query"):
    if ip and port and query:
        try:
            response = send_query(ip, port, query)
            st.subheader("Response")
            st.json(response)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please fill in all fields.")
