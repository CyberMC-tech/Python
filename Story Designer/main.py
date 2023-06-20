import random
import openai
from elevenlabs import generate, play, set_api_key

from lists import *

set_api_key("bc197f7f5dd95733bf29158658a2dc9e")
openai.api_key = "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"
num = 1
# select four jobs from the list of jobs
job_sample = random.sample(jobs, 4)
emotion_sample = random.sample(emotions, 4)
relationship_sample = random.sample(relationship, 4)
actions_sample = random.sample(actions, 4)
writings_sample = random.sample(writings, 4)


def selected_jobs(sample, n):
    for i in sample:
        print(f"{n}.) {i}")
        n += 1


def selected_emotions(sample, n):
    for i in sample:
        print(f"{n}.) {i}")
        n += 1


def selected_relationships(sample, n):
    for i in sample:
        print(f"{n}.) {i}")
        n += 1


def selected_actions(sample, n):
    for i in sample:
        print(f"{n}.) {i}")
        n += 1


def selected_writing(sample, n):
    for i in sample:
        print(f"{n}.) {i}")
        n += 1


# Select a random name for the person
name = input("Please enter a name: ")

# print the list of jobs with a corresponding number
selected_jobs(job_sample, num)
print("5.) Other")

acceptable_job = False

while not acceptable_job:

    # receive input from user for the job
    j = input("Please enter a number corresponding to the job or select 'Other' to type in your own job: ")

    try:
        job_num = int(j)
        if job_num <= 4:
            job = job_sample[int(j) - 1]
            acceptable_job = True
        elif job_num == 5:
            job = input("Please enter your own job: ")
            acceptable_job = True
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a number between 1 and 5.")

selected_emotions(emotion_sample, num)
print("5.) Other")

acceptable_emotion = False

while not acceptable_emotion:

    emotion = input(
        "Please enter a number corresponding to the emotion or select 'Other' to type in your own emotion: ")

    try:
        emotion_num = int(emotion)
        if emotion_num <= 4:
            emotion = emotion_sample[int(emotion) - 1]
            acceptable_emotion = True
        elif emotion_num == 5:
            emotion = input("Please enter your own emotion: ")
            acceptable_emotion = True
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a number between 1 and 5.")

name2 = input("Please enter another name: ")

selected_relationships(relationship_sample, num)
print("5.) Other")

acceptable_relationship = False

while not acceptable_relationship:
    relationship = input(
        "Please enter a number corresponding to the relationship or select 'Other' to type in your own relationship: ")

    try:
        relationship_num = int(relationship)
        if relationship_num <= 4:
            relationship = relationship_sample[int(relationship) - 1]
            acceptable_relationship = True
        elif relationship_num == 5:
            relationship = input("Please enter your own relationship: ")
            acceptable_relationship = True
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a number between 1 and 5.")

selected_actions(actions_sample, num)
print("5.) Other")

acceptable_action = False

while not acceptable_action:
    action = input("Please enter a number corresponding to the action or select 'Other' to type in your own action: ")

    try:
        action_num = int(action)
        if action_num <= 4:
            action = actions_sample[int(action) - 1]
            acceptable_action = True
        elif action_num == 5:
            action = input("Please enter your own action: ")
            acceptable_action = True
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a number between 1 and 5.")

selected_writing(writings_sample, num)
print("5.) Other")

acceptable_writing = False

while not acceptable_writing:
    writing = input(
        "Please enter a number corresponding to the writing or select 'Other' to type in your own writing: ")

    try:
        writing_num = int(writing)
        if writing_num <= 4:
            writing = writings_sample[int(writing) - 1]
            acceptable_writing = True
        elif writing_num == 5:
            writing = input("Please enter your own writing: ")
            acceptable_writing = True
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a number between 1 and 5.")

# noinspection PyUnboundLocalVariable
script = f"{name} was a {job} and one day was feeling {emotion} because {name2} their {relationship} was {action}. " \
         f"since {name} was feeling {emotion} they decided to write a {writing} and this is how it read."

audio = generate(
    text=script,
    voice="Bella",
    model="eleven_monolingual_v1"
)
play(audio)



question = f"please write me a {writing} about {name} a {job} who is {emotion} because {name2} their {relationship} was {action}"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0,
    max_tokens=500,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

human_response = response["choices"][0]["text"]
print(human_response)
audio = generate(
    text=human_response,
    voice="Bella",
    model="eleven_monolingual_v1"
)
play(audio)