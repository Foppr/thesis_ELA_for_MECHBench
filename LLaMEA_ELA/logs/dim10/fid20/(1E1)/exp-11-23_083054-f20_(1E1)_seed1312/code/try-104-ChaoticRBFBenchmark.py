import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 10):
            self.chaotic_seq = np.append(self.chaotic_seq, 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1]))
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic centers
        rbfs = []
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            rbfs.append(np.exp(-12 * (x_norm[i] - center)**2))
        f1 = np.sum(rbfs)
        
        # Logistic map chaotic dynamics component with sine modulation
        f2 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Apply logistic map iteration
                chaotic_val = 4 * x_norm[i] * (1 - x_norm[i])
                f2 += np.sin(12 * chaotic_val) ** 2 + 0.3 * np.cos(7 * chaotic_val)
        
        # Asymmetric polynomial interactions with modified exponents
        f3 = 0.0
        for i in range(self.dim):
            f3 += (x_norm[i]**4 + 0.25 * x_norm[i]**6) * np.cos(2.5 * np.pi * x_norm[i])
        
        # Cross-term interaction with variable coupling strength, sine modulation, and additional cosine term
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.35 * np.sin(0.4 * (i + j)) * np.cos(0.6 * i * j) + 0.1 * np.sin(0.8 * i * j)
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.25 * (x_norm[i] - x_norm[j])**2) * (1 + 0.2 * np.cos(3 * (x_norm[i] + x_norm[j])))
        
        # Combine with dynamic weights based on chaotic sequence
        weight1 = 0.3 + 0.2 * self.chaotic_seq[0]
        weight2 = 0.3 + 0.25 * self.chaotic_seq[1]
        weight3 = 0.2 + 0.3 * self.chaotic_seq[2]
        weight4 = 0.2 + 0.15 * self.chaotic_seq[3]
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4