import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for stability
        self.harmonic_coeffs = np.array([1.0, 0.7, 0.5, 0.3, 0.2])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with conditioning
        result = 0.5 * np.sum(x**4) + 0.3 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        # Polynomial chaos expansion with varying degrees
        for i in range(self.dim):
            result += 2.0 * x[i]**5 + 1.5 * x[i]**4 - 0.8 * x[i]**3
        
        # Radial harmonic components with dynamic frequencies
        radial_sum = np.sum(x**2)
        result += 3.0 * np.exp(-0.1 * radial_sum) * np.sin(10 * np.sqrt(radial_sum))
        
        # Multi-scale harmonic oscillations
        for i in range(self.dim):
            freq_factor = 1.0 + 0.5 * np.sin(0.5 * i)
            result += 1.2 * np.cos(freq_factor * x[i]) * np.sin(2 * freq_factor * x[i])
        
        # Cross-dimensional coupling with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.8 + 0.2 * np.sin(3 * (x[i] + x[j]))
                result += weight * np.exp(-0.5 * (x[i] - x[j])**2) * np.cos(5 * (x[i] + x[j]))
        
        # Asymmetric conditioning with exponential penalties
        for i in range(self.dim):
            if x[i] < 0:
                result += 2.5 * np.exp(-0.3 * (x[i] + 5.0)**2) * (1 + 0.3 * np.sin(12 * x[i]))
            else:
                result += 1.8 * np.exp(-0.4 * (x[i] - 5.0)**2) * (1 + 0.2 * np.cos(10 * x[i]))
        
        # Fractal-like structure with recursive harmonic components
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(15 * x[i]) * np.cos(13 * x[i]) * np.tan(11 * x[i])
        result += 1.5 * fractal_term
        
        # Dynamic conditioning based on dimensionality
        dim_factor = 1.0 + 0.2 * np.sin(0.1 * self.dim)
        result *= dim_factor
        
        # Additional high-frequency modulation
        sum_x = np.sum(x)
        result += 2.0 * np.sin(25 * sum_x) * np.cos(22 * sum_x) * np.exp(-0.1 * np.abs(sum_x))
        
        # Coupling with polynomial chaos terms
        poly_harmonic = 0.0
        for i in range(self.dim):
            poly_harmonic += x[i]**6 * np.sin(7 * x[i])
        result += 0.8 * poly_harmonic
        
        return result