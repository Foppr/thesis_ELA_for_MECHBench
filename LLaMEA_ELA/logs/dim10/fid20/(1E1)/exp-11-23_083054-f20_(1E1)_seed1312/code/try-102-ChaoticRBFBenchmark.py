import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate multiple chaotic sequences for different components
        self.chaotic_seq1 = np.array([1.0])
        self.chaotic_seq2 = np.array([0.5])
        for i in range(dim * 15):
            self.chaotic_seq1 = np.append(self.chaotic_seq1, 4 * self.chaotic_seq1[-1] * (1 - self.chaotic_seq1[-1]))
            self.chaotic_seq2 = np.append(self.chaotic_seq2, 3.8 * self.chaotic_seq2[-1] * (1 - self.chaotic_seq2[-1]))
        self.chaotic_seq1 = self.chaotic_seq1[1:dim+1]
        self.chaotic_seq2 = self.chaotic_seq2[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF component with multiple chaotic centers
        f1 = 0.0
        for i in range(self.dim):
            center1 = (self.chaotic_seq1[i] - 0.5) * 2
            center2 = (self.chaotic_seq2[i] - 0.5) * 2
            rbf1 = np.exp(-20 * (x_norm[i] - center1)**2)
            rbf2 = np.exp(-10 * (x_norm[i] - center2)**2)
            f1 += 0.5 * rbf1 + 0.5 * rbf2
        
        # Dual chaotic dynamics component with sine and cosine modulation
        f2 = 0.0
        for i in range(self.dim):
            chaotic_val1 = 4 * x_norm[i] * (1 - x_norm[i])
            chaotic_val2 = 3.8 * x_norm[i] * (1 - x_norm[i])
            f2 += np.sin(20 * chaotic_val1) ** 3 + np.cos(15 * chaotic_val2) ** 2
        
        # Asymmetric polynomial with stochastic perturbations
        f3 = 0.0
        for i in range(self.dim):
            stochastic_pert = 0.1 * np.sin(7 * x_norm[i]) * np.cos(5 * x_norm[i])
            f3 += (x_norm[i]**4 + 0.4 * x_norm[i]**6 + stochastic_pert) * np.sin(2 * np.pi * x_norm[i])
        
        # Cross-term interactions with dynamic coupling and multi-scale modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.5 * np.sin(0.5 * (i + j)) * np.cos(0.8 * i * j) * np.exp(-0.2 * abs(i-j))
                modulation = np.sin(0.4 * x_norm[i]) * np.cos(0.6 * x_norm[j])
                f4 += coupling * x_norm[i] * x_norm[j] * modulation * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Multi-scale chaotic weighting with additional perturbations
        weights = []
        for i in range(4):
            base_weight = 0.2 + 0.3 * self.chaotic_seq1[i % len(self.chaotic_seq1)]
            perturbation = 0.05 * np.sin(3 * i + self.chaotic_seq2[i % len(self.chaotic_seq2)])
            weights.append(max(0.05, base_weight + perturbation))
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4