import pyautogui
import time
import tkinter as tk

root = tk.Tk()
root.title("chatgpt automation")
root.geometry("100x300")

# Default colors
bg_color = "#2e2e2e"
fg_color = "#f5f5f5"
light_bg = "#f5f5f5"
light_fg = "#2e2e2e"

root.configure(bg=bg_color)

# Default prompt and delays
user_prompt = "Explain what Python is in 10 sentences"
delay_edge = 1        # delay before locating Edge
delay_after_edge = 1  # delay after clicking Edge
delay_chat_load = 2   # delay after opening ChatGPT
delay_response = 8    # wait for response
delay_notepad = 2     # delay before pasting in Notepad

def fetch_chatgpt_response(prompt: str):
    """opent ms edge zoekt chatgpt op vraagt wat python is in 10 zinnen sluit ms edge opent notepad plakt alles in die chatgpt zei"""
    
    # Open Edge
    time.sleep(delay_edge)
    msedge = pyautogui.locateOnScreen("images/msedge.png", confidence=0.8)
    if msedge:
        pyautogui.click(pyautogui.center(msedge))
    else:
        print("MS Edge not found!")
        return
    
    time.sleep(delay_after_edge)
    
    # Go to ChatGPT
    pyautogui.write("chatgpt.com", interval=0)
    pyautogui.press("enter")
    time.sleep(delay_chat_load)
    
    # Type the prompt and submit
    pyautogui.write(prompt, interval=0)
    pyautogui.press("enter")
    time.sleep(delay_response)  # wait for response
    
    # Copy the response
    copy_btn = pyautogui.locateOnScreen("images/copy.png", confidence=0.8)
    if copy_btn:
        pyautogui.click(pyautogui.center(copy_btn))
        print("Found the copy button")
    else:
        print("Copy button not found!")
        return
    
    time.sleep(1)
    
    # Close Edge
    pyautogui.hotkey("alt", "f4")
    time.sleep(1)
    
    # Open Notepad
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write("notepad")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(delay_notepad)
    
    # New file & paste
    pyautogui.hotkey("ctrl", "n")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    
    print("Done!")

# Update colors function
def update_colors(dark_mode: bool):
    global bg_color, fg_color
    if dark_mode:
        bg_color = "#2e2e2e"
        fg_color = "#f5f5f5"
    else:
        bg_color = "#f5f5f5"
        fg_color = "#2e2e2e"
    root.configure(bg=bg_color)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
            widget.configure(bg=bg_color, fg=fg_color)

# Start button
button1 = tk.Button(root, text="Start", command=lambda: fetch_chatgpt_response(user_prompt),
                    bg=bg_color, fg=fg_color)
button1.pack(pady=20)

# Info button
def show_info():
    info_window = tk.Toplevel(root)
    info_window.title("Info")
    info_window.geometry("400x200")
    info_window.configure(bg=bg_color)
    msg = tk.Label(info_window, text="If your computer is slower, consider increasing the time.sleep() delays in the script. If that doesn't work consider trying again as pyautogui can sometimes miss the images if that does not work consider emailing me at arjen8760@gmail.com or send a text message at +32 491722694 data charges may apply", wraplength=350, bg=bg_color, fg=fg_color)
    msg.pack(padx=20, pady=20)

info_button = tk.Button(root, text="Info", command=show_info, bg=bg_color, fg=fg_color)
info_button.pack(pady=10)




# Settings button with prompt, dark mode, and advanced delay adjustments
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x500")
    settings_window.configure(bg=bg_color)
    
    # Prompt input
    prompt_label = tk.Label(settings_window, text="Prompt:", bg=bg_color, fg=fg_color)
    prompt_label.pack(pady=(20,5))
    prompt_entry = tk.Entry(settings_window, width=40)
    prompt_entry.pack(pady=5)
    
    # Dark mode switch
    dark_mode_var = tk.BooleanVar(value=True)
    def toggle_dark_mode():
        update_colors(dark_mode_var.get())
    
    dark_mode_check = tk.Checkbutton(settings_window, text="Dark Mode", variable=dark_mode_var,
                                     command=toggle_dark_mode, bg=bg_color, fg=fg_color, selectcolor=bg_color)
    dark_mode_check.pack(pady=10)
    
    # Advanced delays section
    adv_label = tk.Label(settings_window, text="Advanced (Adjust Delays - user only)", bg=bg_color, fg=fg_color)
    adv_label.pack(pady=(20,5))
    
    # Edge delay
    edge_label = tk.Label(settings_window, text="Edge Delay:", bg=bg_color, fg=fg_color)
    edge_label.pack()
    edge_entry = tk.Entry(settings_window, width=10)
    edge_entry.insert(0, str(delay_edge))
    edge_entry.pack(pady=2)
    
    # ChatGPT load delay
    chat_label = tk.Label(settings_window, text="ChatGPT Load Delay:", bg=bg_color, fg=fg_color)
    chat_label.pack()
    chat_entry = tk.Entry(settings_window, width=10)
    chat_entry.insert(0, str(delay_chat_load))
    chat_entry.pack(pady=2)
    
    # Response wait delay
    resp_label = tk.Label(settings_window, text="Response Delay:", bg=bg_color, fg=fg_color)
    resp_label.pack()
    resp_entry = tk.Entry(settings_window, width=10)
    resp_entry.insert(0, str(delay_response))
    resp_entry.pack(pady=2)
    
    # Notepad delay
    note_label = tk.Label(settings_window, text="Notepad Delay:", bg=bg_color, fg=fg_color)
    note_label.pack()
    note_entry = tk.Entry(settings_window, width=10)
    note_entry.insert(0, str(delay_notepad))
    note_entry.pack(pady=2)
    
    # Save button
    def save_settings():
        global user_prompt, delay_edge, delay_chat_load, delay_response, delay_notepad
        user_prompt = prompt_entry.get()
        try:
            delay_edge = float(edge_entry.get())
            delay_chat_load = float(chat_entry.get())
            delay_response = float(resp_entry.get())
            delay_notepad = float(note_entry.get())
        except ValueError:
            print("Invalid delay input, using previous values")
        print(f"Prompt set to: {user_prompt}")
        settings_window.destroy()
    
    save_button = tk.Button(settings_window, text="Save", command=save_settings, bg=bg_color, fg=fg_color)
    save_button.pack(pady=10)

settings_button = tk.Button(root, text="Settings", command=open_settings, bg=bg_color, fg=fg_color)
settings_button.pack(pady=10)
#stop button
stop_button = tk.Button(root, text="Stop", command=root.destroy, bg=bg_color, fg=fg_color)
stop_button.pack(pady=10)

root.mainloop()
