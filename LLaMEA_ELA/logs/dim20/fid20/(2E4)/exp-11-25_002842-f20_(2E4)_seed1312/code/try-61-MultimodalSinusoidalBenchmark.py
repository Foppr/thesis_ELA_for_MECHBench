import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Enhanced sinusoidal component with varying frequencies and phases
        sinusoidal = np.sum(np.sin(4 * scaled_x) * np.cos(3 * scaled_x) + np.sin(2 * scaled_x) * np.cos(5 * scaled_x))
        
        # Quadratic basin component to create wide optima regions
        quadratic = 0.2 * np.sum(x**2)
        
        # Additional harmonic component with higher frequency and phase shifts
        high_freq = 0.08 * np.sum(np.sin(9 * scaled_x) * np.cos(4 * scaled_x) + np.cos(6 * scaled_x) * np.sin(8 * scaled_x))
        
        # Modified cross-terms with non-linear interaction
        cross_terms = 0.03 * np.sum((x[:-1] ** 2) * x[1:] + x[:-1] * (x[1:] ** 2))
        
        # Add a noise term with varying frequency for increased complexity
        noise = 0.015 * np.sum(np.sin(7 * scaled_x) + np.cos(5 * scaled_x))
        
        # Complex interaction term with mixed frequencies and phase shifts
        complex_interaction = 0.04 * np.sum(np.sin(3 * scaled_x[:-1]) * np.cos(6 * scaled_x[1:]) + 
                                           np.cos(4 * scaled_x[:-1]) * np.sin(7 * scaled_x[1:]) + 
                                           np.sin(5 * scaled_x[:-1]) * np.cos(8 * scaled_x[1:]))
        
        # Fourth-order polynomial term for increased nonlinearity
        fourth_order = 0.015 * np.sum(x**4)
        
        # Fifth-order polynomial term to further increase complexity
        fifth_order = 0.005 * np.sum(x**5)
        
        # Add a logarithmic scaling component for varied curvature
        log_component = 0.02 * np.sum(np.log(1 + np.abs(x)) * np.sin(scaled_x))
        
        # Slight mutation: Adjusted coefficients and added a new chaotic interaction term
        chaotic_interaction = 0.035 * np.sum(np.sin(11 * scaled_x[:-1]) * np.cos(9 * scaled_x[1:]) + 
                                            np.cos(10 * scaled_x[:-1]) * np.sin(12 * scaled_x[1:]))
        
        # New chaotic term with different frequencies and interaction pattern
        new_chaotic = 0.025 * np.sum(np.sin(13 * scaled_x[:-1]) * np.sin(14 * scaled_x[1:]) + 
                                   np.cos(15 * scaled_x[:-1]) * np.cos(16 * scaled_x[1:]))
        
        # Additional mutation: Slight adjustment to coefficients and introduction of a new interaction term
        additional_interaction = 0.02 * np.sum(np.sin(17 * scaled_x[:-1]) * np.cos(18 * scaled_x[1:]) + 
                                              np.cos(19 * scaled_x[:-1]) * np.sin(20 * scaled_x[1:]))
        
        # Fractal-like nested structure with recursive sinusoidal components
        fractal_component = 0.03 * np.sum(np.sin(2 * scaled_x) * np.cos(4 * scaled_x) + 
                                         np.sin(6 * scaled_x) * np.cos(12 * scaled_x) + 
                                         np.sin(8 * scaled_x) * np.cos(16 * scaled_x))
        
        # Nested sinusoidal patterns with increasing complexity
        nested_patterns = 0.02 * np.sum(np.sin(3 * scaled_x) * np.cos(9 * scaled_x) + 
                                       np.sin(5 * scaled_x) * np.cos(15 * scaled_x) + 
                                       np.sin(7 * scaled_x) * np.cos(21 * scaled_x))
        
        # Increased chaos with higher frequency interactions
        high_chaos = 0.04 * np.sum(np.sin(23 * scaled_x[:-1]) * np.cos(25 * scaled_x[1:]) + 
                                  np.cos(24 * scaled_x[:-1]) * np.sin(26 * scaled_x[1:]))
        
        # Adjusted overall scaling for better balance and improved fitness
        return 1.02 * (sinusoidal + quadratic + high_freq + cross_terms + noise + complex_interaction + fourth_order + fifth_order + log_component + chaotic_interaction + new_chaotic + additional_interaction + fractal_component + nested_patterns + high_chaos)