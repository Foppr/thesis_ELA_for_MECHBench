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
            freq = 4**(i % 8 + 1)
            amp = 2.5 + 1.0 * np.sin(i * 1.1)
            chaotic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4) * np.exp(-0.12 * np.abs(x[i]))
        
        # Stronger exponential decay interaction terms with cross-dimensional coupling
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += np.exp(-0.4 * (x[i] - x[j])**2) * np.sin(6 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
        
        # Multi-scale periodic modulation with complex phase shifts and additional harmonic components
        modulation = 0.0
        for i in range(self.dim):
            modulation += 2.5 * np.sin(5 * np.pi * x[i]) * np.cos(1.5 * np.pi * x[i]) * np.exp(-0.2 * x[i]**2) + 0.6 * np.sin(10 * np.pi * x[i])**4
        
        # Enhanced cross-dimensional coupling with higher-order polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j])**6 + 0.8 * (x[i]**4 + x[j]**4) + 0.4 * np.sin(3 * x[i]) * np.cos(3 * x[j])
        
        # Rugged terrain component with multiple local minima and increased frequency
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.7 * np.sin(18 * x[i]) * np.cos(9 * x[i]) + 0.3 * np.sin(25 * x[i])**2 + 0.15 * np.cos(30 * x[i])
        
        # Asymmetric basin term with increased complexity and different scaling per dimension
        basin = 0.0
        for i in range(self.dim):
            basin += 0.5 * (x[i] - 3.0)**6 + 0.3 * (x[i] + 2.0)**5 + 0.15 * np.sin(15 * x[i]) * np.cos(7 * x[i])
        
        # Additional noise term with increased amplitude and frequency to increase landscape complexity
        noise = 0.15 * np.sum(np.sin(12 * x) * np.cos(6 * x))
        
        # Cross-dimensional interaction enhancement with non-linear coupling terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.07 * (x[i]**2 + x[j]**2)) + 0.3 * np.cos(4 * x[i] + 3 * x[j])
        
        # Additional high-frequency oscillation component to increase complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.8 * np.sin(25 * x[i]) * np.cos(18 * x[i]) + 0.4 * np.sin(35 * x[i])**3
        
        # Combined scaling factor to amplify overall landscape complexity
        scaling = 1.2
        
        return scaling * (quadratic + chaotic + exp_decay + modulation + coupling + rugged + basin + noise + cross_interaction + high_freq)