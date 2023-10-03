import random

print("Welcome to Quizzky:)")

count = 0
quizzkydict = {
  1: "Q",
  2: "QU",
  3: "QUI",
  4: "QUIZ",
  5: "QUIZZ",
  6: "QUIZZK",
  7: "QUIZZKY"
}

answers = []

def get_capitals():
    try:
        with open("questions.txt", "r") as f:
            for line in f:
                a = line.strip()  # Strip off the \n
                answer = a.split(",")  # Split the string
                answers.append(answer)
        return answers
    except FileNotFoundError:
        print("Error: The 'questions.txt' file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

get_capitals()

countries = []

def get_countries():
    try:
        with open("questions.txt", "r") as f:
            for line in f:
                country, _ = line.strip().split(",")  # Split the string into country and capital
                countries.append(country)  # Append only the country to the answers list
        return countries
    except FileNotFoundError:
        print("Error: The 'questions.txt' file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

get_countries()

def find_country(country):
    for answer in answers:
        if answer[0] == country:
            return answer[1]
    
asked_questions = []
while count >= 0:
    question_file = random.choice(countries)
    #question = question_file

    if question_file not in asked_questions:
        print("What is the capital of this country?: " + question_file)
        answer = input("type your answer: ").lower()   
        # Check if the answer is correct
        if answer == find_country(question_file):
            asked_questions.append(question_file)
            count += 1
            print(quizzkydict.get(count))
            print("Correct! Spell the next part.")
            if count == len(quizzkydict):
                print("Congratulations! You have spelled 'Quizzky' correctly!") 
        #decrements the count when the answer is wrong
        else:
            print("Incorrect! Try again.")
            count -= 1 
            print(quizzkydict.get(count))
            #asked_questions.remove(question)

print("YoU lOse;)")