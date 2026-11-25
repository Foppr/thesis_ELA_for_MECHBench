import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial chaos expansion with radial basis functions
        for i in range(self.dim):
            xi = x[i]
            # Hermite polynomial terms
            poly_hermite = xi**4 - 6*xi**2 + 3
            # Radial basis function component
            rbf = np.exp(-0.5 * xi**2)
            result += 0.3 * poly_hermite * rbf
            
        # Multi-scale radial basis function with dynamic centers
        for i in range(self.dim):
            xi = x[i]
            center = 2.0 * np.sin(0.5 * i)
            rbf_centered = np.exp(-0.5 * (xi - center)**2 / (1.0 + 0.1 * abs(xi)))
            result += 0.2 * rbf_centered * np.sin(3.0 * xi)
            
        # Cross-dimensional coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 0.4 * (1.0 + 0.3 * np.sin(0.2 * i + 0.3 * j))
                coupling = np.exp(-0.5 * (xi**2 + xj**2)) * np.cos(xi * xj)
                result += weight * coupling
                
        # Dynamic scaling with polynomial modulation
        r = np.sqrt(np.sum(x**2))
        scale_factor = 1.0 + 0.5 * np.sin(0.1 * r) * np.cos(0.2 * r)
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * xi**3 * scale_factor * np.exp(-0.1 * abs(xi))
            
        # Adaptive radial basis with multi-scale Gaussian components
        for i in range(self.dim):
            xi = x[i]
            gauss_sum = 0.0
            for k in range(1, 4):
                center_k = k * np.pi / 3.0
                sigma_k = 0.5 + 0.2 * k
                gauss_sum += np.exp(-0.5 * (xi - center_k)**2 / sigma_k**2)
            result += 0.25 * gauss_sum * np.sin(2.0 * xi)
            
        # Multi-dimensional polynomial with exponential interaction
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_sum += (xi**3 - 2*xi) * np.exp(-0.2 * abs(xi))
        result += 0.15 * poly_sum**2
            
        # Cross-dimensional polynomial coupling with variable exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_i = 1.0 + 0.3 * np.cos(0.1 * i)
                exp_j = 1.0 + 0.2 * np.sin(0.1 * j)
                coupling = (xi**exp_i) * (xj**exp_j) * np.exp(-0.1 * abs(xi-xj))
                result += 0.1 * coupling
                
        # Enhanced radial symmetry with polynomial scaling
        r = np.sqrt(np.sum(x**2))
        result += 0.3 * np.sin(4.0 * r) * np.cos(2.0 * r) * np.exp(-0.1 * r**2)
        
        # Adaptive polynomial with trigonometric modulation
        for i in range(self.dim):
            xi = x[i]
            poly_mod = xi**5 - 10*xi**3 + 15*xi
            mod_factor = 1.0 + 0.4 * np.sin(0.3 * i)
            result += 0.2 * poly_mod * mod_factor * np.exp(-0.1 * abs(xi))
            
        # High-frequency oscillation with exponential envelope
        for i in range(self.dim):
            xi = x[i]
            freq = 10.0 + 5.0 * np.sin(0.2 * i)
            result += 0.1 * np.exp(-0.1 * abs(xi)) * np.sin(freq * xi) * np.cos(freq * xi)
            
        # Cross-dimensional exponential coupling with dynamic amplitude
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                amp = 0.5 * np.exp(-0.2 * abs(xi-xj)) * (1.0 + 0.3 * np.sin(0.1 * i))
                result += amp * np.sin(xi + xj) * np.cos(xi - xj)
                
        # Multi-scale radial basis with varying bandwidths
        for i in range(self.dim):
            xi = x[i]
            band_width = 0.5 + 0.3 * np.cos(0.1 * i)
            rbf_multi = np.exp(-0.5 * xi**2 / band_width**2)
            result += 0.1 * rbf_multi * np.cos(4.0 * xi)
            
        # Adaptive polynomial chaos with cross-dimensional interaction
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 15*xi**4 + 75*xi**2 - 125
            result += 0.05 * poly_term * np.exp(-0.05 * abs(xi))
            
        # Final term: Combined radial and cross-dimensional complexity
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * np.sin(5.0 * xi) * np.cos(3.0 * xi) * np.exp(-0.08 * r)
            
        return result