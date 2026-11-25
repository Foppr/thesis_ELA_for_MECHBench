import numpy as np

class SphericalHarmonicGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Spherical harmonic components with radial dependence
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Normalize x for spherical coordinates
            x_norm = x / r
            
            # Spherical harmonics Y_3,2 (degree 3, order 2)
            theta = np.arccos(x_norm[0] / r) if r > 1e-8 else 0.0
            phi = np.arctan2(x_norm[1], x_norm[0]) if r > 1e-8 else 0.0
            
            # Spherical harmonic Y_3,2 = (5/8)*sqrt(7/(2*pi)) * (3*cos^2(theta) - 1) * sin^2(theta) * cos(2*phi)
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            cos_phi = np.cos(phi)
            sin_phi = np.sin(phi)
            
            y_32 = (5/8) * np.sqrt(7/(2*np.pi)) * (3*cos_theta**2 - 1) * sin_theta**2 * cos_phi**2
            result += 0.5 * r * y_32
            
        # Gaussian radial basis functions with varying widths and centers
        centers = np.linspace(-3, 3, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                center = centers[i]
                sigma = 0.5 + 0.5 * np.sin(i)
                result += np.exp(-0.5 * ((x[i] - center) / sigma)**2) * (1.0 + 0.3 * np.sin(x[i]))
                
        # Adaptive polynomial couplings with dynamic weights
        for i in range(self.dim):
            xi = x[i]
            poly_weight = 1.0 + 0.4 * np.cos(xi)
            result += poly_weight * (xi**3 - xi) * np.exp(-xi**2/4.0)
            
        # Cross-dimensional Gaussian couplings with harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                dist = np.sqrt((xi - xj)**2 + 1e-8)
                coupling = np.exp(-dist**2/2.0) * (1.0 + 0.2 * np.sin(xi + xj))
                result += 0.3 * coupling * np.cos(2.0 * xi * xj) * np.exp(-abs(xi - xj)/3.0)
                
        # Multi-scale sinusoidal radial terms
        for i in range(1, 6):
            freq = i * (1.0 + 0.1 * np.cos(r))
            result += (0.4 / i**2) * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/5.0)
            
        # Polynomial radial terms with adaptive modulation
        for i in range(self.dim):
            xi = x[i]
            mod = 1.0 + 0.2 * np.sin(xi**2)
            result += mod * (xi**4 - 2*xi**2 + 1) * np.exp(-abs(xi)/2.0)
            
        # Adaptive harmonic coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                freq = 1.0 + 0.3 * np.sin(xi * xj)
                result += 0.2 * np.sin(freq * (xi + xj)) * np.cos(freq * (xi - xj)) * np.exp(-(xi**2 + xj**2)/8.0)
                
        # Multi-frequency Gaussian basis with radial dependence
        for i in range(1, 4):
            sigma = 0.3 + 0.2 * np.sin(i * r / 3.0)
            result += (0.6 / i) * np.exp(-0.5 * ((r - i) / sigma)**2) * np.cos(i * r) * np.exp(-r/4.0)
            
        # High-order polynomial with harmonic modulation
        for i in range(self.dim):
            xi = x[i]
            mod = 1.0 + 0.3 * np.cos(xi**3)
            result += mod * (xi**5 - 3*xi**3 + 2*xi) * np.exp(-abs(xi)/3.0)
            
        # Cross-dimensional coupling with radial modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                mod = 1.0 + 0.2 * np.sin(r)
                result += 0.4 * mod * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/5.0)
                
        return result