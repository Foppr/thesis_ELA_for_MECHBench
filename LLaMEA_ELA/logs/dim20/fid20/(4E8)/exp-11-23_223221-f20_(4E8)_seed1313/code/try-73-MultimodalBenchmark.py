import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential terms with altered exponents and exponential scaling
        poly_term = 0.0
        for i in range(self.dim):
            exp = 3 + (i % 4)  # Exponents: 3, 4, 5, 6 repeating
            poly_term += 0.25 * (x[i] ** exp) * np.exp(-0.12 * np.abs(x[i]))
        
        # Chaotic trigonometric coupling with frequency modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.5 + 0.4 * np.sin(0.8 * i)
                freq_j = 1.5 + 0.4 * np.cos(0.8 * j)
                trig_coupling += 0.12 * np.sin(freq_i * x[i] + freq_j * x[j]) * np.cos(0.3 * x[i] * x[j])
        
        # Modified adaptive noise with dimension-dependent scaling
        noise = 0.0
        for i in range(self.dim):
            noise += 0.06 * np.sin(14 * x[i]) * np.cos(9 * x[i]) * (1 + 0.25 * i)
        
        # Cross-dimensional interaction with cosine modulation
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.03)
                interaction += 0.07 * np.exp(-dist) * np.cos(3.5 * x[i]) * np.sin(2.5 * x[j])
        
        # Refined global shaping term with multi-scale sinusoids
        global_shape = 0.0
        for i in range(self.dim):
            global_shape += 0.08 * np.sin(0.45 * x[i]) * np.cos(0.35 * x[i]) * (x[i]**2 + 1) * np.exp(-0.09 * x[i]**2)
        
        return poly_term + trig_coupling + noise + interaction + global_shape