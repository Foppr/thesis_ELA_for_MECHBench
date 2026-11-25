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
        
        # Gaussian peaks with chaotic positioning
        f1 = 0.0
        for i in range(self.dim):
            peak_pos = np.sin(self.chaotic_seq[i] * np.pi) * 0.8
            f1 += np.exp(-10 * (x_norm[i] - peak_pos)**2)
        
        # Sinusoidal oscillation component
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[i])
        
        # Polynomial correlation terms with chaotic coupling
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.3 * np.sin(self.chaotic_seq[i] * self.chaotic_seq[j])
                f3 += coupling * x_norm[i]**2 * x_norm[j]**3
        
        # Cross-term with dynamic weight based on chaotic sequence
        f4 = 0.0
        for i in range(self.dim):
            f4 += (x_norm[i]**4 + 0.5 * x_norm[i]**6) * np.sin(2 * np.pi * x_norm[i])
        
        # Combine all components with dynamic weights
        weight1 = 0.3 + 0.2 * np.sin(self.chaotic_seq[0] * np.pi)
        weight2 = 0.25 + 0.15 * np.cos(self.chaotic_seq[1] * np.pi)
        weight3 = 0.2 + 0.2 * np.sin(self.chaotic_seq[2] * np.pi / 2)
        weight4 = 0.25 + 0.1 * np.cos(self.chaotic_seq[3] * np.pi / 3)
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4