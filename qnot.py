#pip install qiskit-aer
from qiskit import QuantumCircuit, Aer, execute

# Criar um circuito quântico com 1 qubit e 1 bit clássico
circuito = QuantumCircuit(1, 1)

# Aplicar a porta NOT quântica (X gate)
circuito.x(0)

# Medir o qubit no bit clássico correspondente
circuito.measure(0, 0)

# Configurar o simulador Aer
simulador = Aer.get_backend('qasm_simulator')

# Executar o circuito no simulador
job = execute(circuito, backend=simulador, shots=1024)

# Recuperar e imprimir os resultados
resultado = job.result()
contagem = resultado.get_counts(circuito)

# Mostrar o resultado
print("Resultado da medição:", contagem)
