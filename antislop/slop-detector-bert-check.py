import sys
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel

args = sys.argv
if len(args) <= 1:
    print(f"Usage: {args[0]} <inputfile>")
    print("Where <inputfile> is a UTF-8 plaintext document")
    sys.exit(1)

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
base_model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-cased", num_labels=2
)

model = PeftModel.from_pretrained(base_model, "gouwsxander/slop-detector-bert")

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer
)

try:
    with open(args[1], "r", encoding="utf-8") as f:
        text = f.read()
except UnicodeDecodeError:
    print("ERROR: File is not a valid UTF-8 text document.")
    sys.exit(1)
except FileNotFoundError:
    print("ERROR: File does not exist. Try again with a document that exists.")
    sys.exit(1)

inputs = text
results = classifier(inputs, truncation=True, max_length=512)

print(results)
