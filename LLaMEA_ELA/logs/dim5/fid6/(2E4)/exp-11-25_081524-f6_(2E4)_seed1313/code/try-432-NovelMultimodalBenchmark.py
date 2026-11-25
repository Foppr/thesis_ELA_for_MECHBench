import numpy as np

class NovelMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial sinusoidal components with varying amplitudes
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for i in range(1, min(5, self.dim + 1)):
                amp = 1.0 + 0.5 * np.sin(i * r / 3.0)
                freq = i * (2.0 + 0.3 * np.cos(r / 4.0))
                radial_term = amp * np.sin(freq * r) * np.cos(freq * r)
                result += radial_term * np.exp(-r**2 / 25.0)
        
        # Cross-dimensional cubic coupling terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling scope
                xi = x[i]
                xj = x[j]
                coupling = (xi**3 + xj**3) * np.sin(xi * xj)
                result += coupling * np.exp(-((xi - xj)**2) / 4.0)
        
        # Adaptive polynomial scaling with exponential modulation
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 15*xi**4 + 75*xi**2 - 125
            exp_mod = np.exp(-xi**2 / 8.0)
            poly_sum += poly_term * exp_mod
        result += 0.3 * poly_sum
        
        # Multi-scale fractal-like interactions
        for i in range(1, 4):
            scale = 2.0 ** i
            freq = i * (1.5 + 0.2 * np.sin(r / 2.0))
            fractal_term = np.sin(freq * r) * np.cos(freq * r)
            result += fractal_term * np.exp(-scale * r**2 / 30.0)
        
        # Sigmoidal cubic interactions
        for i in range(self.dim):
            xi = x[i]
            sig = 1.0 / (1.0 + np.exp(-xi / 3.0))
            cubic_term = xi**3 - 3*xi
            result += sig * cubic_term * np.exp(-abs(xi) / 6.0)
        
        # Angular harmonic with radial dependency
        angular_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            angle = np.arctan2(x[(i+1) % self.dim], xi) if self.dim > 1 else 0.0
            angular_harmonic = np.sin(3.0 * angle) * np.cos(2.0 * angle)
            angular_sum += angular_harmonic
        result += 0.4 * angular_sum * np.exp(-r / 12.0)
        
        # High-order harmonic with modified amplitude
        high_order_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            high_order = xi**8 - 12*xi**6 + 54*xi**4 - 108*xi**2 + 81
            amp_mod = 1.0 + 0.3 * np.sin(xi / 2.0)
            high_order_sum += high_order * amp_mod
        result += 0.2 * high_order_sum * np.exp(-r**2 / 20.0)
        
        return result