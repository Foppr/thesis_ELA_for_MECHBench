import numpy as np

class HybridChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic sequence for varying frequencies and amplitudes
        self.chaotic_seq = np.zeros(dim)
        x = 0.5
        r = 3.9
        for i in range(dim):
            x = r * x * (1 - x)
            self.chaotic_seq[i] = x
            
        # Precompute radial basis function centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Sinusoidal oscillation component with chaotic frequencies
        for i in range(self.dim):
            freq = 2 * (1 + 3 * self.chaotic_seq[i])
            amp = 1.5 * (1 + 0.5 * np.sin(5 * self.chaotic_seq[i]))
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Radial basis function component
        for i in range(self.dim):
            rbfs = 0.0
            for j in range(self.dim):
                diff = x - self.centers[i, :]
                rbfs += np.exp(-0.5 * np.sum((diff / self.widths[i])**2))
            result += 0.5 * rbfs
            
        # Cross-dimensional interaction terms with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * (1 + np.sin(self.chaotic_seq[i] * self.chaotic_seq[j]))
                result += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Chaotic polynomial interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term = (x[i]**2 + x[j]**2) * (1 + 0.2 * np.sin(self.chaotic_seq[i] * 10))
                result += 0.1 * poly_term * np.sin(x[i] * x[j])
                
        # Adaptive penalty with chaotic center
        center = np.array([2.0 * np.sin(self.chaotic_seq[i]) for i in range(self.dim)])
        penalty = np.sum(((x - center) / 3.0)**2)
        result += 0.3 * penalty
        
        # Multi-scale chaotic modulation
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(self.chaotic_seq[i] * 7)
            result += 0.05 * scale * np.sin(10 * x[i] * scale)
            
        # Add global minimum attraction
        result += 0.02 * np.sum(x**2)
        
        return result