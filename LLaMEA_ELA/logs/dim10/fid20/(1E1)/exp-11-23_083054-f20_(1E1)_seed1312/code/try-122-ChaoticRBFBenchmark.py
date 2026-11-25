import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate longer chaotic sequence for enhanced complexity
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 20):
            self.chaotic_seq = np.append(self.chaotic_seq, 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1]))
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF with frequency-modulated centers
        rbfs = []
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            freq_mod = 1 + 0.5 * np.sin(2 * np.pi * i / self.dim)
            rbfs.append(freq_mod * np.exp(-20 * (x_norm[i] - center)**2))
        f1 = np.sum(rbfs)
        
        # Multiple logistic map dynamics with different growth rates
        f2 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Apply multiple logistic maps with varying parameters
                r1 = 3.8 + 0.2 * np.sin(0.5 * i)
                r2 = 3.9 + 0.1 * np.cos(0.3 * i)
                chaotic_val1 = r1 * x_norm[i] * (1 - x_norm[i])
                chaotic_val2 = r2 * x_norm[i+1] * (1 - x_norm[i+1])
                f2 += np.sin(20 * chaotic_val1) ** 2 + np.cos(15 * chaotic_val2) ** 2
        
        # Asymmetric polynomial with time-varying exponents
        f3 = 0.0
        for i in range(self.dim):
            exp_mod = 3 + 2 * np.sin(0.4 * i)
            f3 += (x_norm[i]**exp_mod + 0.4 * x_norm[i]**(exp_mod + 2)) * np.cos(4 * np.pi * x_norm[i])
        
        # Cross-term interaction with dynamic coupling and phase shifts
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.5 * np.sin(0.5 * (i + j)) * np.cos(0.8 * i * j)
                phase_shift = 0.2 * np.sin(0.6 * i) * np.cos(0.4 * j)
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2 + phase_shift)
        
        # Dynamic weights based on chaotic sequence with higher frequency modulation
        weight1 = 0.3 + 0.2 * np.sin(3 * self.chaotic_seq[0])
        weight2 = 0.4 + 0.15 * np.cos(2 * self.chaotic_seq[1])
        weight3 = 0.2 + 0.25 * np.sin(4 * self.chaotic_seq[2])
        weight4 = 0.1 + 0.15 * np.cos(5 * self.chaotic_seq[3])
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4