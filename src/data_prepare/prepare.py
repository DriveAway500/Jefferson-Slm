# copied from https://github.com/karpathy/nanoGPT/blob/master/data/shakespeare/prepare.py
import tiktoken
import numpy as np

from utils import DataCleaner

class Prepare:

    @staticmethod
    def prepare():
        data = DataCleaner.training_data_loader()
        n = len(data)
        train_data = data[:int(n*0.9)]
        val_data = data[int(n*0.9):]

        # encode with tiktoken gpt2 bpe
        enc = tiktoken.get_encoding("gpt2")
        train_ids = enc.encode_ordinary(train_data)
        val_ids = enc.encode_ordinary(val_data)
        print(f"train has {len(train_ids):,} tokens")
        print(f"val has {len(val_ids):,} tokens")

        # export to bin files
        train_ids = np.array(train_ids, dtype=np.uint16)
        val_ids = np.array(val_ids, dtype=np.uint16)
        train_ids.tofile("data/bin/train.bin")
        val_ids.tofile("data/bin/val.bin")
        


    # @staticmethod
    # def train(size=8000):
    #     tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    #     tokenizer.pre_tokenizer = Whitespace()

    #     trainer = BpeTrainer(
    #         vocab_size=size,
    #         special_tokens=["[PAD]", "[BOS]", "[EOS]"]
    #     )

    #     data= DataCleaner.training_data_loader()

    #     if isinstance(data, str):
    #         data = data.split("\n")

    #     tokenizer.train_from_iterator(
    #         data,
    #         trainer
    #     )

    #     tokenizer.save("tokenizer.json")