def get_book_text(x):
	with open(x) as f:
		book_text = f.read()
		return(book_text)
def main():
	file_path = "./books/frankenstein.txt"
	book_text = get_book_text(file_path)
	words = book_text.split()
	word_count = len(words)
	print (f"{word_count} words found in the document")
main()
