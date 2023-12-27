import subprocess

def run_xfoil(airfoil_file, alpha):
    # Run XFOIL as a subprocess
    process = subprocess.Popen(
        ["xfoil"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Send XFOIL commands
    commands = [
        f"load {airfoil_file}",
        "oper",
        f"alfa {alpha}",
        "iter 100",
        "pacc",
        "pol",
        "quit"
    ]

    for command in commands:
        process.stdin.write(command + "\n")
        process.stdin.flush()

    process.stdin.close()

    # Read the output
    output = process.stdout.read()

    # Close the process
    process.wait()

    return output

def extract_cl_cd(output):
    # Extract Cl and Cd values from XFOIL output
    cl, cd = None, None
    lines = output.split('\n')
    for line in lines:
        if "Cl" in line and "Cd" in line:
            values = line.split()
            cl = float(values[2])
            cd = float(values[5])
            break

    return cl, cd

def main():
    airfoil_file = "path/to/your/airfoil.dat"  # Replace with the path to your airfoil coordinates file
    alpha = 0.0  # Set the angle of attack to 0 degrees

    # Run XFOIL
    xfoil_output = run_xfoil(airfoil_file, alpha)

    # Extract Cl and Cd values
    cl, cd = extract_cl_cd(xfoil_output)

    # Print the results
    print(f"At alpha = {alpha} degrees:")
    print(f"Cl: {cl}")
    print(f"Cd: {cd}")

if __name__ == "__main__":
    main()
