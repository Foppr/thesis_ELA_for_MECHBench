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
            
        # Enhanced cross-dimensional coupling with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                scale_factor = 1.0 + 0.2 * np.sin(0.5 * r) * np.cos(xi + xj)
                result += scale_factor * np.sin(3.0 * (xi + xj)) * np.cos(2.0 * (xi - xj)) * np.exp(-abs(xi-xj)/6.0)
                
        # Additional high-frequency harmonic components
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * np.sin(7.0 * xi) * np.cos(4.0 * xi) * np.exp(-xi**2/12.0)
            
        # Multi-scale polynomial with dynamic conditioning
        for i in range(self.dim):
            xi = x[i]
            condition_factor = 1.0 + 0.1 * np.sin(r) * np.cos(0.5 * i)
            result += condition_factor * (xi**7 - 4*xi**5 + 6*xi**3 - 4*xi) * np.exp(-abs(xi)/2.0)
            
        # Radial harmonic with variable frequency and amplitude
        for i in range(1, 8):
            freq = 1.0 + 0.5 * np.sin(i * r / 3.0)
            amp = 0.3 * (1.0 + 0.2 * np.cos(i * r / 2.0))
            result += amp * np.sin(freq * i * r) * np.cos(freq * i * r) * np.exp(-r/8.0)
            
        # Enhanced exponential coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 0.6 * (1.0 + np.sin(xi) * np.cos(xj))
                result += weight * np.exp(-(xi**2 + xj**2)/8.0) * np.sin(2.0 * (xi + xj)) * np.cos(3.0 * (xi - xj))
                
        # High-order polynomial with sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * (xi**8 - 5*xi**6 + 10*xi**4 - 10*xi**2 + 5) * np.sin(3.0 * xi) * np.exp(-abs(xi)/3.0)
            
        return result