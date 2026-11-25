import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Chaotic phase modulation component using logistic map
        chaotic_phase = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x_scaled[i]
            else:
                x_prev = x_scaled[i-1]
            chaotic_phase += np.sin(r * x_prev * (1 - x_prev)) * np.cos(x_scaled[i])
        
        # Polynomial interaction terms with varying degrees
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_scaled[i]**2 + x_scaled[j]**3) * (i + j + 1)
                
        # Fractal-like self-similarity pattern with recursive scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(x_scaled[i] * (1 + 0.5 * np.sin(x_scaled[i] * 2))) * (i + 1)
            
        # Cross-dimensional coupling with exponential decay
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.exp(-abs(x_scaled[i] - x_scaled[j]) / (i + j + 1)) * (i + j + 1)
                
        # Multi-scale sinusoidal modulation with different frequencies
        multi_scale = 0.0
        scales = [1, 2, 3, 4]
        for scale in scales:
            for i in range(self.dim):
                multi_scale += np.sin(x_scaled[i] * scale) * np.cos(x_scaled[i] * scale * 0.5)
                
        # Combine all components with adaptive weights
        return (1.5 * chaotic_phase + 
                2.0 * poly_interaction + 
                0.8 * fractal_term + 
                1.2 * coupling_term + 
                0.6 * multi_scale + 
                3.0)