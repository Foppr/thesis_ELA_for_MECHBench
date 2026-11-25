import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Multi-frequency sinusoidal wave component with varying amplitudes and phases
        sin_term = np.sum(np.sin(2.0 * x) + 0.7 * np.sin(5.0 * x) + 0.4 * np.sin(9.0 * x) + 0.2 * np.sin(13.0 * x) + 0.1 * np.sin(17.0 * x))
        
        # Polynomial distortion with fractional exponents for irregular shaping
        poly_term = np.sum((x**3.2 + 0.9 * x**2.1 - 0.6 * x**1.7 + 1.3 * x + 0.8)**1.2)
        
        # Chaotic component using logistic map with parameter tuning for complexity
        chaotic_term = 0.0
        r = 3.95
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev))
        
        # Gaussian modulation with variable widths to create localized peaks and valleys
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(3.0 * x) + 0.5 * np.exp(-0.7 * (x**2)) * np.sin(2.5 * x))
        
        # Radial basis function component with adaptive centers and widths
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 15)
        widths = np.linspace(0.3, 1.5, 15)
        for i, center in enumerate(centers):
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / widths[i]**2)
        
        # High-frequency interference pattern with multiple wave components
        interference_term = np.sum(np.sin(25.0 * x) * np.cos(18.0 * x) + 0.6 * np.sin(30.0 * x) * np.cos(22.0 * x))
        
        # Cross-term interaction with higher-order coupling
        cross_term = np.sum(x[:-2] * x[1:-1] * x[2:] * np.sin(x[:-2] + x[1:-1] + x[2:]))
        
        # Additional quadratic distortion with sine modulation to enhance non-convexity
        quad_distort = np.sum(0.4 * (x**2) * np.sin(0.7 * x) + 0.3 * (x**3) * np.cos(0.5 * x))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.18 * sin_term + 0.16 * poly_term + 0.14 * chaotic_term + 0.13 * gauss_term + 0.11 * rbf_term + 0.10 * interference_term + 0.07 * cross_term + 0.06 * quad_distort + 2.5