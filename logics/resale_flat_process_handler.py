from bs4 import BeautifulSoup
import requests
from helper_functions import llm

#Main Function 
def process_resale_flat_process_message(agentBool):
    if agentBool != None:
        url_link = ["https://ohmyhome.com/en-sg/blog/timeline-buying-hdb-resale-flat-hdb-resale-procedure",
                    "https://blog.seedly.sg/buy-a-hdb-resale-flat-without-an-agent/"]

        responseList = []
        for url in url_link:
            response = requests.get(url)
            responseList.append(response)

        soupList = []
        for response in responseList:        
            soup = BeautifulSoup(response.content, 'html.parser')
            soupList.append(soup)

        finaltext_list = []
        for soup in soupList:
            final_text = soup.text.replace('\n', '')
            finaltext_list.append(final_text)

        # This example shows the use of angled brackets <> as the delimiters
        prompt = f"""
        Buyer have made their decision delimited by triple backticks. 
        ```
        {agentBool}
        ```
        With the decision made above, summarize the articles which delimited by triple backticks and bring the potiential buyer through the resale flat process.
        The texts are scraped from different websites and parsed using `html.parser`:

        ```
        for finaltext in finaltext_list:
            {final_text}
        ```
        
        """
        response = llm.get_completion1(prompt)
        return response
    else :
        # This example shows the use of angled brackets <> as the delimiters
        prompt = f"""
        Write a short message to the buyer in a friendly way to seek for their help to answer the question above in one sentence.
        """
        response = llm.get_completion1(prompt)
        return response