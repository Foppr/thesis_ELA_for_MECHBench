import numpy as np

class TrigonometricEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base elliptical valley term with adaptive eccentricity
        ellipse = np.sum((x_norm[:-1]**2 + 0.3 * x_norm[1:]**2) * np.exp(-0.15 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Periodic trigonometric oscillations with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                          np.exp(-0.25 * x_norm**2))
        
        # Saddle point structure with hyperbolic tangent interactions
        saddle = np.sum(np.tanh(2.5 * x_norm[:-1]) * np.tanh(2.5 * x_norm[1:]) * 
                       (x_norm[:-1]**2 - x_norm[1:]**2))
        
        # Adaptive Gaussian peaks with elliptical contours and dynamic positioning
        gaussian_elliptic = 0.9 * np.sum(np.exp(-4 * ((x_norm[:-1] - 0.35 * np.sin(3.5 * x_norm[:-1]))**2 + 
                                                      (x_norm[1:] + 0.25 * np.cos(2.5 * x_norm[1:]))**2)))
        
        # Cross-dimensional coupling with logarithmic spiral pattern
        spiral_coupling = 0.7 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                     np.sin(12 * np.pi * np.arctan2(x_norm[1:], x_norm[:-1])))
        
        # High-frequency modulated sinusoidal component
        high_freq = 1.0 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                               np.exp(-0.15 * x_norm**2))
        
        # Dimension-dependent conditioning factor with exponential growth
        condition_factor = 1.0 + 0.6 * np.log(self.dim + 1)
        
        # Combine all terms
        return condition_factor * (ellipse + trig_term + saddle + gaussian_elliptic + 
                                 spiral_coupling + high_freq)