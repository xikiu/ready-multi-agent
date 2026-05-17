import subprocess
import time
import shlex

session_name = "test_sess2"
# 240x60
subprocess.run(["tmux", "new-session", "-d", "-x", "240", "-y", "60", "-s", session_name, "bash", "-c", "echo 'Pane 1' > test.log; tput cols >> test.log; sleep 10"])
subprocess.run(["tmux", "split-window", "-t", session_name, "bash", "-c", "echo 'Pane 2' >> test.log; tput cols >> test.log; sleep 10"])
subprocess.run(["tmux", "select-layout", "-t", session_name, "tiled"])

print("Created session.")
