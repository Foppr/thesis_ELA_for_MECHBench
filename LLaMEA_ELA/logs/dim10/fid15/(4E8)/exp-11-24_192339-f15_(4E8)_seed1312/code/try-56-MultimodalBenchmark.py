import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Exponential decay modulations with quaternion-inspired interactions
        exp_mod = 0
        for i in range(self.dim):
            # Quaternion-like cross-dimensional interactions
            interaction = 0
            for j in range(self.dim):
                if i != j:
                    interaction += np.exp(-0.5 * (x[i] - x[j])**2) * np.cos(2 * np.pi * (x[i] + x[j]))
            exp_mod += np.exp(-0.1 * np.abs(x[i])) * np.sin(3 * np.pi * x[i]) * interaction
        
        # Time-varying harmonic components with dynamic frequencies
        harmonic = 0
        for i in range(self.dim):
            freq = 2 + 0.5 * np.sin(0.1 * self.dim + i)
            harmonic += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2) * np.exp(-0.05 * x[i]**2)
        
        # Polynomial cross-terms with mixed powers and dynamic coefficients
        poly_cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-terms for complexity control
                poly_cross += (x[i]**4) * (x[j]**3) * np.cos(0.5 * (i + j)) + \
                              (x[i]**2) * (x[j]**5) * np.sin(0.3 * (i - j))
        
        # Dynamic scaling factor based on dimensionality and position
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1) + 0.03 * np.sin(np.sum(x)**2)
        
        # Chaotic shift component using logistic map dynamics
        chaotic_shift = 0
        for i in range(self.dim):
            chaotic_shift += 0.2 * np.sin(5 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Combined function with enhanced fitness characteristics
        return sphere + scale_factor * (0.15 * exp_mod + 0.02 * harmonic + 0.01 * poly_cross) + chaotic_shift