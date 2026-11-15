import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component with sinusoidal modulation
        f1 = np.sum(0.5 * x**2 * (1.0 + 0.3 * np.sin(2.0 * x)))
        
        # Multi-modal sinusoidal component with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.5 * i)
            amp = 1.0 + 0.4 * np.cos(0.3 * i)
            f2 -= amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interaction with exponential decay
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += np.exp(-0.05 * (x[i] - x[j])**2) * np.sin(3.0 * x[i] * x[j])
        
        # Chaotic coupling with dynamic weights
        f4 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.2 * np.sin(0.7 * i + np.cos(0.4 * i))
            f4 += weight * np.sin(1.5 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.08 * x[i]**2)
        
        # Deceptive global term with multiple peaks
        f5 = 0.0
        for i in range(self.dim):
            f5 -= 2.0 * np.exp(-0.5 * ((x[i] - 2.0) / 1.5)**2) + \
                  1.5 * np.exp(-0.5 * ((x[i] + 2.0) / 1.2)**2) + \
                  0.8 * np.exp(-0.5 * ((x[i] - 0.5) / 0.8)**2)
        
        # Fractional power interaction with chaotic modulation
        f6 = 0.0
        for i in range(self.dim):
            f6 += 0.3 * np.abs(x[i])**1.7 * np.sin(4.0 * x[i]) * np.cos(1.2 * x[i])
        
        # High-frequency oscillation component
        f7 = 0.0
        for i in range(self.dim):
            f7 -= 0.5 * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) * np.exp(-0.02 * x[i]**2)
        
        # Combined chaotic and conditioning term
        f8 = 0.0
        for i in range(self.dim):
            f8 += 0.4 * np.sin(3.0 * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.03 * np.sum(x**2))
        
        # Asymmetric scaling and coupling
        f9 = 0.0
        for i in range(self.dim):
            f9 += 0.2 * np.sin(2.5 * x[i]) * np.exp(-0.04 * np.sum(x**2)) * (1.0 + 0.3 * np.sin(0.5 * i))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9