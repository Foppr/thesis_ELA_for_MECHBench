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
        
        # Gaussian peaks with adaptive widths based on chaotic sequence
        f2 = 0.0
        for i in range(self.dim):
            peak_center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            width = 0.1 + 0.3 * np.abs(self.chaotic_seq[i])
            f2 += np.exp(-0.5 * ((x_norm[i] - peak_center) / width)**2)
        
        # Cross-dimensional coupling with chaotic modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(2 * np.pi * (i + j) * self.chaotic_seq[i])
                distance = (x_norm[i] - x_norm[j])**2
                f3 += coupling * np.exp(-distance / (0.1 + 0.2 * self.chaotic_seq[j]))
        
        # Asymmetric polynomial with chaotic modulation
        f4 = 0.0
        for i in range(self.dim):
            modulator = 1 + 0.5 * np.sin(5 * np.pi * self.chaotic_seq[i])
            f4 += (x_norm[i]**3 + 0.2 * x_norm[i]**7) * modulator
        
        # Combine components with dynamic weights
        weight1 = 0.2 + 0.1 * self.chaotic_seq[0]
        weight2 = 0.3 + 0.15 * self.chaotic_seq[1]
        weight3 = 0.25 + 0.1 * self.chaotic_seq[2]
        weight4 = 0.25 + 0.1 * self.chaotic_seq[3]
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4