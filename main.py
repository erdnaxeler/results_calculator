import streamlit as st

def calculate_metrics(total_revenue, email_revenue):
    # Calculating various metrics based on user input
    email_rev_share_current = (email_revenue / total_revenue) if total_revenue else 0
    email_rev_share_goal = 0.30  # 30%
    monthly_missed_revenue = (email_rev_share_goal - email_rev_share_current) * total_revenue

    return email_rev_share_current, monthly_missed_revenue

def main():
    st.title("Performance Contract Simulation")

    # User input fields with USD formatting
    total_revenue = st.number_input("Total Revenue (USD)", min_value=0.0, format='%f', step=1000.0)
    email_revenue = st.number_input("Email Revenue (USD)", min_value=0.0, format='%f', step=1000.0)

    if st.button("Calculate"):
        # Perform calculations
        email_rev_share_current, monthly_missed_revenue = calculate_metrics(total_revenue, email_revenue)

        # Displaying results with USD formatting
        st.metric(label="Email Revenue Share - Current Level", value=f"{email_rev_share_current:.2%}")
        st.metric(label="Email Revenue - Monthly Missed Revenue", value=f"${monthly_missed_revenue:,.2f} USD")

if __name__ == "__main__":
    main()
