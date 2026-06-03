import re

from .load_path import LoadPath

class DataCleaner():

    @staticmethod
    def load_text_content():
        text_path = LoadPath.loadby_txt_file_path()

        content= []
        for path in text_path:
            with open(path, 'r', encoding='utf-8') as f:
                
                content.append(f.read())

        return content

    @staticmethod
    def clean_text(raw_text):
        text = raw_text.replace('\r\n', '\n')
        
        text = re.sub(r'(\w+)-\s*\n?\s*(\w+)', r'\1\2', text)

        text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
        
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()

    @staticmethod
    def training_data_loader():
        raw_contents=DataCleaner.load_text_content()

        full_text = "\n\n".join(raw_contents)

        cleaned_text = DataCleaner.clean_text(full_text)

        return cleaned_text


