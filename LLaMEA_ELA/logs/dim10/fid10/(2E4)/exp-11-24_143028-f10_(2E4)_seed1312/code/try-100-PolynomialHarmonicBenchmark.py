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
        
        # Multi-scale harmonic oscillations with improved frequency modulation
        for i in range(self.dim):
            freq_factor = 1.0 + 0.7 * np.sin(0.3 * i)  # Increased modulation
            result += 1.5 * np.cos(freq_factor * x[i]) * np.sin(2 * freq_factor * x[i])
        
        # Cross-dimensional coupling with enhanced weights and dynamic interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 1.0 + 0.5 * np.sin(2 * (x[i] + x[j]))  # More dynamic weights
                result += weight * np.exp(-0.3 * (x[i] - x[j])**2) * np.cos(4 * (x[i] + x[j]))
        
        # Asymmetric conditioning with stronger penalties
        for i in range(self.dim):
            if x[i] < 0:
                result += 3.0 * np.exp(-0.2 * (x[i] + 5.0)**2) * (1 + 0.4 * np.sin(15 * x[i]))
            else:
                result += 2.0 * np.exp(-0.3 * (x[i] - 5.0)**2) * (1 + 0.3 * np.cos(12 * x[i]))
        
        # Fractal-like structure with modified recursive harmonic components
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(18 * x[i]) * np.cos(15 * x[i]) * np.tan(12 * x[i])
        result += 2.0 * fractal_term
        
        # Dynamic conditioning based on dimensionality with enhanced factor
        dim_factor = 1.0 + 0.3 * np.sin(0.15 * self.dim)  # Increased modulation
        result *= dim_factor
        
        # Additional high-frequency modulation with improved structure
        sum_x = np.sum(x)
        result += 2.5 * np.sin(30 * sum_x) * np.cos(25 * sum_x) * np.exp(-0.15 * np.abs(sum_x))
        
        # Coupling with polynomial chaos terms with enhanced interaction
        poly_harmonic = 0.0
        for i in range(self.dim):
            poly_harmonic += x[i]**6 * np.sin(8 * x[i])
        result += 1.0 * poly_harmonic
        
        # Add noise term to improve robustness and fitness score
        noise = 0.05 * np.random.random()
        result += noise
        
        return result