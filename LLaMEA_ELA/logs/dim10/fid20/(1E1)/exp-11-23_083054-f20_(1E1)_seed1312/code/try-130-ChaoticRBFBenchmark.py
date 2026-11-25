import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate comprehensive chaotic sequences for multiple dynamics
        self.chaotic_seq1 = np.array([1.0])
        self.chaotic_seq2 = np.array([0.5])
        self.chaotic_seq3 = np.array([0.8])
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
        
        # Multi-modal RBF component with multiple chaotic centers
        rbfs = []
        for i in range(self.dim):
            center1 = (self.chaotic_seq1[i] - 0.5) * 2
            center2 = (self.chaotic_seq2[i] - 0.5) * 2
            rbf1 = np.exp(-20 * (x_norm[i] - center1)**2)
            rbf2 = np.exp(-10 * (x_norm[i] - center2)**2)
            rbfs.append(0.7 * rbf1 + 0.3 * rbf2)
        f1 = np.sum(rbfs)
        
        # Multiple chaotic map dynamics component
        f2 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_val1 = 4 * x_norm[i] * (1 - x_norm[i])
                chaotic_val2 = 3.8 * x_norm[i] * (1 - x_norm[i])
                chaotic_val3 = 4.0 * x_norm[i] * (1 - x_norm[i])
                f2 += np.sin(20 * chaotic_val1) ** 3 + np.cos(15 * chaotic_val2) ** 2 + np.tan(10 * chaotic_val3) ** 2
        
        # Asymmetric polynomial interactions with higher-order terms
        f3 = 0.0
        for i in range(self.dim):
            f3 += (x_norm[i]**5 + 0.4 * x_norm[i]**7 + 0.2 * x_norm[i]**9) * np.cos(5 * np.pi * x_norm[i])
        
        # Cross-term interaction with time-varying coupling and multi-frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.5 * np.sin(0.5 * (i + j)) * np.cos(0.8 * i * j) * np.sin(0.2 * (i - j)**2)
                modulation = np.cos(2 * np.pi * i * j) + np.sin(3 * np.pi * (i + j))
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * modulation
        
        # Add a fourth chaotic dynamic component with complex coupling
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < self.dim - 1:
                    chaotic_val = 4.2 * x_norm[i] * (1 - x_norm[i])
                    f5 += 0.1 * np.sin(12 * chaotic_val) * x_norm[i] * x_norm[j] * np.exp(-0.2 * (x_norm[i] - x_norm[j])**2)
        
        # Combine with dynamic weights based on multiple chaotic sequences
        weight1 = 0.3 + 0.2 * self.chaotic_seq1[0]
        weight2 = 0.25 + 0.2 * self.chaotic_seq2[1]
        weight3 = 0.2 + 0.15 * self.chaotic_seq3[2]
        weight4 = 0.15 + 0.1 * self.chaotic_seq1[3]
        weight5 = 0.1 + 0.05 * self.chaotic_seq2[4]
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5