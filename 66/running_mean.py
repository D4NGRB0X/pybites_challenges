def running_mean(sequence):
    return [round(
        sum(sequence[:i+1])/len(sequence[:i+1]), 2
    ) for i, item in enumerate(sequence)]
