
import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for PNG/JPG support
import os
import webbrowser  # To open a URL in a web browser

# Create the main window
root = tk.Tk()
root.title("surprised Movie Posters")
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

folder_path = "poster/surprised_poster"
image_files = get_image_files_from_folder(folder_path)
image_files = image_files[:12]  # Limit to 12 posters

# Movie names list
movie_names = [
    "HAPPY BIRTHDAY", "SALTBURN", "MUNNA BHAI M.B.B.S", "A WEDNESDAY", "GET OUT",
    "DECISION TO LEAVE", "ARRIVAL", "COCO", "THE DECENT", "IDENTIFY"
]

# URLs for posters
poster_urls = [
    "https://www.netflix.com/search?q=happy%20bir&jbv=81551312",
    "https://www.primevideo.com/detail/Saltburn/0TI31ZT0BH50GS6FXUYQ7E46UG",
    "https://www.primevideo.com/dp/amzn1.dv.gti.0eb620e0-09e4-053f-0dbe-9e498c8a1017?autoplay=0&ref_=atv_cf_strg_wb",
    "https://www.netflix.com/search?q=a%20wednesday&jbv=70107499",
    "https://www.primevideo.com/dp/amzn1.dv.gti.34ad9d89-2a6b-11a1-c5c3-27569d5ee969?autoplay=0&ref_=atv_cf_strg_wb",
    "https://www.primevideo.com/detail/0I4S8QWVGR7074JRD0WYSH28LD/ref=atv_sr_fle_c_Tn74RA_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0D9KQ98QN&qid=1738144825554",
    "https://www.primevideo.com/dp/amzn1.dv.gti.2a7ec332-a69e-45e4-8827-88b4c24d577e?autoplay=0&ref_=atv_cf_strg_wb",
    "https://www.hotstar.com/in/movies/coco-singalong/1260103804?utm_source=gwa",
    "https://www.primevideo.com/detail/The-Descent/0PZ1U97T5LLNK9AAN7SPNT19CB",
    "https://www.primevideo.com/dp/amzn1.dv.gti.8ea9f65c-33fe-d30b-414e-b2b3eef089f1?autoplay=0&ref_=atv_cf_strg_wb"
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
