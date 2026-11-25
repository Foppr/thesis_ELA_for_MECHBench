import numpy as np

class QuantumEntangledBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired parameters
        self.entanglement_levels = np.random.uniform(0.2, 0.8, dim)
        self.phase_angles = np.random.uniform(0, 2*np.pi, dim)
        self.superposition_weights = np.random.dirichlet(np.ones(dim))
        self.quantum_distances = np.random.uniform(0.3, 1.5, dim)
        self.decoherence_factors = np.random.uniform(0.05, 0.4, dim)
        # Additional parameters for improved landscape structure
        self.coupling_strengths = np.random.uniform(0.1, 0.7, (dim, dim))
        self.frequency_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum superposition state calculation with modified weights
        result = 0.0
        for i in range(self.dim):
            # Base quantum component with phase and weight
            quantum_component = self.superposition_weights[i] * np.sin(
                self.quantum_distances[i] * x_norm[i] + self.phase_angles[i]
            )
            
            # Enhanced entanglement effect between dimensions using coupling matrix
            entanglement_effect = 1.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.coupling_strengths[i, j]
                    entanglement_effect *= np.cos(coupling_strength * (x_norm[i] - x_norm[j]) + 
                                                np.sin(x_norm[i] * x_norm[j]))
            
            # Adaptive decoherence factor
            decoherence = np.exp(-self.decoherence_factors[i] * (1.0 + 0.5 * np.abs(x_norm[i])))
            
            result += quantum_component * entanglement_effect * decoherence
        
        # Enhanced Fourier-based interaction terms with frequency weighting
        fourier_terms = 0.0
        for i in range(self.dim):
            freq_sum = 0.0
            for k in range(1, min(5, self.dim + 1)):
                freq_sum += (self.frequency_weights[i] * 
                           np.sin(k * x_norm[i]) * np.cos(k * x_norm[(i+k) % self.dim]))
            fourier_terms += freq_sum
        
        # Add quantum noise and non-linear transformation
        noise = np.random.normal(0, 0.015)
        total = result + 0.4 * fourier_terms + noise
        
        # Apply enhanced quantum-inspired non-linearity with tunable parameter
        alpha = np.mean(self.entanglement_levels)
        beta = np.std(self.coupling_strengths)
        total = np.tanh(total) * (1.0 + alpha * np.sin(np.sum(x_norm**2)) + 
                                0.3 * beta * np.cos(np.sum(x_norm)))
        
        # Add a global scaling factor to improve fitness score
        return total * (1.0 + 0.1 * np.sin(np.sum(x_norm**3)))