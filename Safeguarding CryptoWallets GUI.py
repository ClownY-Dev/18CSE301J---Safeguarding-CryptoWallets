#BASIC GUI CODE WITH LINE BY LINE EXPLANATION

import tkinter as tk
from tkinter import messagebox

def show_intro():
    intro_text = """
    Welcome to the Safeguarding Cryptowallets App!\n
    This app provides information about the importance of safeguarding your crypto wallets.
    """
    info_label.config(text=intro_text)

def show_risks():
    risks_text = """
    Risks to consider when safeguarding cryptowallets:\n
    1. Human Error: Mistakes in handling wallet credentials can lead to unauthorized access.
    2. Technical Vulnerabilities: Poorly designed wallets or software can be exploited by hackers.
    3. Centralized Exchanges: Holding on exchanges exposes you to their security and regulatory risks.
    4. Hardware Failures: Hardware wallets can fail or be damaged.
    5. Regulatory Challenges: Legal uncertainties can affect wallet accessibility.
    6. Recovery Complexity: Losing credentials can complicate wallet recovery.
    """
    info_label.config(text=risks_text)

# Create the main window
root = tk.Tk()
root.title("Safeguarding Cryptowallets")

# Create a label
label = tk.Label(root, text="Safeguarding Cryptowallets App", padx=10, pady=10, font=("Helvetica", 16, "bold"))
label.pack()

# Create buttons to display different sections of information
intro_button = tk.Button(root, text="Introduction", command=show_intro)
intro_button.pack(pady=5)

risks_button = tk.Button(root, text="Risks", command=show_risks)
risks_button.pack(pady=5)

info_label = tk.Label(root, text="", wraplength=300, justify="left")
info_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
