import sys
from googlenewsdecoder import new_decoderv1

def decode(url):
    return new_decoderv1(url)

if __name__ == "__main__":
    res = decode(sys.argv[1])
    print(res)
