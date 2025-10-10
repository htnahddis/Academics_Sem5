def hiring_problem(ranks):
  
    best_so_far = float('inf')
    total_firings = 0

    for i, candidate_rank in enumerate(ranks):
        if candidate_rank < best_so_far:
         
            best_so_far = candidate_rank
            total_firings += 1
            print(f"Hired candidate with rank {candidate_rank} at interview {i + 1}")

    print(f"\nTotal firing cost (number of hires): {total_firings}")
    print(f"Final hired candidate rank: {best_so_far}")

    return total_firings, best_so_far

# Example usage:
candidate_ranks = [5, 3, 6, 2, 4, 1]
hiring_problem(candidate_ranks)
