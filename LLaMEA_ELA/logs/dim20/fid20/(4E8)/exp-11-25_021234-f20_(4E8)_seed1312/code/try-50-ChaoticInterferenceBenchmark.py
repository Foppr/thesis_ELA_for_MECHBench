import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier terms to create steep gradients near boundaries
        barrier = 0.0
        for i in range(self.dim):
            barrier += 1.0 / (1.0 + np.exp(-10.0 * (x[i] - 5.0))) + 1.0 / (1.0 + np.exp(10.0 * (x[i] + 5.0)))
        
        # Trigonometric wave interference pattern with varying frequencies
        wave = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 3.0 * np.sin(0.5 * i)
            freq2 = 1.5 + 2.5 * np.cos(0.4 * i)
            wave += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        
        # Adaptive noise component that changes based on position
        noise = 0.0
        for i in range(self.dim):
            noise += 0.5 * np.random.uniform(-1, 1) * (1.0 + 0.1 * np.abs(x[i]))
        
        # Fractional power terms to introduce non-smooth behavior
        fractional = 0.0
        for i in range(self.dim):
            fractional += np.power(np.abs(x[i]), 1.3 + 0.7 * np.sin(0.6 * i))
        
        # Cross-term interactions with exponential decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3.0 * (x[i] + x[j]))
        
        # Global scaling factor with chaotic behavior
        chaos_factor = 1.0 + 0.3 * np.sin(np.sum(x**2) / 25.0) * np.cos(np.sum(x) / 5.0)
        
        return chaos_factor * (barrier + wave + noise + fractional + cross)