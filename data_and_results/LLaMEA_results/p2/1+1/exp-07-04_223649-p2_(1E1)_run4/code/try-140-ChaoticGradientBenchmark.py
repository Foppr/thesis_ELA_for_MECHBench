import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Exponential decay interaction terms with chaotic multipliers
        exp_decay = 0.5 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(2.0 * np.pi * x))
        
        # Trigonometric coupling with adaptive frequencies
        trig_coupling = 0.3 * np.sum(np.sin(x[:-1] * x[1:] + np.pi/4) * np.cos(x[:-1] + x[1:]))
        
        # Chaotic perturbation using logistic map-like behavior
        chaotic = 0.4 * np.sum(np.sin(np.pi * np.sin(x)) * np.cos(np.pi * np.cos(x)))
        
        # Adaptive noise component with varying intensity
        noise = 0.2 * np.sum(np.sin(10.0 * x) * np.exp(-0.5 * x**2))
        
        # Multi-scale oscillatory behavior with diminishing amplitude
        multi_scale = 0.3 * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Saddle-point inducing term with hyperbolic tangent
        saddle = 0.25 * np.sum(np.tanh(x) * np.sin(x**2))
        
        # Polynomial distortion with exponential scaling
        poly_dist = 0.15 * np.sum(np.exp(0.5 * x**2) - 1.0)
        
        # Combined result
        result = result + exp_decay + trig_coupling + chaotic + noise + multi_scale + saddle + poly_dist
        
        return result