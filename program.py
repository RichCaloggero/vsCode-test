
def average_rainfall (data):
    sum = 0.0
    count = 0

    for i in range(0,len(data)):
        if data[i] == -999:
            break
        elif data[i] < 0:
            continue
        else:
            count += 1
            sum += data[i]

    if count > 0:
        return sum / count
    else:
        return None


