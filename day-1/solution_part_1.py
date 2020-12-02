INPUT_FILE = './input.txt'
GOAL = 2020

def solution(filename):
    entries = {}
    with open(filename) as f:    
        for line in f:
            value = int(line.strip())
            diff = GOAL - value 
            if diff in entries:
                print('\nSolution found:')      
                print(f'Entry 1: {diff}')
                print(f'Entry 2: {value}')
                print(f'Solution: {str(diff * value)}')         
                return diff * value
            entries[value] = value 
    
    print('No valid entries found')
    return None

if __name__ == "__main__":
    solution(INPUT_FILE)