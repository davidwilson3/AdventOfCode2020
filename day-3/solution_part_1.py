INPUT_FILE = './input.txt'

TREE = "#"

def solution(filename):
    trees = 0
    idx = 0 
    map = ''
    with open(filename) as f:    
        for line in f:              
            if idx >= len(line.strip()):
                idx = idx - len(line.strip())

            if line[idx] == TREE:                    
                line = line[:idx] + 'X' + line[idx + 1:]
                trees += 1
            else:                    
                line = line[:idx] + 'O' + line[idx + 1:]   

            idx += 3
            
            map = map + line
       
    print('Course taken: ')
    print(map)
    print(f'\nTrees hit: {trees}')

    return trees

if __name__ == "__main__":
    solution(INPUT_FILE)