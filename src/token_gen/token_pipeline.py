from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

from .text_cleaner import DataCleaner

class TokenTrainer:

    @staticmethod
    def train(size=8000):
        tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
        tokenizer.pre_tokenizer = Whitespace()

        trainer = BpeTrainer(
            vocab_size=size,
            special_tokens=["[PAD]", "[BOS]", "[EOS]"]
        )

        data= DataCleaner.training_data_loader()

        if isinstance(data, str):
            data = data.split("\n")

        tokenizer.train_from_iterator(
            data,
            trainer
        )

        tokenizer.save("tokenizer.json")