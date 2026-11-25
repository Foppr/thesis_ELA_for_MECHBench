import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with varying frequencies and amplitudes
        sin_term = np.sum(0.8 * np.sin(1.0 * x) + 0.4 * np.sin(3.0 * x) + 0.2 * np.sin(7.0 * x) + 0.1 * np.sin(11.0 * x))
        
        # Polynomial distortion with non-integer exponents for irregular shaping
        poly_term = np.sum((x**2.7 + 0.9 * x**1.8 - 0.6 * x**1.4 + 1.3 * x + 0.6)**1.2)
        
        # Chaotic component using logistic map with parameter tuning for complexity
        chaotic_term = 0.0
        r = 3.98
        x_prev = 0.5
        for i in range(self.dim):
            x_prev = r * x_prev * (1 - x_prev)
            chaotic_term += np.sin(x_prev)
        
        # Gaussian modulation to create localized peaks and valleys
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(1.5 * x))
        
        # Cross-term interaction for increased complexity with modified coefficients
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.5 * (x[:-1] + x[1:])))
        
        # Additional harmonic component to increase multimodality
        harm_term = np.sum(0.3 * np.sin(5.0 * x) * np.cos(2.0 * x))
        
        # Combine all terms with optimized weights
        return 0.30 * sin_term + 0.20 * poly_term + 0.25 * chaotic_term + 0.15 * gauss_term + 0.05 * cross_term + 0.05 * harm_term + 1.8