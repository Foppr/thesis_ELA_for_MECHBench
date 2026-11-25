import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with varying frequencies and amplitudes
        sin_term = np.sum(0.8 * np.sin(1.0 * x) + 0.4 * np.sin(3.0 * x) + 0.2 * np.sin(7.0 * x) + 0.1 * np.sin(11.0 * x))
        
        # Modified polynomial distortion with non-integer exponents for irregular shaping
        poly_term = np.sum((x**2.7 + 0.9 * x**1.8 - 0.6 * x**1.4 + 1.1 * x + 0.6)**1.2)
        
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
        
        # Enhanced Gaussian modulation to create localized peaks and valleys
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(2.5 * x))
        
        # Improved radial basis function component for multi-scale landscape features
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 12)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.4**2)
        
        # Enhanced high-frequency interference pattern to increase complexity
        interference_term = np.sum(np.sin(25.0 * x) * np.cos(18.0 * x))
        
        # Improved cross-term interaction for increased complexity
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]) * 0.5)
        
        # Enhanced quadratic distortion to boost non-convexity
        quad_distort = np.sum(0.4 * (x**2) * np.sin(0.6 * x))
        
        # Additional harmonic component for increased multimodality
        harmonic_term = np.sum(np.sin(5.0 * x) * np.cos(8.0 * x) * 0.3)
        
        # Add a global scaling factor to balance contribution of terms
        return 0.22 * sin_term + 0.20 * poly_term + 0.14 * chaotic_term + 0.16 * gauss_term + 0.13 * rbf_term + 0.11 * interference_term + 0.09 * cross_term + 0.06 * quad_distort + 0.05 * harmonic_term + 2.0