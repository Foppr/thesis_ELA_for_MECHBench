import numpy as np

class PolynomialRBFTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial coefficients for chaos expansion
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 5))
        
    def f(self, x):
        x = np.array(x)
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial chaos expansion component with varying degrees
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(5):
                poly_term += self.poly_coeffs[i, j] * (x[i] ** j)
            result += 0.3 * poly_term * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function with Gaussian kernels and varying widths
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(min(3, self.dim)):
                if i != j:
                    width = 0.5 + 0.5 * np.abs(x[i] - x[j])
                    rbf_sum += np.exp(-0.5 * ((x[i] - x[j]) / width)**2)
            result += 0.2 * rbf_sum * (1.0 + 0.1 * i)
        
        # Sine-cosine coupling with radial interaction
        for i in range(self.dim):
            freq = 3.0 + 0.5 * i
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.2 * abs(x[i]))
        
        # Multi-scale trigonometric interactions with radial symmetry
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.5 * np.sin(5.0 * r) * np.cos(3.0 * r) * np.exp(-0.1 * r)
        
        # Cross-dimensional polynomial coupling with interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Asymmetric exponential terms with coordinate-dependent scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.25 * np.exp(-0.4 * x[i]) * (1.0 + 0.2 * x[i]**3)
            else:
                result += 0.2 * np.exp(-0.5 * abs(x[i])) * (1.0 + 0.15 * x[i]**3)
        
        # High-frequency oscillatory component with varying amplitudes
        for i in range(self.dim):
            result += 0.3 * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i]) * (1.0 + 0.05 * abs(x[i]))
        
        # Add global modulation with polynomial and exponential components
        sum_squares = np.sum(x**2)
        result += 0.35 * np.exp(-0.15 * sum_squares) * np.sin(2.0 * sum_squares + 0.05 * sum_squares**2)
        
        # Boundary attraction with enhanced penalty
        for i in range(self.dim):
            result += 0.2 * (5.0 - abs(x[i]))**4
        
        # Additional coupling through higher-order polynomial terms
        for i in range(min(3, self.dim)):
            result += 0.1 * x[i]**5 * np.sin(x[i])
        
        return result