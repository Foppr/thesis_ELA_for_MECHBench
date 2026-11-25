import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate longer chaotic sequence for enhanced complexity
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 20):
            self.chaotic_seq = np.append(self.chaotic_seq, 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1]))
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF with chaotic centers and dynamic variances
        rbfs = []
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            variance = 0.1 + 0.2 * np.sin(2 * np.pi * self.chaotic_seq[i])
            rbfs.append(np.exp(-10 / variance * (x_norm[i] - center)**2))
        f1 = np.sum(rbfs)
        
        # Multi-step chaotic dynamics with sine modulation
        f2 = 0.0
        x_temp = x_norm.copy()
        for step in range(3):
            for i in range(self.dim):
                x_temp[i] = 4 * x_temp[i] * (1 - x_temp[i])
                f2 += np.sin(20 * x_temp[i]) ** 3 * np.cos(5 * step)
        
        # Asymmetric polynomial with cubic and quintic terms, plus sine modulation
        f3 = 0.0
        for i in range(self.dim):
            term = (x_norm[i]**3 + 0.4 * x_norm[i]**5) * np.cos(2 * np.pi * x_norm[i])
            f3 += term * (1 + 0.3 * np.sin(3 * self.chaotic_seq[i]))
        
        # Cross-dimensional coupling with time-varying strength and multi-frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.5 * np.sin(0.5 * (i + j)) * np.cos(0.8 * i * j) * np.sin(0.2 * self.chaotic_seq[i])
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Dynamic weighting with chaotic influence
        weights = []
        for i in range(4):
            base_weight = 0.2 + 0.3 * np.sin(1.5 * self.chaotic_seq[i % self.dim])
            weights.append(base_weight)
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4