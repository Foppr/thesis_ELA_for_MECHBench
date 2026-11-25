import numpy as np

class QuantumFractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal and quantum components
        self.fractal_exponent = 1.3 + 0.2 * np.random.rand()
        self.quantum_freq = 2.0 + 1.5 * np.random.rand(dim)
        self.gate_weights = 0.5 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        quantum_term = np.sum(self.quantum_freq * (x**2 + 0.1 * np.sin(self.quantum_freq * x)))
        
        # Fractional Brownian motion fractal component
        fractal_term = 0.0
        for i in range(self.dim):
            pos = x[i] / 5.0
            # Generate fractal noise with Hurst parameter
            hurst = 0.3 + 0.4 * np.sin(i * np.pi / self.dim)
            fractal_term += np.sin(pos * (2**i)) * (np.abs(pos) ** (2 * hurst))
        
        # Neural network gating mechanism
        gating_term = 0.0
        for i in range(self.dim):
            # Apply sigmoid gating based on neighboring dimensions
            gate_input = np.sum(x[max(0, i-1):min(self.dim, i+2)]) * self.gate_weights[i]
            gating_term += self.gate_weights[i] * (1.0 / (1.0 + np.exp(-gate_input)))
        
        # Multi-modal interaction terms
        multimodal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                multimodal_term += np.exp(-dist**2) * np.sin(3.0 * dist)
        
        # Combine all components with adaptive scaling
        result = 0.5 * quantum_term + 0.3 * fractal_term + 0.2 * gating_term + 0.1 * multimodal_term
        
        # Add boundary penalty
        penalty = np.sum(np.maximum(0.0, np.abs(x) - 4.8)**2)
        result += penalty
        
        return result