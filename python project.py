
import numpy as np
import matplotlib.pyplot as plt


# INTERACTIVE SIGNAL GENERATOR & ANALYZER

def generate_signal(signal_type, t, amplitude, frequency):

    if signal_type == "Sine":
        return amplitude * np.sin(2 * np.pi * frequency * t)

    elif signal_type == "Cosine":
        return amplitude * np.cos(2 * np.pi * frequency * t)

    elif signal_type == "Square":
        return amplitude * np.where(
            np.sin(2 * np.pi * frequency * t) >= 0, 1, -1
        )

    elif signal_type == "Triangular":
        return amplitude * (2 / np.pi) * np.arcsin(
            np.sin(2 * np.pi * frequency * t)
        )

    elif signal_type == "Ramp":
        return amplitude * np.maximum(t, 0)

    elif signal_type == "Unit Step":
        return np.where(t >= 0, amplitude, 0)

    elif signal_type == "Impulse":
        y = np.zeros_like(t)
        y[np.argmin(np.abs(t))] = amplitude
        return y

    elif signal_type == "Exponential":
        return amplitude * np.exp(frequency * t)

    return np.zeros_like(t)


# EVEN AND ODD SIGNAL DECOMPOSITION

def even_odd_decomposition(y):

    even = (y + y[::-1]) / 2
    odd = (y - y[::-1]) / 2

    return even, odd


# ENERGY AND POWER CALCULATION

def calculate_energy_power(y, t):

    dt = t[1] - t[0]

    energy = np.sum(y ** 2) * dt

    duration = t[-1] - t[0]

    power = energy / duration

    return energy, power


# MAIN PROGRAM

def main():

    print("\n======================================")
    print("   INTERACTIVE SIGNAL GENERATOR")
    print("======================================")

    signals = {
        1: "Sine",
        2: "Cosine",
        3: "Square",
        4: "Triangular",
        5: "Ramp",
        6: "Unit Step",
        7: "Impulse",
        8: "Exponential"
    }

    print("\nSelect Signal Type:")

    for key, value in signals.items():
        print(f"{key}. {value}")

    try:
        choice = int(input("\nEnter your choice (1-8): "))

        if choice not in signals:
            print("Invalid choice! Please select between 1 and 8.")
            return

        signal_type = signals[choice]

        amplitude = float(input("Enter amplitude: "))

        frequency = float(input("Enter frequency: "))

        if frequency <= 0:
            print("Frequency must be positive.")
            return

    except ValueError:
        print("Please enter valid numerical values.")
        return

    # Time range
    t = np.linspace(-5, 5, 1000)

    # Generate original signal
    y = generate_signal(signal_type, t, amplitude, frequency)

    # Time shifting and scaling
    print("\nSelect Signal Operation:")
    print("1. No Operation")
    print("2. Time Shifting")
    print("3. Time Scaling")

    try:
        operation = int(input("Enter operation (1-3): "))

        if operation == 2:
            shift = float(input("Enter time shift value: "))
            y = generate_signal(
                signal_type, t - shift, amplitude, frequency
            )

        elif operation == 3:
            scale = float(input("Enter scaling factor: "))

            if scale == 0:
                print("Scaling factor cannot be zero.")
                return

            y = generate_signal(
                signal_type, scale * t, amplitude, frequency
            )

        elif operation != 1:
            print("Invalid operation!")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    # Signal analysis
    even, odd = even_odd_decomposition(y)

    energy, power = calculate_energy_power(y, t)

    # Classification
    periodic_signals = ["Sine", "Cosine", "Square", "Triangular"]

    classification = (
        "Periodic" if signal_type in periodic_signals else "Aperiodic"
    )

    print("\n========== SIGNAL ANALYSIS ==========")
    print("Signal Type:", signal_type)
    print("Classification:", classification)
    print("Amplitude:", amplitude)
    print("Frequency:", frequency, "Hz")
    print("Energy (approx.):", round(energy, 4))
    print("Average Power (approx.):", round(power, 4))

    print("\nEven and Odd decomposition completed.")

    # -------------------------------------
    # GRAPH PLOTTING
    # -------------------------------------

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    fig.suptitle(
        "Interactive Signal Generator & Analyzer",
        fontsize=16,
        fontweight="bold"
    )

    axes[0, 0].plot(t, y, label="Original Signal")
    axes[0, 0].set_title(signal_type + " Signal")
    axes[0, 0].set_xlabel("Time")
    axes[0, 0].set_ylabel("Amplitude")
    axes[0, 0].grid(True)
    axes[0, 0].legend()

    axes[0, 1].plot(t, even, label="Even Component")
    axes[0, 1].set_title("Even Signal")
    axes[0, 1].set_xlabel("Time")
    axes[0, 1].set_ylabel("Amplitude")
    axes[0, 1].grid(True)
    axes[0, 1].legend()

    axes[1, 0].plot(t, odd, label="Odd Component")
    axes[1, 0].set_title("Odd Signal")
    axes[1, 0].set_xlabel("Time")
    axes[1, 0].set_ylabel("Amplitude")
    axes[1, 0].grid(True)
    axes[1, 0].legend()

    axes[1, 1].plot(t, y, label="Original")
    axes[1, 1].plot(t, even + odd, "--", label="Even + Odd")
    axes[1, 1].set_title("Signal Reconstruction")
    axes[1, 1].set_xlabel("Time")
    axes[1, 1].set_ylabel("Amplitude")
    axes[1, 1].grid(True)
    axes[1, 1].legend()

    plt.tight_layout()

    # Save graph
    plt.savefig("output_graph.png", dpi=300)

    print("\nGraph saved successfully as output_graph.png")

    plt.show()


if __name__ == "__main__":
    main()
