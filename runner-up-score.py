if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = sorted(arr, reverse=True)
    runner_up = arr[0]

    for num in arr:
        if num < runner_up:
            runner_up = num
            break

    print(runner_up)