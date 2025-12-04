# Summary Generation with Gemini API

This project is about generating a 60 word summary for various **topics** through **Google GenAI** and saving them in the CSV file with **pandas library**

## Workflow

flowchart TD
    A["Import Libraries
(google-gen-ai, csv, pandas)"] --> B["Set Up API Key"]
    B --> C["Read Input CSV File"]
    C --> D["Loop Through Each Row"]
    D --> E["Generate 60-Word Summary
Using Model Prompt"]
    E --> F["Append Result to Summary List
(as Dictionary)"]
    F --> G["Save Output Using Pandas
to output.csv"]

## Steps to Run the Code

1. Cloning the repository:

git clone: https://github.com/blackstag2k/Topic-Summary-Generation.git

2. Installing the Dependencies for the project:

* dependencies listed in the requirements.txt

pip install -r requirements.txt 

* If you want to execute the installed pip module instead of a script file, then use the command below in Command Window

pip -m install -r requirements.txt

### Example:

- python -m pip install pandas,
- python -m pip install google-generativeai

3. Add your API Key 

* Google AI API, Open AI API, etc. generated from any platform. Google Genai key is used here.

export GOOGLE_API_KEY="YOUR_KEY"

4. Run

python main.py

**Output**

Output CSV:
| Topic | Summary |
|-------|--------|
| How to Stay Fit | Staying fit requires consistent physical activity, blending cardio, strength, and flexibility exercises. Aim for 150 minutes of moderate aerobic activity weekly. Complement this with a balanced diet emphasizing whole foods, proper hydration, and adequate sleep. Manage stress effectively. Consistency makes fitness a sustainable lifestyle, boosting energy, mood, and long-term health while preventing chronic diseases. Make it a holistic priority for a healthier life. |
| Benefits of Meditation | Meditation profoundly benefits mind and body. Regular practice significantly reduces stress and anxiety, improving emotional regulation and fostering calm. It enhances focus, concentration, and self-awareness, leading to better decision-making. Physically, it can lower blood pressure, improve sleep quality, and bolster the immune system. Embracing meditation cultivates inner peace, resilience, and a deeper connection to the present, enriching overall well-being. |
| Healthy Eating Habits | Healthy eating prioritizes nutrient-dense foods: fruits, vegetables, whole grains, and lean proteins. Limit processed items, sugary drinks, and unhealthy fats. Practice portion control and mindful eating, respecting hunger cues. Stay well-hydrated with water. Meal planning aids consistent good choices. These habits fuel your body, manage weight, boost energy, and significantly reduce the risk of chronic diseases, ensuring long-term health and vitality. |
| Time Management for Students | Effective time management is vital for student success. Create a detailed schedule, allocating time for classes, study, assignments, and breaks. Prioritize tasks using methods like the Eisenhower Matrix. Break down large assignments into smaller, manageable steps to avoid overwhelm. Combat procrastination by starting early and minimizing distractions. Regularly review and adjust your schedule for flexibility. This approach reduces stress, enhances academic performance, and preserves personal time. |
| Sustainable Gardening Tips | Sustainable gardening prioritizes environmental health and resource conservation. Enhance soil fertility naturally with compost, minimizing chemicals. Implement rainwater harvesting and efficient drip irrigation. Choose native plants suitable for your climate to reduce water and pesticide reliance. Practice companion planting and crop rotation for natural pest control. Encourage pollinators and beneficial insects. This approach fosters a thriving ecosystem, conserves resources, and supports biodiversity for a healthier planet. |

## Tools Used

- Google AI API (Gemini)
- Pandas
- Python 3.14

## Lessons to be Learned

- Using the Pandas DataFrame as a worksheet to save the particulars of the prompt.
- Executing the code through a virtual environment (.venv) like VS Code.
- Understanding the significance of *for* loop in executing multiple topics and *append* function to classify them as an item in a dictionary.


Documented during the Prompt Engineering Course for a 60- word summary generation.


