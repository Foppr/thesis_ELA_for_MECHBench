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
        
        # Multimodal sinusoidal component
        f1 = 0.0
        for i in range(self.dim):
            f1 += np.sin(5 * np.pi * x_norm[i]) ** 2 + 0.5 * np.sin(10 * np.pi * x_norm[i]) ** 2
        
        # Gaussian peaks with chaotic positioning
        f2 = 0.0
        for i in range(self.dim):
            peak_pos = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            f2 += np.exp(-10 * (x_norm[i] - peak_pos)**2)
        
        # Cross-dimensional coupling with chaotic modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.5 * (i + j) * self.chaotic_seq[i])
                f3 += coupling * (x_norm[i]**2 + x_norm[j]**2) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Asymmetric polynomial with chaotic weights
        f4 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(3 * self.chaotic_seq[i])
            f4 += weight * (x_norm[i]**4 + 0.8 * x_norm[i]**6)
        
        # Combine components with dynamic weights
        weight1 = 0.2 + 0.3 * self.chaotic_seq[0]
        weight2 = 0.3 + 0.2 * self.chaotic_seq[1]
        weight3 = 0.25 + 0.25 * self.chaotic_seq[2]
        weight4 = 0.25 + 0.15 * self.chaotic_seq[3]
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4