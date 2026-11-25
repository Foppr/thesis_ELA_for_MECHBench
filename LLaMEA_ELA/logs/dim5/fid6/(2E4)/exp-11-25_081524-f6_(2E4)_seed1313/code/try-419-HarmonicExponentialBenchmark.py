import numpy as np

class HarmonicExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced radial harmonic oscillations with dynamic frequency modulation
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for i in range(1, min(8, self.dim + 1)):
                freq = i * (1.5 + 0.5 * np.sin(r / 3.0) * np.cos(r / 7.0))
                amp = 1.2 + 0.3 * np.cos(i * r / 4.0) * np.sin(i * r / 5.0)
                result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r**2 / 15.0)
        
        # Cross-dimensional exponential coupling with enhanced sigmoidal scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_coupling = np.exp(-((xi - xj)**2 + (xi + xj)**2) / 4.0)
                sigmoid_scale = 1.0 / (1.0 + np.exp(-0.7 * (xi + xj)))
                result += exp_coupling * sigmoid_scale * (1.0 + 0.15 * np.sin(4.0 * xi) * np.cos(5.0 * xj))
        
        # Enhanced adaptive polynomial with harmonic modulation
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**7 - 6*xi**5 + 15*xi**3 - 10*xi
            harmonic_mod = 1.0 + 0.4 * np.sin(2.0 * xi) * np.cos(3.0 * xi) * np.sin(5.0 * xi)
            poly_sum += poly_term * harmonic_mod
        result += 0.6 * poly_sum * np.exp(-r / 12.0)
        
        # Multi-scale exponential terms with enhanced angular coupling
        for i in range(1, 7):
            scale = 3.0 ** i
            freq = i * (1.2 + 0.3 * np.cos(r / 4.0) * np.sin(r / 6.0))
            result += np.exp(-scale * r**2 / 30.0) * np.sin(freq * r) * np.cos(freq * r)
        
        # Enhanced sigmoidal radial scaling with cross-dimensional interactions
        for i in range(self.dim):
            xi = x[i]
            sigmoid_term = 1.0 / (1.0 + np.exp(-xi / 1.5))
            result += sigmoid_term * (xi**4 - 3*xi**2) * np.exp(-abs(xi) / 6.0)
        
        # Enhanced fractal-like exponential coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = (1.0 + 0.3 * np.sin(xi) * np.cos(xj) * np.sin(xj))
                result += weight * np.exp(-((xi - xj)**2) / 2.5) * np.sin(xi + xj) * np.cos(xi - xj)
        
        # Enhanced high-order harmonic polynomial with radial coupling
        harmonic_poly = 0.0
        for i in range(self.dim):
            xi = x[i]
            harmonic_poly += (np.sin(xi) + 0.6 * np.cos(2*xi) + 0.2 * np.sin(3*xi))**5
        result += 0.4 * harmonic_poly * np.exp(-r / 10.0)
        
        # Enhanced adaptive angular harmonic terms with exponential decay
        for i in range(self.dim):
            xi = x[i]
            angle_term = np.sin(xi) * np.cos(xi) * np.sin(2*xi)
            adaptive_weight = 1.0 + 0.5 * np.sin(3.0 * xi) * np.cos(4.0 * xi) * np.sin(5.0 * xi)
            result += adaptive_weight * angle_term * np.exp(-abs(xi) / 5.0)
        
        # Additional fractal-like coupling with frequency-dependent scaling (modified)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                freq_scale = 1.0 + 0.2 * np.sin(xi) * np.cos(xj) * np.sin(3*xi) * np.cos(4*xj)
                result += freq_scale * np.exp(-((xi - xj)**2 + (xi + xj)**2) / 6.0) * np.sin(xi + xj) * np.cos(xi - xj)
        
        # Minor modification: increased harmonic polynomial weight and added cross-dimensional sine coupling
        cross_harmonic = 0.0
        for i in range(self.dim):
            xi = x[i]
            cross_harmonic += (np.sin(xi) + 0.6 * np.cos(2*xi) + 0.2 * np.sin(3*xi))**7
        result += 0.5 * cross_harmonic * np.exp(-r / 11.0)
        
        # Added a new interaction term with higher frequency coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.2 * np.sin(7*xi) * np.cos(8*xj) * np.exp(-((xi-xj)**2)/3.0)
        
        return result