import streamlit as st

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Airbnb Pricing vs Sentiment Analysis",
    layout="wide"
)

# --------------------------------------------------
# Title & Introduction
# --------------------------------------------------
st.title("🏠 Airbnb Pricing vs Sentiment Analysis")
st.markdown(
    """
    This interactive app presents insights from an AI-driven analysis of **Rhode Island Airbnb listings**.
    The project combines **pricing data**, **listing attributes**, and **VADER-based sentiment analysis**
    of guest reviews to understand how customer experience aligns with pricing and listing characteristics.
    """
)

# --------------------------------------------------
# Project Overview
# --------------------------------------------------
st.header("🔍 Project Overview")
st.write(
    """
    The objective of this project is to analyze the relationship between Airbnb listing prices and
    customer sentiment extracted from review text. By converting unstructured reviews into measurable
    sentiment scores and combining them with structured listing data, we uncover patterns that help
    explain guest satisfaction, pricing strategy, and operational risks.
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
    - Price range bands for comparative analysis
    """
)

# --------------------------------------------------
# Methodology
# --------------------------------------------------
st.header("🧰 Methodology")
st.markdown(
    """
    - **Exploratory Data Analysis (EDA)**  
      Examined price distributions, removed extreme outliers, and created price range bands.

    - **Sentiment Analysis (VADER)**  
      Generated compound sentiment scores and classified reviews as Positive, Neutral, or Negative.

    - **Aggregation & Data Joining**  
      Aggregated sentiment to the listing level and merged with pricing and listing attributes.

    - **Visual & Segment Analysis**  
      Compared sentiment across price ranges, room types, Superhost status, and over time.
    """
)

# --------------------------------------------------
# Results & Insights
# --------------------------------------------------
st.header("📊 Results & Key Insights")

st.subheader("🗣️ Guest Experience Drivers")
st.write(
    """
    Positive reviews are dominated by terms such as *clean*, *great*, *location*, and *stay*,
    highlighting cleanliness and comfort as key satisfaction drivers. Negative reviews,
    although limited in volume, often reference issues with rooms, hosts, and unmet expectations.
    """
)

st.subheader("📈 Sentiment Over Time")
st.write(
    """
    Guest sentiment remains consistently positive over a 14-year period, with occasional dips
    corresponding to short-term dissatisfaction events. Sentiment trends often shift earlier
    than star ratings, making sentiment a valuable early-warning indicator.
    """
)

st.subheader("💰 Pricing vs Sentiment")
st.write(
    """
    Higher prices do not consistently lead to higher sentiment. While premium listings generally
    maintain strong sentiment, some high-priced listings exhibit neutral or negative sentiment,
    signaling potential price–value mismatches.
    """
)

st.subheader("🧩 Segment-Level Patterns")
st.write(
    """
    Superhost listings receive substantially more positive sentiment, validating the Superhost badge
    as a strong performance signal. Entire homes and apartments outperform private rooms in sentiment,
    emphasizing the importance of privacy and professionalism.
    """
)

# --------------------------------------------------
# Forecasting Section
# --------------------------------------------------
st.header("⭐ Forecasting Guest Satisfaction")
st.write(
    """
    A Random Forest regression model was used to predict review scores using structured listing
    attributes and average sentiment scores. Although ratings are tightly clustered between
    4.5 and 5.0, sentiment improves predictive signal beyond structured features alone.
    """
)

# --------------------------------------------------
# Business Impact
# --------------------------------------------------
st.header("💼 Business Impact")
st.markdown(
    """
    - Enables early detection of declining guest experience  
    - Helps hosts align pricing with perceived value  
    - Identifies operational pain points such as cleanliness and check-in issues  
    - Supports proactive quality improvements before ratings decline  
    """
)

# --------------------------------------------------
# Key Takeaways
# --------------------------------------------------
st.header("📌 Key Takeaways")
st.markdown(
    """
    - VADER sentiment provides a fast and interpretable measure of guest experience  
    - Sentiment complements structured listing data and improves insight depth  
    - Pricing alone does not guarantee guest satisfaction  
    - Monitoring sentiment trends enables smarter, proactive decision making  
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("📊 AI & Analytics Project | Airbnb Pricing vs Sentiment | Portfolio Demonstration")

