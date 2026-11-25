import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Fractal ridge structure with adaptive curvature
            curvature = 1.0 + 0.5 * np.sin(i * 0.8 + self.dim * 0.3)
            ridge = curvature * (xi**2 + 0.3 * np.sin(5.0 * xi))
            
            # Adaptive difficulty field with dimension coupling
            difficulty = 1.0 + 0.4 * np.cos(i * 0.6 + self.dim * 0.2)
            
            # Cross-dimensional coupling with fractal interference
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling_strength = 0.15 * np.exp(-abs(i - j) * 0.3)
                    coupling += coupling_strength * np.sin(xi + x_norm[j] + 0.2 * np.cos(i + j))
            
            # Fractal modulation with multi-scale interference
            fractal_mod = np.sin(xi * 7.0 + np.sum(x_norm[:i]) * 0.4) * np.cos(xi * 5.0 + self.dim * 0.3)
            
            # Add to result with adaptive weighting
            weight = 1.0 + 0.2 * np.sin(i * 0.5) * np.cos(self.dim * 0.2 + i * 0.3)
            
            # Apply adaptive amplitude modulation
            amplitude = 1.0 + 0.1 * np.sin(np.sum(x_norm**2) * 0.4 + i * 0.2)
            
            result += weight * amplitude * (difficulty * ridge**2 + 
                                          coupling**2 + 
                                          fractal_mod**2)
            
        # Global scaling with fractal dimension correction
        global_scale = 1.0 + 0.25 * np.sin(np.log(self.dim + 1) * 2.0)
        
        # Add multi-scale superposition
        superposition = 1.0 + 0.2 * np.sin(np.sum(np.abs(x_norm)) * 3.0 + self.dim * 0.3)
        
        return global_scale * superposition * result / self.dim