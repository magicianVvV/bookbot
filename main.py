def main():
	import sys
	from stats import get_word_count
	from stats import sorted_count
	if len(sys.argv) != 2:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		print ("============ BOOKBOT ============")
		print ("Analyzing book found at books/frankenstein.txt...")
		print ("----------- Word Count ----------")
		get_word_count()
		print ("--------- Character Count -------")
		sorted_chars = sorted_count()
		for dics in sorted_chars:
			print (f"{dics["char"]}: {dics["num"]}")
		print ("============= END ===============")
main()
