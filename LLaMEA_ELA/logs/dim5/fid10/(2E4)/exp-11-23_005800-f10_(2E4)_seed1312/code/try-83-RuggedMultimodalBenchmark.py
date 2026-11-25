import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Modified parameters for increased difficulty
        self.alpha = 0.92
        self.beta = 0.85
        self.gamma = 0.75
        self.delta = 0.55
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hierarchical basin structure with modified exponential decay
        basin = 0.0
        for i in range(self.dim):
            dist = abs(x[i])
            basin += self.alpha * np.exp(-self.beta * dist) * (1.0 + 0.6 * np.sin(2.5 * dist))
            
        # Self-similar fitness valleys with modified harmonic components
        valley = 0.0
        for i in range(self.dim):
            freqs = [1.5, 3.0, 6.0, 12.0]  # Increased frequencies
            amplitudes = [1.2, 0.6, 0.3, 0.15]
            for f, a in zip(freqs, amplitudes):
                valley += a * np.sin(f * x[i]) * np.cos(f * x[i] / 2.0)
                
        # Enhanced ruggedness through modified correlation structure
        rugged = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                corr = np.exp(-self.gamma * abs(diff))
                rugged += corr * (np.sin(4.0 * diff) + 0.6 * np.cos(2.5 * diff))  # Modified terms
                
        # Scale-free complexity with modified polynomial terms
        scale_free = 0.0
        for i in range(self.dim):
            scale_free += (x[i]**5 + x[i]**4 + x[i]**3) * np.exp(-self.delta * abs(x[i]))  # Higher order polynomials
            
        # Enhanced global modulation
        modulation = 0.0
        norm_x = np.linalg.norm(x)
        if norm_x < 1.0:
            modulation = 6.0 * np.exp(-norm_x**2)
        elif norm_x > 4.0:
            modulation = 4.0 * np.exp(-(norm_x - 4.0)**2)
            
        # Combine all components with modified weights
        result = 1.3 * basin + 1.1 * valley + 0.9 * rugged + 0.7 * scale_free + modulation
        
        # Add offset to ensure positive fitness and scale appropriately
        return result + 9.0 * self.dim