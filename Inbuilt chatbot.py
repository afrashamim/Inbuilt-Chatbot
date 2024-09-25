import random

nameofbot = input("What do you like to name your bot?")
username = ""
str1 = nameofbot + ": Hey, I am " + nameofbot + ". What would you like to ask me?"
print(str1)

greetby = ["Hi there", "Hello", "Hi", "Greetings,"]
endby = ["Goodbye..!", "Have a good day"]

questions = {
    "A chatbot is a software application designed to simulate human conversation through text or voice interactions. Chatbots can be integrated into websites, messaging platforms, mobile apps, and other digital interfaces to interact with users, answer questions, and perform various tasks.": [
        "What is the primary purpose of a chatbot?", "How do chatbots interact with users?", "What role do chatbots play in enhancing user interactions?"
    ],
    "Neural networks are a subset of machine learning models inspired by the human brain's architecture. They consist of interconnected nodes organized in layers. Neural networks are important because they can model complex relationships in data and are the foundation of deep learning, which has driven many recent advances in AI, such as image and speech recognition.": [
        "What are neural networks inspired by?", "How do neural networks model complex relationships in data?", "What is the relationship between neural networks and deep learning?"
    ],
    "Natural language processing (NLP) is a field of AI focused on the interaction between computers and human languages. It involves enabling machines to understand, interpret, and generate human language in a way that is both meaningful and useful. Applications of NLP include language translation, sentiment analysis, and chatbots.": [
        "What is Natural Language Processing (NLP)?", "What role do chatbots play in the context of NLP?", "How does NLP enable machines to interact with human languages?"
    ],
    "AI can mimic creativity by generating art, music, or even writing stories, but it does so based on patterns and data it has learned from humans. AI creativity lacks the emotional and imaginative depth that human creativity has.": [
        "How does AI generate creative outputs like art or music?", "What is the primary difference between AI creativity and human creativity?", "How does the absence of emotions affect AI's creative process?"
    ],
    "AI operates based on algorithms and data, making decisions faster and more accurately in specific areas than humans. However, it lacks emotional intelligence, creativity, and general problem-solving abilities outside its programming, unlike human intelligence, which is versatile and adaptive.": [
        "How does AI differ from human intelligence?", "How do algorithms and data influence the decision-making process in AI?", "Why is AI able to make decisions faster and more accurately than humans in specific areas?"
    ],
    "AI has the potential to automate certain jobs, especially those that are repetitive or data-driven. However, it is also likely to create new jobs in AI development, maintenance, and oversight. The key is for workers to adapt by gaining new skills that complement AI technologies.": [
        "What types of jobs are most likely to be automated by AI?", "Will AI replace human jobs?", "What new skills should workers develop to stay relevant in an AI-driven workplace?"
    ]
}

while True:
    Input = input("You: ")
    valid = Input.capitalize()

    if valid in [greeting.capitalize() for greeting in greetby]:
        if username == "":
            print(nameofbot + ": Hi there!")
            print(nameofbot + ": Please enter your name")
            username = input("You: ")
            n = random.randint(0, len(greetby) - 1)
            print(nameofbot + ": " + greetby[n] + ", " + username)
        else:
            n = random.randint(0, len(greetby) - 1)
            print(nameofbot + ": " + greetby[n] + ", " + username)
    elif valid in [statement.capitalize() for statement in endby]:
        s = random.randint(0, len(endby) - 1)
        print(nameofbot + ": " + endby[s] + ", " + username)
        break
    else:
        flag = False
        for ans, qn in questions.items():
            if valid in [question.capitalize() for question in qn]:
                print(nameofbot + ": " + ans)
                flag = True
                break
        if not flag:
            print(nameofbot + ": Sorry, please enter a valid question.")
            choice = input("Would you like to add information to the bot? (y/n) ")
            if choice.upper() == "Y":
                enter = input("Enter your question: ")
                enter = enter.capitalize()
                new = input("Enter the answer: ")
                new = new.capitalize()
                if new in questions:
                    questions[new].append(enter)
                else:
                    questions[new] = [enter]
                print(nameofbot + ": Updated successfully")
            elif choice.upper() == "N":
                print(nameofbot + ": OK!")
            else:
                print(nameofbot + ": Please enter a valid option!")
