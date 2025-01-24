import streamlit as st
import google.generativeai as genai
import os
import pandas as pd

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

st.title("Itinerary Generator")

def get_travel_basics():
    st.subheader("Travel Details : ")
    destination = st.text_input("Where would you like to travel? ")
    duration = st.text_input("How many days are you planning to stay? ")
    budget = st.text_input("What is your budget for this trip? ")
    accommodation = st.selectbox("Accommodation preferences", ["Hotels", "Air-bnb", "Home stay", "No Preferences"])
    activities = st.text_input("What types of activities do you enjoy? (e.g., culture, adventure, food, relaxation) ")
    return destination, duration, budget, accommodation, activities
def get_travel_specifics():
    diet = st.selectbox("Dietary preferences", ["Veg", "Non-veg", "Both"])
    interests = st.text_input("Mention if you have any other specific interests:")
    travel = st.text_input("Mention if you have any walking tolerance or mobility concerns:")
    return diet, interests, travel


def generate_itinerary(destination, duration, budget, accommodation, activities, diet, interests, travel):
    # Create a detailed prompt for Gemini API
    prompt = f"""
    Create a personalized {duration}-day itinerary for a trip to {destination}.
    Budget: {budget}.
    Accommodation preference: {accommodation}.
    Preferred type of activities: {activities}.
    Dietary preferencess: {diet}
    Specific interest within given preferences: {interests}
    Specific travel concerns: {travel}
    Provide a complete, well structured itineraries including preferred activities.
    Suggest restaurants with the dietary preferrences.
    Give sightseeing suggestions including the specific interests.
    Generate the itinerary while taking care of all the travel concerns, if any.
    """

    # Send the prompt to Gemini API
    model=genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    # Extract the generated text
    return response.text


destination, duration, budget, accommodation, activities = get_travel_basics()
diet, interests, travel = get_travel_specifics()
if st.button("Generate"):
    with st.spinner("Generating summary..."):
        itinerary = generate_itinerary(destination, duration, budget, accommodation, activities, diet, interests, travel)
        st.write(itinerary)

