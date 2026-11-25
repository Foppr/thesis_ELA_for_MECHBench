import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(1.2 * x) + 0.6 * np.sin(3.5 * x) + 0.4 * np.sin(7.5 * x) + 0.15 * np.sin(11.5 * x))
        
        # Polynomial distortion with non-integer exponents for irregular shaping
        poly_term = np.sum((x**2.7 + 0.9 * x**2.1 - 0.6 * x**1.5 + 1.3 * x + 0.8)**1.2)
        
        # Chaotic component using tent map with parameter tuning for complexity
        chaotic_term = 0.0
        a = 1.9  # Slight increase in chaos parameter
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
        gauss_term = np.sum(np.exp(-0.5 * (x**2)) * np.cos(2.2 * x))
        
        # Radial basis function component for multi-scale landscape features
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 10)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.4**2)
        
        # High-frequency interference pattern to increase complexity
        interference_term = np.sum(np.sin(23.0 * x) * np.cos(18.0 * x))  # Increased frequencies
        
        # Cross-term interaction for increased complexity
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]))
        
        # Additional quadratic distortion to enhance non-convexity
        quad_distort = np.sum(0.4 * (x**2) * np.sin(0.6 * x))  # Slight increase in coefficient
        
        # Add a global scaling factor to balance contribution of terms
        return 0.18 * sin_term + 0.16 * poly_term + 0.14 * chaotic_term + 0.15 * gauss_term + 0.12 * rbf_term + 0.10 * interference_term + 0.08 * cross_term + 0.07 * quad_distort + 2.1