class Book:
    def __init__(self, score="null", link="https://amazon.com",
                author='', page_count=0, name='', status='Ready to Start',
                type='book', puplisher="",
                release_date="2021-05-11T11:00:00.000-04:00") -> None:
        self.score = score
        self.link = link
        self.author = author
        self.page_count = page_count
        self.name = name
        self.status = status
        self.type = type
        self.puplisher = puplisher
        self.release_date = release_date
        
    def get_score(self):
        return self.score
    
    def set_score(self, score):
        self.score = score
        
    def get_link(self):
        return self.link
    
    def set_link(self, link):
        self.link = link
        
    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author
        
    def get_page_count(self):
        return self.page_count
    
    def set_page_count(self, page_count):
        self.page_count = page_count
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status
        
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type
        
    def get_puplisher(self):
        return self.puplisher
    
    def set_puplisher(self, puplisher):
        self.puplisher = puplisher
        
    def get_release_date(self):
        return self.release_date
    
    def set_release_date(self, release_date):
        self.release_date = release_date
        
    