import numpy as np

class SinusoidalValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Multiple parabolic valleys with varying depths and positions
        f2 = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Create valley structure with sinusoidal modulation
                valley_depth = 2.0 + 1.5 * np.sin(0.5 * i)
                valley_pos = np.array([3.0 * np.sin(0.3 * i), 3.0 * np.cos(0.3 * i)] + [0.0] * (self.dim - 2))[:self.dim]
                # Valley function with sinusoidal modulation
                valley = valley_depth * (np.sum((x - valley_pos)**2) + 0.1 * np.sin(3.0 * np.sum(x)))
                f2 += valley
        
        # Add sinusoidal modulation across dimensions
        f3 = 0.0
        for i in range(self.dim):
            f3 += 1.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Add periodic peaks with varying frequencies
        f4 = 0.0
        for i in range(self.dim):
            f4 -= 2.0 * np.cos(3.0 * x[i]) * np.sin(2.0 * x[i])
        
        # Cross-dimensional interaction terms
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f5 += 0.5 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Asymmetric basin structure with exponential decay
        f6 = 0.0
        for i in range(self.dim):
            f6 -= 1.0 * np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(0.5 * x[i])
        
        # Add noise term to increase robustness
        noise = 0.02 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise