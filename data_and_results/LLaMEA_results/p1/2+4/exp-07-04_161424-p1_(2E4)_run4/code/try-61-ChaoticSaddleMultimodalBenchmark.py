import numpy as np

class ChaoticSaddleMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for saddle point positioning
        self.chaotic_seq = np.array([0.1])
        for i in range(dim * 10):
            next_val = 3.8 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1])
            self.chaotic_seq = np.append(self.chaotic_seq, next_val)
        self.chaotic_seq = self.chaotic_seq[:dim]
        
        # Precompute Gaussian RBF centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        
        # Precompute sinusoidal frequencies
        self.freqs = np.random.uniform(1.0, 10.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies
        sin_comp = np.sum(np.sin(self.freqs * x_norm) * np.cos(2 * self.freqs * x_norm))
        
        # Gaussian radial basis functions with chaotic center placement
        rbf_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.chaotic_seq[i] * np.ones(self.dim))**2)
            rbf_sum += np.exp(-dist / (2 * self.rbf_widths[i]**2))
        
        # Chaotic saddle point with multiple unstable fixed points
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i] - self.chaotic_seq[i])**2 * np.sin(10 * x_norm[i])
        
        # Multi-scale noise with varying amplitude
        noise = np.sum(np.random.normal(0, 0.1 * (1 + np.abs(x_norm)), self.dim))
        
        # Combined fitness with dynamic weighting
        total = 0.4 * sin_comp + 0.3 * rbf_sum + 0.2 * saddle + 0.1 * noise
        
        # Add a global conditioning factor
        condition = 1.0 + 0.3 * np.sin(np.sum(x_norm**2) / self.dim)
        
        return total * condition