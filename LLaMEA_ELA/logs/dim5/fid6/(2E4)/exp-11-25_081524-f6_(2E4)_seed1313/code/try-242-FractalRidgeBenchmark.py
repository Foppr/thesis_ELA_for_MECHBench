import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal-like structure with self-similar patterns
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal frequency modulation
            freq = 2.0 + 3.0 * np.sin(0.5 * self.t + i * 0.3)
            amp = 1.0 + 0.8 * np.cos(0.4 * self.t + i * 0.2)
            # Multi-scale fractal pattern with sine and cosine components
            result += amp * (xi**2) * np.sin(freq * xi) * np.cos(0.2 * xi**3)
            
        # Dynamic ridge structures with varying orientations
        ridge_strength = 1.5 + 0.5 * np.sin(0.6 * self.t)
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for sparsity
                # Ridge-like interaction with elliptic shaping
                dist = (x[i] - x[j])**2
                ridge = ridge_strength * np.exp(-dist/2.0) * np.sin(1.5 * (x[i] + x[j]) + 0.4 * self.t)
                result += ridge * (x[i]**2 + x[j]**2)
                
        # Time-varying elliptic shaping with dynamic eccentricity
        ellipse_factor = 0.5 + 0.3 * np.cos(0.7 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Elliptic terms with varying eccentricity
            result += ellipse_factor * (xi**4) * np.sin(0.8 * xi + 0.3 * self.t) * np.cos(0.6 * xi**2)
            
        # Multi-scale periodic modulation with chaotic phase shifts
        mod_freq = 4.0 + 2.0 * np.sin(0.9 * self.t)
        mod_amp = 0.8 + 0.4 * np.cos(0.8 * self.t)
        modulation = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.6 * self.t + i * 0.4)
            modulation += mod_amp * np.sin(mod_freq * x[i] + phase_shift) * (x[i]**3)
            
        # Adaptive weighting
        w1 = 0.7 + 0.1 * np.sin(0.5 * self.t)
        w2 = 0.2 + 0.1 * np.cos(0.6 * self.t)
        w3 = 0.1 + 0.05 * np.sin(0.7 * self.t)
        
        result = w1 * result + w2 * modulation
        return result