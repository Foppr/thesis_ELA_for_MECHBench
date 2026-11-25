import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate multiple chaotic sequences for diverse dynamics
        self.chaotic_seq1 = np.array([1.0])
        self.chaotic_seq2 = np.array([0.5])
        self.chaotic_seq3 = np.array([0.8])
        for i in range(dim * 15):
            self.chaotic_seq1 = np.append(self.chaotic_seq1, 4 * self.chaotic_seq1[-1] * (1 - self.chaotic_seq1[-1]))
            self.chaotic_seq2 = np.append(self.chaotic_seq2, 3.8 * self.chaotic_seq2[-1] * (1 - self.chaotic_seq2[-1]))
            self.chaotic_seq3 = np.append(self.chaotic_seq3, 4.2 * self.chaotic_seq3[-1] * (1 - self.chaotic_seq3[-1]))
        self.chaotic_seq1 = self.chaotic_seq1[1:dim+1]
        self.chaotic_seq2 = self.chaotic_seq2[1:dim+1]
        self.chaotic_seq3 = self.chaotic_seq3[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF with multiple chaotic centers and varying widths
        f1 = 0.0
        for i in range(self.dim):
            center1 = (self.chaotic_seq1[i] - 0.5) * 2
            center2 = (self.chaotic_seq2[i] - 0.5) * 2
            width1 = 0.5 + 0.3 * np.sin(0.5 * i)
            width2 = 0.4 + 0.2 * np.cos(0.3 * i)
            rbf1 = np.exp(-width1 * (x_norm[i] - center1)**2)
            rbf2 = np.exp(-width2 * (x_norm[i] - center2)**2)
            f1 += 0.5 * rbf1 + 0.5 * rbf2
        
        # Combined chaotic dynamics from multiple maps
        f2 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_val1 = 4 * x_norm[i] * (1 - x_norm[i])
                chaotic_val2 = 3.8 * x_norm[i] * (1 - x_norm[i])
                chaotic_val3 = 4.2 * x_norm[i] * (1 - x_norm[i])
                f2 += np.sin(20 * chaotic_val1) ** 3 + np.cos(15 * chaotic_val2) ** 2 + np.tan(10 * chaotic_val3)
        
        # Asymmetric polynomial interactions with variable exponents
        f3 = 0.0
        for i in range(self.dim):
            exp1 = 3 + 2 * np.sin(0.4 * i)
            exp2 = 5 + 3 * np.cos(0.3 * i)
            term1 = x_norm[i]**exp1
            term2 = 0.3 * x_norm[i]**exp2
            f3 += (term1 + term2) * np.cos(4 * np.pi * x_norm[i])
        
        # Complex cross-term interactions with dynamic coupling and multi-frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.5 * np.sin(0.5 * (i + j)) * np.cos(0.7 * i * j) * np.sin(0.2 * (i - j))
                freq_mod = np.sin(0.4 * i) + np.cos(0.3 * j)
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * freq_mod
        
        # Additional chaotic modulation with fractal-like behavior
        f5 = 0.0
        for i in range(self.dim):
            mod1 = np.sin(12 * self.chaotic_seq1[i]) + np.cos(8 * self.chaotic_seq2[i])
            mod2 = np.tan(6 * self.chaotic_seq3[i]) + np.sin(9 * self.chaotic_seq1[i])
            f5 += mod1 * x_norm[i]**2 + mod2 * x_norm[i]**3
        
        # Dynamic weights based on multiple chaotic sequences
        weight1 = 0.2 + 0.15 * self.chaotic_seq1[0]
        weight2 = 0.25 + 0.2 * self.chaotic_seq2[1]
        weight3 = 0.3 + 0.18 * self.chaotic_seq3[2]
        weight4 = 0.15 + 0.12 * self.chaotic_seq1[3]
        weight5 = 0.1 + 0.08 * self.chaotic_seq2[4]
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5