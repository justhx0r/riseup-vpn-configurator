from subprocess import run, PIPE, CompletedProcess
import logging,os,sys,getpass,stat,random

def wipe_file(file_path):
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, 'wb') as f:
            for _ in range(48):
                # Generate 1 MB of random data
                random_data = os.urandom(1024 * 1024)
                f.write(random_data)
                f.flush()
                os.fsync(f.fileno())  # Flush data to disk
    except Exception as e:
        print(f"Error securely wiping file: {e}")

def cmd(run_cmd: str, verbose: bool = False) -> CompletedProcess:
    # Split the command string into a list of arguments
    cmd_list = run_cmd.strip().split(" ")

    # Run the command and capture both stdout and stderr
    completed_process = subprocess.run(cmd_list, stdout=PIPE, stderr=PIPE, text=True)

    # Log the command output if verbose is True
    if verbose:
        for line in completed_process.stdout.splitlines():
            logging.info(f"Output: {line}")

        for line in completed_process.stderr.splitlines():
            logging.info(f"Error: {line}")

    return completed_process


execute_permission = 0o111
logging.basicConfig(level=logging.INFO)
        

def get_cmd_path(command_name):
    for path in os.environ["PATH"].split(os.pathsep):
        full_path = os.path.join(path, command_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return None



def distro_ident() -> str:
    if get_cmd_path("nix") != None:
        return "nix"
    elif get_cmd_path("apt-get") != None:
        return "debian"
    elif get_cmd_path("pacman") != None:
        return "archlinux"
    elif get_cmd_path("emerge") != None:
        return "gentoo"
    else:
        return "busybox"

print("System prepared")