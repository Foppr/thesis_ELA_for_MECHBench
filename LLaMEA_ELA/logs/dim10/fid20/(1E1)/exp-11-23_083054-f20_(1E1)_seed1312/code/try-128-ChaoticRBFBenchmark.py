import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate extended chaotic sequence using multiple map types
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 15):
            # Alternate between logistic and sine map for increased complexity
            if i % 2 == 0:
                val = 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1])
            else:
                val = 1.5 * np.sin(self.chaotic_seq[-1]) * np.cos(self.chaotic_seq[-1])
            self.chaotic_seq = np.append(self.chaotic_seq, val)
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF with chaotic centers and dynamic widths
        rbfs = []
        for i in range(self.dim):
            center = (self.chaotic_seq[i] - 0.5) * 2  # Map to [-1, 1]
            width = 0.5 + 0.5 * np.sin(2 * np.pi * self.chaotic_seq[i])
            rbfs.append(np.exp(-10 * (x_norm[i] - center)**2 / width))
        f1 = np.sum(rbfs)
        
        # Multi-chaos dynamics component with multiple map types
        f2 = 0.0
        for i in range(self.dim):
            # Apply different chaotic maps based on dimension
            if i % 3 == 0:
                chaotic_val = 4 * x_norm[i] * (1 - x_norm[i])
            elif i % 3 == 1:
                chaotic_val = np.sin(3 * x_norm[i]) * np.cos(x_norm[i])
            else:
                chaotic_val = 3.5 * x_norm[i] * (1 - x_norm[i]**2)
            f2 += np.sin(20 * chaotic_val) ** 3 + 0.5 * np.cos(10 * chaotic_val)
        
        # Asymmetric polynomial with variable exponents and chaotic modulation
        f3 = 0.0
        for i in range(self.dim):
            exp_mod = 1 + 0.5 * np.sin(3 * self.chaotic_seq[i])
            f3 += (x_norm[i]**(3*exp_mod) + 0.4 * x_norm[i]**(5*exp_mod)) * np.cos(5 * np.pi * x_norm[i])
        
        # Cross-term interaction with dynamic coupling and multi-frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.4 * np.sin(0.5 * (i + j)) * np.cos(0.8 * i * j) * np.sin(0.2 * self.chaotic_seq[i])
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.cos(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Add a fourth chaotic component with higher dimensional coupling
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    coupling = 0.1 * np.sin(0.3 * (i + j + k)) * np.cos(0.4 * i * j * k)
                    f5 += coupling * x_norm[i] * x_norm[j] * x_norm[k]
        
        # Combine with dynamic weights based on chaotic sequence and multi-frequency modulation
        weight1 = 0.3 + 0.2 * np.sin(2 * self.chaotic_seq[0])
        weight2 = 0.25 + 0.15 * np.cos(3 * self.chaotic_seq[1])
        weight3 = 0.2 + 0.2 * np.sin(4 * self.chaotic_seq[2])
        weight4 = 0.15 + 0.1 * np.cos(5 * self.chaotic_seq[3])
        weight5 = 0.1 + 0.05 * np.sin(6 * self.chaotic_seq[4])
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5