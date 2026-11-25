import numpy as np

class DynamicHarmonicBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Dynamic frequency modulation based on dimension index
            freq = 2.0 + 1.5 * np.sin(i * 0.6) * np.cos(i * 0.3) + \
                   0.8 * np.sin(i * 1.2) * np.cos(i * 0.9)
            
            # Asymmetric harmonic contributions with fractal-like behavior
            h1 = np.sin(freq * xi + i * 0.5) * np.cos(1.3 * xi + i * 0.2)
            h2 = np.sin(2.1 * freq * xi + i * 0.7) * np.cos(1.8 * xi + i * 0.4)
            h3 = np.sin(3.7 * freq * xi + i * 1.1) * np.cos(2.5 * xi + i * 0.6)
            
            # Fractal-like coupling with asymmetric interaction weights
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    dist = abs(xi - x_norm[j])
                    weight = 0.6 * np.sin(i * 0.8 + j * 0.5) * np.cos(i * 0.3 + j * 0.7)
                    coupling += weight * np.exp(-dist**1.5) * (np.sin(xi + x_norm[j]) + 0.5 * np.cos(xi - x_norm[j]))
            
            # Asymmetric conditioning factor with dynamic phase
            cond_factor = 1.0 + 0.8 * np.sin(i * 0.7) * np.cos(i * 0.4) + \
                         0.4 * np.sin(i * 1.3) * np.cos(i * 0.9) + \
                         0.3 * np.sin(i * 2.1) * np.cos(i * 1.5)
            
            # Combined term with asymmetric scaling
            term = cond_factor * (h1 + 0.7 * h2 + 0.3 * h3 + 0.5 * coupling)**2
            
            result += term
            
        # Global fractal-like modulation with multi-scale interference
        global_mod = 0.0
        for k in range(1, 6):
            scale = 0.8 / k
            phase = k * 0.4 + 0.3 * np.sin(k * 0.7)
            global_mod += scale * np.sin(np.sum(x_norm**k) * phase) * np.cos(np.mean(np.abs(x_norm)) * k * 0.5)
        
        # Dimension-dependent basin asymmetry
        asymmetry = 1.0 + 0.6 * np.sin(self.dim * 0.9) * np.cos(self.dim * 0.4) + \
                   0.3 * np.sin(self.dim * 1.7) * np.cos(self.dim * 1.2)
        
        return asymmetry * (result / self.dim + global_mod * 0.5)