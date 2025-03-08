import os
import platform
import socket
import sys

# Get the machine type
print("Current machine type: " + platform.machine())

# Get the processor type
print("Processor type: " + str(platform.architecture()))

# Set the default timeout for a socket (in seconds) to 50 seconds
socket.setdefaulttimeout(50)

# Get the default socket timeout
print("Default Socket Timeout: " + str(socket.getdefaulttimeout()))

# Get the operating system name
print(
    f"Operating System: \n\tos.name - {os.name}\n\tplatorm.system() - {platform.system()}\n\tsys.platform - {sys.platform}"
)

# Get the current process ID
print("Current Process ID: " + str(os.getpid()))

file_name = "fdpractice.txt"
# Open the file using os.open (low-level file manipulation)
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"Process ID: {os.getpid()} opened file_handle: {file_handle}")
file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()

print(f"Before fork Process ID: {os.getpid()}")
# Fork a new process (Unix-based systems only)
if hasattr(os, "fork"):
    pid = os.fork()
    if pid == 0:
        print(f"Child Process ID: {os.getpid()} (Forked)")
        file_object_TextIO.seek(0)
        file_bytes = file_object_TextIO.read(100)
        print(file_bytes)
        file_object_TextIO.close()
        sys.exit(0)
    else:
        print(f"Parent Process ID: {os.getpid()}, Child Process ID: {pid}")
        os.waitpid(pid, 0)
        file_object_TextIO.close()