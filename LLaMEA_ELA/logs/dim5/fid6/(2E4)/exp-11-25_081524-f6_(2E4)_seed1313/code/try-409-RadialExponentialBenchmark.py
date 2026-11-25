import numpy as np

class RadialExponentialBenchmark:
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
                result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/5.0)
        
        # Cross-dimensional exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_interaction = np.exp(-((xi - xj)**2 + (xi + xj)**2) / 4.0)
                result += exp_interaction * (1.0 + 0.5 * np.sin(xi * xj))
        
        # Adaptive noise modulation with radial dependency
        noise_factor = 0.1 * (1.0 + 0.3 * np.sin(r / 2.0))
        for i in range(self.dim):
            xi = x[i]
            result += noise_factor * np.sin(10.0 * xi) * np.cos(8.0 * xi)
        
        # Multi-scale harmonic polynomial terms
        for i in range(1, 5):
            poly_term = 1.0
            for j in range(self.dim):
                poly_term *= (x[j]**(2*i) + 0.3 * np.sin(x[j]))
            result += 0.3 * poly_term * np.exp(-r/4.0)
        
        # Exponential radial coupling with angular components
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                angle = np.arctan2(xj, xi)
                coupling = np.exp(-((xi**2 + xj**2)/2.0)) * np.sin(angle) * np.cos(angle)
                result += 0.4 * coupling
        
        # Adaptive polynomial with dynamic scaling
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_sum += xi**6 - 3*xi**4 + 3*xi**2 - 1
        result += 0.5 * poly_sum * np.exp(-r/3.0) * (1.0 + 0.2 * np.cos(5.0 * r))
        
        # Fractional harmonic terms with exponential weighting
        for i in range(1, 7):
            freq = i * (1.0 + 0.2 * np.cos(r / 3.0))
            result += np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/6.0) * (1.0 + 0.1 * np.sin(7.0 * r))
        
        # Angular exponential coupling with radial modulation
        for i in range(self.dim):
            xi = x[i]
            angular_term = 0.0
            for j in range(i+1, self.dim):
                xj = x[j]
                angle_diff = np.arctan2(xj, xi)
                angular_term += np.exp(-abs(angle_diff)) * np.sin(xi + xj) * np.cos(xi - xj)
            result += 0.3 * angular_term
        
        # Multi-dimensional Gaussian-like peaks with adaptive heights
        for i in range(1, min(4, self.dim + 1)):
            peak_height = 1.0 + 0.5 * np.sin(i * r / 2.0)
            gaussian_sum = 0.0
            for j in range(self.dim):
                gaussian_sum += (x[j] - i)**2
            result += peak_height * np.exp(-gaussian_sum / 3.0)
        
        return result