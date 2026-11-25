import numpy as np

class GaussianSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components with varying widths and centers
        gauss_term = np.sum(np.exp(-np.sum((x[:, None] - np.linspace(-4, 4, 9))**2, axis=0) / (2 * 0.5**2)))
        
        # Sinusoidal modulation with multiple frequencies and amplitudes
        sin_term = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.sin(1.0 * x))
        
        # Cross-term interaction with global scaling factor
        cross_term = np.sum(x**2) * np.exp(-np.sum(x**2) / (2 * 10.0**2))
        
        # Polynomial distortion with non-integer exponents for added complexity
        poly_term = np.sum((x**3.5 + 0.7 * x**2.3 - 0.9 * x**1.8 + 1.2 * x)**1.5)
        
        # Sine-based chaotic component with nested frequencies
        chaotic_term = np.sum(np.sin(5.0 * np.sin(2.0 * x)) + np.cos(4.0 * np.cos(3.0 * x)))
        
        # Combine all terms with dynamically adjusted weights based on dimensionality
        weight_gauss = 0.25 + 0.05 * self.dim
        weight_sin = 0.20 + 0.03 * self.dim
        weight_cross = 0.15 + 0.02 * self.dim
        weight_poly = 0.25 - 0.01 * self.dim
        weight_chaotic = 0.15 - 0.02 * self.dim
        
        return weight_gauss * gauss_term + weight_sin * sin_term + weight_cross * cross_term + \
               weight_poly * poly_term + weight_chaotic * chaotic_term + 2.0