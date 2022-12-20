import math


def h_index(citations: [int]):
    count = len(citations)
    min_citations = -math.inf
    citations.sort()
    
    for i in range(len(citations)):
        count -= 1
        if citations[i] > min_citations and count >= min_citations:
            min_citations = citations[i]
        elif min_citations > count:
            return min_citations

    return min_citations


if __name__ == "__main__":
    print(h_index([1, 4, 1, 4, 2, 1, 3, 5, 6]))
    print(h_index([3, 1, 5, 3, 6, 7, 8, 3, 2, 1, 5, 3, 2, 5, 7, 4, 2, 5]))
