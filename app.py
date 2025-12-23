import os
import streamlit as st

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Airbnb Pricing vs Sentiment Analysis",
    layout="wide"
)

# --------------------------------------------------
# Helper: Safe image loader
# --------------------------------------------------
def show_image(path: str, caption: str, width: int | None = None) -> None:
    """
    Displays an image if it exists; otherwise shows a helpful warning.
    """
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=(width is None), width=width)
    else:
        st.warning(f"Image not found: `{path}`. Please upload it to the repo and confirm the filename/path.")

# --------------------------------------------------
# Title & Introduction
# --------------------------------------------------
st.title("🏠 Airbnb Pricing vs Sentiment Analysis")
st.markdown(
    """
    This app summarizes an AI-driven analysis of **Rhode Island Airbnb listings** by combining:
    **pricing + listing attributes** with **VADER sentiment scores** from guest reviews.
    """
)

# --------------------------------------------------
# Project Overview
# --------------------------------------------------
st.header("🔍 Project Overview")
st.write(
    """
    The objective is to analyze the relationship between Airbnb listing prices and customer sentiment
    extracted from review text. By converting unstructured reviews into measurable sentiment scores and
    joining them with structured listing data, we uncover patterns related to guest satisfaction and
    price–value alignment.
    """
)

# --------------------------------------------------
# Data Description
# --------------------------------------------------
st.header("📂 About the Data")
st.markdown(
    """
    **Listings Dataset**
    - Price, room type, bedrooms, bathrooms, amenities, neighborhood
    - Host attributes including Superhost status

    **Reviews Dataset**
    - Guest review comments and timestamps
    - Processed using VADER sentiment analysis

    **Engineered Variables**
    - Average sentiment per listing
    - Most common sentiment label per listing
    - Price range bands for comparison
    """
)

# --------------------------------------------------
# Methodology
# --------------------------------------------------
st.header("🧰 Methodology")
st.markdown(
    """
    - **EDA + Cleaning**: price standardization, missing value handling, outlier control  
    - **VADER Sentiment**: compound score per review and sentiment labeling  
    - **Aggregation + Join**: listing-level average sentiment merged with listing attributes  
    - **Comparative Analysis**: sentiment trends across price ranges and listing segments  
    """
)

# --------------------------------------------------
# Results & Key Insights
# --------------------------------------------------
st.header("📊 Results & Key Insights")

st.subheader("💰 Pricing vs Sentiment")
st.write(
    """
    Prices cluster in affordable ranges with a small tail of extreme values.
    Positive sentiment dominates across all price bands, meaning higher prices do not consistently guarantee higher sentiment.
    High-priced listings with weaker sentiment indicate potential price–value mismatch risk.
    """
)

st.subheader("🧩 Segment Differences")
st.write(
    """
    Superhost listings show substantially more positive sentiment, supporting the Superhost badge as a quality signal.
    Entire homes/apartments tend to receive stronger sentiment than private rooms, suggesting privacy and professionalism shape satisfaction.
    """
)

st.subheader("🗣️ Guest Experience Drivers")
st.write(
    """
    Negative sentiment is driven mainly by operational and expectation gaps, especially cleanliness, communication, and check-in issues.
    These factors often matter more than amenities when reviews turn negative.
    """
)

st.subheader("📈 Sentiment Over Time")
st.write(
    """
    Sentiment stays consistently positive over a long horizon with occasional dips that can flag guest dissatisfaction events.
    Sentiment shifts can act as an early-warning signal before star ratings show meaningful change.
    """
)

# --------------------------------------------------
# Visuals (Images from README)
# --------------------------------------------------
st.header("🖼️ Visuals Included in README")

img_dir = "images"

col1, col2 = st.columns(2)
with col1:
    show_image(
        os.path.join(img_dir, "positive_negative_words.png"),
        "Top Positive and Negative Words"
    )
with col2:
    show_image(
        os.path.join(img_dir, "sentiment_over_time.png"),
        "Average Sentiment Over Time"
    )

col3, col4 = st.columns(2)
with col3:
    show_image(
        os.path.join(img_dir, "sentiment_price_ranges.png"),
        "Sentiment Distribution Across Price Ranges"
    )
with col4:
    show_image(
        os.path.join(img_dir, "predicted_vs_actual.png"),
        "Forecasting Ratings: Predicted vs Actual"
    )

# --------------------------------------------------
# Business Impact
# --------------------------------------------------
st.header("💼 Business Impact")
st.markdown(
    """
    - Enables early detection of declining guest experience  
    - Helps hosts align pricing with perceived value  
    - Highlights operational pain points (cleanliness, check-in, communication)  
    - Supports proactive improvements before ratings decline  
    """
)

# --------------------------------------------------
# Key Takeaways
# --------------------------------------------------
st.header("📌 Key Takeaways")
st.markdown(
    """
    - VADER provides a fast and interpretable sentiment signal at scale  
    - Joining review sentiment with listing attributes enables price–value insights  
    - Price does not automatically predict satisfaction  
    - Monitoring sentiment trends helps prioritize operational fixes  
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("📊 AI & Analytics Project | Rhode Island Airbnb | Pricing vs Sentiment (VADER)")
