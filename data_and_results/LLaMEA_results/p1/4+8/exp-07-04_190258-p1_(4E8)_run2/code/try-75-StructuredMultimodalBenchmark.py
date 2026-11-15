import numpy as np

class StructuredMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Sinusoidal periodic components with varying frequencies and amplitudes
        sinusoidal = 0
        for i in range(self.dim):
            sinusoidal += (np.sin(2 * np.pi * x[i]) + 0.5 * np.sin(4 * np.pi * x[i]) + 
                          0.3 * np.sin(8 * np.pi * x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive polynomial conditioning based on dimension index
        adaptive_poly = 0
        for i in range(self.dim):
            adaptive_poly += (i + 1) * x[i]**4 * np.cos(0.5 * x[i])
        
        # Cross-dimensional coupling with interaction terms
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.1 * (x[i]**2 + x[j]**2) * np.sin(0.3 * (x[i] - x[j]))
        
        # Gaussian-like local minima with varying widths
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.exp(-0.5 * ((x[i] - 2)**2 + (x[i] + 2)**2)) * np.cos(0.2 * x[i])
        
        # Saddle point structure with hyperbolic tangent components
        saddle = 0
        for i in range(self.dim):
            saddle += np.tanh(x[i]) * x[i]**3
        
        # Combined high-frequency oscillation with exponential decay
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        return quadratic + sinusoidal + adaptive_poly + coupling + local_minima + saddle + high_freq