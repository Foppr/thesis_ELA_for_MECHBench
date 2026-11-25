import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate extended chaotic sequence for enhanced dynamics
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 20):
            self.chaotic_seq = np.append(self.chaotic_seq, 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1]))
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF with time-varying chaotic centers and dynamic widths
        rbfs = []
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2
            width = 0.5 + 0.5 * np.sin(2 * np.pi * self.chaotic_seq[i])
            rbfs.append(np.exp(-10 * width * (x_norm[i] - center)**2))
        f1 = np.sum(rbfs)
        
        # Multiple logistic map iterations with varying parameters
        f2 = 0.0
        for i in range(self.dim):
            chaotic_val = 4 * x_norm[i] * (1 - x_norm[i])
            f2 += np.sin(20 * chaotic_val) ** 3 + 0.5 * np.cos(10 * chaotic_val)
        
        # Asymmetric polynomial with higher-order terms and dynamic coefficients
        f3 = 0.0
        for i in range(self.dim):
            coeff = 0.5 + 0.5 * np.sin(3 * self.chaotic_seq[i])
            f3 += (coeff * x_norm[i]**4 + 0.4 * x_norm[i]**6) * np.cos(2 * np.pi * x_norm[i])
        
        # Cross-term interactions with dynamic coupling and multi-frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.7 * np.sin(0.5 * (i + j)) * np.cos(0.9 * i * j) * np.sin(0.2 * (i - j))
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Additional chaotic modulation with higher frequency components
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.sin(12 * x_norm[i]) * np.cos(8 * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Dynamic weighting with chaotic sequence and multi-scale modulation
        weight1 = 0.3 + 0.2 * np.sin(4 * self.chaotic_seq[0])
        weight2 = 0.25 + 0.15 * np.cos(3 * self.chaotic_seq[1])
        weight3 = 0.2 + 0.2 * np.sin(5 * self.chaotic_seq[2])
        weight4 = 0.15 + 0.1 * np.cos(6 * self.chaotic_seq[3])
        weight5 = 0.1 + 0.1 * np.sin(7 * self.chaotic_seq[4])
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5