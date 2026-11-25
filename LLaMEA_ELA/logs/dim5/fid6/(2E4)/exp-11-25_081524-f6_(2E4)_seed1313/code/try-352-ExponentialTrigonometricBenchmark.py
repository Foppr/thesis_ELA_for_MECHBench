import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial exponential decay with trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        result += np.exp(-r/3.0) * np.sin(2.0 * r) * np.cos(r / 2.0)
        
        # Multi-scale trigonometric coupling with exponential weights
        for i in range(self.dim):
            xi = x[i]
            weight = np.exp(-i/5.0)
            result += weight * np.sin(3.0 * xi + 0.5 * r) * np.cos(2.0 * xi - 0.3 * r)
            
        # Exponential polynomial terms with radial dependency
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**4 - 2*xi**2 + 1
            result += 0.5 * np.exp(-abs(xi)/2.0) * poly_term * np.cos(0.5 * r)
            
        # Cross-dimensional exponential coupling with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                scale = 1.0 / (1.0 + 0.3 * np.exp(-abs(xi-xj)/2.0))
                result += 0.4 * np.sin(xi + xj) * np.cos(xi - xj) * scale
                
        # Adaptive exponential decay with sinusoidal perturbations
        for i in range(self.dim):
            xi = x[i]
            decay = np.exp(-xi**2/4.0)
            perturbation = 0.3 * np.sin(5.0 * xi + 0.2 * r)
            result += decay * perturbation
            
        # Multi-frequency radial component with exponential amplitude
        for i in range(self.dim):
            xi = x[i]
            amp = 0.8 * np.exp(-abs(xi)/3.0)
            result += amp * np.sin(4.0 * r + i) * np.cos(3.0 * r - i)
            
        # Quadratic exponential terms with cross-dimensional interaction
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * xi**2 * np.exp(-r/5.0) * np.sin(xi)
            
        # Dynamic amplitude modulation with radial dependence
        for i in range(self.dim):
            xi = x[i]
            amp_mod = 1.0 + 0.4 * np.cos(0.5 * i + r / 3.0)
            result += 0.6 * amp_mod * np.sin(2.0 * xi) * np.cos(1.5 * xi) * np.exp(-r/8.0)
            
        # High-frequency exponential oscillation
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * np.exp(-abs(xi)/2.0) * np.sin(10.0 * xi) * np.cos(7.0 * xi)
            
        # Adaptive coupling with exponential weights and trigonometric interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 0.5 * np.exp(-(xi**2 + xj**2)/4.0)
                result += weight * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/3.0)
                
        # Additional term to improve conditioning and reduce bias
        result += 0.1 * np.sum(np.abs(x)) * np.exp(-r/4.0)
        
        return result