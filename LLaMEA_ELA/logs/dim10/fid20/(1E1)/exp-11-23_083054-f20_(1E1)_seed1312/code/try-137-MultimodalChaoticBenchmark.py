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
        
        # Sinusoidal oscillation component with chaotic frequency modulation
        f1 = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(0.5 * self.chaotic_seq[i])
            f1 += np.sin(freq * x_norm[i]) ** 2 + 0.5 * np.cos(2 * freq * x_norm[i])
        
        # Gaussian peaks with adaptive spacing based on chaotic sequence
        f2 = 0.0
        for i in range(self.dim):
            peak_pos = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            peak_height = 1.0 + 0.5 * np.sin(3 * self.chaotic_seq[i])
            sigma = 0.1 + 0.2 * np.cos(0.7 * i)
            f2 += peak_height * np.exp(-0.5 * ((x_norm[i] - peak_pos) / sigma) ** 2)
        
        # Cross-dimensional coupling with chaotic interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling range
                coupling_strength = 0.5 + 0.5 * np.sin(2 * self.chaotic_seq[i] + 0.3 * self.chaotic_seq[j])
                distance = (x_norm[i] - x_norm[j]) ** 2
                f3 += coupling_strength * np.exp(-distance / (2 * 0.3**2))
        
        # Asymmetric cubic polynomial with chaotic bias
        f4 = 0.0
        for i in range(self.dim):
            bias = 0.5 * np.sin(1.5 * self.chaotic_seq[i])
            f4 += (x_norm[i]**3 + bias * x_norm[i]**2) * np.cos(2 * x_norm[i])
        
        # Combine with dynamic weights
        weight1 = 0.2 + 0.1 * np.sin(self.chaotic_seq[0])
        weight2 = 0.3 + 0.2 * np.cos(self.chaotic_seq[1])
        weight3 = 0.25 + 0.15 * np.sin(2 * self.chaotic_seq[2])
        weight4 = 0.25 + 0.1 * np.cos(3 * self.chaotic_seq[3])
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4