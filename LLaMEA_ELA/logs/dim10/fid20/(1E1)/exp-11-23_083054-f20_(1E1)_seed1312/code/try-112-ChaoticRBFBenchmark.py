import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic sequence using multiple map types for increased complexity
        self.chaotic_seq = np.zeros(dim)
        x1, x2, x3 = 0.5, 0.5, 0.5
        for i in range(dim):
            x1 = 4 * x1 * (1 - x1)  # Logistic map
            x2 = 3.8 * x2 * (1 - x2)  # Sine map
            x3 = 3.5 * x3 * np.sin(np.pi * x3)  # Sinusoidal map
            self.chaotic_seq[i] = (x1 + x2 + x3) / 3.0
            
        # Precompute basis centers and weights
        self.centers = np.array([(self.chaotic_seq[i] - 0.5) * 2 for i in range(dim)])
        self.weights = np.array([0.2 + 0.1 * np.sin(0.5 * i) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-modal RBF component with chaotic centers and variable widths
        f1 = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            width = 0.5 + 0.5 * np.sin(0.3 * i)  # Dynamic width
            f1 += np.exp(-width * (x_norm[i] - center)**2) * (1 + 0.3 * np.cos(5 * x_norm[i]))
        
        # Multi-chaotic dynamics component with different map types
        f2 = 0.0
        for i in range(self.dim):
            chaotic_val1 = 4 * x_norm[i] * (1 - x_norm[i])  # Logistic
            chaotic_val2 = 3.8 * x_norm[i] * (1 - x_norm[i])  # Sine
            chaotic_val3 = 3.5 * x_norm[i] * np.sin(np.pi * x_norm[i])  # Sinusoidal
            f2 += np.sin(10 * chaotic_val1) * np.cos(8 * chaotic_val2) + np.tan(0.5 * chaotic_val3)
        
        # Asymmetric polynomial interactions with dynamic exponents
        f3 = 0.0
        for i in range(self.dim):
            exp1 = 3 + 2 * np.sin(0.4 * i)
            exp2 = 5 + 3 * np.cos(0.6 * i)
            f3 += (x_norm[i]**exp1 + 0.5 * x_norm[i]**exp2) * np.cos(2 * np.pi * x_norm[i])
        
        # Cross-term interactions with dynamic coupling and multi-frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.4 * np.sin(0.5 * (i + j)) * np.cos(0.8 * i * j) * np.tan(0.2 * (i - j))
                freq_mod = np.sin(0.7 * x_norm[i]) * np.cos(0.9 * x_norm[j])
                f4 += coupling * x_norm[i] * x_norm[j] * freq_mod * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Combine with dynamic weights based on chaotic sequence
        weight1 = 0.3 + 0.2 * self.chaotic_seq[0]
        weight2 = 0.25 + 0.15 * self.chaotic_seq[1]
        weight3 = 0.2 + 0.1 * self.chaotic_seq[2]
        weight4 = 0.25 + 0.1 * self.chaotic_seq[3]
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4