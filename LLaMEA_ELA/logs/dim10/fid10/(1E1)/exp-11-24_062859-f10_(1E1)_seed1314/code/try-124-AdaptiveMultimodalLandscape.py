import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for adaptive conditioning
        self.conditioning_factors = np.linspace(1.0, 10.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive conditioning
        result = np.sum(self.conditioning_factors * x**4) / 100.0
        
        # Trigonometric component with varying frequencies
        for i in range(self.dim):
            result += 3.0 * np.sin(2.5 * x[i])**2 + 2.0 * np.cos(3.0 * x[i])**2
            
        # Radial basis function component with dynamic centers
        rb_result = 0.0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i, center in enumerate(centers):
            if i < self.dim:
                rb_result += np.exp(-0.5 * (x[i] - center)**2) * np.sin(5 * (x[i] - center))
        result += 1.5 * rb_result
        
        # Adaptive coupling between dimensions
        coupling_strength = 0.8
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.abs(x[i] - x[j])
                result += coupling_strength * np.exp(-dist**2) * np.sin(4 * (x[i] + x[j]))
                
        # Asymmetric polynomial with dynamic exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.7 * x[i]**3.5 * np.exp(-0.1 * x[i])
            else:
                result += 0.25 * x[i]**4.2 * np.exp(-0.15 * np.abs(x[i]))
                
        # Multi-scale harmonic component
        for i in range(self.dim):
            result += 1.8 * np.sin(7 * x[i]) * np.cos(11 * x[i]) * np.sin(3 * x[i]**2)
            
        # Dynamic symmetry breaking term
        symmetry_break = 0.0
        for i in range(self.dim):
            symmetry_break += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]) * (i + 1) / self.dim
        result += 0.6 * symmetry_break
        
        # Add small noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result