import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - encourages convergence to center
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal grid terms - create multiple local minima in a grid pattern
        grid_terms = 0.0
        for i in range(self.dim):
            # Create chaotic periodic structure with varying frequencies
            freq1 = 0.7 + 0.3 * np.sin(0.5 * i)
            freq2 = 0.5 + 0.2 * np.cos(0.3 * i)
            grid_terms += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            
            # Add higher frequency components for increased complexity
            grid_terms += 0.4 * np.sin(3.0 * x[i]) * np.cos(2.5 * x[i])
            
            # Add cross-terms between dimensions with chaotic coupling coefficients
            if i > 0:
                coupling1 = 0.15 + 0.05 * np.sin(0.4 * i)
                coupling2 = 0.12 + 0.08 * np.cos(0.6 * i)
                grid_terms += coupling1 * np.sin(coupling2 * x[i-1]) * np.cos(coupling2 * x[i])
            
            # Add additional nonlinear interaction terms with adaptive scaling
            adaptive_scale = 0.2 + 0.1 * np.sin(0.8 * i)
            grid_terms += adaptive_scale * np.sin(1.5 * x[i])**2
            
            # Introduce chaotic modulation based on position
            chaos_mod = 1.0 + 0.3 * np.sin(2.0 * x[i])
            grid_terms += 0.1 * chaos_mod * np.sin(2.2 * x[i]) * np.cos(1.8 * x[i])
        
        # Add chaotic interaction terms between all dimensions
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < self.dim and j < self.dim:
                    coupling_strength = 0.05 + 0.02 * np.sin(0.3 * (i + j))
                    chaotic_interaction += coupling_strength * np.sin(x[i]) * np.cos(x[j])
        
        # Combine terms with different weights to create challenging landscape
        return basin + 0.7 * grid_terms + 1.8 * np.sum(np.abs(x)) / self.dim + 0.5 * chaotic_interaction