import numpy as np

class DynamicResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Dynamic gradient modulation with adaptive curvature
            curvature = 1.0 + 0.5 * np.sin(3.0 * xi + i * 0.7) + 0.3 * np.cos(2.0 * xi - i * 0.4)
            
            # Adaptive resonance peaks with dimensionally coupled frequencies
            peak_height = 2.0 + 1.5 * np.sin(i * 0.8 + 1.2) + 0.8 * np.cos(i * 0.6 - 0.9)
            peak_width = 0.3 + 0.2 * np.sin(i * 0.5 + 0.3) + 0.1 * np.cos(i * 0.4 + 0.7)
            
            # Resonance peak function with dynamic center position
            center = 0.5 * np.sin(i * 0.9 + 0.2) + 0.3 * np.cos(i * 0.6 + 0.5)
            resonance = peak_height * np.exp(-0.5 * ((xi - center) / peak_width)**2)
            
            # Multi-scale interference pattern with cross-dimensional coupling
            interference = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling_strength = 0.1 + 0.05 * np.sin(i * 0.3 + j * 0.4)
                    interference += coupling_strength * np.sin(5.0 * (xi - x_norm[j]) + 2.0 * i + 1.5 * j)
            
            # Dimensionally adaptive weighting with nonlinear transformation
            weight = 1.0 + 0.4 * np.sin(i * 0.7) * np.cos(self.dim * 0.2) + 0.2 * np.cos(i * 0.5)
            
            # Adaptive noise modulation for increased complexity
            noise_modulation = 0.1 + 0.05 * np.sin(xi * 3.0 + i * 0.8)
            
            # Combined function with dynamic scaling
            combined = weight * (curvature * resonance + 0.5 * interference + noise_modulation * np.sin(7.0 * xi + 3.0 * i))
            result += combined**2
            
        # Global dimension-dependent scaling with adaptive complexity factor
        complexity_factor = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 1.5) + 0.2 * np.cos(np.log(self.dim + 1) * 2.3)
        return complexity_factor * result / self.dim