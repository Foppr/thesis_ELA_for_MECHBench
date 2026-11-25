import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with dimension scaling
        quadratic = 0.5 * np.sum(x**2) / self.dim
        
        # Enhanced chaotic sinusoidal component with varying frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3**(i % 3 + 1)
            amp = 1.5 + 0.5 * np.sin(i * 0.5)
            chaotic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Improved exponential decay interaction terms between variables
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(4 * (x[i] + x[j]))
        
        # Multi-scale periodic modulation with different phase shifts and modified amplitudes
        modulation = 0.0
        for i in range(self.dim):
            modulation += 1.5 * np.sin(3 * np.pi * x[i]) * np.cos(0.7 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j])**4
        
        # Rugged terrain component with multiple local minima and enhanced complexity
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.5 * np.sin(12 * x[i]) * np.cos(6 * x[i]) + 0.2 * np.sin(18 * x[i])**2
        
        # Asymmetric basin term with different scaling per dimension and additional complexity
        basin = 0.0
        for i in range(self.dim):
            basin += 0.3 * (x[i] - 2.0)**4 + 0.15 * (x[i] + 1.5)**3 + 0.05 * np.sin(5 * x[i])
        
        return quadratic + chaotic + exp_decay + modulation + coupling + rugged + basin