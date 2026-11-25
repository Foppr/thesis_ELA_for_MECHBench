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
        
        # Multi-scale polynomial coupling with harmonic weights
        for i in range(self.dim):
            xi = x[i]
            weight = 1.0 / (1.0 + 0.2 * i**2)
            result += weight * (xi**4 - 2*xi**2 + 1) * np.sin(2.0 * xi + 0.5 * r)
            
        # Exponential polynomial terms with radial dependency
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**3 - xi
            result += 0.4 * np.exp(-abs(xi)/3.0) * poly_term * np.cos(0.7 * r)
            
        # Cross-dimensional polynomial coupling with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                scale = 1.0 / (1.0 + 0.5 * np.exp(-abs(xi-xj)/2.0))
                result += 0.3 * (xi**2 + xj**2) * np.sin(xi + xj) * np.cos(xi - xj) * scale
                
        # Adaptive polynomial decay with harmonic perturbations
        for i in range(self.dim):
            xi = x[i]
            decay = np.exp(-xi**2/5.0)
            perturbation = 0.2 * np.cos(4.0 * xi + 0.3 * r)
            result += decay * perturbation
            
        # Multi-frequency radial component with polynomial amplitude
        for i in range(self.dim):
            xi = x[i]
            amp = 0.6 * (1.0 + 0.4 * np.sin(i))
            result += amp * np.cos(3.0 * r + i) * np.sin(2.0 * r - i)
            
        # Cubic polynomial terms with cross-dimensional interaction
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * xi**3 * np.exp(-r/6.0) * np.cos(xi)
            
        # Dynamic amplitude modulation with radial dependence
        for i in range(self.dim):
            xi = x[i]
            amp_mod = 1.0 + 0.3 * np.sin(0.4 * i + r / 2.0)
            result += 0.5 * amp_mod * np.cos(1.5 * xi) * np.sin(xi) * np.exp(-r/7.0)
            
        # High-frequency polynomial oscillation
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * (xi**2) * np.cos(8.0 * xi) * np.sin(6.0 * xi)
            
        # Adaptive coupling with polynomial weights and harmonic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 0.4 * (1.0 + 0.1 * (xi**2 + xj**2))
                result += weight * np.cos(xi + xj) * np.sin(xi - xj) * np.exp(-abs(xi-xj)/4.0)
                
        # Additional term to improve conditioning and reduce bias
        result += 0.08 * np.sum(x**2) * np.exp(-r/5.0)
        
        return result