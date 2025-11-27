
import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for PNG/JPG support
import os
import webbrowser  # To open a URL in a web browser

# Create the main window
root = tk.Tk()
root.title("Happy Movie Posters")
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

folder_path = "poster/happy_poster"
image_files = get_image_files_from_folder(folder_path)
image_files = image_files[:12]  # Limit to 12 posters

# Movie names list
movie_names = [
    "GOOD NEWWZ", "MARNE BHI DO YAARON", "BABE BHANGRA PAUNDE NE", "HAPPY ENDiNG", "PHIR HERA PHERI", 
    "DADDY DAYCARE", "DAMO & IVOR", "ANDAZZ apna apna", "FUKREY", "POSTER BOYZ"
]

# URLs for posters
poster_urls = [
    "https://www.primevideo.com/detail/0TADXLVJKEHMYZ1SZS4DRS176C/ref=atv_sr_fle_c_Tn74RA_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B084633L13&qid=1737976970005",
    "https://www.primevideo.com/dp/amzn1.dv.gti.c51ef122-5546-476a-acd7-d09af62a497f?autoplay=0&ref_=atv_cf_strg_wb",
    "https://www.zee5.com/movies/details/babe-bhangra-paunde-ne/0-0-1z5277662",
    "https://www.primevideo.com/detail/0S3S4W0423KF5P7GB1YYRK15V6/ref=atv_sr_fle_c_Tn74RA_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B08JPN3FB4&qid=1737977180777",
    "https://www.primevideo.com/detail/0S2DU89DLBW41S0DZZZYAIH3WQ/ref=atv_sr_fle_c_Tn74RA_2_1_2?sr=1-2&pageTypeIdSource=ASIN&pageTypeId=B0B1VWR8N2&qid=1737977297358",
    "https://www.primevideo.com/detail/0N0E9X4IQ06XBID0695PGJ1RP6/ref=atv_sr_fle_c_Tn74RA_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B07527F9CK&qid=1737977535654",
    "https://www.rottentomatoes.com/m/damo_and_ivor_the_movie",
    "https://www.youtube.com/watch?v=ttCUfDtrYlU",
    "https://www.primevideo.com/detail/0KABXK1J44L6C7MKF5FD4DZGQ4/ref=atv_sr_fle_c_Tn74RA_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B01M5COJ2R&qid=1737977757300",
    "https://play.google.com/store/movies/details?id=PCjIODxyH3U"
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
