import streamlit as st
import os
from utils.detect import extract_frames_and_detect_players
from utils.ocr import extract_jersey_numbers
from utils.score import score_players

st.set_page_config(page_title="Best Player Finder", layout="wide")

st.title("🏆 Best Player Finder - Football AI Tool")
st.markdown("Upload a short match clip and get the top players (based on jersey recognition).")

video = st.file_uploader("Upload a football match video", type=["mp4", "mov"])

if video:
    with open("temp/uploaded_video.mp4", "wb") as f:
        f.write(video.read())
    st.video("temp/uploaded_video.mp4")

    if st.button("Analyze Video"):
        st.info("⏳ Processing video...")
        extract_frames_and_detect_players("temp/uploaded_video.mp4")
        jerseys = extract_jersey_numbers("temp/frames")
        top_players = score_players(jerseys)

        st.success("✅ Analysis Complete!")
        st.subheader("🏅 Top 3 Players Detected:")
        for i, p in enumerate(top_players[:3]):
            st.write(f"**#{p['player']}** — Score: {p['score']}")