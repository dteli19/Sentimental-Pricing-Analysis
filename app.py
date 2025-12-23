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
# Styling (clean & professional, not flashy)
# --------------------------------------------------
st.markdown(
    """
    <style>
      .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
      }
      .card {
        border-radius: 14px;
        padding: 18px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 4px 14px rgba(0,0,0,0.10);
        margin-bottom: 14px;
      }
      .title {
        color: #E5E7EB;
        font-weight: 700;
      }
      .subtitle {
        color: #9CA3AF;
        font-size: 0.95rem;
      }
      .divider {
        height: 1px;
        background: rgba(255,255,255,0.15);
        margin: 18px 0;
      }
      .muted {
        color: #9CA3AF;
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
    "Go to section",
    [
        "Overview",
        "Problem Statement",
        "Data & Methodology",
        "Results & Visuals",
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
    <h1 class="title">Rhode Island Airbnb: Sentiment vs Pricing</h1>
    <p class="subtitle">
      Pricing analysis combined with VADER-based sentiment insights from guest reviews
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
        This project analyzes <b>Rhode Island Airbnb listings</b> by combining structured pricing
        and listing attributes with unstructured guest reviews. Using
        <b>VADER sentiment analysis</b>, guest experiences are quantified and compared across
        pricing ranges, room types, and host segments.
        </div>
        """,
        unsafe_allow_html=True
    )

elif section == "Problem Statement":
    st.header("❓ Problem Statement")
    st.markdown(
        """
        <div class="card">
        Airbnb pricing is often assumed to reflect quality, but higher prices do not always
        translate into better guest experiences.

        This project addresses:
        <ul>
          <li>Do higher-priced listings consistently receive more positive sentiment?</li>
          <li>Which operational factors drive negative guest experiences?</li>
          <li>Can sentiment reveal experience issues earlier than star ratings?</li>
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

        <b>Approach</b><br>
        • Cleaned and standardized pricing data, removed extreme outliers<br>
        • Applied VADER to compute sentiment scores and labels<br>
        • Aggregated sentiment at the listing level<br>
        • Merged sentiment with pricing and listing attributes<br>
        • Compared sentiment across price ranges, segments, and time
        </div>
        """,
        unsafe_allow_html=True
    )

elif section == "Results & Visuals":
    st.header("📊 Results & Visual Insights")

    st.markdown(
        """
        • Positive sentiment dominates across nearly all listings<br>
        • Higher prices do <b>not</b> consistently lead to higher satisfaction<br>
        • Superhost and entire-home listings receive stronger sentiment<br>
        • Cleanliness, communication, and check-in issues drive most negative reviews
        """
    )

    st.subheader("🖼️ Key Visuals")

    col1, col2 = st.columns(2)
    with col1:
        show_image("positive_negative_words.png", "Top Positive and Negative Review Words")
    with col2:
        show_image("sentiment_over_time.png", "Average Sentiment Over Time")

    col3, col4 = st.columns(2)
    with col3:
        show_image("sentiment_price_ranges.png", "Sentiment Distribution Across Price Ranges")
    with col4:
        show_image("sentiment_price_ranges.png", "Sentiment Distribution Across Price Ranges")

elif section == "Business Impact":
    st.header("💼 Business Impact")
    st.markdown(
        """
        <div class="card">
        • Identify price–value mismatches in premium listings<br>
        • Detect experience issues earlier using sentiment trends<br>
        • Prioritize operational improvements such as cleaning and check-in clarity<br>
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
        • VADER sentiment provides a fast and interpretable signal of guest experience<br>
        • Pricing alone does not guarantee customer satisfaction<br>
        • Sentiment trends act as an early-warning indicator<br>
        • Combining text and structured data delivers deeper marketplace insights
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.caption("📊 Portfolio Project | Rhode Island Airbnb | Sentiment & Pricing Analysis")
