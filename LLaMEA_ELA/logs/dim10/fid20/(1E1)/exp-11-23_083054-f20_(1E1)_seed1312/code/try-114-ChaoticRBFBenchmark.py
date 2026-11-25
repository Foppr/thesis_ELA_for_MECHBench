import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic sequence using multiple map types for enhanced complexity
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 15):
            # Alternate between logistic and tent maps for richer dynamics
            if i % 2 == 0:
                new_val = 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1])
            else:
                new_val = 2 * self.chaotic_seq[-1] if self.chaotic_seq[-1] < 0.5 else 2 * (1 - self.chaotic_seq[-1])
            self.chaotic_seq = np.append(self.chaotic_seq, new_val)
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF component with chaotic centers and variable widths
        rbfs = []
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            width = 0.5 + 0.5 * np.sin(0.5 * i) + 0.3 * np.cos(0.7 * i)
            rbfs.append(np.exp(-width * (x_norm[i] - center)**2))
        f1 = np.sum(rbfs)
        
        # Multi-chaos dynamics component with sine and cosine modulation
        f2 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Apply logistic map iteration
                chaotic_val = 4 * x_norm[i] * (1 - x_norm[i])
                # Add tent map influence
                tent_val = 2 * chaotic_val if chaotic_val < 0.5 else 2 * (1 - chaotic_val)
                f2 += np.sin(10 * chaotic_val) ** 2 + np.cos(7 * tent_val) ** 2
        
        # Asymmetric polynomial interactions with perturbed exponents
        f3 = 0.0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.2 * np.sin(0.3 * i)
            f3 += (x_norm[i]**(3*exp_factor) + 0.4 * x_norm[i]**(5*exp_factor)) * np.cos(2 * np.pi * x_norm[i])
        
        # Cross-term interaction with dynamic coupling and phase modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.5 * np.sin(0.4 * (i + j)) * np.cos(0.6 * i * j) * np.sin(0.2 * self.chaotic_seq[i])
                phase_shift = np.cos(0.5 * (i - j)) * np.sin(0.3 * self.chaotic_seq[j])
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * (1 + 0.1 * phase_shift)
        
        # Add gradient perturbation field
        grad_pert = 0.0
        for i in range(self.dim):
            grad_pert += 0.1 * np.sin(5 * x_norm[i]) * np.cos(3 * self.chaotic_seq[i])
        
        # Combine with dynamic weights based on chaotic sequence and perturbation
        weight1 = 0.3 + 0.2 * np.sin(0.4 * self.chaotic_seq[0])
        weight2 = 0.25 + 0.2 * np.cos(0.3 * self.chaotic_seq[1])
        weight3 = 0.2 + 0.15 * np.sin(0.5 * self.chaotic_seq[2])
        weight4 = 0.15 + 0.1 * np.cos(0.6 * self.chaotic_seq[3])
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + 0.05 * grad_pert