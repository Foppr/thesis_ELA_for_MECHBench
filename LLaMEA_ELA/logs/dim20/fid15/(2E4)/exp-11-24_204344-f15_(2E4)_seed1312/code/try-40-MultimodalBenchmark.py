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
            freq = 2**(i % 4 + 2)  # Slightly increased frequency range
            amp = 1.2 + 0.8 * np.sin(i * 0.5)  # Modified amplitude modulation
            chaotic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)  # Different coupling
        
        # Enhanced exponential decay interaction terms between variables
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(3 * (x[i] + x[j]))  # Increased decay rate
        
        # Multi-scale periodic modulation with different phase shifts
        modulation = 0.0
        for i in range(self.dim):
            modulation += 1.8 * np.sin(2.5 * np.pi * x[i]) * np.cos(0.9 * np.pi * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Improved cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j])**3 + 0.6 * (x[i]**2 + x[j]**2)  # Reduced power and increased coefficient
        
        # Rugged terrain component with multiple local minima
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.5 * np.sin(10 * x[i]) * np.cos(5 * x[i]) + 0.2 * np.sin(15 * x[i])**2
        
        # Asymmetric basin term with different scaling per dimension
        basin = 0.0
        for i in range(self.dim):
            basin += 0.4 * (x[i] - 1.8)**4 + 0.2 * (x[i] + 1.2)**3 + 0.08 * np.sin(8 * x[i])  # Adjusted powers and coefficients
        
        # Additional noise term to increase landscape complexity
        noise = 0.08 * np.sum(np.sin(6 * x))  # Increased noise amplitude
        
        return quadratic + chaotic + exp_decay + modulation + coupling + rugged + basin + noise