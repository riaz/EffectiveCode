from tqdm.auto import tqdm

from datasets import load_dataset

# defining the dataloaders
from torch.utils.data import DataLoader
from accelerate import Accelerator
from transformers import AdamW, AutoModelForSequenceClassification, AutoTokenizer, get_scheduler, DataCollatorWithPadding

accelerator = Accelerator()

checkpoint = "bert-base-uncased"

BATCH_SIZE = 8

# loading the data

raw_datasets = load_dataset("glue", "mrpc")
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def tokenizer_func(data):
    return tokenizer(data["sentence1"], data["sentence2"], truncation=True)

tokenized_dataset = raw_datasets.map(tokenizer_func)
data_collator = DataCollatorWithPadding(tokenizer)

tokenized_dataset = tokenized_dataset.remove_columns(["sentence1", "sentence2", "idx"])
tokenized_dataset = tokenized_dataset.rename_columns({"label": "labels"})
tokenized_dataset.set_format("torch")


train_dataloader = DataLoader(tokenized_dataset["train"], shuffle=True, batch_size=BATCH_SIZE, collate_fn=data_collator)
eval_dataloader = DataLoader(tokenized_dataset["validation"], shuffle=True, batch_size=BATCH_SIZE, collate_fn=data_collator)


model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
optimizer = AdamW(model.parameters(), lr=3e-5)


train_dl, eval_dl, model, optimizer = accelerator.prepare(
    train_dataloader, eval_dataloader, model, optimizer
)


num_epochs = 3
num_training_steps = num_epochs * len(train_dl)
lr_scheduler = get_scheduler(
    "linear",
    optimizer=optimizer,
    num_warmup_steps=0,
    num_training_steps=num_training_steps,
)

progress_bar = tqdm(range(num_training_steps))

model.train()
for epoch in range(num_epochs):
    for batch in train_dl:
        outputs = model(**batch)
        loss = outputs.loss
        accelerator.backward(loss)

        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()
        progress_bar.update(1)