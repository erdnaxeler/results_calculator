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
        st.markdown("<p style='color:#000000;'>Email Revenue share should be around 30%. You are most likely missing some key components in your email strategy. Reach out to us and ask for an audit and a detailed action plan to capture all the missed revenue in 90 days.</p>", unsafe_allow_html=True)
    elif 0.25 <= email_rev_share_current <= 0.35:
        st.markdown("<p style='color:#000000;'>Email Revenue share should be around 30%. It looks like you are in a good spot. Reach out to us for an audit if you fear that the revenue your email provider gives you is overestimated.</p>", unsafe_allow_html=True)
    elif email_rev_share_current > 0.35:
        st.markdown("<p style='color:#000000;'>Email Revenue share should be around 30%. You are likely facing either an over-attribution of revenue or a lack of performance at the top of your funnel. Reach out to us for a more detailed audit.</p>", unsafe_allow_html=True)

def main():
    # Inject custom CSS for the color scheme and styling
    st.markdown("""
        <style>
            .st-bb {
                border-top: none;
            }
            .st-at {
                background-color: #FFF;
            }
            .stButton > button {
                color: white;
                background-color: #6BB33B;  /* Button color */
                border: none;
                border-radius: 4px;
                padding: 10px 24px;
                font-size: 16px;
                line-height: 1.5;
            }
            .stButton > button:hover {
                background-color: #5da331;  /* Button hover color */
            }
            h1 {
                color: #072E60;  /*  color */
                text-align: center;
                font-size: 2.5rem !important;
            }
            .stNumberInput > div > div > input {
                font-size: 20px !important;
                color: #000000;  /* Input text color */
            }
            .css-1syf3y0 {
                padding: 0 !important;
            }
            .stTextInput > div > div > input, .stNumberInput > div > div > input {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("Results calculator")

    # Centered elements using a single column
    total_revenue = st.number_input("Total Revenue (USD)", min_value=0.0, format='%f', step=1000.0)
    email_revenue = st.number_input("Email Revenue (USD)", min_value=0.0, format='%f', step=1000.0)

    if st.button("Calculate"):
        with st.spinner("Hang on while we compile your data..."):
            time.sleep(4)  # Simulating data processing time
            email_rev_share_current, monthly_missed_revenue = calculate_metrics(total_revenue, email_revenue)
            st.metric(label="Email Revenue Share - Current Level", value=f"{email_rev_share_current:.2%}")
            if monthly_missed_revenue is not None:
                st.metric(label="Email Revenue - Monthly Missed Revenue", value=f"${monthly_missed_revenue:,.2f} USD")
            display_message(email_rev_share_current)

        # Add a button for scheduling an audit
        st.markdown("<a href='https://calendly.com/alexmoulartmarketing/30min' target='_blank'><button class='calendly-button'>Schedule an Audit Here</button></a>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
