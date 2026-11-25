import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global quadratic basin
        f1 = 0.1 * np.sum(x**2)
        
        # Multiple sinusoidal wells with chaotic frequencies based on golden ratio
        f2 = 0.0
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(phi * i)  # Chaotic frequency modulation
            f2 += np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Overlapping periodic modulations with fractal-like amplitudes
        f3 = 0.0
        for i in range(self.dim):
            amp = 0.3 + 0.7 * np.sin(np.pi * i / (self.dim + 1)) * np.cos(2 * np.pi * i / (self.dim + 1))
            f3 += amp * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Add cubic and quartic terms for increased complexity
        f4 = 0.01 * np.sum(x**3)
        f5 = 0.005 * np.sum(x**4)
        
        # Add chaotic saddle points using a logistic map
        f6 = 0.0
        r = 3.95  # Chaotic regime
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]
            else:
                x_prev = x[i-1]
            logistic_val = r * x_prev * (1 - x_prev)
            f6 += np.sin(logistic_val * x[i]) * np.cos(x[i]**2)
        
        # Add a fractal-like scaling factor
        f7 = 0.05 * np.sum(np.sin(0.3 * x) * np.cos(0.1 * x) * np.exp(-0.05 * np.abs(x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7