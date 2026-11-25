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
            
            # Fractal ridge structure with self-similar patterns
            ridge = 0.0
            for k in range(1, 6):
                scale = 2.0 ** (-k)
                freq = 2 ** k
                ridge += scale * np.sin(freq * xi) * np.cos(freq * xi)
            
            # Adaptive curvature field with dimension-dependent scaling
            curvature = 1.0 + 0.5 * np.sin(self.dim * 0.2 + i * 0.3) * np.cos(i * 0.4)
            
            # Cross-dimensional coupling with fractal interaction
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Fractal interaction strength
                    interaction_strength = 1.0 / (1.0 + distance**2)
                    coupling += interaction_strength * np.sin(xi + x_norm[j] + 0.5 * np.cos(i + j))
            
            # Multi-scale harmonic modulation
            modulation = 1.0
            for k in range(1, 4):
                modulation *= (1.0 + 0.3 * np.sin(k * xi + k * 0.2))
            
            # Add to result with adaptive weighting
            weight = 1.0 + 0.4 * np.sin(i * 0.5) * np.cos(self.dim * 0.1 + i)
            
            # Apply chaotic amplification
            chaos_amp = 1.0 + 0.3 * np.sin(np.sum(x_norm**2) + i * 0.2)
            
            result += weight * chaos_amp * (curvature * ridge**2 + 0.5 * coupling)**2
            
        # Global fractal scaling with dimension-dependent correction
        global_scale = 1.0 + 0.25 * np.sin(np.log(self.dim + 1) * 4.0)
        
        # Add hyper-fractal modulation based on all dimensions
        hyper_fractal = 1.0 + 0.2 * np.sin(np.sum(np.abs(x_norm)) * 3.0 + self.dim * 0.3)
        
        return global_scale * hyper_fractal * result / self.dim