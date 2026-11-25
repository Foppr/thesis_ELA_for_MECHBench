import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_seq = np.array([1.0])
        for i in range(dim * 15):
            self.chaotic_seq = np.append(self.chaotic_seq, 4 * self.chaotic_seq[-1] * (1 - self.chaotic_seq[-1]))
        self.chaotic_seq = self.chaotic_seq[1:dim+1]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced sinusoidal oscillation with chaotic frequency modulation and phase shifts
        f1 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 2.5 * np.sin(0.3 * self.chaotic_seq[i])
            phase = 0.2 * np.cos(0.4 * self.chaotic_seq[i])
            f1 += (np.sin(freq * x_norm[i] + phase) ** 2 + 
                   0.3 * np.cos(2 * freq * x_norm[i] + phase) + 
                   0.1 * np.sin(3 * freq * x_norm[i] + phase))
        
        # Modified Gaussian peaks with dynamic positioning and width
        f2 = 0.0
        for i in range(self.dim):
            peak_pos = (self.chaotic_seq[i] - 0.5) * 1.8  # Slightly narrower range
            peak_height = 1.2 + 0.4 * np.sin(2.5 * self.chaotic_seq[i])
            sigma = 0.08 + 0.15 * np.cos(0.6 * i + 0.3 * self.chaotic_seq[i])
            f2 += peak_height * np.exp(-0.5 * ((x_norm[i] - peak_pos) / sigma) ** 2)
        
        # Enhanced cross-dimensional coupling with variable interaction range
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range
                coupling_strength = 0.4 + 0.3 * np.sin(1.5 * self.chaotic_seq[i] + 0.2 * self.chaotic_seq[j])
                distance = (x_norm[i] - x_norm[j]) ** 2
                f3 += coupling_strength * np.exp(-distance / (2 * 0.25**2))
        
        # Novel asymmetric polynomial with chaotic bias and higher-order terms
        f4 = 0.0
        for i in range(self.dim):
            bias = 0.3 * np.sin(2.0 * self.chaotic_seq[i])
            f4 += (x_norm[i]**4 + bias * x_norm[i]**3 + 
                   0.5 * x_norm[i]**2) * np.cos(1.5 * x_norm[i])
        
        # Dynamic weights with more complex chaotic modulation
        weight1 = 0.25 + 0.1 * np.sin(self.chaotic_seq[0] + 0.3)
        weight2 = 0.35 + 0.15 * np.cos(self.chaotic_seq[1] - 0.2)
        weight3 = 0.2 + 0.1 * np.sin(2 * self.chaotic_seq[2] + 0.4)
        weight4 = 0.2 + 0.1 * np.cos(3 * self.chaotic_seq[3] - 0.1)
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4