import numpy as np

class RadialHarmonicGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial harmonic terms with modified frequencies
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for i in range(1, min(6, self.dim + 1)):
                freq = i * (1.5 + 0.3 * np.sin(r / 4.0))
                poly_harmonic = (x[0]**2 + x[1]**2) * np.sin(freq * r) * np.cos(freq * r)
                result += poly_harmonic * np.exp(-r**2 / 20.0)
        
        # Cross-dimensional sine-cosine coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 1.0 + 0.3 * np.sin(xi) * np.cos(xj)
                coupling = weight * (np.sin(xi) * np.cos(xj) + np.cos(xi) * np.sin(xj))
                result += coupling * np.exp(-((xi - xj)**2) / 5.0)
        
        # Adaptive Gaussian scaling with higher-order polynomial modulation
        gaussian_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            gaussian = np.exp(-xi**2 / 2.5)
            poly_mod = 1.0 + 0.4 * (xi**6 - 3*xi**4 + 3*xi**2 - 1)
            gaussian_sum += gaussian * poly_mod
        result += 0.6 * gaussian_sum * np.exp(-r / 10.0)
        
        # Multi-scale sine-cosine harmonics with enhanced radial coupling
        for i in range(1, 5):
            scale = 4.0 ** i
            freq = i * (1.2 + 0.2 * np.cos(r / 3.0))
            harmonic = np.sin(freq * r) * np.cos(freq * r)
            result += harmonic * np.exp(-scale * r**2 / 25.0)
        
        # Sigmoidal radial interaction with higher-order polynomial terms
        for i in range(self.dim):
            xi = x[i]
            sigmoid_term = 1.0 / (1.0 + np.exp(-xi / 2.5))
            poly_term = xi**6 - 5*xi**4 + 10*xi**2 - 1
            result += sigmoid_term * poly_term * np.exp(-abs(xi) / 7.0)
        
        # Fractal-like coupling with increased complexity and dynamic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = (1.0 + 0.3 * np.sin(xi) * np.cos(xj) * np.sin(xj - xi))
                coupling = weight * np.sin(xi + xj) * np.cos(xi - xj)
                result += coupling * np.exp(-((xi - xj)**2) / 6.0)
        
        # High-order polynomial with angular harmonic modulation and additional complexity
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**9 - 8*xi**7 + 21*xi**5 - 20*xi**3 + 5*xi
            angular_mod = np.sin(4.0 * xi) * np.cos(3.0 * xi) + 0.5 * np.sin(2.0 * xi)
            poly_sum += poly_term * angular_mod
        result += 0.3 * poly_sum * np.exp(-r / 15.0)
        
        # Enhanced radial harmonic with exponential decay and additional coupling
        for i in range(self.dim):
            xi = x[i]
            radial_harmonic = np.sin(xi) * np.cos(xi) * (1.0 + 0.4 * np.sin(2.0 * xi) * np.cos(3.0 * xi))
            result += radial_harmonic * np.exp(-xi**2 / 12.0)
        
        # Additional cross-dimensional coupling with fractal characteristics
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                coupling = np.sin(xi * xj) * np.cos(xi + xj) * (1.0 + 0.2 * np.sin(xi - xj))
                result += coupling * np.exp(-((xi - xj)**2) / 4.5)
        
        return result