import pyttsx3

def shoutout_with_speaker(names):
    engine = pyttsx3.init()

    for name in names:
        engine.say(f"Shoutout to {name}!")
        engine.runAndWait()

# Example usage:
names_list = ["Alice", "Bob", "Charlie", "David"]
shoutout_with_speaker(names_list)
