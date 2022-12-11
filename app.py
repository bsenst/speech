import json
import requests
import streamlit as st
import streamlit.components.v1 as components

# https://discuss.streamlit.io/t/displaying-multiple-tweets-on-streamlit/25650
# https://discuss.streamlit.io/t/dispalying-a-tweet/16061/2
class Tweet(object):
    def __init__(self, s, embed_str=False):
        if not embed_str:
            # Use Twitter's oEmbed API
            # https://dev.twitter.com/web/embedded-tweets
            api = "https://publish.twitter.com/oembed?url={}".format(s)
            response = requests.get(api, timeout=5)
            self.text = response.json()["html"]
        else:
            self.text = s

    def _repr_html_(self):
        return self.text

    def component(self):
        return components.html(self.text, height=300)

st.header("Know more about the last Q&A Session")

# make dynamic - not static url
col1, col2, col3 = st.columns([1,6,1])
with col1: st.write("")
with col2: t = Tweet("https://twitter.com/knowmedge/status/1601627902054871040").component()
with col3: st.write("")

st.caption("Questions and Answers are publically available on Twitter. Copyrights by @Knowmedge. Additional content automatically generated using the cohere.ai API.")

if st.button("Tell me more about the last Q&A Session"):
    # load tellmore json
    with open("content.json", "r", encoding="utf-8") as infile:
        content = json.load(infile)
    
    for entry in content:
        with st.expander(entry[0]):
            st.write("**"+entry[1]+"**")
            st.write("Tell me more:")
            st.write("*"+entry[2].replace("\n", " ")+"*")

with st.expander("Question: A cocaine user has a weak handshake. These buzz words are clues to what rheumatological condition? "):
    st.write("**Answer: Inclusion body myositis**")
    st.write("Tell me more:")
    st.write("*Inclusion body myositis (IBM) is a rare inflammatory muscle disease characterized by slowly progressive weakness and wasting of both distal and proximal muscles, most apparent in the muscles of the arms and legs. IBM is one of a group of muscle diseases known as the inflammatory myopathies, which are characterized by chronic, progressive muscle inflammation accompanied by muscle weakness.*")

# add link to github repo
st.markdown("[github.com/bsenst/speech](https://github.com/bsenst/speech)")