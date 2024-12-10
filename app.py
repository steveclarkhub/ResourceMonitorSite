from flask import Flask, render_template
import psutil
# may get diff args w/Nix v Win or Macos.

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cpu')
def cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    return render_template('cpu.html', cpu_percent=cpu_percent, cpu_freq=cpu_freq, cpu_count=cpu_count, cpu_count_logical=cpu_count_logical)

@app.route('/memory')
def memory():
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    return render_template('memory.html', virtual_memory=virtual_memory, swap_memory=swap_memory)

@app.route('/disk')
def disk():
    disk_partitions = psutil.disk_partitions()
    disk_usage = psutil.disk_usage('/')
    return render_template('disk.html', disk_partitions=disk_partitions, disk_usage=disk_usage)

@app.route('/network')
def network():
    net_io_counters = psutil.net_io_counters(pernic=True)
    net_if_addrs = psutil.net_if_addrs()
    return render_template('network.html', net_io_counters=net_io_counters, net_if_addrs=net_if_addrs)

@app.route('/process')
def process():
    process_list = psutil.pids()
    processes = []
    for pid in process_list:
       p = psutil.Process(pid)
       try:     
           processes.append({
           'pid': p.pid,
           'name': p.name(),
           'status': p.status(),
           'started': p.create_time(),
           'cmdline': p.cmdline()
       })
       except Exception as e:
            processes.append({
            'pid':p.pid,
            'error':e
            })
    return render_template('process.html', processes=processes)

if __name__ == '__main__':
    app.run(debug=True)