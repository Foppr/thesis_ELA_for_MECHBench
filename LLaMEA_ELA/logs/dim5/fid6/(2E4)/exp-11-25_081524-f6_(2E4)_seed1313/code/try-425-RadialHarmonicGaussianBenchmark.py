import numpy as np

class RadialHarmonicGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced radial polynomial harmonic terms with dynamic frequencies
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for i in range(1, min(7, self.dim + 1)):
                freq = i * (1.5 + 0.5 * np.sin(r / 2.0) * np.cos(r / 4.0))
                poly_harmonic = (x[0]**2 + x[1]**2) * np.sin(freq * r) * np.cos(freq * r)
                result += poly_harmonic * np.exp(-r**2 / 20.0)
        
        # Dynamic cross-dimensional sine-cosine coupling with fractal-like weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = (1.0 + 0.3 * np.sin(xi) * np.cos(xj) * np.sin(xj - xi))
                coupling = weight * (np.sin(xi) * np.cos(xj) + np.cos(xi) * np.sin(xj))
                result += coupling * np.exp(-((xi - xj)**2) / 6.0)
        
        # Enhanced adaptive Gaussian scaling with polynomial modulation
        gaussian_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            gaussian = np.exp(-xi**2 / 3.0)
            poly_mod = 1.0 + 0.4 * (xi**6 - 3*xi**4 + 3*xi**2 - 1)
            gaussian_sum += gaussian * poly_mod
        result += 0.7 * gaussian_sum * np.exp(-r / 10.0)
        
        # Multi-scale sine-cosine harmonics with radial coupling and angular modulation
        for i in range(1, 5):
            scale = 4.0 ** i
            freq = i * (2.0 + 0.2 * np.cos(r / 3.0) * np.sin(r / 5.0))
            harmonic = np.sin(freq * r) * np.cos(freq * r)
            angular_mod = np.sin(2.0 * r) * np.cos(3.0 * r)
            result += harmonic * angular_mod * np.exp(-scale * r**2 / 25.0)
        
        # Sigmoidal radial interaction with higher-order polynomial terms
        for i in range(self.dim):
            xi = x[i]
            sigmoid_term = 1.0 / (1.0 + np.exp(-xi / 2.0))
            poly_term = xi**7 - 5*xi**5 + 10*xi**3 - 5*xi
            result += sigmoid_term * poly_term * np.exp(-abs(xi) / 8.0)
        
        # Fractal-like coupling with adaptive weights and higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = (1.0 + 0.4 * np.sin(xi) * np.cos(xj) * np.sin(xi + xj))
                coupling = weight * np.sin(xi + xj) * np.cos(xi - xj) * np.sin(xi * xj)
                result += coupling * np.exp(-((xi - xj)**2) / 7.0)
        
        # High-order polynomial with angular harmonic modulation and radial coupling
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**9 - 8*xi**7 + 21*xi**5 - 20*xi**3 + 5*xi
            angular_mod = np.sin(4.0 * xi) * np.cos(3.0 * xi)
            poly_sum += poly_term * angular_mod
        result += 0.3 * poly_sum * np.exp(-r / 15.0)
        
        # Enhanced radial harmonic with exponential decay and frequency modulation
        for i in range(self.dim):
            xi = x[i]
            radial_harmonic = np.sin(xi) * np.cos(xi) * (1.0 + 0.4 * np.sin(3.0 * xi) * np.cos(2.0 * xi))
            result += radial_harmonic * np.exp(-xi**2 / 15.0)
        
        # Additional cross-dimensional coupling with hyperbolic functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                coupling = np.tanh(xi) * np.sech(xj) + np.tanh(xj) * np.sech(xi)
                result += coupling * np.exp(-((xi - xj)**2) / 8.0)
        
        return result