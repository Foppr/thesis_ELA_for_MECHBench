import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic conditioning
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 15):
            self.chaotic_seq = np.append(self.chaotic_seq, 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1]))
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with chaotic frequency modulation
        f1 = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(0.5 * self.chaotic_seq[i])
            f1 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Polynomial chaos expansion with chaotic coefficients
        f2 = 0.0
        for i in range(self.dim):
            coeff = 0.5 + 0.5 * self.chaotic_seq[i]
            f2 += coeff * (x_norm[i]**4 + 0.3 * x_norm[i]**6) * np.exp(-0.5 * x_norm[i]**2)
        
        # Adaptive radial basis functions with chaotic width scaling
        f3 = 0.0
        for i in range(self.dim):
            width = 0.1 + 0.4 * np.sin(0.7 * self.chaotic_seq[i])
            center = np.sin(2 * np.pi * self.chaotic_seq[i])
            f3 += np.exp(-0.5 * ((x_norm[i] - center) / width)**2)
        
        # Cross-term interactions with dynamic coupling strengths
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                coupling = 0.3 + 0.4 * np.cos(0.2 * (i + j)) * np.sin(0.5 * self.chaotic_seq[i])
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Dynamic weighting based on chaotic sequence
        weights = np.abs(self.chaotic_seq) / np.sum(np.abs(self.chaotic_seq))
        weights = weights / np.sum(weights)  # Normalize
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4