import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial decay with harmonic modulation
        r = np.sqrt(np.sum(x**2))
        result += (1.0 + 0.5 * np.sin(r)) * np.exp(-r**2/20.0) * (1.0 + 0.3 * np.cos(3.0 * r))
        
        # Multi-scale polynomial terms with sinusoidal coupling
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 3*xi**4 + 3*xi**2 - 1
            result += 0.8 * np.sin(2.0 * xi) * np.cos(xi) * np.exp(-abs(xi)/3.0) * poly_term
            
        # Cross-dimensional harmonic coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 0.5 * (1.0 + np.cos(xi - xj))
                result += weight * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/4.0)
                
        # Radial harmonic series with exponential decay
        for i in range(1, 6):
            result += (0.2 / i) * np.sin(i * r) * np.cos(i * r) * np.exp(-r/5.0)
            
        # Multi-frequency sinusoidal components with polynomial amplitude
        for i in range(self.dim):
            xi = x[i]
            amp = 1.0 + 0.4 * np.sin(xi) * np.cos(xi)
            result += amp * np.sin(5.0 * xi) * np.cos(3.0 * xi) * np.exp(-xi**2/8.0)
            
        # Adaptive polynomial weighting with radial dependency
        for i in range(self.dim):
            xi = x[i]
            weight = 1.0 + 0.3 * np.sin(r) * np.cos(i)
            result += weight * (xi**5 - 2*xi**3 + xi) * np.exp(-abs(xi)/4.0)
            
        # Quadratic exponential terms with harmonic interaction
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * xi**2 * np.sin(xi) * np.cos(xi) * np.exp(-r/6.0)
            
        # Cross-dimensional exponential coupling with harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                coupling = np.exp(-(xi**2 + xj**2)/10.0) * np.sin(xi + xj)
                result += 0.4 * coupling * np.cos(xi - xj)
                
        # Multi-scale radial harmonic with dynamic amplitude
        for i in range(self.dim):
            xi = x[i]
            amp = 0.7 * (1.0 + 0.3 * np.sin(2.0 * r))
            result += amp * np.sin(4.0 * xi) * np.cos(2.0 * xi) * np.exp(-abs(xi)/5.0)
            
        # Enhanced cross-dimensional interactions with higher-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    xi = x[i]
                    xj = x[j]
                    xk = x[k]
                    coupling = np.sin(xi + xj + xk) * np.cos(xi - xj) * np.exp(-abs(xi+xj+xk)/6.0)
                    result += 0.25 * coupling
                    
        # Additional high-frequency polynomial components
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * (xi**7 - 4*xi**5 + 6*xi**3 - 4*xi) * np.sin(7.0 * xi) * np.exp(-xi**2/12.0)
            
        # Increased radial harmonic complexity
        for i in range(1, 8):
            result += (0.15 / i**1.5) * np.sin(i**1.2 * r) * np.cos(i**0.8 * r) * np.exp(-r/7.0)
            
        # Enhanced adaptive conditioning with dynamic weights
        for i in range(self.dim):
            xi = x[i]
            weight = 1.0 + 0.4 * np.sin(r) * np.cos(2.0 * i)
            result += weight * (xi**4 - xi**2) * np.exp(-abs(xi)/3.0)
            
        return result