def generate_binary_strings(n, current_string, results):
    if n < 0:
        return ["Only Positive & Zero Number ! ! !"]
    if n == 0:
        results.append(current_string)
    else:
        generate_binary_strings(n - 1, current_string + "0", results)
        generate_binary_strings(n - 1, current_string + "1", results)

input_num = int(input("Enter Number : "))
output_results = []
generate_binary_strings(input_num, "", output_results)
for result in output_results:
    print(result)
