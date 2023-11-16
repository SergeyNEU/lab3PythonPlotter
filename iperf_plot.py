import json
import matplotlib.pyplot as plt

# Path to the iPerf output file in JSON format
iperf_json_file_path = './iperf_udp_output.json'

# Read and parse the JSON data from the file
with open(iperf_json_file_path, 'r') as iperf_file:
    iperf_data = json.load(iperf_file)

# Initialize lists to store the time intervals and throughput values
time_intervals_seconds = []
throughput_bits_per_second = []

# Loop through each interval in the data to extract relevant information
for interval in iperf_data['intervals']:
    # The 'end' key holds the ending time of the interval
    interval_end_time = interval['sum']['end']
    time_intervals_seconds.append(interval_end_time)

    # The 'bits_per_second' key holds the throughput in bits/sec
    interval_throughput = interval['sum']['bits_per_second']
    throughput_bits_per_second.append(interval_throughput)

# Convert throughput from bits per second to megabits per second for better readability
throughput_megabits_per_second = [throughput / 1e6 for throughput in throughput_bits_per_second]

# Plotting the UDP throughput over time using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(time_intervals_seconds, throughput_megabits_per_second, marker='o', linestyle='-', color='blue')
plt.title('UDP Throughput Over Time from iPerf Data')
plt.xlabel('Time (Seconds)')
plt.ylabel('Throughput (Megabits per Second)')
plt.grid(True)
plt.show()
