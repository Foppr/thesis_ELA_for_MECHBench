import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with increased frequency and amplitude variations
        sin_term = np.sum(1.2 * np.sin(2.0 * x) + 0.8 * np.sin(5.0 * x) + 0.4 * np.sin(9.0 * x) + 0.2 * np.sin(13.0 * x))
        
        # Modified polynomial distortion with higher-order non-integer exponents
        poly_term = np.sum((x**3.1 + 0.9 * x**2.7 - 0.6 * x**2.1 + 1.4 * x + 0.8)**1.3)
        
        # Enhanced chaotic component using logistic map with increased parameter for greater complexity
        chaotic_term = 0.0
        r = 3.95  # Increased chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev))
        
        # Modified Gaussian modulation with variable width and phase shifts
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(3.0 * x + 0.5))
        
        # Enhanced radial basis function component with adaptive centers and widths
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 15)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.3**2)
        
        # High-frequency interference pattern with multiple harmonic components
        interference_term = np.sum(np.sin(25.0 * x) * np.cos(19.0 * x) + 0.5 * np.sin(31.0 * x) * np.cos(23.0 * x))
        
        # Novel cross-term interaction with trigonometric coupling for increased complexity
        cross_term = np.sum(np.sin(x[:-1]) * np.cos(x[1:]) * (x[:-1] + x[1:]))
        
        # Additional quadratic distortion with phase modulation to enhance non-convexity
        quad_distort = np.sum(0.45 * (x**2) * np.sin(0.7 * x + 0.3))
        
        # Novel exponential distortion component for enhanced landscape ruggedness
        exp_distort = np.sum(0.25 * np.exp(0.5 * x) * np.cos(1.5 * x))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.18 * sin_term + 0.16 * poly_term + 0.14 * chaotic_term + 0.13 * gauss_term + 0.12 * rbf_term + 0.10 * interference_term + 0.08 * cross_term + 0.07 * quad_distort + 0.06 * exp_distort + 2.5