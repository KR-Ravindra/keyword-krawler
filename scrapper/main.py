import re
import requests
from collections import Counter
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, Text
from algorithms import rabin_karp, SuffixTree, SuffixArray, naive_string_matching, kmp_string_matching
import time

def preprocess_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

# Function to count word frequencies and display the top N words and execution time
def analyze_text(text, algorithm):
    start_time = time.time()
    text = preprocess_text(text)
    tokens = text.split()

    word_frequency = Counter(tokens)
    top_words = word_frequency.most_common(10)
    
    execution_time = time.time() - start_time
    return top_words, execution_time

# Function to perform the selected algorithm
def perform_analysis():
    input_text = text_entry.get("1.0", "end-1c")  # Read text from the text area
    selected_algorithm = algorithm_var.get()
    
    if selected_algorithm == "Rabin-Karp":
        top_words, execution_time = analyze_text(input_text, rabin_karp)
    elif selected_algorithm == "Suffix Tree":
        top_words, execution_time = analyze_text(input_text, SuffixTree)
    elif selected_algorithm == "Suffix Array":
        top_words, execution_time = analyze_text(input_text, SuffixArray)
    elif selected_algorithm == "Naive String Matching":
        top_words, execution_time = analyze_text(input_text, naive_string_matching)
    elif selected_algorithm == "KMP":
        top_words, execution_time = analyze_text(input_text, kmp_string_matching)
    
    # Clear previous results
    result_text.delete("1.0", "end")
    
    # Display top words and execution time
    result_text.insert("end", "Top 10 Words by Frequency:\n")
    for word, frequency in top_words:
        result_text.insert("end", f"{word}: {frequency}\n")
    result_text.insert("end", f"Execution Time: {execution_time:.5f} seconds")

# Create the main application window
root = Tk()
root.title("String Matching Algorithms")

# Label for algorithm selection
algorithm_label = Label(root, text="Select a string matching algorithm:")
algorithm_label.pack()

# Drop-down menu for algorithm selection
algorithms = ["Rabin-Karp", "Suffix Tree", "Suffix Array", "Naive String Matching", "KMP"]
algorithm_var = StringVar()
algorithm_var.set(algorithms[0])  # Default selection
algorithm_dropdown = OptionMenu(root, algorithm_var, *algorithms)
algorithm_dropdown.pack()

# Label and text area for text input
text_label = Label(root, text="Enter text or URL:")
text_label.pack()
text_entry = Text(root, height=5, width=40)
text_entry.pack()

# Button to perform the analysis
perform_button = Button(root, text="Perform Analysis", command=perform_analysis)
perform_button.pack()

# Text widget to display the results
result_text = Text(root, height=10, width=40)
result_text.pack()

if __name__ == "__main__":
    root.mainloop()
