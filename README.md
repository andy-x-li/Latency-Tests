# Latency-Tests

These programs record human visual/movement latency and cognitive latency. 

After a series of user inputs, these programs return to you a list of your reaction times in milliseconds. This list will outputed to the terminal. 

To run: <br>
> **1)** Install pygame (pip3 install pygame) and have Python 3.8 or higher <br>
> **2)** Run via cmd line (python3.8 **Button_Latency.py**) or (python3.8 **Word_Latency.py**)

**Button_Latency.py** changes from two states, respond and wait. It takes the first 30 responses, and outputs the latencies of all 30 responses in milliseconds. It can also calculate average response times. This program is used to measure visual latency (from eye to brain). 

**Word_Latency.py** generates 4 words from a list and the user must use the arrow keys to determine if the given word (written in green) is among those 4 words or not. Press the right arrow key if the green text is one of the 4 words. If not press the left arrow key. The program will take the first 10 correct answers and output the latencies of these answers in milliseconds. This program is used to measure cognitive latency (from eye to brain to movement). 

An example: 

![Word_Latency](https://github.com/andy-x-li/Latency-Tests/assets/125074849/6f0e2b13-09a3-4f2b-ba52-cbaea170583b)





