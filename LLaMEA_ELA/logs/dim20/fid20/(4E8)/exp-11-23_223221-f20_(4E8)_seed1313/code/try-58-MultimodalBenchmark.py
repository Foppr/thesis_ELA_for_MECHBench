import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Modified polynomial potential terms with non-uniform exponents
        poly_term = 0.0
        for i in range(self.dim):
            exp = 2 + (i % 5)  # Exponents: 2, 3, 4, 5, 6, 2, 3, ...
            poly_term += 0.1 * (x[i] ** exp)
        
        # Enhanced trigonometric coupling with frequency modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod = 1.0 + 0.2 * np.sin(0.5 * i) * np.cos(0.3 * j)
                trig_coupling += 0.06 * np.sin(freq_mod * (x[i] + x[j])) * np.cos(freq_mod * x[i] * x[j])
        
        # Adaptive noise with dimensionally varying frequency - mutated version
        noise = 0.0
        for i in range(self.dim):
            freq = 8 + i % 3  # Varying frequencies: 8, 9, 10, 8, 9, ...
            # Mutated: replaced sin*cos product with Gaussian-like envelope
            noise += 0.025 * np.exp(-0.5 * (freq * x[i])**2) * (1 + 0.15 * i)
        
        # Cross-dimensional interaction with weighted exponential decay - slightly modified weights
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)  # Avoid singularity
                # Mutated: slightly increased weight coefficient
                weight = 1.0 / (1.0 + 0.5 * i + 0.3 * j)
                interaction += weight * 0.06 * np.exp(-dist) * np.sin(3 * x[i]) * np.cos(2 * x[j])
        
        # Global shaping term with multi-scale sinusoidal modulation
        global_shape = 0.0
        for i in range(self.dim):
            scale1 = 0.5 + 0.5 * np.sin(0.4 * x[i])
            scale2 = 1.0 + 0.3 * np.cos(0.6 * x[i])
            global_shape += 0.05 * scale1 * scale2 * (x[i]**2 + 1) * np.sin(0.2 * x[i])
        
        return poly_term + trig_coupling + noise + interaction + global_shape