import numpy as np

class QuantumFractalNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal structure parameters
        self.fractal_exponents = np.random.uniform(0.1, 0.9, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Quantum interference parameters
        self.quantum_phases = np.random.uniform(0, 2*np.pi, dim)
        self.quantum_amplitudes = np.random.uniform(0.3, 1.5, dim)
        # Neural network inspired dynamics
        self.neural_weights = np.random.randn(dim, dim) * 0.5
        self.neural_biases = np.random.randn(dim) * 0.3
        self.activation_strength = np.random.uniform(0.5, 2.0, dim)
        # Adaptive coupling parameters
        self.coupling_strengths = np.random.uniform(0.1, 1.0, dim)
        self.coupling_frequencies = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Fractal component with self-similar structure
        fractal_term = 0.0
        for i in range(self.dim):
            # Generate fractal pattern using power law scaling
            scaled_x = np.abs(x[i]) ** self.fractal_exponents[i]
            fractal_term += self.fractal_amplitudes[i] * np.sin(scaled_x) * np.cos(scaled_x)
        
        # Quantum interference component
        quantum_term = 0.0
        for i in range(self.dim):
            # Quantum-like interference pattern
            interference = (self.quantum_amplitudes[i] * 
                          np.sin(x[i] * self.coupling_frequencies[i] + self.quantum_phases[i]) *
                          np.cos(x[i] * self.coupling_frequencies[i] * 0.5 + self.quantum_phases[i]))
            quantum_term += interference
        
        # Neural network inspired dynamics
        neural_term = 0.0
        for i in range(self.dim):
            # Apply activation function with adaptive strength
            activation_input = np.dot(self.neural_weights[i], x) + self.neural_biases[i]
            activation_output = np.tanh(activation_input * self.activation_strength[i])
            neural_term += activation_output
        
        # Adaptive coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling with adaptive frequency and strength
                coupling = (self.coupling_strengths[i] * np.sin(x[i] * x[j] * self.coupling_frequencies[i]) *
                           np.cos(x[i] * x[j] * self.coupling_frequencies[j]))
                coupling_term += coupling
        
        # Periodic modulation with fractal characteristics
        periodic_mod = 1.0
        for i in range(self.dim):
            periodic_mod *= (1.0 + 0.3 * np.sin(x[i] * 2.0) * np.cos(x[i] * 0.5))
        
        # Combine all terms with different weights
        total = 0.35 * fractal_term + 0.30 * quantum_term + 0.20 * neural_term + 0.15 * coupling_term
        
        # Global scaling and nonlinearity
        global_scale = 1.0 + 0.2 * np.sin(np.sum(x**2) * 0.1)
        result = total * global_scale * periodic_mod
        
        return result