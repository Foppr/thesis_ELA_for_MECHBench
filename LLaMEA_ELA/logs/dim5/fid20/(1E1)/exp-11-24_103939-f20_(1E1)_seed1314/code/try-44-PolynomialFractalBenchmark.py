import numpy as np

class PolynomialFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for fractal-like behavior
        self.chaos_coeffs = np.random.randn(dim, 10) * 0.5
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Polynomial chaos expansion component with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(10):
                poly_term += self.chaos_coeffs[i, j] * np.polynomial.hermite.hermval(x_scaled[i], [0]*j + [1])
        
        # Fractal sinusoidal modulation with multiple frequencies and amplitudes
        fractal_term = 0.0
        frequencies = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for freq in frequencies:
            fractal_term += np.sin(freq * x_scaled) * np.cos(freq * x_scaled**2) * np.sin(freq**0.5 * x_scaled)
        
        # Multi-scale Gaussian mixture with varying covariances
        gaussian_term = 0.0
        centers = np.linspace(-1, 1, 8)
        for center in centers:
            gaussian_term += np.exp(-5 * (x_scaled - center)**2) + np.exp(-3 * (x_scaled + center)**2)
        
        # Cross-dimensional coupling with asymmetric interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_scaled[i] * x_scaled[j]) * np.cos(x_scaled[i]**2 + x_scaled[j]**2)
        
        # Power-law modified trigonometric terms for scale-invariant ruggedness
        power_term = 0.0
        for i in range(self.dim):
            power_term += (np.abs(x_scaled[i])**1.5) * np.sin(20 * x_scaled[i])**2
        
        # Logarithmic barrier to create narrow valleys
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += np.log(1 + 0.1 * np.abs(x_scaled[i])) * np.sin(30 * x_scaled[i])**2
        
        # Combine all terms with appropriate weights
        return (0.8 * poly_term + 
                0.6 * fractal_term + 
                0.7 * gaussian_term + 
                0.5 * cross_term + 
                0.4 * power_term + 
                0.3 * barrier_term)