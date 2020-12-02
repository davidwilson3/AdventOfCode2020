INPUT_FILE = './input.txt'


def solution(filename):
    valid = 0
    with open(filename) as f:    
        for line in f:        
            arr = line.split(' ')            
            ranges = arr[0].split('-')

            # adjust for array index positions
            pos1 = int(ranges[0]) - 1
            pos2 = int(ranges[1]) - 1
            letter = arr[1].split(':')[0]
            password = arr[2].strip()
            eval1 = password[pos1] == letter
            eval2 = password[pos2] == letter 
            
            if (eval1 or eval2) and eval1 != eval2:
                valid += 1   

    print(f'Valid passwords: {valid}')
    return valid

if __name__ == "__main__":
    solution(INPUT_FILE)