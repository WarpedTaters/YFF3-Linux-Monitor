

cd /home/YFF-project
source venv/bin/activate
python -m http.server 8000 &
server_pid=$!

cleanup() {
    kill "$server_pid" 2>/dev/null
    wait "$server_pid" 2>/dev/null
}

trap cleanup EXIT INT TERM

python3 collector.py