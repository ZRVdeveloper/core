import gspread #https://www.youtube.com/watch?v=bu5wXjz2KvU ===========>
import gdown
import os

class LeadBook():
    key_place = "D:/Games/refined-analogy-280417-934a54eea5db.json"
    sheetName = 'EasyAnswer'
    book = {
        'h9іster':0,
        'h8ister':1,
        'h7ister':2,
        'a9ister':3,
        'a8ister':4,
        'a7ister':5,
        }
    def file_is_be(self, file_path):
        # Перевірка, чи файл існує
        if os.path.exists(file_path):
            print(f"Файл {file_path} уже завантажено.")
            return True
        else:
            print(f"Файл {file_path} не знайдено.")
            return False
            
    def Answer(self, needBook = None, needNomber = None):
        #print(needBook,needNomber)
        if needBook in self.book:
            #print (self.book[needBook], needNomber)
            self.sh = self.gc.open(self.sheetName).get_worksheet(self.book[needBook])
            file_id = self.sh.get(f'b{needNomber}')[0][0]
            url = f"https://drive.google.com/uc?id={file_id}"
            path_name = f'img_{file_id}.png'
            #print(url)
            if self.file_is_be(path_name) == False:
                gdown.download(url,f'{path_name}', quiet=False, fuzzy=True)
            return path_name
        else:
            return False
        
    def __init__(self,needBook = None, needNomber = None):
        self.gc = gspread.service_account(filename=self.key_place)
        '''
        if needBook in self.book:
            print (self.book[needBook], needNomber)
            self.sh = self.gc.open(self.sheetName).get_worksheet(self.book[needBook])
            m = self.sh.get(f'b{needNomber}')
            print (m)
        else: print('error')
        '''

if __name__ == "__main__":
    m = LeadBook()
    print(m.Answer('а9іster', 1))