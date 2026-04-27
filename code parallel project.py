# ==========================================
# Quantum Computing Simulation using Qiskit
# (Spyder Graph Fixed Version)
# ==========================================

print("\nQuantum Computing Simulation using Qiskit\n")

# ===== IMPORTS =====
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import random

# Force interactive plotting (important for Spyder)
plt.ion()

# Simulator backend
sim = Aer.get_backend('qasm_simulator')


# ==========================================
# PART 1: SUPERPOSITION
# ==========================================
print("\n===== SUPERPOSITION =====")

qc1 = QuantumCircuit(1, 1)
qc1.h(0)
qc1.measure(0, 0)

compiled1 = transpile(qc1, sim)
job1 = sim.run(compiled1, shots=1000)
result1 = job1.result()
counts1 = result1.get_counts()

print("Superposition Result:", counts1)

plot_histogram(counts1)
plt.title("Superposition Output")
plt.tight_layout()
plt.show(block=True)


# ==========================================
# PART 2: ENTANGLEMENT
# ==========================================
print("\n===== ENTANGLEMENT =====")

qc2 = QuantumCircuit(2, 2)
qc2.h(0)
qc2.cx(0, 1)
qc2.measure([0, 1], [0, 1])

compiled2 = transpile(qc2, sim)
job2 = sim.run(compiled2, shots=1000)
result2 = job2.result()
counts2 = result2.get_counts()

print("Entanglement Result:", counts2)

plot_histogram(counts2)
plt.title("Entanglement Output")
plt.tight_layout()
plt.show(block=True)


# ==========================================
# PART 3: QUANTUM vs CLASSICAL COIN FLIP
# ==========================================
print("\n===== COIN FLIP COMPARISON =====")

# Classical coin flip
classical_results = [random.choice([0, 1]) for _ in range(1000)]
classical_counts = {
    "0": classical_results.count(0),
    "1": classical_results.count(1)
}

print("Classical Result:", classical_counts)
print("Quantum Result:", counts1)

# Classical plot
plt.figure()
plt.bar(classical_counts.keys(), classical_counts.values())
plt.title("Classical Coin Flip")
plt.tight_layout()
plt.show(block=True)

# Quantum plot
plot_histogram(counts1)
plt.title("Quantum Coin Flip")
plt.tight_layout()
plt.show(block=True)


# ==========================================
# PART 4: DEUTSCH-JOZSA ALGORITHM
# ==========================================
print("\n===== DEUTSCH-JOZSA ALGORITHM =====")

qc3 = QuantumCircuit(2, 1)

qc3.x(1)
qc3.h([0, 1])
qc3.cx(0, 1)
qc3.h(0)
qc3.measure(0, 0)

compiled3 = transpile(qc3, sim)
job3 = sim.run(compiled3, shots=1000)
result3 = job3.result()
counts3 = result3.get_counts()

print("Deutsch-Jozsa Result:", counts3)

plot_histogram(counts3)
plt.title("Deutsch-Jozsa Output")
plt.tight_layout()
plt.show(block=True)


# ==========================================
# PART 5: PERFORMANCE COMPARISON
# ==========================================
print("\n===== PERFORMANCE COMPARISON =====")

labels = ['Classical Steps', 'Quantum Steps']
values = [100, 1]

plt.figure()
plt.bar(labels, values)
plt.title("Quantum vs Classical Efficiency")
plt.ylabel("Number of Steps")
plt.tight_layout()
plt.show(block=True)


# ==========================================
# END
# ==========================================
print("\n✅ Project Execution Completed Successfully!\n")
