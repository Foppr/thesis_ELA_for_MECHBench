import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for polynomial chaos expansion
        self.poly_coeffs = np.random.randn(dim, 5)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            xi = x[i]
            poly_val = 0.0
            for j in range(5):
                poly_val += self.poly_coeffs[i, j] * (xi ** j)
            result += 0.3 * poly_val * np.exp(-xi**2/4.0)
        
        # Radial basis function component with dynamic scaling
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            rbf_val = np.exp(-np.sum((x - center)**2) / (2 * width**2))
            result += 0.4 * rbf_val * np.sin(np.sum(center) * 0.5)
        
        # Dynamic coupling terms with time-varying weights
        for i in range(self.dim):
            xi = x[i]
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 0.2 * np.sin(0.3 * (i + j)) * np.cos(0.2 * (i - j))
                    coupling_sum += weight * np.exp(-abs(xi - x[j])/3.0)
            result += coupling_sum * np.cos(xi)
        
        # Multi-scale polynomial modulation with radial dependency
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            xi = x[i]
            poly_mod = 1.0 + 0.5 * (xi**3 - xi**2 + 0.3*xi)
            result += 0.25 * poly_mod * np.sin(3.0 * r + i) * np.cos(2.0 * r - i)
        
        # Adaptive exponential scaling with polynomial weights
        for i in range(self.dim):
            xi = x[i]
            scale_factor = 1.0 + 0.4 * np.sin(0.5 * i) * np.cos(0.3 * i)
            result += 0.3 * np.exp(-abs(xi)/2.0) * (xi**4 - 2*xi**2 + 1) * scale_factor
        
        # Cross-dimensional harmonic coupling with variable amplitude
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                amp = 0.5 * np.exp(-(xi**2 + xj**2)/5.0)
                result += amp * np.sin(2.0 * xi + 3.0 * xj) * np.cos(xi - xj)
        
        # High-order polynomial with exponential decay
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_sum += (xi**6 - 4*xi**4 + 6*xi**2 - 1) * np.exp(-abs(xi)/3.0)
        result += 0.15 * poly_sum
        
        # Dynamic radial symmetry with multi-frequency components
        result += 0.2 * np.exp(-r**2/8.0) * (np.sin(4.0 * r) + 0.5 * np.cos(6.0 * r))
        
        # Adaptive coupling with polynomial modulation and exponential weights
        for i in range(self.dim):
            xi = x[i]
            poly_mod = 1.0 + 0.3 * (xi**3 - xi)
            weight = 0.4 * np.exp(-abs(xi)/4.0)
            result += weight * poly_mod * np.sin(5.0 * xi) * np.cos(3.0 * xi)
        
        # Additional multi-modal term with variable scaling
        for i in range(self.dim):
            xi = x[i]
            result += 0.35 * np.exp(-xi**2/6.0) * np.sin(7.0 * xi) * np.cos(4.0 * xi)
        
        # Complex cross-dimensional interaction with polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                poly_coupling = (xi**2 + xj**2) * np.sin(xi + xj)
                result += 0.2 * np.exp(-abs(xi-xj)/3.0) * poly_coupling
        
        # Final adaptive scaling term
        result *= (1.0 + 0.2 * np.sin(r))
        
        return result