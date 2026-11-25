import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for temporal modulation
        self.chaotic_seq = np.zeros(dim)
        r = 3.9
        x = 0.5
        for i in range(dim):
            x = r * x * (1 - x)
            self.chaotic_seq[i] = x
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial activation with dynamic weights
        poly_activation = 0.0
        for i in range(self.dim):
            weight = np.sin(i * 0.5) * np.cos(i * 0.3) + 1.5
            poly_activation += weight * (x_norm[i] ** 3 + x_norm[i] ** 2)
        
        # Dynamic coupling with chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight based on position and sequence
                w = (np.sin(x_norm[i] * self.chaotic_seq[i]) + 
                     np.cos(x_norm[j] * self.chaotic_seq[j]) + 
                     2.0) / 4.0
                coupling += w * np.sin(5 * (x_norm[i] - x_norm[j]))
        
        # Multi-scale sinusoidal modulation with exponential decay
        modulated = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 5)
            amp = np.exp(-0.1 * i)
            modulated += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial basis with dynamic centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.7) * np.cos(i * 0.9)
            width = 0.1 + 0.2 * np.sin(i * 0.4)
            radial += np.exp(-0.5 * ((x_norm[i] - center) / width)**2)
        
        # Exponential fitness landscape with sharp transitions
        exp_landscape = 0.0
        for i in range(self.dim):
            exp_landscape += np.exp(2 * np.abs(x_norm[i])) * np.sin(10 * x_norm[i])
        
        # Cross-dimensional interaction with sigmoidal coupling
        sigmoid_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_norm[i] - x_norm[j]
                sigmoid_coupling += (1 / (1 + np.exp(-diff))) * np.cos(3 * diff)
        
        # Combine all components with adaptive coefficients
        return (0.25 * poly_activation + 0.2 * coupling + 
                0.15 * modulated + 0.15 * radial + 
                0.1 * exp_landscape + 0.15 * sigmoid_coupling)