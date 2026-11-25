import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2.0 * x) + 0.6 * np.sin(5.0 * x) + 0.4 * np.sin(9.0 * x) + 0.2 * np.sin(13.0 * x))
        
        # Modified polynomial distortion with non-integer exponents for irregular shaping
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
        
        # Gaussian modulation to create localized peaks and valleys with modified parameters
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(3.0 * x))
        
        # Radial basis function component for multi-scale landscape features with adjusted centers
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 12)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.3**2)
        
        # High-frequency interference pattern to increase complexity with modified frequencies
        interference_term = np.sum(np.sin(25.0 * x) * np.cos(20.0 * x))
        
        # Enhanced cross-term interaction for increased complexity
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        # Additional quadratic interaction term to improve conditioning
        quad_interaction = np.sum((x[:-1] - x[1:])**2)
        
        # Combine all terms with optimized weights for better performance
        return 0.30 * sin_term + 0.25 * poly_term + 0.18 * chaotic_term + 0.12 * gauss_term + 0.08 * rbf_term + 0.07 * interference_term + 0.04 * cross_term + 0.03 * quad_interaction + 1.5