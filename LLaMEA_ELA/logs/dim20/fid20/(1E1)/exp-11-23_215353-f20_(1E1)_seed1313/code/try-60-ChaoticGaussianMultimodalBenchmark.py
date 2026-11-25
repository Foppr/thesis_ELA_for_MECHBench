import numpy as np

class ChaoticGaussianMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components with varying widths and centers
        centers = np.linspace(-4.0, 4.0, self.dim)
        widths = np.logspace(-1, 1, self.dim)
        gaussian_term = np.sum(widths * np.exp(-0.5 * ((x - centers) / (0.5 * widths))**2))
        
        # Sinusoidal modulation with multiple frequencies and amplitudes
        sin_term = np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * np.sin(2.0 * x) * np.exp(-0.1 * x**2))
        
        # Chaotic component using logistic map iterations with parameter modulation
        chaotic_input = np.sin(x) * 3.5
        chaotic_term = 0.0
        for i in range(10):
            chaotic_input = 3.8 * chaotic_input * (1 - chaotic_input)
            chaotic_term += np.sin(chaotic_input * 10.0)
        chaotic_term /= 10.0
        
        # Polynomial distortion with non-integer exponents
        poly_term = np.sum((x**2.3 + 0.7 * x**1.9 - 0.5 * x**1.1 + 0.9 * x)**1.5)
        
        # Additional harmonic and exponential mixing
        harm_exp_term = np.sum(np.exp(-0.3 * x**2) * np.cos(5.0 * x) * np.sin(1.2 * x))
        
        # Combine all terms with optimized weights
        return 0.25 * gaussian_term + 0.20 * sin_term + 0.25 * chaotic_term + 0.15 * poly_term + 0.15 * harm_exp_term + 2.0