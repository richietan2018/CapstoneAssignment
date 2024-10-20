# Common imports
import os
import requests
from helper_functions import llm

# Import the key CrewAI classes
from crewai import Agent, Task, Crew
import crew

# import other necessary packages you need
from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
)

def get_requirements_recommendations(input, url):
    if input != "":
        tool_webscrape = ScrapeWebsiteTool()

        # Specify the path
        file_path = './data/dreamHouse.txt'
        # Open file and delete the existsing content
        with open(file_path, 'w') as file:
            # Write the new content into the file
            file.write(input)

        tool_buyer_requirements = FileReadTool(file_path='./data/dreamHouse.txt')

        final_reco = ""

        #AGENT
        # Agent 1: HomeResearchAgent
        homeResearchAgent = Agent(
            role="Home Research Agent",
            goal="Do an great analysis on "
                "the housing to help buyer to get their ideal house",
            tools=[tool_webscrape],
            verbose=True,
            backstory="""\
                    As Home Research Agent, your are required to extracting critical information from the home listing.
                    Your skills help pinpoint the necessary housing requirements and match with the buyer requirments and provide effective recommendation."""
        )

        # Agent 2: Profiler
        buyerDreamAgent = Agent(
            role="Buyer Dream Agent",
            goal="Do an incredible match on house available with the requirements given",
            tools=[tool_buyer_requirements],
            verbose=True,
            backstory=("""\
                    Equipped with analytical prowess, you use the requirements given and find other information that will be helpful for the choosing of houses."""
            )
        )

        # Agent 3: Housing Agent
        housing_agent = Agent(
            role="Housing Agent",
            goal="Find the best ways to give the recommedations.",
            tools=[tool_webscrape, tool_buyer_requirements],
            verbose=True,
            backstory=("""\
                    With a detailed and outsmart and careful mind, you refine and select housing that matches the requirements by the buyer."""
            )
        )

        #TASK
        # Task for Home Research Agent: Extract House Information
        research_task = Task(
            description="""/
                Analyze the house posting URL provided ({housing_listing_url}) to extract key requirements such as town/area, room flat type, nearby ammenities and housing years left. 
                Use the tools to gather content and identify and categorize the requirements.""",
            expected_output="A structured list of information, including town/area, room flat type, nearby ammenities and housing years left",
            agent=homeResearchAgent,
            async_execution=True
        )

        # Task for Buyer Dream Agent : Compile Comprehensive Profile
        buyer_dream_task = Task(
            description="""\
                Compile a detailed information such as what kind of housing buyer is looking for based on the requirements given.
                Utilize tools to extract and synthesize information from the buyer input.""",
            expected_output="A comprehensive document that includes the requirements.",
            agent=buyerDreamAgent,
            async_execution=True
        )

        
        # Task for Resume Strategy Task: Align Dream House with Housing Available.
        resume_strategy_task = Task(
            description="""\
                Using the input by the buyer and housing details gathered from previous tasks, produce if is viable for user selection 
                Show the relevant details if it matches and give information such as the town/area, room flat type, nearby ammenities and housing years left.
                Tell the buyer why buy this house and why it is the dreamhouse.""",
            expected_output=
                "An output that return if he/she should buyer the house and reason why it matches it dream house. The output should give a grading out of 5 stars on if the house matches the buyer dream house. ",
            
            #output_file="tailored_resume.md",
            
            context=[research_task, buyer_dream_task],
            agent=housing_agent
        )

        crew = Crew(
        agents=[homeResearchAgent,
                buyerDreamAgent,
                housing_agent],

        tasks=[research_task,
            buyer_dream_task,
            resume_strategy_task],

        verbose=True
        )

        housing_listing_inputs = {
            #Use Propnex Site eg. https://www.propnex.com/listing-details/576918/270a-sengkang-central
        'housing_listing_url': url,
    }


        ### this execution will take a few minutes to run
        result = crew.kickoff(inputs=housing_listing_inputs)
        rawResults = result.raw
        homeResearchAgentReplies = result.tasks_output[0]
        buyerDreamAgentReplies = result.tasks_output[1]
        housing_agentReplies = result.tasks_output[2]
        return rawResults,homeResearchAgentReplies, buyerDreamAgentReplies, housing_agentReplies