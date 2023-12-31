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
    # Inject custom CSS for the color scheme and styling
    st.markdown("""
        <style>
            body {
                color: #000000;  /* Regular text color */
            }
            h1, h2, h3, h4, h5, h6 {
                color: #072E60;  /* Titles and important text color */
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
            .css-1syf3y0 {
                width: 100% !important;
                padding: 0 !important;
            }
            /* Additional custom styles */
        </style>
    """, unsafe_allow_html=True)

    st.title("Performance Contract Simulation")

    # ... [your Streamlit app's main code]

    if st.button("Calculate"):
        # ... [calculations and displaying results]

        # Add a button for scheduling an audit
        cal_link = "https://calendly.com/your-link"  # Replace with your actual Calendly link
        st.markdown(f'<a href="{cal_link}" target="_blank"><button class="calendly-button">Schedule an Audit Here</button></a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
