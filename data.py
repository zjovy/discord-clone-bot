import pandas as pd
import json

from datasets import Dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import TrainingArguments, Trainer

with open('zuru.json', 'r', encoding='utf-8') as f: # open data file
    data = json.load(f)

df = pd.json_normalize(data['messages']) # create pandas dataframe for messages

# rename the fields for clarity
df.rename(
    columns={
        'id': 'message_id',
        'content': 'message_content',
        'author.id': 'author_id',
        'author.name': 'author_name',
        'timestamp': 'message_timestamp'
    },
    inplace=True
)

df = df[['message_id', 'message_content', 'author_id', 'author_name', 'message_timestamp']] # extract fields

print(df.head()) # visualize data

messages = df.to_dict(orient='records')

data_for_training = []
input_messages = []
output_messages = []
my_id = '160941753619185664' # get my author_id
current_author = None

# algorithm to parse the messages to get input/output
for message in messages:
    author = message['author_id']
    content = message['message_content']
    
    if author != current_author: # if author changes
        if current_author == my_id and input_messages: # if I am the author, generate input/output pair
            data_for_training.append({
                'input': ' '.join(input_messages),
                'output': ' '.join(output_messages)
            })
            input_messages = [] # clear messages
            output_messages = []
        
        current_author = author # update the current author
    
    # collect messages
    if author == my_id:
        output_messages.append(content)
    else:
        input_messages.append(content)

# put last pair into data
if output_messages and input_messages:
    data_for_training.append({
        'input': ' '.join(input_messages),
        'output': ' '.join(output_messages)
    })
    
# dataset = Dataset.from_pandas(pd.DataFrame(data_for_training))

# small_dataset = dataset.shuffle(seed=42).select(range(int(len(dataset) * 0.1)))

# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")
# tokenizer.pad_token = tokenizer.eos_token

# def tokenize_function(examples):
#     # Tokenize the inputs and outputs, and concatenate them with a special token
#     inputs_and_outputs = [inp + tokenizer.eos_token + out for inp, out in zip(examples['input'], examples['output'])]
#     tokenized_outputs = tokenizer(inputs_and_outputs, padding="max_length", truncation=True, max_length=512)
#     # GPT-2 uses the same tokenized input IDs as labels for language modeling
#     tokenized_outputs["labels"] = tokenized_outputs["input_ids"].copy()
#     return tokenized_outputs

# tokenized_dataset = dataset.map(tokenize_function, batched=True)

# tokenized_small_dataset = small_dataset.map(tokenize_function, batched=True)

# training_args = TrainingArguments(
#     output_dir="test_trainer",
#     per_device_train_batch_size=1,
#     per_device_eval_batch_size=1,
#     gradient_accumulation_steps=4
# )

# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=tokenized_small_dataset,
#     eval_dataset=None,
# )

# trainer.train()

# model.save_pretrained("./discord_clone")