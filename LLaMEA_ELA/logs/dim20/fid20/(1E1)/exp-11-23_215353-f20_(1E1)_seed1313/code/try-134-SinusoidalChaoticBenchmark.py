import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(1.5 * x) + 0.6 * np.sin(3.5 * x) + 0.4 * np.sin(7.5 * x) + 0.2 * np.sin(11.5 * x))
        
        # Polynomial distortion with non-integer exponents for irregular shaping
        poly_term = np.sum((x**2.7 + 0.9 * x**2.1 - 0.6 * x**1.5 + 1.3 * x + 0.8)**1.2)
        
        # Chaotic component using tent map with parameter tuning for complexity
        chaotic_term = 0.0
        a = 1.9
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
        gauss_term = np.sum(np.exp(-0.5 * (x**2)) * np.cos(2.5 * x))
        
        # Radial basis function component for multi-scale landscape features with shifted centers
        rbf_term = 0.0
        centers = np.linspace(-4.5, 4.5, 12)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.6**2)
        
        # High-frequency interference pattern to increase complexity
        interference_term = np.sum(np.sin(22.0 * x) * np.cos(17.0 * x))
        
        # Cross-term interaction for increased complexity
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]))
        
        # Additional quadratic distortion to enhance non-convexity
        quad_distort = np.sum(0.35 * (x**2) * np.sin(0.6 * x))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.18 * sin_term + 0.20 * poly_term + 0.14 * chaotic_term + 0.13 * gauss_term + 0.11 * rbf_term + 0.11 * interference_term + 0.07 * cross_term + 0.06 * quad_distort + 2.1