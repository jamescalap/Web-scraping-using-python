import webbrowser

query = input("enter your query:")
url = "https://www.youtube.com/results?search_query="
webbrowser.open_new(url+query)