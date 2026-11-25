import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants for stability
        self.chaotic_const = 4.0 * np.sin(np.pi / 6.0)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-based component with dynamic frequency modulation
        chaotic = 0.0
        for i in range(self.dim):
            freq = self.chaotic_const * (1.0 + 0.2 * np.sin(i * np.pi / 4.0))
            chaotic += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Radial basis function component with varying widths
        radial = 0.0
        for i in range(self.dim):
            width = 0.5 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            radial += np.exp(-width * np.sum((x_scaled - np.sin(i * np.pi / self.dim))**2))
        
        # Adaptive conditioning with exponential decay
        adaptive = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 1))
            adaptive += cond_factor * x_scaled[i]**4
        
        # Cross-terms with hyperbolic tangent modulation
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tanh_term = np.tanh(x_scaled[i] + x_scaled[j])
                cross_terms += tanh_term * np.sin(5 * x_scaled[i] * x_scaled[j])
        
        # Polynomial with mixed degrees and sign changes
        poly = 0.0
        for i in range(self.dim):
            deg = (i % 4) + 2
            sign = (-1)**(i % 2)
            poly += sign * x_scaled[i]**deg
        
        # Global scaling factors
        return 3.2 * chaotic + 2.1 * radial + 1.8 * adaptive + 1.5 * cross_terms + 0.7 * poly