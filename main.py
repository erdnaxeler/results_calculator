import streamlit as st
import time

def calculate_metrics(total_revenue, email_revenue):
    email_rev_share_current = (email_revenue / total_revenue) if total_revenue else 0
    email_rev_share_goal = 0.30  # 30%
    if email_rev_share_current <= email_rev_share_goal:
        monthly_missed_revenue = (email_rev_share_goal - email_rev_share_current) * total_revenue
    else:
        monthly_missed_revenue = None
    return email_rev_share_current, monthly_missed_revenue

def display_message(email_rev_share_current):
    if email_rev_share_current < 0.25:
        st.info("Email Revenue share should be around 30%. You are most likely missing some key components in your email strategy. Reach out to us and ask for an audit and a detailed action plan to capture all the missed revenue in 90 days.")
    elif 0.25 <= email_rev_share_current <= 0.35:
        st.info("Email Revenue share should be around 30%. It looks like you are in a good spot. Reach out to us for an audit if you fear that the revenue your email provider gives you is overestimated.")
    elif email_rev_share_current > 0.35:
        st.info("Email Revenue share should be around 30%. You are likely facing either over-attribution of revenue or a lack of performance at the top of your funnel. Reach out to us for a more detailed audit.")


def main():
    # Inject custom CSS for centering and styling
    st.markdown("""
        <style>
            .main .block-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .stNumberInput, .stButton, .stAlert, .stMarkdown {
                width: 100%;
                margin: 0 auto;
            }
            .stNumberInput > div > div > input {
                font-size: 20px !important;
                text-align: right;  /* For number input */
            }
            .stButton > button {
                display: block;
                width: 200px;
                margin: 10px auto;  /* Center-align buttons */
            }
            h1 {
                text-align: center !important;
                font-size: 2.5rem !important;
            }
            h2, h3, h4, h5, h6 {
                text-align: center !important;
                font-size: 2rem !important;
            }
            .css-1syf3y0 {
                width: 100% !important;
                padding: 0 !important;
            }
            .stTextInput > div > div > input, .stNumberInput > div > div > input {
                text-align: center;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("Performance Contract Simulation")

    # Centered elements using a single column
    total_revenue = st.number_input("Total Revenue (USD)", min_value=0.0, format='%f', step=1000.0)
    email_revenue = st.number_input("Email Revenue (USD)", min_value=0.0, format='%f', step=1000.0)

    if st.button("Calculate"):
        with st.spinner("Hang on while we compile your data..."):
            time.sleep(5)  # Simulating data processing time
            email_rev_share_current, monthly_missed_revenue = calculate_metrics(total_revenue, email_revenue)
            st.metric(label="Email Revenue Share - Current Level", value=f"{email_rev_share_current:.2%}")
            if monthly_missed_revenue is not None:
                st.metric(label="Email Revenue - Monthly Missed Revenue", value=f"${monthly_missed_revenue:,.2f} USD")
            display_message(email_rev_share_current)

if __name__ == "__main__":
    main()
