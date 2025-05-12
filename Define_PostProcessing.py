# This is a wrapper function that combines the processing functions below into one callable function that processes the sampler job and eliminates any constraint violating results.
# B is the budget constraint
def process_sampler_results(job, B):
    counts = get_counts(job)
    filtered_counts = filter_counts(counts, B)
    return filtered_counts

# Takes the counts directly from the sampler job and converts it to a sorted list.
# The bitstrings are reversed to match logical qubit order (qubit 0 on the right).
def get_counts(job):
    counts_bin = job.result()[0].data.meas.get_counts()

    # Reverse each bitstring to fix Qiskit’s default little-endian format
    counts = [(count, bitstring[::-1]) for bitstring, count in counts_bin.items()]
    counts.sort(reverse=True)
    return counts

# Filters results to include only those that satisfy the constraint of exactly B ones.
def filter_counts(counts, B):
    return [result for result in counts if result[1].count('1') == B]
