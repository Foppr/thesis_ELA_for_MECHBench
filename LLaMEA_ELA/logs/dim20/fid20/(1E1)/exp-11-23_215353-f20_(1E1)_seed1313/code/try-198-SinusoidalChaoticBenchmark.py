import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with variable frequencies and amplitudes
        sin_term = np.sum(1.2 * np.sin(1.5 * x) + 0.6 * np.sin(4.0 * x) + 0.4 * np.sin(8.0 * x) + 0.2 * np.sin(12.0 * x))
        
        # Adaptive polynomial distortion with non-integer exponents for irregular shaping
        poly_term = np.sum((x**2.7 + 0.9 * x**2.1 - 0.6 * x**1.5 + 1.3 * x + 0.8)**1.2)
        
        # Chaotic component using tent map with parameter tuning for complexity
        chaotic_term = 0.0
        a = 1.9  # Increased chaos parameter for more complex dynamics
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
        gauss_term = np.sum(np.exp(-0.4 * (x**2)) * np.cos(2.5 * x))
        
        # Radial basis function component for multi-scale landscape features
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 12)  # Increased number of centers for finer granularity
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.4**2)
        
        # High-frequency interference pattern to increase complexity
        interference_term = np.sum(np.sin(25.0 * x) * np.cos(20.0 * x))  # Increased frequencies
        
        # Cross-term interaction for increased complexity
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]) * 0.5)
        
        # Additional quadratic distortion to enhance non-convexity with adaptive scaling
        quad_distort = np.sum(0.4 * (x**2) * np.sin(0.6 * x))  # Increased coefficient and frequency
        
        # Adaptive scaling factors to balance contributions
        return 0.21 * sin_term + 0.19 * poly_term + 0.15 * chaotic_term + 0.16 * gauss_term + 0.12 * rbf_term + 0.13 * interference_term + 0.08 * cross_term + 0.07 * quad_distort + 2.2