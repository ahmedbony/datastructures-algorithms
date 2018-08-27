from huffman import HuffmanCoding

path = "/home/ubuntu/Desktop/github/datastructures-algorithms/sample.txt"

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path:")

h.decompress(output_path)