import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate multiple chaotic sequences for diverse dynamics
        self.chaotic_seq1 = np.array([1.0])
        self.chaotic_seq2 = np.array([1.0])
        self.chaotic_seq3 = np.array([1.0])
        for i in range(dim * 15):
            self.chaotic_seq1 = np.append(self.chaotic_seq1, 4 * self.chaotic_seq1[-1] * (1 - self.chaotic_seq1[-1]))
            self.chaotic_seq2 = np.append(self.chaotic_seq2, 3.8 * self.chaotic_seq2[-1] * (1 - self.chaotic_seq2[-1]))
            self.chaotic_seq3 = np.append(self.chaotic_seq3, 4.0 * self.chaotic_seq3[-1] * (1 - self.chaotic_seq3[-1]))
        self.chaotic_seq1 = self.chaotic_seq1[1:dim+1]
        self.chaotic_seq2 = self.chaotic_seq2[1:dim+1]
        self.chaotic_seq3 = self.chaotic_seq3[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF with multiple chaotic centers
        rbfs = []
        for i in range(self.dim):
            center1 = (self.chaotic_seq1[i] - 0.5) * 2
            center2 = (self.chaotic_seq2[i] - 0.5) * 2
            rbf1 = np.exp(-20 * (x_norm[i] - center1)**2)
            rbf2 = np.exp(-10 * (x_norm[i] - center2)**2)
            rbfs.append(rbf1 + 0.5 * rbf2)
        f1 = np.sum(rbfs)
        
        # Multi-chaotic logistic map dynamics with sine modulation
        f2 = 0.0
        for i in range(self.dim):
            chaotic_val1 = 4 * x_norm[i] * (1 - x_norm[i])
            chaotic_val2 = 3.8 * x_norm[i] * (1 - x_norm[i])
            chaotic_val3 = 4.0 * x_norm[i] * (1 - x_norm[i])
            f2 += np.sin(20 * chaotic_val1) ** 2 + 0.5 * np.cos(15 * chaotic_val2) + 0.3 * np.sin(10 * chaotic_val3)
        
        # Asymmetric polynomial with higher-order terms and multipliers
        f3 = 0.0
        for i in range(self.dim):
            term = (x_norm[i]**5 + 0.4 * x_norm[i]**7 + 0.2 * x_norm[i]**9) * np.cos(5 * np.pi * x_norm[i])
            f3 += term
        
        # Complex cross-term interactions with dynamic coupling and multiple modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling1 = 0.3 + 0.5 * np.sin(0.4 * (i + j)) * np.cos(0.8 * i * j)
                coupling2 = 0.2 + 0.3 * np.sin(0.6 * i) * np.cos(0.5 * j)
                modulation = np.sin(0.5 * (x_norm[i] + x_norm[j])) * np.cos(0.3 * (x_norm[i] - x_norm[j]))
                f4 += coupling1 * x_norm[i] * x_norm[j] * np.exp(-0.4 * (x_norm[i] - x_norm[j])**2) * modulation
                f4 += coupling2 * x_norm[i] * x_norm[j] * np.sin(3 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine with dynamic weights based on multiple chaotic sequences
        weight1 = 0.3 + 0.2 * self.chaotic_seq1[0]
        weight2 = 0.4 + 0.15 * self.chaotic_seq2[1]
        weight3 = 0.2 + 0.25 * self.chaotic_seq3[2]
        weight4 = 0.1 + 0.1 * self.chaotic_seq1[3]
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4