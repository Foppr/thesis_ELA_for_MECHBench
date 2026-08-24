import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Add nested periodic valleys with varying depths and widths
        f2 = 0.0
        for i in range(self.dim):
            # Create nested valley structure with periodic modulation
            valley_depth = 2.0 + 1.5 * np.sin(0.3 * i)
            valley_width = 0.5 + 0.3 * np.cos(0.4 * i)
            f2 -= valley_depth * np.exp(-0.5 * ((x[i] - 2.0 * np.sin(0.5 * i)) / valley_width)**2)
        
        # Add chaotic saddle points with sine-cosine interactions
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += 0.8 * np.sin(x[i]) * np.cos(x[j]) * np.sin(0.7 * x[i] * x[j])
        
        # Introduce asymmetric basin structures with exponential decay
        f4 = 0.0
        for i in range(self.dim):
            f4 += 1.2 * np.exp(-0.2 * (x[i] - 1.0)**2) * np.cos(1.5 * x[i]) + 0.5 * np.exp(-0.3 * (x[i] + 1.5)**2) * np.sin(1.2 * x[i])
        
        # Add fractal-like structure with recursive modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 += 0.3 * np.sin(5.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add cross-term interactions with varying weights
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.1 + 0.2 * np.sin(0.5 * (i + j))
                f6 += weight * np.tanh(x[i] + x[j]) * np.sin(0.3 * x[i] * x[j])
        
        # Add chaotic modulation with logistic map behavior
        f7 = 0.0
        for i in range(self.dim):
            chaos_factor = 3.8 * np.sin(x[i]) * (1 - np.sin(x[i])**2)
            f7 += 0.2 * chaos_factor * np.cos(0.8 * x[i])
        
        # Add noise term to increase robustness
        noise = 0.01 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise