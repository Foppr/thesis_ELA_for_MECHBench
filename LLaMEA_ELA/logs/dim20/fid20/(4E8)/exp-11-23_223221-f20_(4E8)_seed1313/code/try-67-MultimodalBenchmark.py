import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms with chaotic scaling
        poly_term = 0.0
        for i in range(self.dim):
            exp = 2 + (i % 3)  # Exponents: 2, 3, 4 repeating
            poly_term += 0.2 * (x[i] ** exp) * np.exp(-0.1 * x[i]**2)
        
        # Trigonometric coupling with chaotic frequency modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.3 * np.sin(0.7 * i + 0.5 * x[i])
                freq_j = 1.0 + 0.3 * np.cos(0.7 * j + 0.5 * x[j])
                trig_coupling += 0.1 * np.sin(freq_i * x[i] + freq_j * x[j]) * np.cos(x[i] * x[j])
        
        # Adaptive noise with chaotic amplitude modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * (1 + 0.2 * np.sin(3 * i))
        
        # Cross-dimensional interaction with exponential decay and sine modulation
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                interaction += 0.06 * np.exp(-dist) * np.sin(2 * x[i]) * np.cos(3 * x[j])
        
        # Global shaping term with multi-scale chaotic sinusoids
        global_shape = 0.0
        for i in range(self.dim):
            global_shape += 0.1 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[i]) * (x[i]**2 + 2) * np.exp(-0.1 * x[i]**2)
        
        return poly_term + trig_coupling + noise + interaction + global_shape