import fitz
#from chunker import chunk_text
from recursive_chunker import recursive_chunk_text
pdf_path="data/papers/paper.pdf"

doc=fitz.open(pdf_path)

print("="*50)
print("ResearchMind PDF Loader")
print("="*50)

print(f"Total Pages: {len(doc)}")

full_text=""



for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()

    full_text +=text

print("\nFirst 1000 characters:\n")
print(full_text[:1000])

print("\n")
print("="*50)
print(f"Total Character Extracted: {len(full_text)}")
print("="*50)

chunks=recursive_chunk_text(full_text)

print(f"\n Total Chunks Created: {len(chunks)}")

print("\n First Chunk Preview:\n")
print(chunks[0][:500])

print(type(chunks))
print(len(chunks))