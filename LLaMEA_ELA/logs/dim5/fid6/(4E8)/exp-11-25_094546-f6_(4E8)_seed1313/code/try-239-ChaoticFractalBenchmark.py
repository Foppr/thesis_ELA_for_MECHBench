import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        # Base quadratic term with adaptive stiffness
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Adaptive stiffness gradient based on position and dimension
            stiffness = 1.0 + 0.5 * np.sin(xi * 3.0) + 0.3 * np.cos(xi * 2.0)
            
            # Fractal basin boundary modulation
            basin_mod = 1.0 + 0.4 * np.sin(7.0 * xi + self.dim * 0.5)
            
            # Chaotic resonance term with dimension coupling
            chaos_term = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling = 0.15 * np.exp(-abs(i - j) * 0.4)
                    chaos_term += coupling * np.sin(xi + x_norm[j] * 2.0 + 0.3 * np.cos(i + j))
            
            # Multi-modal component with fractal interference
            modal_component = xi**4 + 0.8 * np.sin(5.0 * xi) + 0.3 * np.cos(3.0 * xi)
            
            # Combine components with dynamic weighting
            weight = 1.0 + 0.2 * np.sin(i * 0.5 + self.dim * 0.3)
            amplitude = 1.0 + 0.1 * np.cos(xi * 4.0 + i * 0.7)
            
            result += weight * amplitude * (stiffness * basin_mod * modal_component + 
                                          chaos_term**2)
        
        # Global scaling with fractal dimension effect
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 2.5)
        
        # Add chaotic attractor modulation
        attractor_mod = 1.0 + 0.25 * np.sin(np.sum(x_norm**3) * 1.5 + self.dim * 0.4)
        
        # Final normalization and smoothing
        return global_scale * attractor_mod * result / self.dim