import numpy as np

class TrigonometricEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base elliptical valley term with adaptive eccentricity and chaotic modulation
        ellipse = np.sum((x_norm[:-1]**2 + 0.3 * x_norm[1:]**2) * 
                        np.exp(-0.15 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                        (1 + 0.2 * np.sin(10 * x_norm[:-1]) * np.cos(8 * x_norm[1:])))
        
        # Chaotic trigonometric oscillations with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(12 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                          np.exp(-0.4 * x_norm**2) * (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Saddle point structure with hyperbolic tangent interactions and chaotic perturbations
        saddle = np.sum(np.tanh(4 * x_norm[:-1]) * np.tanh(4 * x_norm[1:]) * 
                       (x_norm[:-1]**2 - x_norm[1:]**2) * 
                       (1 + 0.1 * np.cos(7 * x_norm[:-1]) * np.sin(6 * x_norm[1:])))
        
        # Adaptive Gaussian peaks with elliptical contours, dynamic positioning, and chaotic shifts
        gaussian_elliptic = 1.0 * np.sum(np.exp(-4 * ((x_norm[:-1] - 0.2 * np.sin(5 * x_norm[:-1]))**2 + 
                                                      (x_norm[1:] + 0.15 * np.cos(4 * x_norm[1:]))**2)) * 
                                        (1 + 0.25 * np.sin(8 * x_norm[:-1]) * np.cos(7 * x_norm[1:])))
        
        # Cross-dimensional coupling with logarithmic spiral pattern and chaotic modulation
        spiral_coupling = 0.7 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                     np.sin(15 * np.pi * np.arctan2(x_norm[1:], x_norm[:-1])) * 
                                     (1 + 0.2 * np.cos(9 * x_norm[:-1]) * np.sin(8 * x_norm[1:])))
        
        # High-frequency modulated sinusoidal component with chaotic amplitude modulation
        high_freq = 1.5 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                               np.exp(-0.25 * x_norm**2) * 
                               (1 + 0.3 * np.sin(12 * x_norm)))
        
        # Dimension-dependent conditioning factor with exponential growth and chaotic scaling
        condition_factor = 1.0 + 0.7 * np.log(self.dim + 1) + 0.1 * np.sin(5 * self.dim)
        
        # Combine all terms
        return condition_factor * (ellipse + trig_term + saddle + gaussian_elliptic + 
                                 spiral_coupling + high_freq)