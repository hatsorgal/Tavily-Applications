from tavily import TavilyClient






if __name__ == '__main__':
    tavily = TavilyClient(api_key="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")
    response = tavily.search(query="Should I invest in Tesla today?")

    context = [{"url": obj["url"], "content": obj["content"]} for obj in response["results"]]
    what = 0

