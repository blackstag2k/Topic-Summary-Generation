import csv
import google.genai as genai
import pandas as pd

client = genai.Client(api_key="ENTER_API_KEY")

df = pd.read_csv(r"C:\Users\Bhaskar Rana\OneDrive\Desktop\topics.csv")

with open(r"C:\Users\Bhaskar Rana\OneDrive\Desktop\topics.csv", "r")as file:
	topics = [row[0] for row in csv.reader(file)]

for topic in topics:
	prompt = f"""Give a 60 word summary for each of the topics: \n\n{topics}"""
	response = client.models.generate_content(
		model="gemini-2.5-flash",
		contents=prompt
	)

	summary = response.text

summaries = []

summaries.append({
	"topic": topic,
	"summary": summary
})

df = pd.DataFrame(summaries)
df.to_csv(r"C:\Users\Bhaskar Rana\OneDrive\Desktop\output_topic_summaries.csv", index=False)
print("summaries are generated and saved to output_topic_summaries.csv")