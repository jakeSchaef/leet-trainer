def view_statistics():
    from collections import Counter
    algo_count = Counter()
    with open("results.txt", "r") as file:
        for raw in file:
            line = raw.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split("|")]
            # require at least Date | User | Algo | Result
            if len(parts) < 4:
                continue
            algo_part = parts[2]
            if ":" in algo_part:
                algorithm = algo_part.split(":", 1)[1].strip()
            else:
                algorithm = algo_part.strip()
            if algorithm:
                algo_count[algorithm] += 1
       
        print("=" * 30)
        print("\tSTATISTICS")
        print("=" * 30)
       
        for algo, c in algo_count.items():
            print(f"Algo: {algo}, Algo Count: {c}\n")