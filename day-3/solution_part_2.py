INPUT_FILE = './input.txt'
TREE = "#"

def calculate_trees(map, right, down):
    if down == 0: return 0

    x = y = 0
    trees = 0
    while x < len(map):
        segment = map[x]

        if y >= len(segment):
            y = y - len(segment)

        if segment[y] == TREE:                   
            trees += 1
    
        x += down
        y += right
        
    return trees


def solution(filename): 
    map = []
    with open(filename) as f:    
        for line in f:      
            map.append(line.strip())
        
    answer = calculate_trees (map, 1, 1) \
             * calculate_trees (map, 3, 1) \
             * calculate_trees (map, 5, 1) \
             * calculate_trees (map, 7, 1) \
             * calculate_trees (map, 1, 2) 

    print(f'\nSolution: {answer}')
    return answer

if __name__ == "__main__":
    solution(INPUT_FILE)