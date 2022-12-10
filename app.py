import streamlit as st
import cohere
import os
import time

key = os.environ.get("cohere")
co = cohere.Client(key)

prompt = st.text_area('Text to summarize', '''COVID-19 related thrombosis does not appear to be limited to the venous circulation. A single-center cohort study found significantly increased rates of acute limb ischemia in patients with COVID-19 (16.3%) from January 2020 to March 2020, compared to patients without COVID-19 (1.8%) presenting from January 2019 to March 2019.38 Generally, young age and female gender are risk factors associated with hypercoagulable disorders, however, in patients with COVID-19, native arterial occlusions were observed in both younger and older individuals, and more often in males.38 Additionally, the macroscopic appearance of thrombosis specimens in these patients was quite different than pre-COVID-19 specimens, as they were much more gelatinous and longer than typical thrombi, an observed hallmark of COVID-19 thrombi.38 Both observations suggest that the increased rates of acute limb ischemia are likely not related to well-known hypercoagulability disorders, but due to COVID-19 infection. Coronary thrombosis also has been reported in patients with COVID-19.39 Coronary angiography in this particular case revealed multivessel thrombotic stenosis believed to be in situ thrombosis, since no significant atheroma was found and thrombus of the left anterior descending was non-occlusive (60%) making a coronary embolus unlikely.39 These findings imply a COVID-19 coagulopathy as the cause of thrombosis and provide further evidence that thrombotic complications of COVID-19 are not limited to the venous vasculature.''')

max_tokens = st.sidebar.slider("Tokens", min_value=10, max_value=100, value=10, step=10)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

response = co.generate( 
    model='xlarge', 
    prompt = prompt,
    max_tokens=max_tokens, 
    temperature=temperature,
    stop_sequences=["--"])

summary = response.generations[0].text
summary = summary[:summary.rindex(".")+1] # remove incomplete sentence at the end

st.write(summary)

# https://stackoverflow.com/questions/21470318/python-code-output-to-a-file-and-add-timestamp-to-filename
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)

# with open(f"../summary-{timestamp}.txt", "w", encoding="utf-8") as outfile:
#    outfile.write(summary)"""