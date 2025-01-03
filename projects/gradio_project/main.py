import gradio as gr
import numpy as np
from transformers import pipeline
import random
import time
pipe = pipeline("translation", model="t5-base")
dslgames = [1, 2, 3]
dsl_game_state = 0
got_wrong = 0

def translate(text):
    return pipe(text)[0]["translation_text"]

def chat(message, history):
    global dsl_game_state, got_wrong

    history = history or []
    message = message.lower()
    if message.startswith("how many"):
        response = str(random.randint(1, 100))
    elif message.startswith("how are you"):
        response = random.choice(["Great", "Good", "Okay", "Bad"])
    elif message.startswith("where"):
        response = random.choice(["DSL_HQ", "DSL10git.github.io","One of DSL_games", "Sleeping on your message😴💤", "DSLChat"])
    elif message == "help":
        response = "Go to help on the top!"
    elif message.startswith("hello"):
        response = random.choice(["Hi, how may I assist you?"])
    elif message == "dslgames" or dsl_game_state in dslgames:
        if dsl_game_state == 0:
            response = random.choice(["Let's play math game. "])
            response += random.choice(["what is 2+0?", "what is 2x1?", "what is 8÷4?", "what is 8-6?"])
            dsl_game_state += 1
        elif dsl_game_state == 1:
            if message == "2" or message == 2:
                response = "Right! "
            else:
                response = "Wrong! "
                got_wrong += 1
            response += random.choice(["what is 8+8?", "what is 8x2?", "what is 32÷2?", "what is 100-84?"])
            dsl_game_state += 1
        elif dsl_game_state == 2:
            if message == "16" or  message == 16:
                response = "Right! "
            else:
                response = "Wrong! "
                got_wrong += 1
            response += random.choice(["what is 66+33?", "what is 3x13?", "what is 277÷3?", "what is 109-10?"])
            dsl_game_state += 1
        elif dsl_game_state == 3:
            if message == "99" or  message == 99:
                response = "Right! "
            else:
                response = "Wrong! "
                got_wrong += 1

            response += f"You got {got_wrong} wrong\n"
            if got_wrong == 0 or got_wrong == "0":
                response += "You got a perfect score! Great Job"
            elif got_wrong == 1 or got_wrong == "1":
                response += "Still good!"
            elif got_wrong == 2 or got_wrong == "2":
                response += "pracice every day!"
            else:
                response += "It's okay"
            dsl_game_state = 0
            got_wrong = 0
        time.sleep(1.0)
    else:
        response = "I can't understand! Go to help on the top learn what I can do!"
    history.append((message, response))
    return history, history

def help(message):
    if message == "help":
        return "Hello, scroll down to get a greet and more stuff! Speech to text isn't working. At simple Chatbot, if the sentence starts with how many, it will give you a number from 1 - 100! If the sentence starts with how are you, it will say Great, bad, or ect. If the sentence starts with where, it will tell you some where it is in dsl(dsl10git.github.io, dsl games, and ect). If the sentence starts with 'hello' it will say Hi, how may I assit you? If you type 'DSLGames' it will give a math game, It's very easy"
    else:
        return "type help to get help"

def greet(greet):
    return "Hello " + greet + "!"
def advance_greet_and_basic_temperature(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, f"{round(celsius, 2)}°C (Converted fahrenheit to celsius)"
def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    print(input_img.shape, sepia_img.shape)
    return sepia_img
def speech_to_text(name):
    return "ERROR 666(not added) ˙´¬π µ´, ®¨˜™£¢∞§¶•ªºª•¶§∞¢£´®ƒ©˙∆˚®ˆ∑¥ß¨∆∂˚ƒ®ˆ´¨ß∆∂˚ç√¬©˚ƒ∆˙"
with gr.Blocks() as demo:
    title = gr.HTML("""
    <h1 style="text-align:center">DSLChat</h1>
    
                    """)
    gr.Markdown("## Help")
    demo1 = gr.Interface(fn=help, inputs=gr.Textbox(lines=2, placeholder="Type help for help"), outputs="text")
    gr.Markdown("## Simple greeting")
    demo2 = gr.Interface(fn=greet, inputs=gr.Textbox(lines=2, placeholder="Name here"), outputs="text")
    gr.Markdown("## Better Greeting and added temperature")
    demo3 = gr.Interface(fn=advance_greet_and_basic_temperature, inputs=["text", "checkbox", gr.Slider(-20, 100)], outputs=["text", "text"])
    gr.Markdown("## Sepia Filter")
    demo4 = gr.Interface(sepia, gr.Image(height=200, width=200), "image")
    gr.Markdown("## Speech To Text")
    demo5 = gr.Interface(fn=speech_to_text, inputs=gr.Audio(label="Audio file"), outputs=gr.Text())
    with gr.Column():
        gr.Markdown("## Translator")
        english = gr.Textbox(label="English text")
        translate_btn = gr.Button(value="Translate")
    with gr.Column():
        german = gr.Textbox(label="German text")
    examples = gr.Examples(examples=["I broke my arm.", "My mom drived to the store on the blue market street around 3:00 pm and bought an apple, banana, pear, meat, jam, and bread and paid 30000$.", "where is the apple in my car?"], inputs=[english])
    translate_btn.click(translate, inputs=english, outputs=german)
    gr.Markdown("## Simple Chatbot")
    chatbot = gr.Chatbot()
    demo6 = gr.Interface(
        chat,
        ["text", "state"],
        [chatbot, "state"],
        allow_flagging="never",
    )
demo.launch(server_name="0.0.0.0", debug=True)
