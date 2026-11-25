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
            
            # Enhanced fractal ridge structure with multi-scale interference
            ridge = 0.0
            for k in range(1, 8):
                scale = 3.0 ** (-k)
                freq = 3 ** k
                ridge += scale * np.sin(freq * xi) * np.cos(freq * xi) * np.sin(k * xi)
            
            # Dynamic curvature field with time-like dimension coupling
            curvature = 1.0 + 0.7 * np.sin(self.dim * 0.3 + i * 0.4) * np.cos(i * 0.5 + self.dim * 0.2)
            
            # Enhanced cross-dimensional coupling with weighted interaction
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Weighted fractal interaction strength
                    interaction_strength = 1.0 / (1.0 + distance**3)
                    coupling += interaction_strength * np.sin(xi + x_norm[j] + 0.7 * np.cos(i + j) + 0.3 * np.sin(i * j))
            
            # Multi-scale harmonic modulation with phase shifts
            modulation = 1.0
            for k in range(1, 5):
                modulation *= (1.0 + 0.4 * np.sin(k * xi + k * 0.3) * np.cos(k * 0.2))
            
            # Adaptive weighting with dynamic phase
            weight = 1.0 + 0.5 * np.sin(i * 0.6 + self.dim * 0.1) * np.cos(self.dim * 0.2 + i * 0.3)
            
            # Chaotic amplification with dimension-dependent chaos
            chaos_amp = 1.0 + 0.4 * np.sin(np.sum(x_norm**3) + i * 0.3 + self.dim * 0.1)
            
            # Add to result with enhanced nonlinearity
            result += weight * chaos_amp * (curvature * ridge**3 + 0.7 * coupling)**2
            
        # Global scaling with enhanced fractal correction
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 2) * 5.0)
        
        # Hyper-fractal modulation with complex interaction
        hyper_fractal = 1.0 + 0.3 * np.sin(np.sum(np.abs(x_norm)) * 4.0 + self.dim * 0.4) * np.cos(np.sum(x_norm**2) * 0.5)
        
        return global_scale * hyper_fractal * result / self.dim