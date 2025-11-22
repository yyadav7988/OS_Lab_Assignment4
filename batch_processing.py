import subprocess

scripts = ['scripts/script1.py', 'scripts/script2.py', 'scripts/script3.py']

print("=== Batch Execution Simulation ===")
for script in scripts:
    print(f"\nExecuting {script}...")
    try:
        subprocess.call(['python3', script])
    except Exception as e:
        print(f"Error executing {script}: {e}")
