import streamlit as st
from data import DATA

st.set_page_config(
    page_title="OSINT Framework",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 OSINT Framework")
st.caption("Browse OSINT resources by category")

category = st.sidebar.radio(
    "Categories",
    list(DATA.keys())
)

st.header(category)

for section, websites in DATA[category].items():
    with st.expander(f"📂 {section}", expanded=True):
        cols = st.columns(3)

        for i, (name, info) in enumerate(websites.items()):
            with cols[i % 3]:
                with st.container(border=True):

                    st.markdown(f"### {name}")

                    st.write(info["description"])

                    st.link_button(
                        "🌐 Visit Website",
                        info["url"],
                        use_container_width=True
                    )