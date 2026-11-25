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
            for i in range(1, min(6, self.dim + 1)):
                amp = 1.0 + 0.4 * np.sin(i * r / 2.5)
                freq = i * (2.5 + 0.4 * np.cos(r / 3.0))
                radial_term = amp * np.sin(freq * r) * np.cos(freq * r)
                result += radial_term * np.exp(-r**2 / 30.0)
        
        # Cross-dimensional cubic coupling terms with enhanced interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling scope for better control
                xi = x[i]
                xj = x[j]
                coupling = (xi**3 + xj**3) * np.sin(xi * xj)
                result += coupling * np.exp(-((xi - xj)**2) / 5.0)
        
        # Adaptive polynomial scaling with exponential modulation
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 15*xi**4 + 75*xi**2 - 125
            exp_mod = np.exp(-xi**2 / 10.0)
            poly_sum += poly_term * exp_mod
        result += 0.25 * poly_sum
        
        # Multi-scale fractal-like interactions with modified scaling
        for i in range(1, 5):
            scale = 1.5 ** i
            freq = i * (1.8 + 0.3 * np.sin(r / 3.0))
            fractal_term = np.sin(freq * r) * np.cos(freq * r)
            result += fractal_term * np.exp(-scale * r**2 / 40.0)
        
        # Sigmoidal cubic interactions with modified parameters
        for i in range(self.dim):
            xi = x[i]
            sig = 1.0 / (1.0 + np.exp(-xi / 2.5))
            cubic_term = xi**3 - 3*xi
            result += sig * cubic_term * np.exp(-abs(xi) / 5.0)
        
        # Angular harmonic with radial dependency and modified coefficients
        angular_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            angle = np.arctan2(x[(i+1) % self.dim], xi) if self.dim > 1 else 0.0
            angular_harmonic = np.sin(4.0 * angle) * np.cos(3.0 * angle)
            angular_sum += angular_harmonic
        result += 0.35 * angular_sum * np.exp(-r / 10.0)
        
        # High-order harmonic with modified amplitude and scaling
        high_order_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            high_order = xi**8 - 12*xi**6 + 54*xi**4 - 108*xi**2 + 81
            amp_mod = 1.0 + 0.25 * np.sin(xi / 1.5)
            high_order_sum += high_order * amp_mod
        result += 0.25 * high_order_sum * np.exp(-r**2 / 25.0)
        
        return result