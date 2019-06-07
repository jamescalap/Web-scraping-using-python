import webbrowser
url = input('enter the full video path eq (https://www.youtube.com/watch?v=lrX6ktLg8WQ) ')#enter the url of the video to be opend
for i in range(1, 11): #this will open it for n number of times
    webbrowser.open_new(url)