import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 15):
            self.chaotic_seq = np.append(self.chaotic_seq, 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1]))
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component
        f1 = 0.0
        for i in range(self.dim):
            f1 += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Radial basis function with chaotic variance
        f2 = 0.0
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            variance = 0.1 + 0.2 * np.sin(0.5 * self.chaotic_seq[i])
            f2 += np.exp(-5 * (x_norm[i] - center)**2 / variance)
        
        # Polynomial chaos expansion with heterogeneous exponents
        f3 = 0.0
        for i in range(self.dim):
            exponent = 2 + 3 * np.sin(0.7 * self.chaotic_seq[i])
            f3 += x_norm[i]**exponent
        
        # Cross-term interactions with dynamic coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                coupling = 0.5 + 0.3 * np.sin(2 * (i + j) * self.chaotic_seq[i])
                distance = np.abs(x_norm[i] - x_norm[j])
                f4 += coupling * np.exp(-2 * distance**2) * (x_norm[i]**2 + x_norm[j]**2)
        
        # Add noise component with chaotic amplitude
        noise_amp = 0.1 + 0.05 * np.sin(3 * self.chaotic_seq[0])
        noise = np.sum(noise_amp * np.random.randn(self.dim))
        
        # Combine components with dynamic weights
        weight1 = 0.3 + 0.2 * np.sin(self.chaotic_seq[0])
        weight2 = 0.25 + 0.15 * np.cos(self.chaotic_seq[1])
        weight3 = 0.2 + 0.2 * np.sin(self.chaotic_seq[2])
        weight4 = 0.25 + 0.1 * np.cos(self.chaotic_seq[3])
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + noise