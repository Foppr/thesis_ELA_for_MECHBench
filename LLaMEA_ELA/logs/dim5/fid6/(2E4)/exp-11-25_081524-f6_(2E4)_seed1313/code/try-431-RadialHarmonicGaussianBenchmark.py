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
                freq = i * (1.7 + 0.2 * np.sin(r / 3.0))
                poly_harmonic = (x[0]**2 + x[1]**2) * np.sin(freq * r) * np.cos(freq * r)
                result += poly_harmonic * np.exp(-r**2 / 25.0)
        
        # Cross-dimensional sine-cosine coupling with altered weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                coupling = 0.9 * (np.sin(xi) * np.cos(xj) + np.cos(xi) * np.sin(xj))
                result += coupling * np.exp(-((xi - xj)**2) / 4.0)
        
        # Adaptive Gaussian scaling with modified polynomial modulation
        gaussian_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            gaussian = np.exp(-xi**2 / 2.0)
            poly_mod = 1.0 + 0.3 * (xi**4 - 2*xi**2)
            gaussian_sum += gaussian * poly_mod
        result += 0.7 * gaussian_sum * np.exp(-r / 12.0)
        
        # Multi-scale sine-cosine harmonics with different radial coupling
        for i in range(1, 5):
            scale = 3.5 ** i
            freq = i * (1.3 + 0.1 * np.cos(r / 4.0))
            harmonic = np.sin(freq * r) * np.cos(freq * r)
            result += harmonic * np.exp(-scale * r**2 / 30.0)
        
        # Sigmoidal radial interaction with modified polynomial terms
        for i in range(self.dim):
            xi = x[i]
            sigmoid_term = 1.0 / (1.0 + np.exp(-xi / 3.0))
            poly_term = xi**5 - 3*xi**3 + 2*xi
            result += sigmoid_term * poly_term * np.exp(-abs(xi) / 6.0)
        
        # Fractal-like coupling with modified adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = (1.0 + 0.25 * np.sin(xi) * np.cos(xj))
                coupling = weight * np.sin(xi + xj) * np.cos(xi - xj)
                result += coupling * np.exp(-((xi - xj)**2) / 7.0)
        
        # High-order polynomial with angular harmonic modulation
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**9 - 8*xi**7 + 20*xi**5 - 15*xi**3 + 5*xi
            angular_mod = np.sin(4.0 * xi) * np.cos(3.0 * xi)
            poly_sum += poly_term * angular_mod
        result += 0.3 * poly_sum * np.exp(-r / 18.0)
        
        # Adaptive radial harmonic with modified exponential decay
        for i in range(self.dim):
            xi = x[i]
            radial_harmonic = np.sin(xi) * np.cos(xi) * (1.0 + 0.3 * np.sin(2.0 * xi))
            result += radial_harmonic * np.exp(-xi**2 / 15.0)
        
        return result