import numpy as np

class ChaoticInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.5, 2.0, dim)
        self.modulation_freq = np.random.uniform(1.0, 3.0, dim)
        self.decay_rates = np.random.uniform(0.1, 0.5, dim)
        # Saddle point configuration
        self.saddle_points = np.random.uniform(-3.0, 3.0, (3, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic exponential term
        f_val = np.sum(np.exp(self.chaos_params * np.abs(x)) - 1.0)
        
        # Sinusoidal modulation with varying frequencies
        for i in range(self.dim):
            f_val += 2.0 * np.sin(self.modulation_freq[i] * x[i]) * np.cos(self.modulation_freq[i] * x[i])
            
        # Exponential decay interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay_factor = np.exp(-self.decay_rates[i] * np.abs(x[i] - x[j]))
                f_val += 0.5 * decay_factor * x[i] * x[j]
                
        # Saddle point influence
        saddle_influence = 0.0
        for point in self.saddle_points:
            dist = np.sum((x - point)**2)
            saddle_influence += np.exp(-dist / 2.0)
        f_val += 0.3 * saddle_influence
        
        # Add quartic and quintic terms for increased curvature
        f_val += 0.02 * np.sum(x**4) + 0.005 * np.sum(x**5)
        
        # Add a small constant to ensure positive fitness
        f_val += 0.1
        
        return f_val