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
        
        # Multi-modal RBF component with multiple chaotic centers
        rbfs = []
        for i in range(self.dim):
            center1 = (self.chaotic_seq1[i] - 0.5) * 2
            center2 = (self.chaotic_seq2[i] - 0.5) * 2
            center3 = (self.chaotic_seq3[i] - 0.5) * 2
            rbf1 = np.exp(-20 * (x_norm[i] - center1)**2)
            rbf2 = np.exp(-10 * (x_norm[i] - center2)**2) * 0.5
            rbf3 = np.exp(-15 * (x_norm[i] - center3)**2) * 0.3
            rbfs.append(rbf1 + rbf2 + rbf3)
        f1 = np.sum(rbfs)
        
        # Multi-chaotic map dynamics component with different map types
        f2 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Apply multiple chaotic maps
                logistic_val = 4 * x_norm[i] * (1 - x_norm[i])
                tent_val = 2 * x_norm[i] if x_norm[i] < 0.5 else 2 * (1 - x_norm[i])
                circle_val = (x_norm[i] + 0.3) % 1.0
                f2 += np.sin(20 * logistic_val)**2 + np.cos(15 * tent_val)**2 + np.tan(10 * circle_val)**2
        
        # Asymmetric polynomial interactions with higher order terms and trigonometric modulation
        f3 = 0.0
        for i in range(self.dim):
            f3 += (x_norm[i]**5 + 0.4 * x_norm[i]**7 + 0.2 * x_norm[i]**9) * np.cos(5 * np.pi * x_norm[i]) * np.sin(2 * np.pi * x_norm[i])
        
        # Enhanced cross-term interaction with time-varying coupling and multiple modulation functions
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling based on chaotic sequences
                coupling = 0.3 + 0.5 * np.sin(0.5 * (i + j)) * np.cos(0.4 * i * j) * np.tan(0.2 * (i - j))
                # Add multiple modulation terms
                mod1 = np.sin(3 * (x_norm[i] + x_norm[j]))
                mod2 = np.cos(2 * (x_norm[i] - x_norm[j]))
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * mod1 * mod2
        
        # Additional chaotic modulation component
        f5 = 0.0
        for i in range(self.dim):
            chaotic_mod = np.sin(7 * self.chaotic_seq1[i]) + np.cos(5 * self.chaotic_seq2[i])
            f5 += chaotic_mod * x_norm[i]**4
        
        # Combine all components with dynamic weights from multiple chaotic sequences
        weight1 = 0.3 + 0.2 * np.sin(self.chaotic_seq1[0])
        weight2 = 0.25 + 0.15 * np.cos(self.chaotic_seq2[1])
        weight3 = 0.2 + 0.2 * np.sin(self.chaotic_seq3[2])
        weight4 = 0.15 + 0.1 * np.cos(self.chaotic_seq1[3])
        weight5 = 0.1 + 0.05 * np.sin(self.chaotic_seq2[4])
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5