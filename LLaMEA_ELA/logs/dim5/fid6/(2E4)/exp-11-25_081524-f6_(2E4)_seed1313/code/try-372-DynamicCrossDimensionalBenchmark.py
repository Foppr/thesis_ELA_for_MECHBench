import numpy as np

class DynamicCrossDimensionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial with dynamic scaling
        r = np.sqrt(np.sum(x**2))
        dynamic_scale = 1.0 + 0.5 * np.sin(r / 2.0)
        result += dynamic_scale * (r**4 - 2*r**2 + 1) * np.exp(-r/3.0)
        
        # Multi-scale sinusoidal components with polynomial modulation
        for i in range(self.dim):
            xi = x[i]
            result += (0.7 + 0.3 * np.sin(xi)) * np.sin(3.0 * xi) * np.cos(2.0 * xi) * np.exp(-xi**2/5.0)
            
        # Cross-dimensional coupling with adaptive weights (modified)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 1.2 * (1.0 + np.cos(xi * xj))  # Increased weight
                result += weight * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/4.0)
                
        # Multi-frequency harmonic series with radial dependency
        for i in range(1, 5):
            freq = i * (1.0 + 0.2 * np.sin(r / 4.0))
            result += (0.5 / i) * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/6.0)
            
        # Adaptive polynomial terms with harmonic modulation
        for i in range(self.dim):
            xi = x[i]
            poly_mod = 1.0 + 0.4 * np.sin(xi) * np.cos(xi)
            result += poly_mod * (xi**5 - 3*xi**3 + 2*xi) * np.exp(-abs(xi)/3.0)
            
        # Enhanced cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                coupling = np.exp(-(xi**2 + xj**2)/8.0) * np.sin(xi + xj)
                result += 0.6 * coupling * np.cos(xi - xj) * np.exp(-abs(xi-xj)/5.0)
                
        # Dynamic radial harmonic with variable amplitude
        for i in range(1, 7):
            amp = 0.4 * (1.0 + 0.3 * np.sin(i * r / 3.0))
            result += amp * np.sin(i * r) * np.cos(i * r) * np.exp(-r/4.0)
            
        # Multi-scale polynomial with cross-dimensional interactions (modified exponents)
        for i in range(self.dim):
            xi = x[i]
            result += (0.9 + 0.1 * np.cos(xi)) * (xi**7 - 4*xi**5 + 6*xi**3 - 4*xi) * np.exp(-abs(xi)/2.0)  # Changed exponents
            
        # Adaptive coupling with dynamic frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                freq = 2.0 + 0.5 * np.sin(xi + xj)
                result += 0.5 * np.sin(freq * (xi + xj)) * np.cos(freq * (xi - xj)) * np.exp(-abs(xi-xj)/3.0)
                
        # High-order polynomial with radial modulation
        for i in range(self.dim):
            xi = x[i]
            mod = 1.0 + 0.2 * np.sin(r)
            result += mod * (xi**7 - 5*xi**5 + 10*xi**3 - 10*xi) * np.exp(-abs(xi)/4.0)
            
        # Multi-frequency harmonic with dynamic amplitude and phase
        for i in range(self.dim):
            xi = x[i]
            amp = 0.6 * (1.0 + 0.3 * np.cos(xi))
            freq = 3.0 + 0.4 * np.sin(xi)
            result += amp * np.sin(freq * xi) * np.cos(freq * xi) * np.exp(-xi**2/7.0)
            
        # Cross-dimensional exponential with harmonic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.3 * np.exp(-(xi**2 + xj**2)/6.0) * np.sin(2.0 * (xi + xj)) * np.cos(3.0 * (xi - xj))
                
        # Radial polynomial with sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.8 * (xi**4 - 2*xi**2 + 1) * np.sin(xi) * np.exp(-abs(xi)/5.0)
            
        return result