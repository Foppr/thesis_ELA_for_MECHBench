import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Chaotic gradient modulation using logistic map
        chaotic_mod = 1.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            # Logistic map for chaotic behavior
            if i == 0:
                x_log = 0.5
            else:
                x_log = (r * x_scaled[i-1] * (1 - x_scaled[i-1])) if i > 0 else 0.5
            chaotic_mod *= (1 + 0.3 * np.sin(2 * np.pi * x_log) + 
                           0.2 * np.cos(3 * np.pi * x_log))
        
        # Polynomial interaction terms with varying degrees
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like polynomial interaction
                poly_interaction += (x_scaled[i]**2 + x_scaled[j]**3 + 
                                   0.5 * x_scaled[i] * x_scaled[j]**2 + 
                                   0.3 * x_scaled[i]**3 * x_scaled[j]) * (i + j + 1)
        
        # Multimodal component with fractal-like self-similarity
        fractal_modal = 0.0
        for i in range(self.dim):
            # Self-similar pattern with multiple frequencies
            fractal_modal += (np.sin(2 * x[i]) + 
                             0.5 * np.sin(4 * x[i]) + 
                             0.3 * np.sin(8 * x[i]) + 
                             0.1 * np.sin(16 * x[i]) + 
                             0.2 * np.cos(3 * x[i]) * np.cos(6 * x[i]))
        
        # Cross-dimensional coupling with varying weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (np.sin(x[i] + x[j]) * 
                                 np.cos(x[i] - x[j]) * 
                                 (i + j + 1) * 0.5)
        
        # Combined function with chaotic modulation
        result = chaotic_mod * (poly_interaction + fractal_modal + cross_coupling)
        
        # Add constant offset to ensure positive fitness values for minimization
        return result + 10.0