import numpy as np

class TrigonometricEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base elliptical valley term with adaptive eccentricity
        ellipse = np.sum((x_norm[:-1]**2 + 0.3 * x_norm[1:]**2) * np.exp(-0.15 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Chaotic saddle point structure with logistic map interactions
        saddle = np.sum(np.tanh(4 * x_norm[:-1]) * np.tanh(4 * x_norm[1:]) * 
                       (np.sin(5 * x_norm[:-1]) - np.cos(5 * x_norm[1:])))
        
        # Dynamic Gaussian peaks with chaotic positioning and elliptical contours
        gaussian_elliptic = 1.0 * np.sum(np.exp(-3 * ((x_norm[:-1] - 0.4 * np.sin(5 * x_norm[:-1]))**2 + 
                                                      (x_norm[1:] + 0.3 * np.cos(4 * x_norm[1:]))**2)))
        
        # Cross-dimensional coupling with chaotic spiral pattern
        spiral_coupling = 0.7 * np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                     np.sin(15 * np.pi * np.arctan2(x_norm[1:], x_norm[:-1]) + 
                                            0.5 * np.sin(10 * x_norm[:-1])))
        
        # High-frequency modulated sinusoidal component with chaotic phase
        high_freq = 1.5 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                               np.exp(-0.15 * x_norm**2))
        
        # Trigonometric oscillations with varying frequencies and chaotic amplitudes
        trig_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                          np.exp(-0.25 * x_norm**2))
        
        # Adaptive conditioning factor with chaotic growth
        condition_factor = 1.0 + 0.8 * np.log(self.dim + 1) + 0.2 * np.sin(3 * np.pi * self.dim)
        
        # Combine all terms
        return condition_factor * (ellipse + saddle + gaussian_elliptic + 
                                 spiral_coupling + high_freq + trig_term)