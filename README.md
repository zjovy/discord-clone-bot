# Discord Clone Bot

**Final Project for CS 396 Computational Linguistics by Jovy Zhou**

The project initially aimed to fine-tune a pre-trained Large Language Model (LLM), such as Meta's Llama 2, with my Discord messages to mimic my online presence. Due to training challenges and time constraints, the project's scope was adjusted to explore various topics.

## Overview

This project comprises three main parts:

1. **Learning and Data Preparation**
    - Explored fine-tuning LLM steps via the DeepLearning.AI tutorial.
    - Downloaded Discord data for training, preparing it as described in `data.py`.

2. **Training Attempts**
    - Attempted LLM training with the Lamini API and locally in `data.py` and `model.py`.
    - Explored high-level training options due to resource and time limitations.

3. **Mock Discord LLM Bots**
    - Developed two mock bots: one with my data and another using the OpenAI API.

### Part 1: Data Preparation (`data.py`)

Downloaded direct messages using DiscordChatExporter, in `zuru.json`. The dataset spans multiple years, providing a substantial amount of data. The data was formatted into input/output pairs, mimicking typical training data for language models.

### Part 2: Training (Lamini API and local attempts)

Training attempts included using models like EleutherAI/pythia-70m and gpt2, both requiring extensive training time due to hardware limitations. The Lamini API offered a simpler training option but was costly and ultimately abandoned due to unsatisfactory results.

### Part 3: Mock Bots (`mock_bot.py` and `gpt_bot.py`)

- **Mock Bot**: A bot that responds with randomly selected messages from a list matching the user's input.
- **GPT Bot**: Integrates GPT-3.5-turbo using OpenAI's API, attempting to mimic a specific online persona through prompt engineering.

## Summary and Future Plans

The project offered significant learning opportunities about LLMs and their fine-tuning. Despite the challenges, it laid the groundwork for future exploration in creating more sophisticated models and bots. Future plans include:

- Using better data and more robust cloud services for training.
- Exploring GPT model fine-tuning due to their promising capabilities.

*The journey towards cloning my online presence continues, with hopes of achieving more refined results in the future.*
