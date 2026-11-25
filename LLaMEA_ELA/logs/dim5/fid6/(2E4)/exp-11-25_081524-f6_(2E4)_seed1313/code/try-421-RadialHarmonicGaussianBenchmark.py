import numpy as np

class RadialHarmonicGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial harmonics with varying degrees
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for i in range(1, min(6, self.dim + 1)):
                poly_term = x[i-1]**(2*i) if i < self.dim else x[-1]**(2*i)
                harmonic_term = np.sin(i * r) * np.cos(i * r)
                result += poly_term * harmonic_term * np.exp(-r**2 / 20.0)
        
        # Cross-dimensional sine-cosine couplings with frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                freq_mod = 1.0 + 0.3 * np.sin(xi) * np.cos(xj)
                coupling = np.sin(freq_mod * xi) * np.cos(freq_mod * xj)
                result += coupling * np.exp(-((xi - xj)**2 + (xi + xj)**2) / 8.0)
        
        # Adaptive Gaussian scaling with angular harmonics
        for i in range(self.dim):
            xi = x[i]
            gauss_scale = 1.0 + 0.5 * np.sin(xi) * np.cos(2*xi)
            gaussian = gauss_scale * np.exp(-xi**2 / 10.0)
            result += gaussian * np.sin(3*xi) * np.cos(4*xi)
        
        # Multi-scale radial harmonic terms with dynamic frequency
        for i in range(1, 5):
            scale = 2.0 ** i
            freq = i * (2.0 + 0.5 * np.sin(r / 5.0))
            result += scale * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r**2 / 25.0)
        
        # Fractal-like coupling with polynomial modulation
        for i in range(self.dim):
            xi = x[i]
            poly_mod = xi**4 - 3*xi**2 + 1
            result += poly_mod * np.sin(xi) * np.cos(2*xi) * np.exp(-abs(xi) / 8.0)
        
        # Enhanced angular harmonic components with radial coupling
        angular_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            angular_sum += np.sin(xi) * np.cos(3*xi) + 0.5 * np.sin(2*xi) * np.cos(xi)
        result += 0.8 * angular_sum**2 * np.exp(-r / 15.0)
        
        # Cross-dimensional exponential interactions with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 1.0 + 0.4 * np.sin(xi) * np.cos(xj)
                exp_interaction = np.exp(-weight * ((xi - xj)**2 + (xi + xj)**2) / 12.0)
                result += exp_interaction * np.sin(xi + xj) * np.cos(xi - xj)
        
        # High-order polynomial with radial modulation
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 5*xi**4 + 10*xi**2 - 5
            radial_mod = 1.0 + 0.3 * np.sin(r / 3.0) * np.cos(r / 4.0)
            poly_sum += poly_term * radial_mod
        result += 0.7 * poly_sum * np.exp(-r / 20.0)
        
        # Additional harmonic terms with dynamic scaling
        for i in range(1, min(8, self.dim + 1)):
            xi = x[i-1] if i < self.dim else x[-1]
            freq = i * (1.0 + 0.2 * np.sin(xi))
            result += np.sin(freq * xi) * np.cos(freq * xi) * np.exp(-xi**2 / 15.0)
        
        # Final fractal-like coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += np.exp(-((xi - xj)**2) / 5.0) * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.2 * np.sin(xi) * np.cos(xj))
        
        return result