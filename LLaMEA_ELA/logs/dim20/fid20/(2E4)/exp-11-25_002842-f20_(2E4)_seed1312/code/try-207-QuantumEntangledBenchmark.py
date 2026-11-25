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
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum superposition state calculation with enhanced non-linearity
        result = 0.0
        for i in range(self.dim):
            # Base quantum component with phase and weight
            quantum_component = self.superposition_weights[i] * np.sin(
                self.quantum_distances[i] * x_norm[i] + self.phase_angles[i]
            )
            
            # Enhanced entanglement effect between dimensions using polynomial coupling
            entanglement_effect = 1.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.entanglement_levels[i] * self.entanglement_levels[j]
                    # Use polynomial coupling instead of simple cosine
                    entanglement_effect *= (1.0 + coupling_strength * np.sin(x_norm[i] - x_norm[j])**2)
            
            # Modified decoherence factor with exponential decay
            decoherence = np.exp(-self.decoherence_factors[i] * (x_norm[i]**2))
            
            result += quantum_component * entanglement_effect * decoherence
        
        # Enhanced Fourier-based interaction terms with higher frequency components
        fourier_terms = 0.0
        for i in range(self.dim):
            # Add more complex discrete Fourier-like interactions
            freq_sum = 0.0
            for k in range(1, min(8, self.dim + 3)):
                # Use both sine and cosine with varying weights
                freq_sum += (k * np.sin(k * x_norm[i]) * np.cos(k * x_norm[(i+k) % self.dim]) + 
                           (k/2) * np.cos(k * x_norm[i]) * np.sin(k * x_norm[(i+k) % self.dim]))
            fourier_terms += freq_sum
        
        # Add quantum noise and non-linear transformation
        noise = np.random.normal(0, 0.015)
        total = result + 0.4 * fourier_terms + noise
        
        # Apply enhanced quantum-inspired non-linearity with adaptive parameter
        alpha = np.mean(self.entanglement_levels)
        # Add a more complex non-linear transformation to improve conditioning
        total = np.tanh(total) * (1.0 + alpha * np.sin(np.sum(x_norm**2)) + 0.1 * np.cos(2 * np.sum(x_norm**2)))
        
        return total