import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal structure
        self.fractal_consts = np.random.rand(dim) * 2 - 1
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Fractal-like periodic structure with chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            # Use chaotic sine modulation with varying frequencies
            freq = 2.0 + 3.0 * np.sin(x[i] * 0.5 + i * 0.3)
            f2 += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale periodic peaks with varying amplitudes
        f3 = 0.0
        for i in range(self.dim):
            for k in range(1, 6):
                amp = 1.0 / (k * k)
                f3 += amp * np.sin(k * x[i]) * np.cos(k * x[i] * 0.5)
        
        # Dynamic gradient field with time-like parameter
        f4 = 0.0
        for i in range(self.dim):
            # Simulate time-dependent gradient using a pseudo-random seed
            seed = int((x[i] * 1000) % 1000) + i
            np.random.seed(seed)
            time_factor = np.random.rand()
            f4 += x[i] * np.sin(x[i] * time_factor) * np.cos(x[i] * time_factor * 0.3)
        
        # Embedded fractal structure using recursive-like terms
        f5 = 0.0
        for i in range(self.dim):
            # Use a modified logistic map for fractal behavior
            val = x[i] * 0.5
            for _ in range(5):
                val = 3.8 * val * (1 - val)
            f5 += val * np.sin(x[i] * 2.0)
        
        # Asymmetric basin with exponential and trigonometric components
        f6 = 0.0
        for i in range(self.dim):
            f6 += np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(0.5 * x[i]) + \
                  np.exp(-0.3 * (x[i] + 2.0)**2) * np.cos(0.3 * x[i])
        
        # Cross-dimensional interaction with hyperbolic terms
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f7 += np.tanh(x[i] * x[j]) * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Add noise for robustness
        noise = 0.01 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise