import numpy as np

class NovelBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal modulation component with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(10 * x) * np.cos(7 * x) * np.exp(-0.1 * x**2))
        
        # Radial basis function with dynamic centers and varying widths
        rbf = 0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.5 * i)
            width = 0.5 + 0.5 * np.cos(0.3 * i)
            rbf += np.exp(-width * (x[i] - center)**2) * np.sin(5 * (x[i] - center))
        
        # Cross-dimensional interaction terms with varying coupling strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Limited interaction scope
                coupling = 1.0 + 0.5 * np.sin(0.7 * (x[i] + x[j]))
                cross += coupling * np.sin(3 * (x[i] - x[j])) * np.cos(2 * (x[i] + x[j]))
        
        # Polynomial chaos component with mixed even and odd powers
        poly = np.sum(x**8) + 0.8 * np.sum(x**7) + 0.6 * np.sum(x**6) + 0.4 * np.sum(x**5)
        
        # Memory-less chaotic component with exponential decay
        chaotic = np.sum(np.sin(x * np.pi * (1 + 0.3 * np.sin(10 * x))) * np.exp(-0.2 * x**2))
        
        # Fractal-like self-similarity through recursive scaling
        fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                fractal += np.sin(20 * dist) * np.exp(-0.5 * dist**2) * (1 + 0.2 * np.sin(3 * x[i]))
        
        # Combine components with adaptive weights
        return 0.25 * sin_mod + 0.30 * rbf + 0.15 * cross + 0.15 * poly + 0.08 * chaotic + 0.07 * fractal