import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with dimension scaling
        quadratic = 0.5 * np.sum(x**2) / self.dim
        
        # Chaotic sinusoidal component with varying frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 1.0 + 0.5 * np.sin(i)
            chaotic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Exponential decay interaction terms between variables
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3 * (x[i] + x[j]))
        
        # Multi-scale periodic modulation with different phase shifts
        modulation = 0.0
        for i in range(self.dim):
            modulation += 2.0 * np.sin(2 * np.pi * x[i]) * np.cos(0.5 * np.pi * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j])**3
        
        # Rugged terrain component with multiple local minima
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.3 * np.sin(10 * x[i]) * np.cos(5 * x[i]) + 0.1 * np.sin(15 * x[i])**2
        
        # Asymmetric basin term with different scaling per dimension
        basin = 0.0
        for i in range(self.dim):
            basin += 0.2 * (x[i] - 2.0)**4 + 0.1 * (x[i] + 1.5)**3
        
        return quadratic + chaotic + exp_decay + modulation + coupling + rugged + basin