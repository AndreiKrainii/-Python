# TODO Найдите количество книг, которое можно разместить на дискете

weight_of_book_byte = 25*50*100*4
weight_of_book_Mbyte = weight_of_book_byte/(1024*1024)
count_of_books = round((1.44/weight_of_book_Mbyte), )
print("Количество книг, помещающихся на дискету:", count_of_books)
