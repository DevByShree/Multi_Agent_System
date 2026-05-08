from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:

    state = {}

    # step 1 search agent working
    print("\n" + "=" * 50)
    print("Step 1 - search agent is working....")
    print("=" * 50)

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            ("user", f"Find recent, reliable and detailed information about: {topic}")
        ]
    })

    state["search_results"] = search_result['messages'][-1].content

    print("\nsearch result:", state['search_results'])

    # step2 Reader agent
    print("\n" + "=" * 50)
    print("Step 2 - Reader agent is scraping top resources....")
    print("=" * 50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({

        "messages": [(
            "user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:100]}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\nScraped Content:\n",state['scraped_content'])

    #step3
    print("\n" + "=" * 50)
    print("Step 3 - Writer is drafting the report...")
    print("=" * 50) 

    #lets combine  result agen1 + agent 2 so agent 1 is for not deep research but it will research little bit and provide links and  the agent 2 is for deep research 

    research_combined=(
        f"SEARCH RESULTS : \n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"]=writer_chain.invoke({
        "topic":topic,
        "research":research_combined
    })

    print("\n Final Report\n",state['report']) 

    #critic report
    print("\n" + "=" * 50)
    print("Step 4 - Critic is reviewing the report")
    print("=" * 50) 

    # state["feedback"] = critic_chain.invoke({
    #     "report": state['report']
    #     })

    # print("\n critic report \n",state['feedback'])

    return state


if __name__=="__main__":
    topic = input("\n Enter a research topic :")
    run_research_pipeline(topic)