import subprocess
import time
import os
import shlex

session_name = "test_sess"
subprocess.run(["tmux", "new-session", "-d", "-s", session_name, "bash", "-c", "while ! tmux list-clients -t test_sess | grep -q .; do sleep 0.1; done; echo 'Attached!' > test.log; tput cols >> test.log; sleep 10"])
subprocess.run(["tmux", "split-window", "-t", session_name, "bash", "-c", "while ! tmux list-clients -t test_sess | grep -q .; do sleep 0.1; done; echo 'Pane 2' >> test.log; tput cols >> test.log; sleep 10"])
subprocess.run(["tmux", "select-layout", "-t", session_name, "tiled"])

print("Session created. Waiting 2s before attaching...")
time.sleep(2)
subprocess.run(["tmux", "attach-session", "-t", session_name])
