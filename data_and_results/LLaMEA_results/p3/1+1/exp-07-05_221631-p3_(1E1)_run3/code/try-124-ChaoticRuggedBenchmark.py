import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis for structured complexity
        self.radial_weights = np.random.rand(dim) * 2.0 + 1.0
        # Multi-scale frequency parameters for varying ruggedness
        self.freqs = np.logspace(0, 2, num=dim, base=10)
        # Chaos control parameters
        self.chaos_factor = 0.5
        self.scale_factor = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 5.0) * self.scale_factor
        
        # Multi-scale sinusoidal perturbations
        sin_sum = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * self.radial_weights[i]
        
        # Cross-dimensional coupling with chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j]) * np.sin(self.chaos_factor * (x[i] + x[j]))
        
        # Add a perturbed quartic term with radial dependence
        quartic = np.sum((x**4) * (1.0 + 0.2 * np.sin(r)))
        
        # Combine all components
        f_val = radial_term + sin_sum + coupling + 0.05 * quartic
        
        # Add a small constant to ensure positivity
        f_val += 0.1
        
        return f_val