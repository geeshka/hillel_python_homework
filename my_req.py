import requests
import datetime
num_paragraphs = input("Enter the number of paragraphs: ")

response = requests.get(f"https://baconipsum.com/api/?type=meat-and-filler&paras={num_paragraphs}")
text = response.json()

for paragraph in text:
    print(paragraph + "\n")

text.reverse()

num_pancetta = 0
for paragraph in text:
    if "Pancetta" in paragraph:
        num_pancetta += 1

with open("results.txt", "w") as file:
    file.write(f"Created by Kateryna Shyianova at {datetime.datetime.now()}\n")
    file.write(f"Number of paragraphs with 'Pancetta': {num_pancetta}\n")
    for paragraph in text:
        file.write(paragraph + "\n")

print(f"Number of paragraphs with 'Pancetta': {num_pancetta}")
for paragraph in text:
    print(paragraph + "\n")

