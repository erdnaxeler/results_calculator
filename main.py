import streamlit as st

def calculate_metrics(total_revenue, email_revenue):
    # Calculating various metrics based on user input
    email_rev_share_current = (email_revenue / total_revenue) if total_revenue else 0
    email_rev_share_goal = 0.30  # 30%
    email_rev_share_needed_change = email_rev_share_goal - email_rev_share_current
    monthly_missed_revenue = (email_rev_share_goal - email_rev_share_current) * total_revenue
    increase_goal = 1.25  # Goal for increase in email revenue

    return email_rev_share_current, email_rev_share_needed_change, monthly_missed_revenue, increase_goal

def main():
    st.title("Performance Contract Simulation")

    # User input fields
    total_revenue = st.number_input("Total Revenue", min_value=0.0, format='%f')
    email_revenue = st.number_input("Email Revenue", min_value=0.0, format='%f')

    if st.button("Calculate"):
        # Perform calculations
        email_rev_share_current, email_rev_share_needed_change, monthly_missed_revenue, increase_goal = calculate_metrics(total_revenue, email_revenue)

        # Displaying results
        st.metric(label="Email Revenue Share - Current Level", value=f"{email_rev_share_current:.2%}")
        st.metric(label="Email Revenue Share - Needed Change", value=f"{email_rev_share_needed_change:.2%}")
        st.metric(label="Email Revenue - Monthly Missed Revenue", value=f"{monthly_missed_revenue:.2f}")
        st.metric(label="Goal for Increase in Email Revenue", value=f"{increase_goal:.2f} times")

if __name__ == "__main__":
    main()
