import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for polynomial chaos expansion
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 5))
        # Precompute RBF centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, size=10)
        # Asymmetric peak parameters
        self.peak_centers = np.random.uniform(-5.0, 5.0, size=dim)
        self.peak_heights = np.random.uniform(1.0, 3.0, size=dim)
        self.peak_widths = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        x = np.array(x)
        # Clip to domain
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(5):
                poly_term += self.poly_coeffs[i, j] * (x[i] ** j)
            result += 0.3 * poly_term * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function component with multiple peaks
        for i in range(10):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x[j] - self.rbf_centers[i, j])**2
            result += 0.4 * np.exp(-self.rbf_widths[i] * rbf_sum)
        
        # Asymmetric Gaussian peaks with varying heights and widths
        for i in range(self.dim):
            peak_dist = (x[i] - self.peak_centers[i])**2
            # Asymmetric effect: different decay rates based on sign of x[i]
            if x[i] >= 0:
                result += self.peak_heights[i] * np.exp(-self.peak_widths[i] * peak_dist) * (1.0 + 0.1 * x[i])
            else:
                result += self.peak_heights[i] * np.exp(-self.peak_widths[i] * peak_dist * 1.5) * (1.0 - 0.1 * x[i])
        
        # Cross-dimensional interaction terms with polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i]**2 + x[j]**2)**0.5
                result += 0.2 * np.sin(interaction) * np.cos(x[i] * x[j]) * (1.0 + 0.05 * (i + j))
        
        # Add high-frequency oscillatory component with polynomial modulation
        for i in range(self.dim):
            result += 0.25 * np.sin(20.0 * x[i]) * (1.0 + 0.1 * x[i]**2) * np.exp(-0.05 * x[i]**2)
        
        # Add global modulation based on sum of absolute values with enhanced nonlinearity
        sum_abs = np.sum(np.abs(x))
        result += 0.3 * np.exp(-0.3 * sum_abs) * np.sin(5.0 * sum_abs + 0.2 * sum_abs**2)
        
        # Add boundary attraction with variable penalty strength
        for i in range(self.dim):
            boundary_penalty = (5.0 - abs(x[i]))**4
            result += 0.15 * boundary_penalty
        
        # Add coupling between distant dimensions
        if self.dim >= 4:
            for i in range(0, self.dim-3):
                for j in range(i+3, self.dim):
                    result += 0.1 * np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (i + j)
        
        return result