# AI-Powered Travel Assistant

## 📌 Overview
The AI-Powered Travel Assistant is a smart conversational tool designed to help users plan personalized travel itineraries. It collects essential travel details, refines user input through guided questions, and generates a structured itinerary based on the provided preferences.

## 🚀 Features
- **User Input Collection:** Gathers key travel details such as budget, duration, destination, and preferences.
- **Prompt Refinement:** Asks follow-up questions for vague or incomplete responses.
- **Personalized Itinerary Generation:** Creates a structured day-wise travel plan with relevant activities and travel tips.
- **Budget Estimation:** Provides an approximate budget breakdown for better trip planning.

## 🛠️ How It Works
1. The assistant asks for key travel details:
   - Budget (low, moderate, high)
   - Trip Duration
   - Destination & Starting Location
   - Purpose of Travel (business, leisure, adventure, etc.)
   - Preferences (food, nature, museums, shopping, etc.)
   - Accommodation Type (luxury, budget, central)
   - Special Requests (accessibility, vegetarian food, kid-friendly, etc.)

2. If user input is incomplete or unclear, follow-up questions are asked to refine the details.

3. A detailed, realistic, and well-structured itinerary is generated based on the provided details.

4. Additional travel tips and budget breakdowns are included for better planning.

## 📝 Prompt Design
- **USER_PROMPT:** Collects necessary details from the user.
- **REFINEMENT_PROMPT:** Ensures vague responses are refined through guided questions.
- **ITINERARY_PROMPT:** Generates a well-structured travel itinerary in a realistic format.

## 📖 Example Output
```plaintext
Day 1:
- 9:00 AM: Arrive in Almaty and check in to your accommodation.
- 11:00 AM: Explore the Green Market to experience local culture.
- 2:00 PM: Visit Panfilov Park for a relaxing stroll.
- 7:00 PM: Enjoy a traditional Kazakh dinner.

Budget Breakdown:
- Accommodation: $200-300
- Food: $150-200
- Transportation: $100-150
- Activities: $50-100
Total: $500-750
```

## 🏆 Evaluation Criteria
The assistant is evaluated based on:
1. **Prompt Design:** Clarity, specificity, and effectiveness.
2. **Prompt Chaining:** Coherence and refinement of responses.
3. **Personalization:** Alignment with user preferences.
4. **Documentation:** Clear explanation of functionality and process.

## 🔧 Future Improvements
- Integration with real-time flight & hotel APIs.
- Support for multiple languages.
- Enhanced itinerary customization based on real-time weather and events.

## 💡 How to Use
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/ai-travel-assistant.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ai-travel-assistant
   ```
3. Create a new environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
4. Install all the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the streamlit application:
   ```sh
   sreamlit run app.py
   ```

## 📜 License
This project is licensed under the MIT License.

---
🚀 *Happy Travels! Let us know if you need further improvements!*
