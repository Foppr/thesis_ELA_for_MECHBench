import numpy as np

class QuantumEntangledBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired parameters
        self.entanglement_levels = np.random.uniform(0.1, 0.9, dim)
        self.phase_angles = np.random.uniform(0, 2*np.pi, dim)
        self.superposition_weights = np.random.dirichlet(np.ones(dim))
        self.quantum_distances = np.random.uniform(0.5, 2.0, dim)
        self.decoherence_factors = np.random.uniform(0.1, 0.5, dim)
        # Chaotic enhancement parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.chaotic_amplitude = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum superposition state calculation
        result = 0.0
        for i in range(self.dim):
            # Base quantum component with phase and weight
            quantum_component = self.superposition_weights[i] * np.sin(
                self.quantum_distances[i] * x_norm[i] + self.phase_angles[i]
            )
            
            # Entanglement effect between dimensions
            entanglement_effect = 1.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.entanglement_levels[i] * self.entanglement_levels[j]
                    entanglement_effect *= np.cos(coupling_strength * (x_norm[i] - x_norm[j]))
            
            # Decoherence factor for quantum-to-classical transition
            decoherence = np.exp(-self.decoherence_factors[i] * np.abs(x_norm[i]))
            
            result += quantum_component * entanglement_effect * decoherence
        
        # Fourier-based interaction terms for complex correlation structure
        fourier_terms = 0.0
        for i in range(self.dim):
            # Discrete Fourier transform-like interactions
            freq_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                freq_sum += np.sin(k * x_norm[i]) * np.cos(k * x_norm[(i+k) % self.dim])
            fourier_terms += freq_sum
        
        # Chaotic enhancement term to increase landscape complexity
        chaotic_term = 0.0
        for i in range(self.dim):
            logistic_map = self.logistic_r[i] * x_norm[i] * (1 - x_norm[i])
            chaotic_term += self.chaotic_amplitude[i] * np.sin(logistic_map * 10)
        
        # Add quantum noise and non-linear transformation
        noise = np.random.normal(0, 0.02)
        total = result + 0.3 * fourier_terms + chaotic_term + noise
        
        # Apply quantum-inspired non-linearity with tunable parameter
        alpha = np.mean(self.entanglement_levels)
        total = np.tanh(total) * (1.0 + alpha * np.sin(np.sum(x_norm**2)))
        
        return total