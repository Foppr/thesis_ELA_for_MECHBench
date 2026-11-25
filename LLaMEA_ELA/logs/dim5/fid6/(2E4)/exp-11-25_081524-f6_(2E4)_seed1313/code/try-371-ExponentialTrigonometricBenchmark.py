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
        
        # New term: Enhanced radial symmetry with improved scaling
        result += 0.2 * np.exp(-r**2/10.0) * np.sin(3.0 * r) * np.cos(r)
        
        # New term: Cross-dimensional exponential interaction with variable weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 0.3 * np.exp(-abs(xi-xj)/4.0)
                result += weight * np.sin(2.0 * xi + xj) * np.cos(xi - 2.0 * xj)
                
        # New term: Adaptive polynomial with exponential modulation
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**3 - xi**2 + 0.5*xi
            result += 0.4 * np.exp(-abs(xi)/3.0) * poly_term * np.sin(0.7 * r)
            
        # New term: Multi-scale harmonic with dynamic amplitude
        for i in range(self.dim):
            xi = x[i]
            amp = 0.6 * np.exp(-xi**2/5.0)
            result += amp * np.sin(6.0 * xi + 0.3 * r) * np.cos(4.0 * xi - 0.2 * r)
            
        # New enhanced multimodal component with higher frequency oscillations
        for i in range(self.dim):
            xi = x[i]
            result += 0.8 * np.exp(-abs(xi)/4.0) * np.sin(15.0 * xi + 0.5 * r) * np.cos(12.0 * xi - 0.4 * r)
            
        # New highly nonlinear cross-dimensional interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 0.7 * np.exp(-abs(xi-xj)/5.0) * np.sin(0.3 * (xi + xj))
                result += weight * np.cos(2.0 * xi - xj) * np.sin(1.5 * xj + xi)
                
        # New term: Enhanced exponential radial coupling with multi-scale modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * np.exp(-xi**2/6.0) * np.sin(8.0 * r + i) * np.cos(6.0 * r - i)
            
        # New term: High-dimensional polynomial with exponential scaling
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_sum += (xi**5 - 3*xi**3 + 2*xi) * np.exp(-abs(xi)/4.0)
        result += 0.3 * poly_sum * np.cos(0.8 * r)
        
        # New term: Stronger cross-dimensional exponential coupling with variable scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                scale_factor = 1.5 * np.exp(-abs(xi-xj)/3.0)
                result += 0.6 * np.sin(3.0 * xi + 2.0 * xj) * np.cos(xi - 3.0 * xj) * scale_factor
                
        # New term: Multi-frequency exponential modulation with radial dependency
        for i in range(self.dim):
            xi = x[i]
            freq_mod = 1.0 + 0.5 * np.sin(0.4 * i + r / 2.0)
            result += 0.7 * np.exp(-abs(xi)/3.0) * np.sin(freq_mod * 8.0 * xi) * np.cos(freq_mod * 6.0 * xi)
            
        # New term: Complex radial symmetry with exponential decay
        result += 0.4 * np.exp(-r**2/15.0) * np.sin(5.0 * r) * np.cos(2.0 * r)
        
        # New term: Adaptive coupling with high-order polynomial modulation
        for i in range(self.dim):
            xi = x[i]
            poly_mod = 1.0 + 0.3 * (xi**4 - 2*xi**2 + 1)
            result += 0.5 * np.exp(-abs(xi)/5.0) * poly_mod * np.sin(0.9 * r)
            
        return result