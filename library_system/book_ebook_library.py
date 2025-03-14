import os

# Book 클래스 정의
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise ValueError(f"⚠ '{self.title}'은(는) 이미 대출된 책입니다!")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError(f"⚠ '{self.title}'은(는) 대출되지 않은 책입니다!")
        self.is_borrowed = False

    def __str__(self):
        status = "대출 중" if self.is_borrowed else "대출 가능"
        return f"[📖 종이책] {self.title} - {self.author} ({status})"

# Ebook 클래스 (Book 상속)
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # 파일 크기 (MB)

    def download(self):
        return f"📥 '{self.title}' 다운로드 완료! ({self.file_size}MB)"

    def __str__(self):
        return f"[📱 전자책] {self.title} - {self.author} ({self.file_size}MB)"

# Library 클래스 정의
class Library:
    def __init__(self, filename="books.txt"):
        self.books = []
        self.filename = filename
        self.load_books()  # 파일에서 기존 책 목록 불러오기

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"✅ '{book.title}'이(가) 도서 목록에 추가되었습니다.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                try:
                    book.borrow()
                    self.save_books()
                    print(f"📚 '{title}'이(가) 대출되었습니다!")
                except ValueError as e:
                    print(e)
                return
        print(f"⚠ '{title}'을(를) 찾을 수 없습니다!")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                try:
                    book.return_book()
                    self.save_books()
                    print(f"📚 '{title}'이(가) 반납되었습니다!")
                except ValueError as e:
                    print(e)
                return
        print(f"⚠ '{title}'을(를) 찾을 수 없습니다!")

    def show_books(self):
        if not self.books:
            print("📭 도서 목록이 비어 있습니다!")
            return
        
        print("\n📖 현재 도서 목록:")
        paper_books = [str(book) for book in self.books if isinstance(book, Book) and not isinstance(book, Ebook)]
        ebooks = [str(book) for book in self.books if isinstance(book, Ebook)]
        
        if paper_books:
            print("\n".join(paper_books))
        if ebooks:
            print("\n".join(ebooks))

    def download_book(self, title):
        for book in self.books:
            if book.title == title:
                if isinstance(book, Ebook):
                    print(book.download())
                else:
                    print(f"⚠ '{title}'은(는) 종이책이므로 다운로드할 수 없습니다!")
                return
        print(f"⚠ '{title}'을(를) 찾을 수 없습니다!")

    # 파일에서 도서 목록 불러오기
    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split("|")
                    if len(data) == 4 and data[0] == "Ebook":
                        self.books.append(Ebook(data[1], data[2], int(data[3])))
                    elif len(data) == 3 and data[0] == "Book":
                        self.books.append(Book(data[1], data[2]))

    # 변경된 도서 목록을 파일에 저장
    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for book in self.books:
                if isinstance(book, Ebook):
                    file.write(f"Ebook|{book.title}|{book.author}|{book.file_size}\n")
                else:
                    file.write(f"Book|{book.title}|{book.author}\n")

# 실행 함수
def main():
    library = Library()

    while True:
        print("\n📚 도서 관리 시스템 📚")
        print("1. 종이책 추가")
        print("2. 전자책 추가")
        print("3. 책 대출")
        print("4. 책 반납")
        print("5. 전자책 다운로드")
        print("6. 책 목록 보기")
        print("7. 종료")
        choice = input("선택: ")

        if choice == "1":
            title = input("종이책 제목: ")
            author = input("저자: ")
            library.add_book(Book(title, author))

        elif choice == "2":
            title = input("전자책 제목: ")
            author = input("저자: ")
            file_size = input("파일 크기(MB): ")
            try:
                file_size = int(file_size)
                library.add_book(Ebook(title, author, file_size))
            except ValueError:
                print("⚠ 파일 크기는 숫자로 입력해야 합니다!")

        elif choice == "3":
            title = input("대출할 책 제목: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("반납할 책 제목: ")
            library.return_book(title)

        elif choice == "5":
            title = input("다운로드할 전자책 제목: ")
            library.download_book(title)

        elif choice == "6":
            library.show_books()

        elif choice == "7":
            print("📚 도서 관리 시스템을 종료합니다.")
            break

        else:
            print("⚠ 올바른 번호를 입력하세요!")

# 프로그램 실행
if __name__ == "__main__":
    main()