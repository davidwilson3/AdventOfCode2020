INPUT_FILE = './input.txt'
GOAL = 2020

def solution(filename):
    entries = {}
    with open(filename) as f:    
        for line in f:
            value = int(line.strip())
            remainder = GOAL - value 

            for entry in entries:
                value2 = entry
                value3 = remainder - value2
                if value3 in entries:
                    print('\nSolution found:')      
                    print(f'Entry 1: {value}')
                    print(f'Entry 2: {value2}')
                    print(f'Entry 3: {value3}')
                    print(f'Solution: {str(value * value2 * value3)}')         
                    return value * value2 * value3
            entries[value] = value

    print('No valid entries found')
    return None

if __name__ == "__main__":
    solution(INPUT_FILE)