import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial terms with trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Multi-scale radial polynomial with harmonic modulation
            for i in range(1, min(6, self.dim + 1)):
                poly_term = x[0]**(2*i) + x[1]**(2*i) if self.dim >= 2 else x[0]**(2*i)
                for j in range(2, min(5, self.dim + 1)):
                    if j < self.dim:
                        poly_term += x[j]**(2*i)
                result += (1.0 + 0.3 * np.sin(i * r)) * poly_term * np.exp(-r/4.0)
        
        # Trigonometric coupling with dynamic scaling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                angle_diff = np.arccos(np.clip((xi * xj) / (np.sqrt(xi**2 + 1e-8) * np.sqrt(xj**2 + 1e-8)), -1.0, 1.0))
                coupling = np.sin(xi + xj) * np.cos(xi - xj)
                scale_factor = 1.0 + 0.5 * np.sin(angle_diff) * np.cos(angle_diff)
                result += scale_factor * coupling * np.exp(-abs(xi-xj)/3.0)
        
        # Adaptive scaling with polynomial modulation
        for i in range(self.dim):
            xi = x[i]
            poly_mod = xi**5 - 2*xi**3 + xi
            scale_factor = 1.0 + 0.4 * np.cos(xi / 2.0) * np.sin(xi / 3.0)
            result += scale_factor * poly_mod * np.exp(-abs(xi)/2.0)
        
        # Cross-dimensional exponential coupling with angular weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                angle_weight = 0.8 + 0.2 * np.cos(np.arctan2(xj, xi))
                coupling = np.exp(-((xi - xj)**2)/5.0) * np.sin(xi * xj)
                result += angle_weight * coupling
        
        # Multi-scale sinusoidal terms with radial modulation
        for i in range(1, 8):
            freq = i * (1.0 + 0.2 * np.cos(r / 3.0))
            amp = 1.0 + 0.3 * np.sin(i * r / 4.0)
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/5.0)
        
        # High-frequency trigonometric components with dynamic scaling
        for i in range(self.dim):
            xi = x[i]
            freq_term = np.sin(12 * xi) * np.cos(10 * xi)  # Slight frequency change
            result += 0.6 * freq_term * np.exp(-abs(xi)/3.5)
        
        # Fractal-like cross-dimensional interactions with modified factor
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                fractal_factor = 1.0 + 0.25 * np.sin(18 * (xi**2 + xj**2))  # Increased frequency
                result += fractal_factor * np.exp(-abs(xi-xj)/4.0) * np.cos(5*(xi+xj))
        
        # Enhanced radial polynomial with angular coupling
        for i in range(self.dim):
            xi = x[i]
            poly = xi**6 - 3*xi**4 + 3*xi**2 - 1
            result += 0.7 * poly * np.sin(xi) * np.exp(-abs(xi)/5.0)
        
        # Dynamic scaling based on radial distance with trigonometric modulation
        dynamic_factor = 1.0 + 0.6 * np.cos(r / 3.0) * np.sin(r / 5.0)
        result *= dynamic_factor
        
        return result