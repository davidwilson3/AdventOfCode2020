INPUT_FILE = './input.txt'


def solution(filename):
    valid = 0
    with open(filename) as f:    
        for line in f:        
            arr = line.split(' ')            
            ranges = arr[0].split('-')

            minTimes = int(ranges[0])
            maxTimes = int(ranges[1])
            letter = arr[1].split(':')[0]
            password = arr[2].strip()            
            freq = password.count(letter)

            if freq >= minTimes and freq <= maxTimes:
                valid += 1           
    
    print(f'Valid passwords: {valid}')
    return valid

if __name__ == "__main__":
    solution(INPUT_FILE)