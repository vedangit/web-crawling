import tkinter as tk
from tkinter import ttk, messagebox
from threading import Thread
import requests
from bs4 import BeautifulSoup
from collections import deque

class WebCrawlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Crawler")
        
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.header_label = ttk.Label(root, text="Web Crawler", font=("Helvetica", 18), background="#f0f0f0")
        self.header_label.pack(pady=15)

        self.start_label = ttk.Label(root, text="Starting URL:", font=("Helvetica", 12), background="#f0f0f0")
        self.start_label.pack()

        self.start_url_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.start_url_entry.pack(pady=5)

        self.max_pages_label = ttk.Label(root, text="Max Pages:", font=("Helvetica", 12), background="#f0f0f0")
        self.max_pages_label.pack()

        self.max_pages_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.max_pages_entry.pack(pady=5)

        self.start_button = ttk.Button(root, text="Start Crawling", command=self.start_crawling)
        self.start_button.pack(pady=15)

    def start_crawling(self):
        start_url = self.start_url_entry.get()
        max_pages = int(self.max_pages_entry.get())
        self.crawl_thread = Thread(target=self.bfs_web_crawler, args=(start_url, max_pages))
        self.crawl_thread.start()

    def bfs_web_crawler(self, start_url, max_pages):
        visited = set()
        queue = deque([(start_url, 0)])  # Queue of (url, depth) tuples
        crawled_pages = []

        while queue and len(crawled_pages) < max_pages:
            url, depth = queue.popleft()
            if url not in visited:
                visited.add(url)
                response = requests.get(url)
                if response.status_code == 200:
                    crawled_pages.append(url)
                    print(f"Crawled: {url} (Depth: {depth})")

                    
                    #Using BeautifulSoup to parse the HTML content of the current URL and extract all anchor (<a>) elements with an href attribute.
                    # For each extracted link, check if it starts with "http" and has not been visited before. If both conditions are met, enqueue the link into the queue with an incremented depth.
                    soup = BeautifulSoup(response.text, 'html.parser')
                    links = [link.get('href') for link in soup.find_all('a', href=True)]
                    for link in links:
                        if link.startswith("http") and link not in visited:
                            queue.append((link, depth + 1))

        messagebox.showinfo("Crawling Complete", f"Crawled {len(crawled_pages)} pages.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebCrawlerApp(root)
    root.mainloop()
