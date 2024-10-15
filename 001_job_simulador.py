 
# Hello World 

# Author: Israel Junior
# linkedin- https://www.linkedin.com/in/israjunior/
# reference - https://qiskit.github.io/qiskit-aer/tutorials/1_aersimulator.html

#________________________________________________________________________________
# To run the code, you ned to install: 
# - pip install qiskit
# - pip install qiskit-aer
# - pip install pylatexenc
#________________________________________________________________________________


# Import bib python
import matplotlib.pyplot as plt
import numpy as np

# Import Qiskit
from qiskit import*
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi

# 

qr=QuantumRegister(2)   # 2 qubit (quantum bits) - q[0] q[1]
cr=ClassicalRegister(2) # classical bits
print("",qr)
print("",cr)

circuit = QuantumCircuit(qr, cr)
circuit.draw(output='mpl')  # Desenha o circuito usando Matplotlib
plt.show()  # Mostra o gráfico

circuit.h(qr[0])  # entrelaçar os circuitos. Vamos aplicar porta Hadamard - está em sobreposição
                  # pode ser 0 ou 1 
circuit.draw(output='mpl')  # Desenha o circuito na porta Hadamard
plt.show()  # 

circuit.cx(qr[0],qr[1])
circuit.draw(output='mpl')  # Desenha o circuito na porta Hadamard
plt.show()  # 

circuit.measure(qr,cr)
simulator = Aer.get_backend('qasm_simulator')
circuit.draw(output='mpl')  # Desenha o circuito na porta Hadamard
plt.show()  # 


# Run and get counts
result = simulator.run(circuit).result()
counts = result.get_counts(circuit)

plot_histogram(counts, title='Bell-State counts')
print(counts)