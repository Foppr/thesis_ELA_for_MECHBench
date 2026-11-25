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
            freq = 6**(i % 7 + 1)
            amp = 3.0 + 1.5 * np.sin(i * 1.3)
            chaotic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.15 * np.abs(x[i]))
        
        # Stronger exponential decay interaction terms with cross-dimensional coupling
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(7 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Multi-scale periodic modulation with complex phase shifts and additional harmonic components
        modulation = 0.0
        for i in range(self.dim):
            modulation += 3.0 * np.sin(6 * np.pi * x[i]) * np.cos(2.0 * np.pi * x[i]) * np.exp(-0.25 * x[i]**2) + 0.8 * np.sin(12 * np.pi * x[i])**4
        
        # Enhanced cross-dimensional coupling with higher-order polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j])**7 + 0.9 * (x[i]**5 + x[j]**5) + 0.5 * np.sin(4 * x[i]) * np.cos(4 * x[j])
        
        # Rugged terrain component with multiple local minima and increased frequency
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.8 * np.sin(20 * x[i]) * np.cos(10 * x[i]) + 0.4 * np.sin(30 * x[i])**2 + 0.2 * np.cos(35 * x[i])
        
        # Asymmetric basin term with increased complexity and different scaling per dimension
        basin = 0.0
        for i in range(self.dim):
            basin += 0.6 * (x[i] - 3.5)**7 + 0.4 * (x[i] + 2.5)**6 + 0.2 * np.sin(18 * x[i]) * np.cos(9 * x[i])
        
        # Additional noise term with increased amplitude and frequency to increase landscape complexity
        noise = 0.2 * np.sum(np.sin(15 * x) * np.cos(7 * x))
        
        # Cross-dimensional interaction enhancement with non-linear coupling terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) + 0.4 * np.cos(5 * x[i] + 4 * x[j])
        
        # Additional high-frequency oscillation component to increase complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 1.0 * np.sin(30 * x[i]) * np.cos(20 * x[i]) + 0.5 * np.sin(40 * x[i])**3
        
        # Additional quartic polynomial interaction term to increase complexity
        quartic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quartic += 0.3 * (x[i]**2 + x[j]**2)**2 * np.sin(2 * x[i] * x[j])
        
        # Combined scaling factor to amplify overall landscape complexity
        scaling = 1.5
        
        return scaling * (quadratic + chaotic + exp_decay + modulation + coupling + rugged + basin + noise + cross_interaction + high_freq + quartic)