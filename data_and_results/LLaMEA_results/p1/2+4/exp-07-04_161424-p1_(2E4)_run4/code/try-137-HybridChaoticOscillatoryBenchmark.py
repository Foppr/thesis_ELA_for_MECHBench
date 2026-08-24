import numpy as np

class HybridChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for gradient modulation
        self.chaotic_seq = np.array([0.5])
        for i in range(dim * 10):
            next_val = 3.8 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1])
            self.chaotic_seq = np.append(self.chaotic_seq, next_val)
        self.chaotic_seq = self.chaotic_seq[:dim]
        
        # Precompute oscillation frequencies
        self.freqs = np.random.uniform(1.0, 5.0, dim)
        
        # Precompute radial basis centers and widths
        self.centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.widths = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component
        sin_comp = np.sum(np.sin(self.freqs * x_norm) * np.cos(self.freqs * x_norm))
        
        # Radial basis function component
        rbf_comp = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            rbf_comp += np.exp(-dist / (2 * self.widths[i]**2))
        
        # Chaotic gradient modulation
        grad_mod = np.sum(self.chaotic_seq * np.cos(x_norm))
        
        # Polynomial interaction with chaotic coefficients
        poly_comp = np.sum((x_norm**3 + 0.5 * x_norm**5) * self.chaotic_seq)
        
        # Combined fitness with dynamic weighting
        total = 0.4 * sin_comp + 0.3 * rbf_comp + 0.2 * grad_mod + 0.1 * poly_comp
        
        # Add conditioning via chaotic scaling factor
        cond_factor = 1.0 + 0.5 * np.sin(np.sum(self.chaotic_seq * x_norm))
        
        return total * cond_factor