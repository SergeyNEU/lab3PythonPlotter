import json
import matplotlib.pyplot as plt
import os

def load_and_parse_iperf_data(filepath):
    """Load and parse iPerf JSON data from a given filepath."""
    with open(filepath, 'r') as iperf_file:
        iperf_data = json.load(iperf_file)
    time_intervals_seconds = [interval['sum']['end'] for interval in iperf_data['intervals']]
    throughput_mbps = [interval['sum']['bits_per_second'] / 1e6 for interval in iperf_data['intervals']]
    return iperf_data, time_intervals_seconds, throughput_mbps

def generate_plot_title(iperf_data):
    """Generate a descriptive title from the iPerf JSON data."""
    protocol = iperf_data['start']['test_start']['protocol']
    host = iperf_data['start']['connecting_to']['host']
    timestamp = iperf_data['start']['timestamp']['time']
    return f"{protocol} Throughput to {host} - {timestamp}"

def plot_throughput(time_intervals, throughput_mbps, title):
    """Plot throughput over time with a given title."""
    plt.plot(time_intervals, throughput_mbps, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('Time (Seconds)')
    plt.ylabel('Throughput (Megabits per Second)')

# Directory containing the iPerf output files
output_folder_path = './output'

# Find all JSON files in the directory
iperf_files = [f for f in os.listdir(output_folder_path) if f.endswith('.json')]

# Initialize the plot
plt.figure(figsize=(12, 6))

# Process each file and add it to the plot
for file in iperf_files:
    file_path = os.path.join(output_folder_path, file)
    iperf_data, time_intervals, throughput = load_and_parse_iperf_data(file_path)
    title = generate_plot_title(iperf_data)
    plot_throughput(time_intervals, throughput, title)

plt.legend([os.path.splitext(file)[0] for file in iperf_files])
plt.grid(True)
plt.show()
