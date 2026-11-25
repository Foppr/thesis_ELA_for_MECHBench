import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(1.0 * x) + 0.5 * np.sin(3.0 * x) + 0.3 * np.sin(7.0 * x) + 0.1 * np.sin(11.0 * x))
        
        # Polynomial distortion with non-integer exponents for irregular shaping
        poly_term = np.sum((x**2.5 + 0.8 * x**1.9 - 0.5 * x**1.3 + 1.2 * x + 0.7)**1.1)
        
        # Chaotic component using tent map with parameter tuning for complexity
        chaotic_term = 0.0
        a = 1.8
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            if x_prev < 0.5:
                chaotic_term += np.sin(a * x_prev)
            else:
                chaotic_term += np.sin(a * (1 - x_prev))
        
        # Gaussian modulation to create localized peaks and valleys
        gauss_term = np.sum(np.exp(-0.5 * (x**2)) * np.cos(2.0 * x))
        
        # Radial basis function component for multi-scale landscape features
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 10)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.5**2)
        
        # High-frequency interference pattern to increase complexity
        interference_term = np.sum(np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Cross-term interaction for increased complexity
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]))
        
        # Combine all terms with optimized weights
        return 0.25 * sin_term + 0.20 * poly_term + 0.15 * chaotic_term + 0.15 * gauss_term + 0.10 * rbf_term + 0.10 * interference_term + 0.05 * cross_term + 2.0