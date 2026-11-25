import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic sequence using multiple map types for enhanced complexity
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 15):
            # Alternate between logistic and tent maps
            if i % 2 == 0:
                val = 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1])
            else:
                val = 2 * self.chaotic_seq[-1] if self.chaotic_seq[-1] < 0.5 else 2 * (1 - self.chaotic_seq[-1])
            self.chaotic_seq = np.append(self.chaotic_seq, val)
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF component with chaotic centers and variable widths
        rbfs = []
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            width = 5 + 3 * np.sin(0.5 * i) + 2 * np.cos(0.3 * i)
            rbfs.append(np.exp(-width * (x_norm[i] - center)**2))
        f1 = np.sum(rbfs)
        
        # Multi-chaotic dynamics component using different map types
        f2 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Apply alternating chaotic maps
                if i % 2 == 0:
                    chaotic_val = 4 * x_norm[i] * (1 - x_norm[i])
                else:
                    chaotic_val = 2 * x_norm[i] if x_norm[i] < 0.5 else 2 * (1 - x_norm[i])
                f2 += np.sin(20 * chaotic_val) ** 3
        
        # Asymmetric polynomial interactions with perturbed exponents
        f3 = 0.0
        for i in range(self.dim):
            exp_factor = 1.5 + 0.5 * np.sin(0.4 * i)
            f3 += (x_norm[i]**exp_factor + 0.2 * x_norm[i]**(exp_factor + 2)) * np.cos(4 * np.pi * x_norm[i])
        
        # Cross-term interaction with dynamic coupling and phase modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.5 * np.sin(0.5 * (i + j)) * np.cos(0.8 * i * j) * np.sin(0.2 * (i - j))
                phase_mod = np.cos(0.6 * i) * np.sin(0.4 * j)
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * phase_mod
        
        # Additional chaotic modulation component
        f5 = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                chaotic_val = 4 * x_norm[i] * (1 - x_norm[i])
                f5 += np.cos(10 * chaotic_val) * np.sin(8 * x_norm[i+1]) * np.exp(-0.2 * x_norm[i+2]**2)
        
        # Combine with dynamic weights based on chaotic sequence and perturbed aggregation
        weight1 = 0.2 + 0.15 * self.chaotic_seq[0] + 0.05 * np.sin(0.3 * self.dim)
        weight2 = 0.25 + 0.2 * self.chaotic_seq[1] + 0.08 * np.cos(0.4 * self.dim)
        weight3 = 0.2 + 0.1 * self.chaotic_seq[2] + 0.06 * np.sin(0.5 * self.dim)
        weight4 = 0.15 + 0.15 * self.chaotic_seq[3] + 0.07 * np.cos(0.6 * self.dim)
        weight5 = 0.2 + 0.1 * self.chaotic_seq[4] + 0.09 * np.sin(0.7 * self.dim)
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5