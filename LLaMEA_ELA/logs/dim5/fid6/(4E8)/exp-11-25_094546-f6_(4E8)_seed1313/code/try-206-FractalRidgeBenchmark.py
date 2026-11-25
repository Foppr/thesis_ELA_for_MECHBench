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
            
            # Enhanced adaptive curvature field with increased nonlinearity
            curvature = 1.0 + 0.8 * np.sin(self.dim * 0.25 + i * 0.35) * np.cos(i * 0.45)
            
            # Modified cross-dimensional coupling with altered interaction weights
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Modified interaction strength
                    interaction_strength = 1.0 / (1.0 + distance**3)
                    coupling += interaction_strength * np.sin(xi + x_norm[j] + 0.7 * np.cos(i + j))
            
            # Enhanced multi-scale harmonic modulation
            modulation = 1.0
            for k in range(1, 4):
                modulation *= (1.0 + 0.4 * np.sin(k * xi + k * 0.25))
            
            # Add to result with modified weighting
            weight = 1.0 + 0.6 * np.sin(i * 0.55) * np.cos(self.dim * 0.12 + i)
            
            # Apply enhanced chaotic amplification
            chaos_amp = 1.0 + 0.4 * np.sin(np.sum(x_norm**2) + i * 0.25)
            
            result += weight * chaos_amp * (curvature * ridge**2 + 0.7 * coupling)**2
            
        # Global fractal scaling with modified dimension-dependent correction
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 4.5)
        
        # Add enhanced hyper-fractal modulation based on all dimensions
        hyper_fractal = 1.0 + 0.25 * np.sin(np.sum(np.abs(x_norm)) * 3.5 + self.dim * 0.35)
        
        return global_scale * hyper_fractal * result / self.dim