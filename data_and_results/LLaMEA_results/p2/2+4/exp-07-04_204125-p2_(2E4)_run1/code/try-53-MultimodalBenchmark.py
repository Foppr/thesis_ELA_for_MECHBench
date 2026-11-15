import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractional Brownian motion
        self.hurst = 0.3 + 0.4 * np.random.random()
        self.fbm_scale = 0.5 + 0.5 * np.random.random()
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Fractional Brownian motion induced roughness
        fbm_term = 0.0
        for i in range(self.dim):
            # Simple fractal-like term with varying scaling
            fbm_term += self.fbm_scale * np.sin(2.0 * np.pi * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Periodic attractor wells with adaptive depth
        well_term = 0.0
        for i in range(self.dim):
            # Multiple periodic wells with varying depths and widths
            well_depth = 1.0 + 0.5 * np.sin(i * 0.5)
            well_width = 0.5 + 0.3 * np.cos(i * 0.3)
            well_term += well_depth * np.exp(-0.5 * ((x[i] - np.sin(i * 0.7)) / well_width)**2)
        
        # Chaotic gradient modulation with dimensionality scaling
        grad_mod = 0.0
        for i in range(self.dim):
            # Adaptive gradient modulation with chaotic phase
            phase = np.sin(3.0 * x[i] + i * 0.8) + 0.5 * np.sin(7.0 * x[i] + i * 0.3)
            grad_mod += np.cos(x[i]) * phase * np.exp(-0.05 * x[i]**2)
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combined terms
        result = cond_factor * (0.3 * np.sum(x**2) + 0.4 * np.sum(np.abs(x)**1.7) + 
                               0.2 * well_term + 0.1 * fbm_term + 0.05 * grad_mod)
        
        # Add cross-dimensional coupling with adaptive weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 * np.exp(-0.1 * (i - j)**2)
                cross_term += weight * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        result += 0.15 * cross_term
        
        # Add non-smooth perturbations with fractal characteristics
        perturbation = 0.0
        for i in range(self.dim):
            perturbation += 0.03 * np.abs(x[i])**1.8 + 0.02 * np.sin(10.0 * x[i])
        
        result += perturbation
        
        # Final scaling with dimensionality
        result *= (1.0 + 0.1 * np.log(self.dim + 1))
        
        return result