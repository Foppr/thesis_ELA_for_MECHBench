import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for radial basis functions
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            xi = x[i]
            # Hermite polynomial terms up to degree 4
            h1 = xi
            h2 = xi**2 - 1
            h3 = xi**3 - 3*xi
            h4 = xi**4 - 6*xi**2 + 3
            result += 0.5 * (h1 + 0.3*h2 + 0.1*h3 + 0.05*h4) * np.cos(0.5*i + np.sum(x)**2)
        
        # Radial basis function component with dynamic widths
        r = np.sqrt(np.sum(x**2))
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i] * (1.0 + 0.3 * np.sin(r / 3.0))
            distance = np.sqrt(np.sum((x - center)**2))
            result += 0.8 * np.exp(-distance**2 / (2 * width**2)) * np.sin(2.0 * r + i)
            
        # Dynamic coupling terms with time-varying coefficients
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                # Time-varying coupling coefficient
                coupling_coeff = 0.5 + 0.3 * np.sin(0.2*i + 0.3*j + r / 4.0)
                result += coupling_coeff * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.2 * np.sin(r))
                
        # Multi-scale harmonic interference
        for i in range(self.dim):
            xi = x[i]
            # Multiple frequency components with varying amplitudes
            freqs = [1.0, 2.5, 4.0, 6.0]
            amps = [1.0, 0.7, 0.4, 0.2]
            for freq, amp in zip(freqs, amps):
                result += amp * np.sin(freq * xi + 0.3 * r) * np.cos(freq * xi - 0.2 * r)
                
        # Adaptive polynomial with radial dependency
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_sum += (xi**5 - 2*xi**3 + xi) * np.exp(-r/8.0)
        result += 0.3 * poly_sum
        
        # Cross-dimensional symmetry breaking terms
        symmetry_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            symmetry_term += xi**2 * np.sin(3.0 * xi + 0.5 * r)
        result += 0.4 * symmetry_term * np.exp(-r/10.0)
        
        # Chaotic-like modulation with radial dependence
        chaotic_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            mod_freq = 2.0 + 1.5 * np.sin(0.3 * i + r / 5.0)
            chaotic_mod += 0.25 * np.sin(mod_freq * xi) * np.cos(mod_freq * xi + 0.1 * r)
        result += chaotic_mod * np.exp(-r/12.0)
        
        # High-frequency oscillatory component
        high_freq = 0.0
        for i in range(self.dim):
            xi = x[i]
            high_freq += 0.6 * np.sin(20.0 * xi + 3.0 * r) * np.cos(15.0 * xi - 2.0 * r)
        result += high_freq
        
        return result