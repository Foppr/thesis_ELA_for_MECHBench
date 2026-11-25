import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential terms with exponential scaling
        poly_term = 0.0
        for i in range(self.dim):
            exp = 2 + (i % 4)  # Exponents: 2, 3, 4, 5 repeating
            poly_term += 0.15 * (x[i] ** exp) * np.exp(-0.1 * np.abs(x[i]))
        
        # Enhanced trigonometric coupling with frequency modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.2 * np.sin(0.5 * i)
                freq_j = 1.0 + 0.2 * np.cos(0.5 * j)
                trig_coupling += 0.08 * np.sin(freq_i * x[i] + freq_j * x[j]) * np.cos(0.3 * x[i] * x[j])
        
        # Modified adaptive noise with dimension-dependent scaling
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(12 * x[i]) * np.cos(9 * x[i]) * (1 + 0.15 * i)
        
        # Improved cross-dimensional interaction with cosine modulation
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                interaction += 0.04 * np.exp(-dist) * np.cos(3 * x[i]) * np.sin(2 * x[j])
        
        # Refined global shaping term with multi-scale sinusoids
        global_shape = 0.0
        for i in range(self.dim):
            global_shape += 0.05 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i]) * (x[i]**2 + 1) * np.exp(-0.05 * x[i]**2)
        
        return poly_term + trig_coupling + noise + interaction + global_shape