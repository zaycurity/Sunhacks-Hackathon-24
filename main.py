from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"gui\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def run_image_recognition():
    # Use raw string (r"") or escape backslashes
    file_to_run = Path(r"ObjectRecognition\image1RT.py")
    
    try:
        # Open the file with subprocess (in this case, running a Python file)
        # The correct command is "python" followed by the file path
        subprocess.run(["python", file_to_run], check=True)
    except Exception as e:
        print(f"Error running file: {e}")

def run_face_detector():
    # Use raw string (r"") or escape backslashes
    file_to_run = Path(r"FaceRecongntion\faceDetect.py")
    
    try:
        # Open the file with subprocess (in this case, running a Python file)
        # The correct command is "python" followed by the file path
        subprocess.run(["python", file_to_run], check=True)
    except Exception as e:
        print(f"Error running file: {e}")


window = Tk()
window.geometry("1000x550")
window.title("Sunhacks Hackathon 24")
window.resizable(height = None, width = None)
window.configure(bg="#007878")

canvas = Canvas(
    window,
    bg="#007878",
    height=550,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load images and create canvas elements (unchanged)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(224.0, 140.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(500.0, 36.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(777.0, 140.0, image=image_image_3)

canvas.create_rectangle(25.0, 187.0, 425.0, 437.0, fill="#3CAEAE", outline="")


image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))

# Adjust the rectangle to match the image size (assuming image size is 200x150)

image_4 = canvas.create_image(
    220.0,  # Center X-coordinate of the new rectangle
    300.0,  # Center Y-coordinate of the new rectangle
    image=image_image_4
)
canvas.create_rectangle(580.0, 187.0, 980.0, 433.0, fill="#3CAEAE", outline="")

image_image_5 = PhotoImage(file=relative_to_assets("image_6.png"))

image_5 = canvas.create_image(
    785.0,
    300.0,
    image=image_image_5

)



# Adding a shadow to the title text by duplicating the text with an offset
canvas.create_text(
    320.0 + 2,  # X offset for shadow
    7.0 + 2,    # Y offset for shadow
    anchor="nw",
    text="Recognition App",
    fill="#000000",  # Shadow color (black)
    font=("Comic Sans MS", 48 * -1)
)

canvas.create_text(
    320.0,  # Original position for main text
    7.0,
    anchor="nw",
    text="Recognition App",
    fill="#FFFFFF",  # Main text color (white)
    font=("Comic Sans MS", 48 * -1)
)

# Adding shadow to subtitle
canvas.create_text(
    154.0 + 2,  # X offset for shadow
    132.0 + 2,  # Y offset for shadow
    anchor="nw",
    text="Face Detector App",
    fill="#000000",  # Shadow color (black)
    font=("Comic Sans MS", 15 * -1)
)

canvas.create_text(
    154.0,
    132.0,
    anchor="nw",
    text="Face Detector App",
    fill="#FFFFFF",  # Main text color (white)
    font=("Comic Sans MS", 15 * -1)
)

# Adding shadow to the second subtitle (on the right side above the rectangle)
canvas.create_text(
    700.0 + 2,  # X offset for shadow
    132.0 + 2,  # Y offset for shadow
    anchor="nw",
    text="Image Recognition App",
    fill="#000000",  # Shadow color (black)
    font=("Comic Sans MS", 15 * -1)
)

canvas.create_text(
    700.0,
    132.0,
    anchor="nw",
    text="Image Recognition App",
    fill="#FFFFFF",  # Main text color (white)
    font=("Comic Sans MS", 15 * -1)
)

# Adding shadow for text on the right rectangle (new shadow added)


# Rest of the code remains the same

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg="#007878",
    activebackground="#007878",
    command=run_face_detector,
    relief="flat"
)
button_1.place(x=144.0, y=444.0, width=160.0, height=50.0)

button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(image=button_image_hover_1)

def button_1_leave(e):
    button_1.config(image=button_image_1)

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)


button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg="#007878",
    activebackground="#007878",
    command=run_image_recognition,
    relief="flat"
)
button_2.place(x=723.0, y=444.0, width=160.0, height=50.0)

button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_2.png"))

def button_2_hover(e):
    button_2.config(image=button_image_hover_2)

def button_2_leave(e):
    button_2.config(image=button_image_2)

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)

window.resizable(False, True)
window.mainloop()
