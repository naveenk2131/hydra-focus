from pynput import keyboard, mouse
import time
import threading
from plyer import notification
import random
import atexit
from datetime import datetime
import tkinter as tk

last_activity = time.time()
FOCUS_THRESHOLD = 2 * 60  # 2 minutes for quick demo
last_reminder_time = None

def on_press(key):
    global last_activity
    last_activity = time.time()

def on_move(x, y):
    global last_activity
    last_activity = time.time()

keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_move=on_move)
keyboard_listener.start()
mouse_listener.start()

def get_fun_fact():
    try:
        with open("fun_facts.txt") as f:
            facts = f.readlines()
        return random.choice(facts).strip()
    except Exception:
        return "Stay hydrated, stay healthy!"

def log_reminder():
    global last_reminder_time
    last_reminder_time = time.strftime('%Y-%m-%d %H:%M:%S')
    with open("reminder_log.txt", "a") as f:
        f.write(f"Water break at {last_reminder_time}\n")
    update_gui()

def check_focus_and_remind():
    while True:
        now = time.time()
        if now - last_activity > FOCUS_THRESHOLD:
            fun_fact = get_fun_fact()
            notification.notify(
                title="💧 Drink Water Break!",
                message=f"You've been focused for 2 minutes. {fun_fact}",
                timeout=10
            )
            log_reminder()
            time.sleep(60)  # prevent repeat notification for 1 minute
        time.sleep(10)   # check every 10 seconds

def daily_summary():
    today = datetime.now().strftime('%Y-%m-%d')
    try:
        with open("reminder_log.txt") as f:
            reminders = [line for line in f if today in line]
        print(f"Total water reminders today: {len(reminders)}")
    except Exception:
        print("No reminders sent today.")

atexit.register(daily_summary)

# GUI setup
def update_gui():
    if last_reminder_time:
        status_label.config(text=f"Last reminder at:\n{last_reminder_time}")
    else:
        status_label.config(text="No reminders yet.")

def run_gui():
    global root, status_label
    root = tk.Tk()
    root.title("Water Reminder")
    root.geometry("300x150")
    root.resizable(False, False)

    label = tk.Label(root, text="Focus-based Water Reminder", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

    status_label = tk.Label(root, text="No reminders yet.", font=("Helvetica", 12))
    status_label.pack(pady=10)

    update_gui()

    root.mainloop()

reminder_thread = threading.Thread(target=check_focus_and_remind, daemon=True)
reminder_thread.start()

run_gui()
