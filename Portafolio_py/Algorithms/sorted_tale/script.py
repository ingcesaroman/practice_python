import utils
import sorts

# Load the original data
bookshelf = utils.load_books('books_small.csv')
#print("Original bookshelf:")
#for book in bookshelf:
#  print(book['title'])

# --- Sort by Title ---
#print("\nSorting by title...")
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

bookshelf_v1 = bookshelf.copy()
#sort_1 = sorts.bubble_sort(bookshelf_v1, by_title_ascending)
#print("\nBooks sorted by title:")
#for book in sort_1:
#  print(book['title'])

# --- Sort by Author using Bubble Sort ---
#print("\nSorting by author with Bubble Sort...")
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

bookshelf_v2 = bookshelf.copy()
#sort_2 = sorts.bubble_sort(bookshelf_v2, by_author_ascending)
#print("\nBooks sorted by author (Bubble Sort):")
#for book in sort_2:
#  print(book['author'])

# --- Sort by Author using Quick Sort ---
#print("\nSorting by author with Quick Sort...")
bookshelf_v3 = bookshelf.copy()
#sorts.quicksort(bookshelf_v3, 0, len(bookshelf_v3) - 1, by_author_ascending)
#print("\nBooks sorted by author (Quick Sort):")
#for book in bookshelf_v3:
#  print(book['author'])

# --- Final Sort: Total Length on Large Bookshelf ---
print("\n--- Final Sort on Large Bookshelf ---")
def by_total_length(book_a, book_b):
    return len(book_a['title']) + len(book_a['author']) > len(book_b['title']) + len(book_b['author'])

long_bookshelf = utils.load_books('books_large.csv')

# The following sort is commented out because it is very slow
# print("\nRunning Bubble Sort on large bookshelf (will be slow)...")
# long_bookshelf_bubble = long_bookshelf.copy()
# sorts.bubble_sort(long_bookshelf_bubble, by_total_length)

print("\nRunning Quick Sort on large bookshelf...")
long_bookshelf_quick = long_bookshelf.copy()
sorts.quicksort(long_bookshelf_quick, 0, len(long_bookshelf_quick) - 1, by_total_length)

print("\nTop 10 books sorted by total length (author + title):")
for i in range(min(10, len(long_bookshelf_quick))):
    book = long_bookshelf_quick[i]
    print(f"{i+1}. {book['title']} by {book['author']} (Length: {len(book['title']) + len(book['author'])})")