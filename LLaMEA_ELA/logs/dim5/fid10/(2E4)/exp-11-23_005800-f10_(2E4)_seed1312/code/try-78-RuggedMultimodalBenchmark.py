import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for hierarchical structure and correlation decay
        self.alpha = 0.85
        self.beta = 0.7
        self.gamma = 0.6
        self.delta = 0.4
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hierarchical basin structure with exponentially decaying correlation
        basin = 0.0
        for i in range(self.dim):
            # Base basin with exponential decay
            dist = abs(x[i])
            basin += self.alpha * np.exp(-self.beta * dist) * (1.0 + 0.5 * np.sin(2.0 * dist))
            
        # Self-similar fitness valleys with multi-scale harmonic components
        valley = 0.0
        for i in range(self.dim):
            # Multi-scale harmonic interference at different frequencies
            freqs = [1.0, 2.0, 4.0, 8.0]
            amplitudes = [1.0, 0.5, 0.25, 0.125]
            for f, a in zip(freqs, amplitudes):
                valley += a * np.sin(f * x[i]) * np.cos(f * x[i] / 2.0)
                
        # Ruggedness through exponentially decaying correlation structure
        rugged = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                # Exponentially decaying correlation between dimensions
                corr = np.exp(-self.gamma * abs(diff))
                rugged += corr * (np.sin(3.0 * diff) + 0.5 * np.cos(2.0 * diff))
                
        # Scale-free complexity with polynomial and exponential terms
        scale_free = 0.0
        for i in range(self.dim):
            # Combination of polynomial and exponential terms with scaling factors
            scale_free += (x[i]**4 + x[i]**3 + x[i]**2) * np.exp(-self.delta * abs(x[i]))
            
        # Add global modulation based on solution quality
        modulation = 0.0
        norm_x = np.linalg.norm(x)
        if norm_x < 1.0:
            modulation = 5.0 * np.exp(-norm_x**2)
        elif norm_x > 4.0:
            modulation = 3.0 * np.exp(-(norm_x - 4.0)**2)
            
        # Combine all components with adaptive weights
        result = 1.2 * basin + 1.0 * valley + 0.8 * rugged + 0.6 * scale_free + modulation
        
        # Add offset to ensure positive fitness and scale appropriately
        return result + 8.0 * self.dim
