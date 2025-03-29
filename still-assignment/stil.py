import streamlit as st
import cohere

# Set up Cohere API key
co = cohere.Client('IDlfxdy11paDxht8zQKuLQZkR61dhaPRTwdNzkpF')

def generate_itinerary(destination, budget, days, preferences):
    prompt = f"""
    Create a {days}-day travel itinerary for {destination} with a {budget} budget.
    Preferences: {preferences}.
    Provide a structured day-by-day plan with morning, afternoon, and evening activities.
    """
    
    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=500
    )
    
    return response.generations[0].text

# Streamlit UI
st.title("AI-Powered Travel Planner")

destination = st.text_input("Where are you traveling?")
budget = st.selectbox("Select your budget", ["Luxury", "Mid-range", "Budget-friendly"])
days = st.slider("Trip Duration (days)", 1, 14, 5)
preferences = st.text_area("Any specific preferences? (e.g., food, adventure, history)")

if st.button("Generate Itinerary"):
    if destination:
        with st.spinner("Generating your personalized itinerary..."):
            itinerary = generate_itinerary(destination, budget, days, preferences)
            st.subheader("Your Travel Itinerary")
            st.write(itinerary)
    else:
        st.error("Please enter a destination!")
