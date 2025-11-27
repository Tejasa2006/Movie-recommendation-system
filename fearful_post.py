
import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for PNG/JPG support
import os
import webbrowser  # To open a URL in a web browser

# Create the main window
root = tk.Tk()
root.title("FEARFUL Movie Posters")
root.geometry("1200x800")  # Adjusted size
root.configure(bg="black")

# Function to create a movie poster
def create_poster(parent, title, image_path, tagline, release_date, credits, image_file_path, url):
    frame = tk.Frame(parent, bg="black", padx=5, pady=10)

    # Title
    title_label = tk.Label(frame, text=title, font=("Helvetica", 14, "bold"), fg="yellow", bg="black")
    title_label.pack(pady=5)

  # Function to get the poster image files from a folder
    try:
        image = Image.open(image_path)
        image = image.resize((150, 250))  # Resize the image to fit the screen width
        poster_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=poster_image, bg="black")
        image_label.image = poster_image  # Keep a reference to avoid garbage collection
        image_label.pack(pady=5)
        
        # Bind click event on the image label to the open_webpage function
        image_label.bind("<Button-1>", lambda event, url=url: open_webpage(url))
        
    except Exception as e:
        print(f"Error loading image: {e}")
        placeholder_label = tk.Label(
            frame, text="Image\n(Placeholder)", font=("Helvetica", 12), fg="white", bg="black"
        )
        placeholder_label.pack(pady=5)

    return frame

  # Poster Image using Pillow (supports PNG and JPG)
def get_image_files_from_folder(folder_path):
    allowed_formats = ('.jpg', '.jpeg', '.png')
    return [f for f in os.listdir(folder_path) if f.lower().endswith(allowed_formats)]

# Function to open the webpage
def open_webpage(url):
    webbrowser.open(url)  # Opens the URL in the default web browser

folder_path = "poster/fearful_poster"
image_files = get_image_files_from_folder(folder_path)
image_files = image_files[:12]  # Limit to 12 posters

# Movie names list
movie_names = [
    "FEAR STREET", "DARK", "THE LEARKING FEAR", "JAWS", "THE EXORCIST",
    "THE SHINING", "HEREDITARY", "THE BABADOOK", "THE CONJURING", 
]

# URLs for posters
poster_urls = [
    "https://www.netflix.com/search?q=fear%20street&jbv=81325689",
    "https://www.netflix.com/search?q=dark%20&jbv=80100172",
    "https://www.youtube.com/watch?v=TuUGFnmfj4k",
    "https://www.jiocinema.com/movies/jaws/3759053/watch?utm_source=WatchAction&utm_medium=MovieWatchAction&utm_campaign=jaws",
    "https://www.primevideo.com/detail/The-Exorcist/0IZ2N9EUUJDP66QBK1ELVZJQQC",
    "https://www.primevideo.com/dp/amzn1.dv.gti.1cff3851-755c-43ed-9423-4cc6b5c20ba6?autoplay=0&ref_=atv_cf_strg_wb",
    "https://www.primevideo.com/detail/0T65HGH8XLZN0612MUMF3JQ2RO/ref=atv_sr_fle_c_Tn74RA_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B08R6952FP&qid=1738146298834",
    "https://www.primevideo.com/dp/amzn1.dv.gti.9cb980f2-5a05-dcfe-1fdf-3ef88135b58d?autoplay=0&ref_=atv_cf_strg_wb",
    "https://www.netflix.com/search?q=con&jbv=70251894",
  
]

posters = []
for index, image_file in enumerate(image_files):
    if index < len(movie_names) and index < len(poster_urls):
        posters.append({
            "title": movie_names[index],
            "image_path": os.path.join(folder_path, image_file),
            "tagline": f"An exciting journey - {movie_names[index]}",
            "release_date": f"202{index}",
            "credits": f"Directed by Director {index + 1}\nStarring Actor {index + 1}, Actress {index + 1}",
            "image_file_path": os.path.join(folder_path, image_file),
            "url": poster_urls[index]
        })

poster_frame = tk.Frame(root, bg="black")
poster_frame.pack(expand=True, fill="both", padx=20, pady=20)

for index, poster in enumerate(posters):
    frame = create_poster(poster_frame, **poster)
    row = index // 5
    column = index % 5
    frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

root.mainloop()
