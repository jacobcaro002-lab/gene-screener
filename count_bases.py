from tkinter import Tk, filedialog

def count_bases(dna):
    dna = dna.upper()
    counts = {"A": 0, "C": 0, "G": 0, "T": 0, "N": 0}
    for base in dna:
        if base in counts:
            counts[base] += 1
    return counts

def reverse_complement(dna):
    dna = dna.upper()
    pairs = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}
    result = ""
    for base in dna:
        if base in pairs:
            result += pairs[base]
        else:
            result += "N"
    return result[::-1]

# Pop up the file picker
root = Tk()
root.withdraw()                       # hide the blank main window
root.attributes("-topmost", True)     # keep the picker in front of VS Code
filename = filedialog.askopenfilename(
    title="Pick a DNA file",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)
root.destroy()

# If you hit Cancel, filename is empty, so stop nicely
if filename == "":
    print("No file selected.")
else:
    with open(filename) as file:
        dna = file.read()

    dna = dna.replace("\n", "").replace(" ", "")

    print("File:", filename)
    print("Top strand    (5' to 3'):", dna.upper())
    print("Bottom strand (5' to 3'):", reverse_complement(dna))
    print("Base counts:", count_bases(dna))