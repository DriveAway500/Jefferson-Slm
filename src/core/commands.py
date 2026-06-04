import sys
import subprocess
from pathlib import Path

from data_prepare import Prepare

class Commands:

    @staticmethod
    def commandsetup():

        def cpu_train():
            subprocess.run([
                "python",
                "core/train.py",
                "utils/debug_config.py",
                "--device=cpu",
                "--compile=False",
                "--eval_iters=20",
                "--log_interval=1",
                "--block_size=64",
                "--batch_size=12",
                "--n_layer=4",
                "--n_head=4",
                "--n_embd=128",
                "--max_iters=2000",
                "--lr_decay_iters=2000",
                "--dropout=0.0",
            ])

        def content_prepare():
            Prepare.prepare()

        def insert_prompt():
            subprocess.run([
            "python",
            "core/sample.py", 
            "--out_dir=out-debbug",
            "--device=cpu"
            ])

        def make_dir():
            Path("data/bin/").mkdir(exist_ok=True)
            Path("data/raw/").mkdir(exist_ok=True)

        commands = {
            "train": cpu_train,
            "prepare": content_prepare,
            "data": make_dir,
            "prompt": insert_prompt
        }

        try:
            commands[sys.argv[1]]()
        except (IndexError, KeyError):
            print(f"comandos disponíveis: {', '.join(commands)}")