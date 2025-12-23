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
# Styling (colors + nicer UI)
# --------------------------------------------------
st.markdown(
    """
    <style>
      .block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
      .kpi-card {
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;
        padding: 16px 18px;
        background: linear-gradient(135deg, rgba(98, 0, 238, 0.14), rgba(3, 218, 198, 0.10));
        box-shadow: 0 6px 24px rgba(0,0,0,0.12);
      }
      .section-card{
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;
        padding: 18px 18px;
        background: rgba(255,255,255,0.04);
        box-shadow: 0 6px 24px rgba(0,0,0,0.10);
      }
      .badge {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-right: 8px;
        background: rgba(3, 218, 198, 0.14);
        border: 1px solid rgba(3, 218, 198, 0.25);
      }
      .muted {opacity: 0.85;}
      .hr {
        height: 1px;
        background: linear-gradient(90deg, rgba(98,0,238,0.55), rgba(3,218,198,0.55));
        margin: 14px 0 6px 0;
        border-radius: 8px;
      }
      .small {font-size: 0.95rem;}
      .tiny {font-size: 0.88rem;}
      .title-gradient {
        background: linear-gradient(90deg, #8B5CF6, #22C55E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Helpers
# --------------------------------------------------
def show_image(path: str, caption: str) -> None:
    """Displays an image if it exists; otherwise shows a helpful warning."""
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=True)
    else:
        st.warning(
            f"Image not found: `{path}`. Upload it to the repo root (same folder as app.py) "
            f"or fix the filename in app.py."
        )

def info_card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="section-card">
          <div class="badge">{title}</div>
          <div class="hr"></div>
          <div class="small muted">{body}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.markdown("## 🎛️ Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Overview", "Data & Methods", "Results & Visuals", "Forecasting", "Business Impact"],
    index=2
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ✅ Images expected in repo root")
st.sidebar.code(
    "positive_negative_words.png\n"
    "sentiment_over_time.png\n"
    "sentiment_price_ranges.png\n"
    "predicted_vs_actual.png",
    language="text"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    """
    <h1 class="title-gradient">🏠 Rhode Island Airbnb: Sentiment vs Pricing</h1>
    <p class="muted small">
      Topic: VADER sentiment analysis on reviews + pricing comparison + listing-level aggregation.
    </p>
    """,
    unsafe_allow_html=True
)

# Top KPI-like cards
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(
        """<div class="kpi-card"><div class="tiny muted">Method</div>
        <div style="font-size:1.15rem;font-weight:700;">VADER Sentiment</div>
        <div class="tiny muted">Compound score + labels</div></div>""",
        unsafe_allow_html=True
    )
with k2:
    st.markdown(
        """<div class="kpi-card"><div class="tiny muted">Granularity</div>
        <div style="font-size:1.15rem;font-weight:700;">Review → Listing</div>
        <div class="tiny muted">Aggregate by listing_id</div></div>""",
        unsafe_allow_html=True
    )
with k3:
    st.markdown(
        """<div class="kpi-card"><div class="tiny muted">Lens</div>
        <div style="font-size:1.15rem;font-weight:700;">Price Ranges</div>
        <div class="tiny muted">Compare sentiment by tier</div></div>""",
        unsafe_allow_html=True
    )
with k4:
    st.markdown(
        """<div class="kpi-card"><div class="tiny muted">Add-on</div>
        <div style="font-size:1.15rem;font-weight:700;">Rating Forecast</div>
        <div class="tiny muted">Predicted vs actual</div></div>""",
        unsafe_allow_html=True
    )

st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

# --------------------------------------------------
# Sections
# --------------------------------------------------
if section == "Overview":
    st.header("🔍 Overview")
    info_card(
        "Goal",
        "Analyze the relationship between Airbnb listing prices and customer review sentiment in Rhode Island. "
        "Identify whether higher-priced listings consistently receive better sentiment scores by combining "
        "structured listing attributes with unstructured review text."
    )
    info_card(
        "Core Idea",
        "Convert review text into measurable sentiment (VADER compound score), aggregate sentiment to the listing level, "
        "merge with listing price bands, and compare patterns across pricing and listing segments."
    )

elif section == "Data & Methods":
    st.header("📂 Data & Methods")

    c1, c2 = st.columns(2)
    with c1:
        info_card(
            "Datasets",
            "Listings dataset includes price, bedrooms, bathrooms, amenities, neighborhood, room type, and Superhost status. "
            "Reviews dataset includes text comments and timestamps."
        )
    with c2:
        info_card(
            "Cleaning & Engineering",
            "Standardized the price column, handled missing values, reduced extreme outliers, created price-range bands, "
            "computed VADER sentiment score per review, and engineered listing-level sentiment (average score and most common label)."
        )

    st.subheader("🧰 Techniques Used")
    st.markdown(
        """
        - 📊 Pricing EDA: distribution checks, outliers, price banding  
        - 💬 VADER Sentiment: compound score (–1 to +1), sentiment labels  
        - 🔗 Aggregation + Join: listing-level sentiment merged with listing features  
        - ☁️ Text Insights: top positive/negative word analysis and visuals  
        """,
    )

elif section == "Results & Visuals":
    st.header("📊 Results, Visual Analysis & Key Insights")

    st.markdown(
        """
        **Summary of key findings from the combined pricing + sentiment dataset:**
        - 💰 Higher prices do **not** consistently guarantee higher sentiment.  
        - 🧩 Superhosts show stronger positivity, supporting the badge as a quality signal.  
        - 🏠 Entire homes/apartments tend to have stronger sentiment than private rooms.  
        - 🧼 Cleanliness, communication, and check-in issues dominate negative reviews.  
        - 📈 Sentiment stays consistently positive over time with occasional dips, which can flag dissatisfaction events.  
        """
    )

    st.subheader("🖼️ Visuals from the Project")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🗣️ Top Positive & Negative Words")
        show_image("positive_negative_words.png", "Top positive and negative review words")
        st.caption("Highlights key experience drivers behind sentiment scores.")

    with col2:
        st.markdown("#### 📈 Average Sentiment Over Time")
        show_image("sentiment_over_time.png", "Average VADER sentiment over time")
        st.caption("Sentiment remains positive across years with occasional dips and recent improvements.")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("#### 💰 Sentiment Across Price Ranges")
        show_image("sentiment_price_ranges.png", "Sentiment distribution across price bands")
        st.caption("Price alone does not ensure satisfaction; high-price low-sentiment listings indicate mismatch risk.")

    with col4:
        st.markdown("#### ⭐ Forecasting Ratings (Visual)")
        show_image("predicted_vs_actual.png", "Predicted vs Actual ratings")
        st.caption("Shows how well the model aligns with true ratings; generalization can be limited by clustered ratings.")

elif section == "Forecasting":
    st.header("⭐ Forecasting Guest Satisfaction")

    info_card(
        "What was attempted",
        "A Random Forest regression approach was used to predict review scores using structured listing features "
        "and the engineered listing-level sentiment (avg VADER score)."
    )

    st.markdown(
        """
        **Interpretation**
        - Ratings are tightly clustered (often around 4.5–5.0), which limits predictability.  
        - Even with this constraint, adding average sentiment strengthens the signal beyond structured features alone.  
        """
    )

    st.subheader("📌 Forecasting Visual")
    show_image("predicted_vs_actual.png", "Predicted vs Actual ratings (training/test view)")

elif section == "Business Impact":
    st.header("💼 Business Impact")

    st.markdown(
        """
        <div class="section-card">
          <div class="badge">Operational Improvements</div>
          <div class="hr"></div>
          <div class="small muted">
            Strengthen cleaning quality, provide clear check-in instructions, communicate promptly, and keep descriptions accurate.
            These operational basics are the most consistent drivers of negative sentiment.
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-card">
          <div class="badge">Early-Warning Signal</div>
          <div class="hr"></div>
          <div class="small muted">
            Monitor monthly sentiment trends and recurring negative keywords to detect experience issues earlier than star ratings.
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-card">
          <div class="badge">Price–Value Alignment</div>
          <div class="hr"></div>
          <div class="small muted">
            Adjust pricing when sentiment dips and increase prices only when sentiment supports a premium experience.
            High-price listings with lower sentiment represent the highest business risk.
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
st.caption("📌 Portfolio App | Rhode Island Airbnb | Sentiment (VADER) + Pricing Analysis")

