import requests
import tkinter as tk
import threading
from ttkbootstrap import Style

def r():
    api_key = "991c7d2846690b9af47bd13cf7ba18736d4d0"

    url = entry.get()

    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    
    data = requests.get(api_url).json()["url"]
    
    if data["status"] == 7:
        shortened_url = data["shortLink"]
        shortUrl.delete("1.0","end")
        shortUrl.insert("1.0","Shortened Link: " + shortened_url)
    else:
        print("[!] Error Shortening URL:", data)


def req():
    thread = threading.Thread(target=r)
    thread.start()


root = tk.Tk()
root.title("URL Shortner by Ryan")
root.geometry("500x500")
root.style = Style(theme="darkly")

label = tk.Label(root, text="URL Shortner by Ryan", font=("Helvetica", 17))
label.pack(pady=5, padx=5)

frame = tk.Frame(root)
frame.pack(pady=5)

entryLabel = tk.Label(frame, text="Input the long URL here:", font=("Helvetica", 13))
entryLabel.pack(pady=1, padx=5)

entry = tk.Entry(frame, font=("Helvetica", 10), width=30)
entry.pack(pady=1, padx=5)

button = tk.Button(frame, text="Convert into Short URL", command=req, font=("Helvetica", 13))
button.pack(pady=10, padx=20)

shortUrl = tk.Text(frame, font=("Helvetica", 13))
shortUrl.insert("1.0","Please enter the Long Url and click the 'Convert into Short URL' button to retreieve the shortened URL.")
shortUrl.configure(state="disabled")
shortUrl.pack(pady=5)

root.mainloop()
