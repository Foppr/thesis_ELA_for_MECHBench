import numpy as np

class RadialHarmonicGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced radial polynomial harmonic terms with dynamic frequency modulation
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for i in range(1, min(7, self.dim + 1)):
                freq = i * (1.5 + 0.5 * np.sin(r / 4.0) * np.cos(r / 3.0))
                poly_harmonic = (x[0]**2 + x[1]**2) * np.sin(freq * r) * np.cos(freq * r)
                result += poly_harmonic * np.exp(-r**2 / 20.0)
        
        # Dynamic cross-dimensional sine-cosine coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 1.0 + 0.4 * np.sin(xi) * np.cos(xj) * np.exp(-abs(xi - xj) / 5.0)
                coupling = weight * (np.sin(xi) * np.cos(xj) + np.cos(xi) * np.sin(xj))
                result += coupling * np.exp(-((xi - xj)**2) / 3.0)
        
        # Enhanced adaptive Gaussian scaling with higher-order polynomial modulation
        gaussian_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            gaussian = np.exp(-xi**2 / 1.5)
            poly_mod = 1.0 + 0.5 * (xi**6 - 3*xi**4 + 3*xi**2 - 1)
            gaussian_sum += gaussian * poly_mod
        result += 0.7 * gaussian_sum * np.exp(-r / 10.0)
        
        # Multi-scale sine-cosine harmonics with complex radial coupling and phase shifts
        for i in range(1, 5):
            scale = 4.0 ** i
            freq = i * (1.2 + 0.3 * np.cos(r / 2.5)) * np.sin(r / 3.0)
            harmonic = np.sin(freq * r) * np.cos(freq * r) * np.exp(-r / 15.0)
            result += harmonic * np.exp(-scale * r**2 / 25.0)
        
        # Sigmoidal radial interaction with complex polynomial terms and angular coupling
        for i in range(self.dim):
            xi = x[i]
            sigmoid_term = 1.0 / (1.0 + np.exp(-xi / 2.5))
            poly_term = xi**7 - 6*xi**5 + 12*xi**3 - 6*xi
            angular_coupling = np.sin(2.0 * xi) * np.cos(3.0 * xi)
            result += sigmoid_term * poly_term * angular_coupling * np.exp(-abs(xi) / 7.0)
        
        # Fractal-like coupling with multi-scale adaptive weights and higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = (1.0 + 0.3 * np.sin(xi) * np.cos(xj) * np.tan((xi + xj) / 4.0))
                coupling = weight * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi - xj) / 6.0)
                result += coupling * np.exp(-((xi - xj)**2) / 4.5)
        
        # High-order polynomial with complex angular harmonic modulation and radial scaling
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**9 - 8*xi**7 + 21*xi**5 - 20*xi**3 + 5*xi
            angular_mod = np.sin(4.0 * xi) * np.cos(3.0 * xi) + 0.5 * np.sin(2.0 * xi)
            poly_sum += poly_term * angular_mod
        result += 0.3 * poly_sum * np.exp(-r / 15.0)
        
        # Enhanced radial harmonic with exponential decay and multi-frequency modulation
        for i in range(self.dim):
            xi = x[i]
            radial_harmonic = (np.sin(xi) * np.cos(xi) + 0.3 * np.sin(2.0 * xi)) * (1.0 + 0.4 * np.sin(3.0 * xi))
            result += radial_harmonic * np.exp(-xi**2 / 8.0)
        
        # Additional high-frequency oscillatory component for increased multimodality
        freq_osc = 10.0 * np.sin(r / 2.0) + 5.0 * np.cos(r / 3.0)
        osc_component = np.sin(freq_osc * r) * np.cos(freq_osc * r) * np.exp(-r**2 / 30.0)
        result += 0.5 * osc_component
        
        return result