import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for fractal structure
        self.chaos_params = np.random.rand(dim) * 2 - 1
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Chaotic saddle points using logistic map modulation
        f2 = 0.0
        for i in range(self.dim):
            # Logistic map for chaotic behavior
            chaos_val = np.sin(np.pi * x[i]) * np.cos(np.pi * x[i])
            f2 += 2.0 * np.sin(3.0 * x[i]) * np.exp(-0.1 * np.abs(x[i])) * chaos_val
        
        # Fractal basin boundaries with sine-wave modulation
        f3 = 0.0
        for i in range(self.dim):
            # Create fractal-like basin with recursive sine modulation
            basin = np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            f3 += 0.5 * np.abs(x[i])**1.3 * basin
        
        # Adaptive gradient field with piecewise linear variation
        f4 = 0.0
        for i in range(self.dim):
            # Piecewise linear gradient that changes based on x[i]
            if x[i] < 0:
                grad = 1.2 * x[i]**2
            else:
                grad = 0.8 * x[i]**3
            f4 += grad * np.cos(0.5 * x[i])
        
        # Multi-scale oscillatory structure with varying frequencies
        f5 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.3 * i)
            f5 += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.05 * x[i]**2)
        
        # Cross-term interactions with exponential decay
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying interaction
                interaction = np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                f6 += interaction
        
        # Add noise for robustness
        noise = 0.02 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise