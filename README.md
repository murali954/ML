# AI-Powered Travel Planner 

## Introduction
This project is an AI-powered travel itinerary planner that generates personalized travel plans based on user inputs such as destination, budget, duration, and preferences. The application is built using **Streamlit** for the frontend and **Cohere's AI API** for text generation.

---

## Features
- **User-Friendly UI**: Simple interface using Streamlit.
- **AI-Powered Itinerary Generation**: Uses Cohere's AI to create structured travel plans.
- **Customizable Inputs**: Allows users to specify their budget, trip duration, and preferences.
- **Real-Time API Calls**: Fetches responses dynamically.
- **Cloud Deployment**: Hosted on Streamlit Cloud for easy access.


## Tech Stack
- **Python**
- **Streamlit**
- **Cohere API**
- **GitHub (for version control & hosting deployment)**


## Installation Guide
### **Step 1: Clone Repository**
```sh
 git clone https://github.com/murali954/ML.git
 cd stil-assignment

### **Step 2: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Step 3: Set Up API Key**
Replace `YOUR_COHERE_API_KEY` in the script with your actual Cohere API key.

### **Step 4: Run the Application**
```sh
streamlit run stil.py

## Hosting on Streamlit Cloud
1. **Push Code to GitHub**: Ensure your code is in a GitHub repository.
2. **Go to Streamlit Cloud**: Visit [Streamlit Share](https://share.streamlit.io/).
3. **Deploy the App**:
   - Select your repository.
   - Set the main file as `travel_planner.py`.
   - Click **Deploy**.
4. **Get Your App URL**: Share the provided link.

### **Live App URL**
🌍 **Try the live app here:** [Travel Planner](https://dfbpyudtcndb2vn3sgcrh9.streamlit.app/)

---

## API Usage
The application utilizes Cohere's `generate` API to create custom travel itineraries. The prompt structure is:
```
Create a {days}-day travel itinerary for {destination} with a {budget} budget.
Preferences: {preferences}.
Provide a structured day-by-day plan with morning, afternoon, and evening activities.
```

---

## Example Usage
**User Input:**
- Destination: **Paris**
- Budget: **Mid-range**
- Duration: **5 days**
- Preferences: **Food, history, adventure**

**Generated Itinerary (Example Snippet):**
```
Day 1:
Morning - Visit Eiffel Tower & breakfast at a local café.
Afternoon - Explore the Louvre Museum.
Evening - Enjoy a dinner cruise on the Seine River.
...
```

---

## Future Improvements
- **Add More AI Models**: Support for OpenAI, Hugging Face, etc.
- **Improve Itinerary Accuracy**: Incorporate real-time location-based suggestions.
- **Enhance UI**: More interactive elements and visuals.
- **User Authentication**: Save itineraries for future reference.

---

## Conclusion
This AI-powered travel planner simplifies trip planning by generating detailed and personalized itineraries. It offers a seamless user experience, leveraging **Streamlit** and **Cohere AI** to make travel planning effortless.



