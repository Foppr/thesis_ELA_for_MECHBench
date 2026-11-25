import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal-like structure with multi-scale self-similarity
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-fractal frequency modulation with chaotic phase
            freq = 1.5 + 4.0 * np.sin(0.3 * self.t + i * 0.5 + np.sin(self.t * 0.7))
            amp = 0.8 + 1.2 * np.cos(0.6 * self.t + i * 0.3 + np.cos(self.t * 0.4))
            # Enhanced fractal pattern with polynomial and trigonometric components
            result += amp * (xi**3) * np.sin(freq * xi) * np.cos(0.1 * xi**4)
            
        # Dynamic cross-dimensional ridge structures with varying coupling strength
        coupling_strength = 2.0 + 1.0 * np.sin(0.8 * self.t)
        for i in range(self.dim):
            for j in range(max(0, i-3), min(i+3, self.dim)):  # Extended coupling range
                if i != j:
                    # Ridge interaction with hyperbolic shaping
                    dist = (x[i] - x[j])**2 + 0.1 * np.abs(x[i] - x[j])
                    ridge = coupling_strength * np.exp(-dist/1.5) * np.sin(2.0 * (x[i] + x[j]) + 0.3 * self.t)
                    result += ridge * (x[i]**2 + x[j]**2 + 0.5 * xi**4)
                
        # Time-varying hyper-elliptic shaping with dynamic eccentricity and skewness
        ellipse_factor = 0.3 + 0.4 * np.cos(0.9 * self.t)
        skew_factor = 0.6 + 0.3 * np.sin(0.5 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Hyper-elliptic terms with skew modulation
            result += ellipse_factor * (xi**5) * np.sin(1.2 * xi + 0.4 * self.t) * np.cos(0.7 * xi**3)
            result += skew_factor * (xi**2) * np.tan(0.3 * xi + 0.2 * self.t)
            
        # Multi-scale chaotic modulation with adaptive phase shifts
        mod_freq = 5.0 + 3.0 * np.sin(1.1 * self.t)
        mod_amp = 1.0 + 0.6 * np.cos(1.0 * self.t)
        modulation = 0.0
        for i in range(self.dim):
            phase_shift = 0.8 * np.sin(0.7 * self.t + i * 0.5 + np.cos(self.t * 0.6))
            modulation += mod_amp * np.sin(mod_freq * x[i] + phase_shift) * (x[i]**4)
            
        # Adaptive weighting with dynamic coefficients
        w1 = 0.8 + 0.15 * np.sin(0.6 * self.t)
        w2 = 0.15 + 0.1 * np.cos(0.7 * self.t)
        w3 = 0.05 + 0.05 * np.sin(0.8 * self.t)
        
        result = w1 * result + w2 * modulation + w3 * np.sum(x**6)
        return result