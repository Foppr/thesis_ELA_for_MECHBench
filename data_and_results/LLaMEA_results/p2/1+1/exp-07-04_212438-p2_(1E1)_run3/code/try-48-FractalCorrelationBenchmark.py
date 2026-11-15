import numpy as np

class FractalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        f1 = np.sum(x**2)
        
        # Fractal-like correlation structure with exponentially decaying weights
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                weight = np.exp(-0.1 * (i - j)**2)
                f2 += weight * np.sin(10.0 * distance) * np.cos(15.0 * distance)
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        f3 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            f3 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Chaotic component with recursive interaction terms
        f4 = 0.0
        for i in range(self.dim):
            if i > 0:
                f4 += np.sin(20.0 * x[i-1] * x[i]) * np.exp(-0.5 * x[i]**2)
        
        # Long-range dependency with power-law decay
        f5 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(i - j)
                    decay = 1.0 / (1.0 + dist**1.5)
                    f5 += decay * np.sin(5.0 * (x[i] + x[j]))
        
        # Combined function with dynamic scaling
        return 0.3 * f1 + 0.25 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5