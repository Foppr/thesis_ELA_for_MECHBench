import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with higher frequency harmonics
        sin_term = np.sum(np.sin(1.5 * x) + 0.6 * np.sin(4.0 * x) + 0.4 * np.sin(9.0 * x) + 0.2 * np.sin(15.0 * x) + 0.1 * np.sin(23.0 * x))
        
        # Modified polynomial distortion with fractional exponents and increased complexity
        poly_term = np.sum((x**2.7 + 0.9 * x**2.1 - 0.6 * x**1.5 + 1.4 * x + 0.8)**1.3)
        
        # Enhanced chaotic component using logistic map with increased parameter for greater complexity
        chaotic_term = 0.0
        r = 3.95  # Increased chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev))
        
        # Modified Gaussian modulation with multiple peaks and valleys
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(2.5 * x) + 0.3 * np.exp(-0.7 * (x**2)) * np.sin(3.0 * x))
        
        # Enhanced radial basis function component with adaptive centers and widths
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 15)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.3**2)
        
        # Increased frequency interference pattern with cross-modulation
        interference_term = np.sum(np.sin(28.0 * x) * np.cos(21.0 * x) + 0.5 * np.sin(35.0 * x) * np.cos(27.0 * x))
        
        # Novel cross-term interaction with higher-order coupling
        cross_term = np.sum(x[:-2] * x[1:-1] * x[2:] * np.sin(x[:-2] + x[1:-1] + x[2:]))
        
        # Enhanced quadratic distortion with additional trigonometric modulation
        quad_distort = np.sum(0.45 * (x**2) * np.sin(0.7 * x) + 0.25 * (x**3) * np.cos(0.4 * x))
        
        # Additional harmonic component for increased multimodality
        harmonic_term = np.sum(0.15 * np.sin(5.0 * x) * np.cos(8.0 * x) + 0.1 * np.sin(12.0 * x) * np.cos(13.0 * x))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.21 * sin_term + 0.19 * poly_term + 0.15 * chaotic_term + 0.16 * gauss_term + 0.12 * rbf_term + 0.13 * interference_term + 0.08 * cross_term + 0.07 * quad_distort + 0.09 * harmonic_term + 2.5