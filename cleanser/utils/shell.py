import subprocess


def run(command):
  out = subprocess.check_output(command, shell=True)
  if out:
    return out.decode('utf-8').strip()


def git_hash(short=False):
  if short:
    return run('git rev-parse --short HEAD')
  return run('git rev-parse HEAD')


def git_origin():
  return run('git remote get-url origin')


def git_current_branch():
  return run('git rev-parse --abbrev-ref HEAD')


def git_repo_name():
  return run('basename `git rev-parse --show-toplevel`')


def github_repo():
  origin = git_origin()
  if 'git@github.com:' in origin:
    origin = origin.replace('git@github.com:', '').replace('.git', '')
    return origin.split('/')[-2:]
  return None, None


def github_repo_name():
  return github_repo()[1]


def github_repo_account():
  return github_repo()[0]


def git_commit(files='.', message='automated commit', branch=None):
  if branch:
    try:
      run(f'git checkout {branch}')
    except subprocess.SubprocessError:
      run(f'git checkout -b {branch}')
  if isinstance(files, str):
    run(f'git add {files}')
  else:
    run(['git', 'add', *files])
  run(f'git commit -m {message}')


def git_diff():
  return run('git diff')


def shutdown_computer():
  return run('sudo shutdown -h now')


def nvidia_smi():
  return run('nvidia-smi')


def pip_freeze():
  return run('pip freeze')


def conda_list(explicit=False):
  return run(f'conda list {"--explicit" if explicit else ""}')
