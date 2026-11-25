import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for different degrees
        self.poly_coeffs = []
        for d in range(1, 6):
            self.poly_coeffs.append(np.random.randn(d+1) * 0.5)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            xi = x[i]
            poly_val = 0.0
            for d, coeffs in enumerate(self.poly_coeffs):
                if d < len(coeffs):
                    poly_val += coeffs[d] * np.power(xi, d)
            result += 0.3 * poly_val * np.exp(-xi**2/10.0)
        
        # Radial basis function with adaptive width
        for i in range(self.dim):
            xi = x[i]
            rbf_sum = 0.0
            for j in range(min(5, self.dim)):
                center = np.sin(i + j) * 3.0
                width = 0.5 + 0.5 * np.abs(np.cos(i + j))
                rbf_sum += np.exp(-0.5 * ((xi - center)/width)**2)
            result += 0.4 * rbf_sum * np.cos(0.5 * xi)
        
        # Multi-scale polynomial coupling with radial interaction
        for i in range(self.dim):
            xi = x[i]
            poly_coupling = 0.0
            for j in range(i+1, self.dim):
                xj = x[j]
                scale_factor = 1.0 + 0.3 * np.sin(xi + xj)
                poly_coupling += (xi**2 + xj**2) * scale_factor * np.cos(0.3 * (xi - xj))
            result += 0.2 * poly_coupling
        
        # Adaptive conditioning with dynamic scaling
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            xi = x[i]
            cond_factor = 1.0 + 0.5 * np.sin(r + i)
            result += 0.1 * xi**3 * cond_factor * np.exp(-abs(xi)/5.0)
        
        # Cross-dimensional exponential interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_interaction = np.exp(-0.1 * (xi**2 + xj**2)) * np.sin(xi * xj)
                result += 0.25 * exp_interaction
        
        # Multi-frequency harmonic terms with polynomial modulation
        for i in range(self.dim):
            xi = x[i]
            freq_sum = 0.0
            for freq in [1.0, 2.0, 3.0, 4.0]:
                freq_sum += np.sin(freq * xi) * np.cos(freq * xi)
            result += 0.3 * freq_sum * (xi**2 + 1.0) * np.exp(-r/8.0)
        
        # Gaussian mixture component with varying weights
        for i in range(3):
            weight = 0.5 + 0.3 * np.sin(i)
            center = np.random.randn(self.dim) * 2.0
            cov = np.eye(self.dim) * (0.5 + 0.2 * np.cos(i))
            diff = x - center
            result += weight * np.exp(-0.5 * np.dot(diff, np.dot(np.linalg.inv(cov), diff)))
        
        # Adaptive polynomial with radial dependency
        for i in range(self.dim):
            xi = x[i]
            poly_degree = 2 + (i % 3)
            poly_val = sum([self.poly_coeffs[poly_degree-1][j] * (xi**j) 
                           for j in range(poly_degree)])
            result += 0.15 * poly_val * np.exp(-r/6.0)
        
        # High-order cross-dimensional interaction
        if self.dim >= 2:
            interaction = 0.0
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    interaction += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
            result += 0.2 * interaction * np.exp(-r/4.0)
        
        # Add noise component to increase ruggedness
        noise = np.random.randn() * 0.1
        result += noise
        
        return result