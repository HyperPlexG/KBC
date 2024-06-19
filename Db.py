import csv

DATABASE = []

with open('questions.csv', 'r', newline='') as f:
  reader = csv.reader(f)
  level = []
  lvlNo = 0
  for row in reader:
    if lvlNo != int(row[0]):
      DATABASE.append(level)
      level = []
      lvlNo = int(row[0])
    level.append(row[1::])

  if level != []:
    DATABASE.append(level)

if __name__ == "__main__":
  print("DATABASE Initialised:")
  import json
  print(json.dumps(DATABASE, indent=2))

def get_question(n, t):
  global DATABASE
  return DATABASE[n][t]


# a[i][j] = ["question", "option A", "option B", "option C", "option D", "correct answer"]
