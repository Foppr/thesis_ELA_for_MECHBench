import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with varying curvature
        quadratic = np.sum(x_scaled**2)
        
        # Saddle point modifier with chaotic frequency modulation
        saddle = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled)) * 0.3
        
        # Chaotic gradient component with time-varying coefficients
        chaotic = np.sum(np.sin(15 * np.sin(x_scaled)) * np.cos(12 * np.cos(x_scaled)) * 
                         (1.0 + 0.2 * np.sin(3 * x_scaled)))
        
        # Multi-scale oscillatory term with varying amplitude
        multi_scale = np.sum((np.sin(20 * x_scaled**2) + 0.5 * np.cos(15 * x_scaled)) * 
                            (0.8 + 0.2 * np.sin(5 * x_scaled)))
        
        # Exponential interaction with variable decay rate
        exp_interaction = np.sum(np.exp(-x_scaled**2 * (1.0 + 0.3 * np.sin(4 * x_scaled))) * 
                               (1.0 + 0.4 * np.cos(6 * x_scaled)))
        
        # Radial harmonic component with phase shifting
        radial_harmonic = np.sum((x_scaled**2 + 0.1) * np.sin(8 * np.arctan2(x_scaled, 1.0)) * 
                                (1.0 + 0.3 * np.cos(3 * x_scaled)))
        
        # Coupled trigonometric and polynomial terms
        coupled = np.sum((np.sin(9 * x_scaled) + 0.5 * x_scaled**3) * 
                        (1.0 + 0.2 * np.cos(5 * x_scaled**2)))
        
        # Combined function with diverse curvature and complex landscape
        return 2.5 * quadratic + 1.8 * saddle + 0.7 * chaotic + 0.6 * multi_scale + 0.5 * exp_interaction + 0.4 * radial_harmonic + 0.3 * coupled