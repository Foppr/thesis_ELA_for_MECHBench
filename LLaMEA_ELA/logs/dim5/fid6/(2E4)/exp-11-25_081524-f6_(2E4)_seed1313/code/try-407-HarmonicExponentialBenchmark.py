import numpy as np

class HarmonicExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial harmonic oscillations with adaptive frequency
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for i in range(1, min(6, self.dim + 1)):
                freq = i * (1.0 + 0.3 * np.sin(r / 4.0))
                amp = 1.0 + 0.2 * np.cos(i * r / 3.0)
                result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r**2 / 20.0)
        
        # Cross-dimensional exponential coupling with sigmoidal scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_coupling = np.exp(-((xi - xj)**2 + (xi + xj)**2) / 5.0)
                sigmoid_scale = 1.0 / (1.0 + np.exp(-0.5 * (xi + xj)))
                result += exp_coupling * sigmoid_scale * (1.0 + 0.1 * np.sin(3.0 * xi) * np.cos(4.0 * xj))
        
        # Adaptive polynomial with harmonic modulation
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 5*xi**4 + 10*xi**2 - 1
            harmonic_mod = 1.0 + 0.3 * np.sin(2.0 * xi) * np.cos(3.0 * xi)
            poly_sum += poly_term * harmonic_mod
        result += 0.5 * poly_sum * np.exp(-r / 10.0)
        
        # Multi-scale exponential terms with angular coupling
        for i in range(1, 5):
            scale = 2.0 ** i
            freq = i * (1.0 + 0.2 * np.cos(r / 3.0))
            result += np.exp(-scale * r**2 / 25.0) * np.sin(freq * r) * np.cos(freq * r)
        
        # Sigmoidal radial scaling with cross-dimensional interactions
        for i in range(self.dim):
            xi = x[i]
            sigmoid_term = 1.0 / (1.0 + np.exp(-xi / 2.0))
            result += sigmoid_term * (xi**3 - 2*xi) * np.exp(-abs(xi) / 5.0)
        
        # Fractal-like exponential coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = (1.0 + 0.2 * np.sin(xi) * np.cos(xj))
                result += weight * np.exp(-((xi - xj)**2) / 3.0) * np.sin(xi + xj)
        
        # High-order harmonic polynomial with radial coupling
        harmonic_poly = 0.0
        for i in range(self.dim):
            xi = x[i]
            harmonic_poly += (np.sin(xi) + 0.5 * np.cos(2*xi))**4
        result += 0.3 * harmonic_poly * np.exp(-r / 8.0)
        
        # Adaptive angular harmonic terms with exponential decay
        for i in range(self.dim):
            xi = x[i]
            angle_term = np.sin(xi) * np.cos(xi)
            adaptive_weight = 1.0 + 0.4 * np.sin(2.0 * xi) * np.cos(3.0 * xi)
            result += adaptive_weight * angle_term * np.exp(-abs(xi) / 4.0)
        
        return result