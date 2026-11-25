import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with dimension scaling
        quadratic = 0.5 * np.sum(x**2) / self.dim
        
        # Enhanced chaotic sinusoidal component with higher frequency variations and amplitude modulation
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3**(i % 7 + 1)
            amp = 2.0 + 0.8 * np.sin(i * 0.9)
            chaotic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.1 * np.abs(x[i]))
        
        # Stronger exponential decay interaction terms with cross-dimensional coupling
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j])) * np.cos(2 * (x[i] - x[j]))
        
        # Multi-scale periodic modulation with complex phase shifts and additional harmonic components
        modulation = 0.0
        for i in range(self.dim):
            modulation += 2.0 * np.sin(4 * np.pi * x[i]) * np.cos(1.2 * np.pi * x[i]) * np.exp(-0.15 * x[i]**2) + 0.5 * np.sin(8 * np.pi * x[i])**3
        
        # Enhanced cross-dimensional coupling with higher-order polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j])**5 + 0.7 * (x[i]**3 + x[j]**3) + 0.3 * np.sin(2 * x[i]) * np.cos(2 * x[j])
        
        # Rugged terrain component with multiple local minima and increased frequency
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.6 * np.sin(15 * x[i]) * np.cos(7 * x[i]) + 0.25 * np.sin(20 * x[i])**2 + 0.1 * np.cos(25 * x[i])
        
        # Asymmetric basin term with increased complexity and different scaling per dimension
        basin = 0.0
        for i in range(self.dim):
            basin += 0.4 * (x[i] - 2.5)**5 + 0.2 * (x[i] + 1.8)**4 + 0.1 * np.sin(12 * x[i]) * np.cos(6 * x[i])
        
        # Additional noise term with increased amplitude and frequency to increase landscape complexity
        noise = 0.1 * np.sum(np.sin(10 * x) * np.cos(5 * x))
        
        # Cross-dimensional interaction enhancement with non-linear coupling terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2)) + 0.2 * np.cos(3 * x[i] + 2 * x[j])
        
        # Small mutation: increased coupling strength and modified noise term
        coupling *= 1.2
        noise *= 1.3
        
        return quadratic + chaotic + exp_decay + modulation + coupling + rugged + basin + noise + cross_interaction