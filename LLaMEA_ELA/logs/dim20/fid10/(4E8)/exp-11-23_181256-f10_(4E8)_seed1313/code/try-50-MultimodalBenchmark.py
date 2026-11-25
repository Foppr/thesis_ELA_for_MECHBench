import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # High-dimensional polynomial with varying exponents
        f1 = np.sum(np.power(np.abs(x_scaled), 3 + np.arange(self.dim) % 4))
        
        # Chaotic sine coupling with frequency modulation
        freqs = 2 * np.pi * (1 + np.sin(np.linspace(0, np.pi, self.dim)))
        f2 = np.sum(np.sin(freqs * x_scaled) * np.exp(-0.5 * np.abs(x_scaled)))
        
        # Radial basis function interactions
        r = np.sqrt(np.sum(x_scaled**2))
        f3 = np.sum(np.exp(-5 * (x_scaled - 0.5)**2) * np.sin(2 * np.pi * r))
        
        # Adaptive curvature scaling with exponential barriers
        f4 = np.sum((1 + 0.1 * x_scaled**2) * np.cos(5 * x_scaled) * np.exp(-0.1 * np.abs(x_scaled)))
        
        # Cross-dimensional coupling with logistic mapping
        coupling = np.zeros(self.dim)
        for i in range(self.dim):
            coupling[i] = np.sin(np.pi * (x_scaled[(i+1) % self.dim] + x_scaled[i]) / 2)
        f5 = np.sum(coupling * x_scaled)
        
        # Combined function with enhanced complexity
        return 3.0 * f1 + 1.5 * f2 + 0.8 * f3 + 0.6 * f4 + 0.4 * f5 + np.sum(np.exp(-x_scaled**2) * np.sin(10 * x_scaled))