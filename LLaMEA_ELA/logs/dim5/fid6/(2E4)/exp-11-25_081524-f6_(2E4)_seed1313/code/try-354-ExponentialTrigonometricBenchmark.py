import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial exponential decay with trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        result += 2.0 * np.exp(-r/3.0) * np.sin(2.0 * r) * np.cos(r/2.0)
        
        # Exponential polynomial terms with adaptive coefficients
        for i in range(self.dim):
            xi = x[i]
            exp_coeff = 1.0 + 0.5 * np.sin(0.4 * i + r / 4.0)
            result += exp_coeff * np.exp(-xi**2/2.0) * (xi**4 - 2*xi**2 + 1)
            
        # Trigonometric coupling with exponential decay
        for i in range(self.dim):
            xi = x[i]
            result += 0.8 * np.sin(xi) * np.cos(2.0 * xi) * np.exp(-abs(xi)/3.0)
            
        # Multi-scale radial symmetry with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            freq1 = 1.5 + 0.8 * np.sin(0.3 * i + r / 5.0)
            freq2 = 2.0 + 1.0 * np.cos(0.4 * i + r / 6.0)
            result += 0.5 * np.sin(freq1 * xi) * np.cos(freq2 * xi) * np.exp(-r/8.0)
            
        # Cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.3 * np.exp(-(xi-xj)**2/4.0) * np.sin(xi + xj) * np.cos(xi - xj)
                
        # Adaptive exponential peaks with dynamic amplitudes
        for i in range(self.dim):
            xi = x[i]
            amp = 1.5 + 0.7 * np.sin(0.6 * i + r / 3.0)
            result += amp * np.exp(-((xi - 1.0)**2)/2.0) + amp * np.exp(-((xi + 1.0)**2)/2.0)
            
        # High-frequency trigonometric components with exponential weighting
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * np.sin(10.0 * xi) * np.cos(8.0 * xi) * np.exp(-r/5.0)
            
        # Radial polynomial with exponential modulation
        result += 0.6 * r**3 * np.exp(-r/4.0) * np.sin(3.0 * r)
        
        # Multi-modal exponential terms with adaptive scaling - modified
        for i in range(self.dim):
            xi = x[i]
            scale = 1.0 + 0.3 * np.cos(0.5 * i + r / 2.0)
            result += scale * np.exp(-xi**2) * np.sin(5.0 * xi)**2
            
        # Enhanced adaptive chaotic-like exponential perturbation
        chaos_pert = 0.0
        for i in range(self.dim):
            xi = x[i]
            pert_coeff = 0.8 + 0.4 * np.sin(0.7 * i + r / 5.0)
            chaos_pert += pert_coeff * np.exp(-xi**2/3.0) * np.sin(12.0 * xi)
        result += chaos_pert * np.exp(-r/10.0)
        
        # Additional harmonic modulation for better conditioning
        result += 0.2 * np.sin(r) * np.cos(r/3.0) * np.exp(-r/6.0)
        
        # Modified polynomial radial component with enhanced nonlinearity
        result += 0.3 * r**4 * np.exp(-r/5.0) * np.sin(2.0 * r)
        
        return result