import numpy as np

class AdaptiveChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive parameters
        self.chaos_seq = np.sin(np.arange(dim) * np.pi / 4 + 0.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f = np.sum(x**4) / 100.0
        
        # Add chaotic radial basis functions with adaptive centers and widths
        for i in range(self.dim):
            center = 3.0 * np.sin(self.chaos_seq[i])
            width = 0.5 + 0.5 * np.cos(self.chaos_seq[i])
            f += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Add polynomial chaos terms with varying degrees
        for i in range(self.dim):
            f += 0.3 * x[i]**(3 + int(self.chaos_seq[i] * 4)) + 0.1 * x[i]**5
            
        # Introduce adaptive noise based on dimensionality and position
        noise_amp = 0.05 * (1.0 + np.std(x) / 5.0)
        f += noise_amp * np.sum(np.sin(20 * x + self.chaos_seq))
        
        # Add cross-dimension coupling with dynamic weights
        for i in range(self.dim):
            j = (i + 1) % self.dim
            weight = 0.8 + 0.2 * np.cos(self.chaos_seq[i] * 3)
            f += weight * x[i]**2 * x[j]**2
            
        # Include a dynamic global minimum shift
        shift = 1.5 * np.sin(np.sum(x) / self.dim)
        f += 0.2 * np.sum((x - shift)**2)
        
        # Add irregular high-frequency oscillations
        for i in range(self.dim):
            f += 0.4 * np.sin(30 * x[i] + self.chaos_seq[i]) * np.cos(15 * x[i])
            
        return f