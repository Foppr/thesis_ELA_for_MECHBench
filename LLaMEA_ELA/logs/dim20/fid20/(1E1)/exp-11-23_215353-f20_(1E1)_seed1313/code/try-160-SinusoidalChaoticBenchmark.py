import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with higher frequency harmonics and dynamic amplitudes
        sin_term = np.sum(np.sin(2.0 * x) + 0.6 * np.sin(5.0 * x) + 0.4 * np.sin(9.0 * x) + 0.2 * np.sin(13.0 * x) + 0.1 * np.sin(17.0 * x))
        
        # Modified polynomial distortion with fractional exponents and dynamic coefficients
        poly_term = np.sum((x**3.2 + 0.9 * x**2.1 - 0.6 * x**1.7 + 1.4 * x + 0.8)**1.3)
        
        # Enhanced chaotic component using logistic map with parameter tuning for increased complexity
        chaotic_term = 0.0
        r = 3.95  # Increased chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev))
        
        # Modified Gaussian modulation with multi-scale localization and dynamic widths
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(3.0 * x) + 0.5 * np.exp(-0.7 * (x**2)) * np.sin(2.5 * x))
        
        # Multi-scale radial basis function component with varying center distributions and kernel widths
        rbf_term = 0.0
        centers1 = np.linspace(-5.0, 5.0, 8)
        centers2 = np.linspace(-5.0, 5.0, 12)
        for center in centers1:
            rbf_term += 0.5 * np.exp(-0.5 * np.sum((x - center)**2) / 0.3**2)
        for center in centers2:
            rbf_term += 0.3 * np.exp(-0.5 * np.sum((x - center)**2) / 0.7**2)
        
        # High-frequency interference pattern with dynamic phase shifts and amplitude modulation
        interference_term = np.sum(np.sin(25.0 * x + 0.5 * np.sin(19.0 * x)) * np.cos(20.0 * x + 0.3 * np.cos(15.0 * x)))
        
        # Cross-term interaction with dynamic coupling strength and directional bias
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:] + 0.3 * np.cos(x[:-1] - x[1:])))
        
        # Additional quadratic distortion with variable coefficients for increased non-convexity
        quad_distort = np.sum(0.45 * (x**2) * np.sin(0.7 * x) + 0.25 * (x**3) * np.cos(0.4 * x))
        
        # Novel hybrid coupling term that combines exponential and trigonometric interactions
        hybrid_term = np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(2.0 * x) * np.cos(1.5 * x))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.21 * sin_term + 0.19 * poly_term + 0.15 * chaotic_term + 0.13 * gauss_term + 0.12 * rbf_term + 0.10 * interference_term + 0.06 * cross_term + 0.05 * quad_distort + 0.04 * hybrid_term + 2.5