from transformers import AutoModelForMaskedLM, AutoTokenizer, pipeline

SAVE_DIR = "./seyonec_chemberta"

model = AutoModelForMaskedLM.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")
tokenizer = AutoTokenizer.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")

fill_mask = pipeline('fill-mask', model=model, tokenizer=tokenizer)

tokenizer.save_pretrained(SAVE_DIR)
model.save_pretrained(SAVE_DIR)


