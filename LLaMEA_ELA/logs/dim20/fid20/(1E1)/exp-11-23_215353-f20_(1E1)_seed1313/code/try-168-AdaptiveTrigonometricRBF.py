import numpy as np

class AdaptiveTrigonometricRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric component with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) + 0.5 * np.sin(5.0 * x) * np.cos(7.0 * x))
        
        # Exponential distortion with adaptive scaling based on dimensionality
        exp_term = np.sum(np.exp(-0.5 * (x**2)) * (1.0 + 0.3 * np.sin(4.0 * x)))
        
        # Radial basis function component with dynamic centers and widths
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, min(20, self.dim * 2))
        for i in range(len(centers)):
            if i < len(centers) and i < self.dim:
                width = 0.3 + 0.2 * np.sin(i * 0.5)
                rbf_term += np.exp(-0.5 * ((x[i] - centers[i])**2) / (width**2))
        
        # Cross-term interaction with adaptive coupling strength
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i]**2 + x[i+1]**2) * np.sin(0.5 * (x[i] + x[i+1]))
        
        # Hyperbolic tangent modulation to create sharp transitions
        tanh_term = np.sum(np.tanh(2.0 * x) * np.cos(0.8 * x))
        
        # Multi-scale oscillation with frequency modulation
        freq_mod = np.sum(np.sin(x * (1.0 + 0.2 * np.sin(0.3 * x))) * np.cos(x * (1.5 + 0.1 * np.cos(0.7 * x))))
        
        # Adaptive quadratic distortion with dimension-dependent coefficients
        quad_term = np.sum(0.4 * (x**2) * (1.0 + 0.1 * np.sin(3.0 * x)))
        
        # Global scaling and offset to ensure proper fitness range
        return 0.2 * trig_term + 0.15 * exp_term + 0.25 * rbf_term + 0.1 * cross_term + 0.12 * tanh_term + 0.08 * freq_mod + 0.07 * quad_term + 1.5