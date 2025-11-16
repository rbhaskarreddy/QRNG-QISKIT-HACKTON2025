Platform:Google colab-Python Jupyter notebook
----------------------------------------------

1) pip install qiskit-ibm-runtime
2) pip install jupyter
3) from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
4) from qiskit_aer import AerSimulator
5) !apt-get -qq install -y libfluidsynth1
6) # Define the number of qubits for the desired range (e.g., 3 qubits for 0-9)
      num_qubits = 3
      n_outcomes = 2**num_qubits # 8 possible outcomes (0-9)
7) # Create quantum and classical registers
    qr = QuantumRegister(num_qubits, 'q')
    cr = ClassicalRegister(num_qubits, 'c')
8) # Create a quantum circuit
   qc = QuantumCircuit(qr, cr)
9) # Apply Hadamard gates to each qubit to create a superposition
10) for i in range(num_qubits): qc.h(qr[i])
11) # Measure each qubit
      qc.measure(qr, cr)
12) # Simulate the circuit
13) from qiskit_aer import AerSimulator
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1) # Run only once for a single random number
    result = job.result()
    counts = result.get_counts(qc)
14) !pip install qiskit-aer
15) # Extract the measured state and convert to an integer
     measured_state_binary = list(counts.keys())[0] # Get the binary string of the measured state
     random_number = int(measured_state_binary, 2) # Convert binary to integer
16) print(f"The quantum circuit generated a random number: {random_number}")
     ******************************************************************

Output:The quantum circuit generated a random number: 6 (for 1 shot, n=3, 0-9)

If we change the no.of qubits (n), shots, range above programme       
       The quantum circuit generated a random number: 5 (for 100 shots, n=3, 0-9)
       The quantum circuit generated a random number: 7 (for 1 shot, n=4, 0-17)
       The quantum circuit generated a random number: 12 (for 100 shot, n=4, 0-17)


