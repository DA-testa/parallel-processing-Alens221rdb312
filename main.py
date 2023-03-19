# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(i, 0) for i in range(n)]
    for i in range(m):
        t = data[i]
        thread_id, end_time = min(threads, key=lambda x: x[1])
        output.append((thread_id, end_time))
        threads[thread_id] = (thread_id, end_time + t)
    return output

def main():
    # input being read
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for thread_id, start_time in result:
        print(thread_id, start_time)



if __name__ == "__main__":
    main()
