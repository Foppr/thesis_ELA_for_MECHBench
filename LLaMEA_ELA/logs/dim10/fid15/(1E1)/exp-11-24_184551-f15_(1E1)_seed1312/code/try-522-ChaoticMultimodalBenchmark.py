import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for chaotic behavior
        self.coefficients = np.random.uniform(-1.0, 1.0, dim)
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Chaotic sinusoidal component
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += self.amplitudes[i] * np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        
        # Polynomial barrier terms
        barrier_term = 0.0
        for i in range(self.dim):
            # Create multiple barriers with different positions and heights
            barrier_positions = np.linspace(-4.0, 4.0, 5)
            for pos in barrier_positions:
                distance = abs(x[i] - pos)
                barrier_term += 0.5 * (1.0 + np.tanh(2.0 * (distance - 1.0))) * np.exp(-0.5 * distance**2)
        
        # Add coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combine all terms with different weights
        result = 2.0 * chaotic_term - barrier_term + coupling_term
        
        # Add small random noise for additional complexity
        noise = np.random.normal(0.0, 0.01)
        
        return result + noise