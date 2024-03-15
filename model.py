from llama import BasicModelRunner
from lamini import Lamini

from data import data_for_training

model = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf") # import pre-trainined model

clone = model.train(data_for_training) # fine-tune model