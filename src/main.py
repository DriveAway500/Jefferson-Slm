# from token_gen import DataCleaner

# def main():
#     clean_data= DataCleaner.training_data_loader()
#     print(clean_data)

from token_gen import TokenTrainer

def main():
    TokenTrainer.train()

if __name__ == '__main__':
    main()