import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial coefficients for chaos expansion
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        
    def f(self, x):
        x = np.array(x)
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(5):
                poly_val += self.poly_coeffs[i, j] * (x[i] ** j)
            result += 0.3 * poly_val * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function with asymmetric peaks
        centers = np.random.uniform(-4.0, 4.0, (5, self.dim))
        widths = np.random.uniform(0.5, 2.0, 5)
        heights = np.random.uniform(1.0, 3.0, 5)
        
        for i in range(5):
            rbf_val = 0.0
            for j in range(self.dim):
                rbf_val += (x[j] - centers[i, j])**2
            rbf_val = np.exp(-widths[i] * rbf_val)
            result += heights[i] * rbf_val
        
        # Asymmetric Gaussian peaks with varying scales
        for i in range(self.dim):
            peak_center = np.random.uniform(-4.0, 4.0)
            sigma_pos = np.random.uniform(0.5, 1.5)
            sigma_neg = np.random.uniform(0.3, 1.2)
            
            diff = x[i] - peak_center
            if diff > 0:
                result += 0.5 * np.exp(-0.5 * (diff**2) / (sigma_pos**2))
            else:
                result += 0.4 * np.exp(-0.5 * (diff**2) / (sigma_neg**2))
        
        # Cross-dimensional coupling with trigonometric modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                result += 0.2 * coupling * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Boundary attraction with polynomial penalty
        for i in range(self.dim):
            boundary_penalty = (5.0 - abs(x[i]))**4
            if boundary_penalty > 0:
                result += 0.15 * boundary_penalty
        
        # Add noise term to increase complexity
        result += 0.05 * np.random.uniform(-1.0, 1.0)
        
        return result