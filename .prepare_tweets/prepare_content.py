import os
import json
import cohere

# get api key from environment variable
key = os.environ.get("cohere")
co = cohere.Client(key)

with open("tweets.json", "r", encoding="utf-8") as infile:
    tweets_raw = json.load(infile)

# get text part from tweets
tweets = [tweet[2] for tweet in tweets_raw]

# load questions and answers from tweets
questions = [tweet[tweet.index(":")+1:tweet.index("?")+2].strip() for tweet in tweets if "Q" in tweet.split(":")[0][-3:]]
answers = [tweet[:tweet.index("#")].strip() for tweet in [tweet[tweet.index(":")+1:].strip() for tweet in tweets if "A" in tweet.split(":")[0][-3:]]]


if len(questions) > len(answers):
    questions = questions[1:]

content = []
for i in range(len(questions)):
    prompt = "Question: " + questions[i] + "\nAnswer: " + answers[i] + "\n\n\nTell me more:"

    tellmore = co.generate(
        model='large',
        prompt=prompt,
        max_tokens=80,
        temperature=0.0,
        presence_penalty=1.0)
    
    generated = tellmore.generations[0].text
    
    line = [questions[i].replace("\n", "")]
    line.append(answers[i].replace("\n", ""))
    line.append(generated[:generated.rindex(".")+1].strip().replace("\n", ""))
    content.append(line)

    # print(*line, sep="\n")

with open("content.json", "w", encoding="utf-8") as outfile:
    json.dump(content, outfile)

    """try:
        with st.expander(prompt[:"Answer:"-1]):
            st.write(prompt["Answer:":])
            generated = answer.generations[0].text
            try:
                st.write("*"+generated[:generated.rindex(".")+1].strip()+"*")
            except:
                st.write("Nothing to tell.")
    except:
        pass

"""