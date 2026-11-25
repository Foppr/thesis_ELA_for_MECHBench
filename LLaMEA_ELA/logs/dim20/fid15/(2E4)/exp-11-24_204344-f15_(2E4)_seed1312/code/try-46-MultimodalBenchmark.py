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
                exp_decay += np.exp(-0.35 * (x[i] - x[j])**2) * np.sin(5.5 * (x[i] + x[j])) * np.cos(2.2 * (x[i] - x[j]))
        
        # Multi-scale periodic modulation with complex phase shifts and additional harmonic components
        modulation = 0.0
        for i in range(self.dim):
            modulation += 2.2 * np.sin(4.2 * np.pi * x[i]) * np.cos(1.3 * np.pi * x[i]) * np.exp(-0.16 * x[i]**2) + 0.55 * np.sin(8.2 * np.pi * x[i])**3
        
        # Enhanced cross-dimensional coupling with higher-order polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j])**5.2 + 0.75 * (x[i]**3 + x[j]**3) + 0.35 * np.sin(2.1 * x[i]) * np.cos(2.1 * x[j])
        
        # Rugged terrain component with multiple local minima and increased frequency
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.65 * np.sin(15.5 * x[i]) * np.cos(7.2 * x[i]) + 0.26 * np.sin(20.2 * x[i])**2 + 0.11 * np.cos(25.3 * x[i])
        
        # Asymmetric basin term with increased complexity and different scaling per dimension
        basin = 0.0
        for i in range(self.dim):
            basin += 0.42 * (x[i] - 2.6)**5 + 0.21 * (x[i] + 1.9)**4 + 0.11 * np.sin(12.2 * x[i]) * np.cos(6.1 * x[i])
        
        # Additional noise term with increased amplitude and frequency to increase landscape complexity
        noise = 0.11 * np.sum(np.sin(10.2 * x) * np.cos(5.1 * x))
        
        # Cross-dimensional interaction enhancement with non-linear coupling terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.055 * (x[i]**2 + x[j]**2)) + 0.21 * np.cos(3.1 * x[i] + 2.1 * x[j])
        
        return quadratic + chaotic + exp_decay + modulation + coupling + rugged + basin + noise + cross_interaction