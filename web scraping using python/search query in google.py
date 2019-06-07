import webbrowser

query = input("enter your query:")
url ="https://www.google.com/?#q="
webbrowser.open_new(url+query)