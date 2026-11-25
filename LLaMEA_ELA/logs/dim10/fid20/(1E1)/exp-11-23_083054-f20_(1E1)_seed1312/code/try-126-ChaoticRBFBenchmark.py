import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate longer chaotic sequence for enhanced dynamics
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 20):
            self.chaotic_seq = np.append(self.chaotic_seq, 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1]))
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF with chaotic centers and varying widths
        rbfs = []
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            width = 10 + 5 * np.sin(0.5 * i) * np.cos(0.3 * self.chaotic_seq[i])
            rbfs.append(np.exp(-width * (x_norm[i] - center)**2))
        f1 = np.sum(rbfs)
        
        # Multi-scale logistic map dynamics with varying parameters
        f2 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Apply multiple logistic map iterations with varying r
                chaotic_val = 4 * x_norm[i] * (1 - x_norm[i])
                chaotic_val = 3.9 * chaotic_val * (1 - chaotic_val)
                f2 += np.sin(20 * chaotic_val) ** 3
        
        # Asymmetric polynomial interactions with dynamic exponents
        f3 = 0.0
        for i in range(self.dim):
            exp_factor = 2 + 3 * np.sin(0.4 * i) * np.cos(0.6 * self.chaotic_seq[i])
            f3 += (x_norm[i]**exp_factor + 0.5 * x_norm[i]**(exp_factor*1.5)) * np.cos(5 * np.pi * x_norm[i])
        
        # Cross-term interaction with time-varying coupling and dynamic phase shifts
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.5 * np.sin(0.5 * (i + j)) * np.cos(0.8 * i * j) * np.sin(0.2 * self.chaotic_seq[i])
                phase_shift = 0.1 * np.cos(0.4 * i) * np.sin(0.3 * j)
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.cos(phase_shift)
        
        # Combine with dynamic weights based on chaotic sequence and additional sine modulation
        weight1 = 0.3 + 0.2 * np.sin(0.7 * self.chaotic_seq[0])
        weight2 = 0.4 + 0.1 * np.cos(0.6 * self.chaotic_seq[1])
        weight3 = 0.2 + 0.3 * np.sin(0.8 * self.chaotic_seq[2])
        weight4 = 0.1 + 0.2 * np.cos(0.5 * self.chaotic_seq[3])
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4