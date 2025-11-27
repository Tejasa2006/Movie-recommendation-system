
import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for PNG/JPG support
import os
import webbrowser  # To open a URL in a web browser

# Create the main window
root = tk.Tk()
root.title("Neutral Movie Posters")
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

folder_path = "poster/Neutral_poster"
image_files = get_image_files_from_folder(folder_path)
image_files = image_files[:12]  # Limit to 12 posters

# Movie names list
movie_names = [
    "NEUTRAL", "THE JOURNEY", "WALK ALONE", "ARGYLLE", "NORTH OF NORMAL", 
    "ONCE UPON a TIME HOLLYWOOD", "OFFICE SPACE", "ALADDIN", "MOON", "SPECTRE"
]

# URLs for posters
poster_urls = [
    "https://www.imdb.com/title/tt7448724/",
    "https://www.imdb.com/title/tt4826674/",
    "https://www.imdb.com/title/tt8408488/",
    "https://www.imdb.com/title/tt15009428/",
    "https://www.primevideo.com/detail/North-of-Normal/0TEBCV527ZNKNJQS1VFVEFURQ8",
    "https://www.imdb.com/title/tt7131622/?ref_=ls_i_2",
    "https://www.imdb.com/title/tt0151804/?ref_=ls_i_13",
    "https://www.hotstar.com/in/movies/aladdin/1260014815?utm_source=gwa",
    "https://www.primevideo.com/dp/amzn1.dv.gti.9eb32035-5af6-73de-295b-f683811f0a87?autoplay=0&ref_=atv_cf_strg_wb3",
    "https://www.primevideo.com/dp/amzn1.dv.gti.0ea9f534-b5ac-29af-c294-2945de2a7393?autoplay=0&ref_=atv_cf_strg_wb"
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
