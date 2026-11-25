import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Tent map chaotic component with parameter control
        tent_map = 0.0
        a = 1.8  # Chaotic parameter
        for i in range(self.dim):
            tent_map += np.abs(x_scaled[i] * a - np.floor(x_scaled[i] * a + 0.5))
        
        # Polynomial interaction terms with varying degrees
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**3 + x[j]**2) * (x[i] * x[j])**2
        
        # Fractal-like curvature with recursive scaling
        fractal_curvature = 0.0
        for i in range(self.dim):
            fractal_curvature += (np.sin(x[i] * 10) * np.cos(x[i] * 7) + 
                                0.5 * np.sin(x[i] * 23) * np.cos(x[i] * 19) +
                                0.2 * np.sin(x[i] * 41) * np.cos(x[i] * 37))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-np.abs(x[i] - x[j]) * 0.1) * (i + j)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        multi_scale = 0.0
        frequencies = [1, 3, 7, 11, 15]
        for i in range(self.dim):
            for freq in frequencies:
                multi_scale += np.sin(x[i] * freq) * np.cos(x[i] * freq * 0.7)
        
        # Asymmetric landscape with different behavior in positive and negative regions
        asymmetry = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asymmetry += 0.3 * np.sin(x[i] * 2) + 0.1 * np.cos(x[i] * 5)
            else:
                asymmetry += 0.4 * np.sin(x[i] * 3) + 0.2 * np.cos(x[i] * 7)
        
        # Combine all components with adaptive weights
        result = (tent_map * 2.0 + 
                 poly_interaction * 0.01 + 
                 fractal_curvature * 0.5 + 
                 cross_coupling * 0.1 + 
                 multi_scale * 0.3 + 
                 asymmetry * 0.4)
        
        # Add a global shift to ensure the minimum is not at the origin
        return result + 10.0