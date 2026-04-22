from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel

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

with open("inputText.txt", "r", encoding="utf-8") as f:
    text = f.read()

inputs = text
results = classifier(inputs, truncation=True, max_length=512)

print(results)
