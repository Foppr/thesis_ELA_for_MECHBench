import numpy as np

class ChaoticNeuralQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_neurons = 12
        self.time_step = 0.05
        self.quantum_factor = 0.1
        self.nonlinearity_strength = 3.0
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Chaotic neural network component with quantum interference
        neural_sum = 0.0
        for i in range(self.num_neurons):
            neuron_input = 0.0
            for j in range(self.dim):
                # Chaotic activation with temporal evolution - slightly modified frequencies
                t = self.time_step * (i * 1.2 + j * 0.5)
                chaotic_factor = np.sin(t) * np.cos(2.5 * t) + 0.6 * np.sin(3.2 * t)
                neuron_input += x[j] * chaotic_factor
                
            # Quantum-inspired activation with complex phase
            phase = np.pi * (i * 0.8 + np.sum(x) * 0.12)
            quantum_activation = np.sin(neuron_input * self.nonlinearity_strength + phase) ** 2
            neural_sum += quantum_activation * (1.0 + self.quantum_factor * np.random.randn())
        
        # Polynomial chaos expansion with quantum coefficients
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Quantum-modulated polynomial terms - modified coefficients
            quantum_coeff = 1.0 + 0.6 * np.sin(i * 3.14 / self.dim) * np.cos(i * 2.71 / self.dim)
            poly_term += quantum_coeff * (xi ** 4) + 0.35 * (xi ** 3) + 0.12 * (xi ** 2)
        
        # Quantum-inspired radial basis functions with dynamic centers
        rbf_sum = 0.0
        for i in range(self.num_neurons):
            center = np.zeros(self.dim)
            for j in range(self.dim):
                # Quantum chaotic center positions - different modulation
                t = self.time_step * (i * 0.8 + j * 0.6)
                center[j] = 3.5 * np.sin(t) * np.cos(2.2 * t) + 1.2 * np.sin(3.1 * t) + 0.6 * np.cos(4.1 * t)
            
            # Quantum RBF with complex width modulation
            width = 1.2 + 0.25 * np.sin(i * 1.7) + 0.18 * np.cos(i * 2.5)
            dist = np.sum((x - center) ** 2)
            rbf_val = np.exp(-dist / (2 * width**2)) * (1.0 + 0.25 * np.sin(dist))
            rbf_sum += rbf_val
        
        # Cross-dimensional quantum interference term
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum correlation between dimensions - modified interaction
                corr_factor = np.sin(np.pi * (x[i] + x[j]) / 8.0) * np.cos(np.pi * (x[i] - x[j]) / 12.0)
                interference_term += corr_factor * np.exp(-abs(x[i] - x[j]))
        
        # Temporal quantum evolution component
        temporal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            t_mod = np.sin(self.time_step * (i + 1) * 2.5) * np.cos(self.time_step * (i + 1) * 1.8)
            temporal_term += t_mod * np.sin(xi * 3.5 + t_mod) * np.cos(xi * 2.5 + t_mod)
        
        # Combine all components with quantum-enhanced weighting
        return 0.32 * neural_sum + 0.28 * poly_term + 0.22 * rbf_sum + 0.16 * interference_term + 0.02 * temporal_term