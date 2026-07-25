import streamlit as st

def show_footer(in_sidebar=False):
    base_styles = f"""
        text-align: center;
        padding: 0.75rem;
        background: linear-gradient(to right,
            rgba(25,118,210,0.03),
            rgba(100,181,246,0.05),
            rgba(25,118,210,0.03));
        border-top: 1px solid rgba(100,181,246,0.15);
        margin-top: {'0' if in_sidebar else '2rem'};
    """

    st.markdown(
        f"""
<div style="{base_styles}">
    <p style="margin:0; text-align:center;">
        <span style="color:#1976D2; font-size:18px; font-weight:bold;">
            ReportIQ AI
        </span>
        <br>
        <span style="color:#64B5F6; font-size:13px;">
            Created by <b>Veeramachineni Greeshma</b>
        </span>
    </p>
</div>
""",
        unsafe_allow_html=True,
    )