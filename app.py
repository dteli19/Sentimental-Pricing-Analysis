import os
import streamlit as st

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Rhode Island Airbnb | Sentiment vs Pricing",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Styling (visual polish)
# --------------------------------------------------
st.markdown(
    """
    <style>
      .block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
      .card {
        border-radius: 18px;
        padding: 18px;
        background: linear-gradient(135deg, rgba(99,102,241,0.12), rgba(34,197,94,0.12));
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 6px 22px rgba(0,0,0,0.12);
        margin-bottom: 14px;
      }
      .badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-bottom: 8px;
        background: rgba(34,197,94,0.15);
        border: 1px solid rgba(34,197,94,0.3);
      }
      .title-gradient {
        background: linear-gradient(90deg, #6366F1, #22C55E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
      }
      .muted {opacity: 0.85;}
      .divider {
        height: 1px;
        background: linear-gradient(90deg, rgba(99,102,241,0.6), rgba(34,197,94,0.6));
        margin: 18px 0;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Helper
# --------------------------------------------------
def show_image(path: str, caption: str):
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=True)
    else:
        st.warning(f"Image not found: `{path}`")

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("📍 Navigation")
section = st.sidebar.radio(
    "Jump to section",
    [
        "Overview",
        "Problem Statement",
        "Data & Methodology",
        "Results & Visuals",
        "Forecasting",
        "Business Impact",
        "Key Takeaways"
    ],
    index=0
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    """
    <h1 class="title-gradient">🏠 Rhode Island Airbnb: Sentiment vs Pricing</h1>
    <p class="muted">
      AI-driven analysis using VADER sentiment scores, pricing exploration, and listing-level aggregation.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# --------------------------------------------------
# Sections
# --------------------------------------------------
if section == "Overview":
    st.header("🔍 Overview")
    st.markdown(
        """
        <div class="card">
        This project analyzes **Rhode Island Airbnb listings** by combining structured pricing and listing
        attributes with unstructured guest reviews. Using **VADER sentiment analysis**, guest experiences
        are quantified and compared across pricing ranges, room types, and host segments.
        </div>
        """,
        unsafe_allow_html=True
    )

elif section == "Problem Statement":
    st.header("❓ Problem Statement")
    st.markdown(
        """
        <div class="card">
        Airbnb hosts and platforms often assume that higher-priced listings deliver superior guest experience.
        However, pricing alone may not reflect how guests actually perceive value.

        This project addresses:
        <ul>
          <li>Do higher-priced Airbnb listings consistently receive better sentiment?</li>
          <li>What operational factors drive positive and negative guest experiences?</li>
          <li>Can sentiment act as an early indicator before star ratings change?</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

elif section == "Data & Methodology":
    st.header("📂 Data & Methodology")
    st.markdown(
        """
        <div class="card">
        <b>Datasets</b><br>
        • Listings data: price, room type, bedrooms, bathrooms, amenities, neighborhood, Superhost status<br>
        • Reviews data: guest comments and timestamps<br><br>

        <b>Techniques Used</b><br>
        • Price cleaning, outlier handling, and price-range binning<br>
        • VADER sentiment scoring (compound score + labels)<br>
        • Aggregation of review sentiment to listing level<br>
        • Merging sentiment with pricing and listing attributes<br>
        • Visual analysis across price tiers, segments, and time
        </div>
        """,
        unsafe_allow_html=True
    )

elif section == "Results & Visuals":
    st.header("📊 Results, Visual Analysis & Insights")

    st.markdown(
        """
        • Positive sentiment dominates across listings, regardless of price<br>
        • Higher prices do <b>not</b> consistently guarantee higher satisfaction<br>
        • Superhosts and entire-home listings show stronger sentiment<br>
        • Cleanliness, communication, and check-in issues drive most negative reviews
        """
    )

    st.subheader("🖼️ Project Visuals")

    col1, col2 = st.columns(2)
    with col1:
        show_image("positive_negative_words.png", "Top Positive and Negative Review Words")
    with col2:
        show_image("sentiment_over_time.png", "Average Sentiment Over Time")

    col3, col4 = st.columns(2)
    with col3:
        show_image("sentiment_price_ranges.png", "Sentiment Distribution Across Price Ranges")
    with col4:
        show_image("predicted_vs_actual.png", "Predicted vs Actual Ratings")

elif section == "Forecasting":
    st.header("⭐ Forecasting Guest Satisfaction")
    st.markdown(
        """
        <div class="card">
        A Random Forest regression approach was explored to predict review scores using structured listing
        features and average sentiment scores.

        While ratings are tightly clustered (4.5–5.0), sentiment improved predictive signal beyond
        structured variables alone, highlighting its complementary value.
        </div>
        """,
        unsafe_allow_html=True
    )

elif section == "Business Impact":
    st.header("💼 Business Impact")
    st.markdown(
        """
        <div class="card">
        • Detect guest dissatisfaction earlier than star ratings<br>
        • Identify price–value mismatches in premium listings<br>
        • Prioritize operational improvements (cleaning, check-in, communication)<br>
        • Support data-driven pricing and quality control decisions
        </div>
        """,
        unsafe_allow_html=True
    )

elif section == "Key Takeaways":
    st.header("📌 Key Takeaways")
    st.markdown(
        """
        <div class="card">
        • VADER sentiment provides a fast, interpretable measure of guest experience<br>
        • Pricing alone does not determine satisfaction<br>
        • Sentiment trends act as an early-warning signal<br>
        • Combining text and structured data unlocks deeper marketplace insights
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.caption("📊 Portfolio Project | Rhode Island Airbnb | Sentiment (VADER) & Pricing Analysis")
