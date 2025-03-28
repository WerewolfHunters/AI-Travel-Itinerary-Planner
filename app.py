import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

USER_PROMPT = """
You are a smart travel assistant. Collect the following details from the user:
- Budget (low, moderate, high)
- Trip Duration (in days)
- Destination & Starting Location
- Purpose of travel (business, leisure, adventure, etc.)
- Preferences (food, nature, museums, shopping, etc.)
- Accommodation type (luxury, budget, central)
- Any special requests (accessibility, vegetarian food, kid-friendly, etc.)
"""

REFINEMENT_PROMPT = """
If a user provides vague details, clarify with follow-up questions. Examples:

1. If the user says "I have a moderate budget and I want a mix of famous and offbeat places," 
   respond with:
   - "Would you like a focus on historical places, nature, food experiences, or something else?"
   - "Do you prefer self-guided experiences or guided tours?"

2. If the user gives incomplete input, ask:
   - "How many days will you be traveling?"
   - "Do you have any must-visit places in mind?"

Generate follow-up prompts based on missing details.
"""

ITINERARY_PROMPT = """
Using the collected details, generate a structured travel itinerary. Format:

Day 1:
- [Time]: [Activity]
- [Time]: [Activity]

Day 2:
- [Time]: [Activity]
- ...
Ensure the plan is realistic with proper timing for travel and rest. Provide additional travel tips.
"""

from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage

# Initialize Groq AI
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

def chat_with_ai(user_input):
    messages = [
        SystemMessage(content=USER_PROMPT),
        HumanMessage(content=user_input)
    ]
    response = llm(messages)
    return response.content

from langchain.utilities import SerpAPIWrapper

search_tool = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)

def get_travel_recommendations(destination, preferences):
    query = f"Best places to visit in {destination} for {preferences}"
    results = search_tool.run(query)
    return results[:5]  # Return top 5 recommendations

def generate_itinerary(user_details, recommendations):
    messages = [
        SystemMessage(content=ITINERARY_PROMPT),
        HumanMessage(content=f"User Details: {user_details}\nRecommended Places: {recommendations}")
    ]
    response = llm(messages)
    return response.content

import streamlit as st

st.title("✈️ AI Travel Planner")

# Collect user input
budget = st.selectbox("Budget", ["Low", "Moderate", "High"])
duration = st.number_input("Trip Duration (Days)", min_value=1, step=1)
destination = st.text_input("Destination")
purpose = st.selectbox("Purpose", ["Leisure", "Adventure", "Business", "Cultural"])
preferences = st.multiselect("Preferences", ["Food", "Nature", "Museums", "Shopping", "Hidden Gems"])
accommodation = st.selectbox("Accommodation Type", ["Budget", "Luxury", "Central"])

if st.button("Generate Itinerary"):
    user_input = f"Budget: {budget}, Duration: {duration} days, Destination: {destination}, Purpose: {purpose}, Preferences: {preferences}, Accommodation: {accommodation}"
    
    st.write("⏳ Refining Inputs...")
    refined_input = chat_with_ai(user_input)

    st.write("🔍 Fetching Travel Recommendations...")
    recommendations = get_travel_recommendations(destination, preferences)

    st.write("📜 Generating Final Itinerary...")
    itinerary = generate_itinerary(refined_input, recommendations)

    st.success("✅ Here is your itinerary:")
    st.text_area("Travel Itinerary", itinerary, height=300)

