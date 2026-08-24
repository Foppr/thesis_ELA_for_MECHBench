import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random weights for each dimension
        np.random.seed(42)
        self.weights = np.random.uniform(0.5, 2.0, dim)
        # Chaos parameters
        self.chaos_factor = 0.7
        self.wave_freq = 3.0
        self.decay_rate = 0.3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply dimension-specific weights
        x_weighted = x * self.weights
        
        # Base exponential decay term
        f_val = np.sum(np.exp(-self.decay_rate * np.abs(x_weighted)))
        
        # Add trigonometric wave interactions with cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 2.0 * np.sin(self.wave_freq * x_weighted[i]) * np.cos(self.wave_freq * x_weighted[j]) * \
                         np.exp(-0.1 * (x_weighted[i] - x_weighted[j])**2)
        
        # Add chaotic modulation using sine and cosine with varying frequencies
        for i in range(self.dim):
            f_val += 1.5 * np.sin(self.chaos_factor * x_weighted[i] + np.sin(2.0 * x_weighted[i])) * \
                     np.cos(self.chaos_factor * x_weighted[i] + np.cos(1.5 * x_weighted[i]))
        
        # Add a perturbed quartic term with adaptive scaling
        f_val += 0.1 * np.sum((x_weighted**4) * (1.0 + 0.3 * np.sin(4.0 * x_weighted)))
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.5
        
        return f_val