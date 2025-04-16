import streamlit as st
from detect import process_video
from report import generate_report
# from detect import process_live_video
from alerts import send_alert
from db import save_report
from db import save_report, init_db
import datetime
from report import generate_report
init_db() 
st.title("🔍 AI-Powered Anomaly Detection")

video_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])
email = st.text_input("Enter your email for alerts")

if video_file:
    st.video(video_file)

    # Process Video & Detect Anomalies
    with st.spinner("Analyzing video..."):
        anomalies = process_video(video_file.name)

    # Generate Report
    report = generate_report(anomalies)
    st.subheader("📄 Incident Report")
    st.write(report)
    # r1=process_live_video()
    # st.write(r1)
    

    # Store in Database
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_report(timestamp, report, "Moderate")

    # Send Alert
    if email:
        send_alert(email, f"An anomaly was detected:\n\n{report}")
        st.success("🚀 Alert sent successfully!")

    st.success("✅ Processing complete!")