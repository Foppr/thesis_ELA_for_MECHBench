import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Hyper-spherical harmonic potential with adaptive stiffness
            spherical_harmonic = np.sin(xi)**2 + 0.3 * np.cos(3 * xi) + 0.1 * np.sin(5 * xi)
            
            # Fractal basin boundary terms with chaotic resonance
            fractal_term = 0.0
            for k in range(1, 10):
                fractal_term += (1.0 / k**2.5) * np.sin(k * xi + 0.5 * np.cos(k * xi)) * np.exp(-k * np.abs(xi))
            
            # Adaptive stiffness gradient with multi-scale interference
            stiffness = 1.0 + 0.5 * np.sin(self.dim * 0.4 + i * 0.3) + 0.2 * np.cos(self.dim * 0.6 + i * 0.2)
            
            # Multi-modal interaction with fractal interference patterns
            multimodal = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    interference = np.sin(5 * (xi + x_norm[j]) + 0.2 * np.cos(i * j))
                    multimodal += (1.0 / (1.0 + distance**2.0)) * interference
            
            # Chaotic resonance with dimension-dependent scaling
            chaotic_resonance = 0.3 * np.sin(xi * 7.0 + 0.5 * np.cos(xi * 3.0) + 0.2 * np.sin(xi * 11.0))
            
            # Combined weighted contribution
            weight = 1.0 + 0.2 * np.sin(i * 0.5) + 0.1 * np.cos(i * 0.3)
            result += weight * (stiffness * spherical_harmonic + fractal_term + multimodal + chaotic_resonance)**2
            
        # Global scaling with hyperchaotic correction factor
        hyperchaos = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 3.0) + 0.1 * np.cos(np.log(self.dim + 1) * 4.5)
        return hyperchaos * result / self.dim