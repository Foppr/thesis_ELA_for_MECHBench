import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic sinusoidal components with nested frequencies
        for i in range(self.dim):
            f_val += np.sin(10 * np.pi * x[i]) * np.cos(7 * np.pi * x[i]) + \
                     0.5 * np.sin(25 * np.pi * x[i]) * np.cos(13 * np.pi * x[i])
        
        # Add radial harmonic conditioning with exponential decay
        radius = np.sum(x**2)
        f_val += 0.3 * np.exp(-0.1 * radius) * np.sin(5 * np.pi * np.sqrt(radius))
        
        # Add nested multi-scale oscillations with varying amplitudes
        for i in range(self.dim):
            f_val += 0.2 * np.sin(3 * np.pi * x[i]) + \
                     0.15 * np.sin(9 * np.pi * x[i]) + \
                     0.1 * np.sin(27 * np.pi * x[i])
        
        # Add cross-dimensional chaotic coupling with sine-cosine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.08 * np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                f_val += coupling * np.sin(x[i] * x[j]) * np.cos(0.7 * (x[i]**2 + x[j]**2))
        
        # Add polynomial chaos with adaptive exponents
        for i in range(self.dim):
            f_val += 0.1 * x[i]**4 + 0.05 * x[i]**6 + 0.02 * x[i]**8
        
        # Add fractal-like interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.03 * np.sin(1.5 * (x[i] + x[j])) * np.cos(2.7 * (x[i] - x[j])) * \
                         np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Add global chaotic modulation
        f_val += 0.25 * np.sin(0.3 * np.sum(x)) * np.cos(0.4 * np.sum(x)**2) + \
                 0.1 * np.sin(0.7 * np.sum(x**2))
        
        return f_val