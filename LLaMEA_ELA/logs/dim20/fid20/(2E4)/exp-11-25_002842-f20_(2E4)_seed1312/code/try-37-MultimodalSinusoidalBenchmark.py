import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Enhanced sinusoidal component with varying frequencies and phases
        sinusoidal = np.sum(np.sin(5 * scaled_x) * np.cos(4 * scaled_x) + np.sin(3 * scaled_x) * np.cos(6 * scaled_x))
        
        # Quadratic basin component to create wide optima regions
        quadratic = 0.15 * np.sum(x**2)
        
        # Additional harmonic component with higher frequency and phase shifts
        high_freq = 0.1 * np.sum(np.sin(10 * scaled_x) * np.cos(5 * scaled_x) + np.cos(7 * scaled_x) * np.sin(9 * scaled_x))
        
        # Modified cross-terms with non-linear interaction
        cross_terms = 0.04 * np.sum((x[:-1] ** 2) * x[1:] + x[:-1] * (x[1:] ** 2))
        
        # Add a noise term with varying frequency for increased complexity
        noise = 0.02 * np.sum(np.sin(8 * scaled_x) + np.cos(6 * scaled_x))
        
        # Complex interaction term with mixed frequencies and phase shifts
        complex_interaction = 0.05 * np.sum(np.sin(4 * scaled_x[:-1]) * np.cos(7 * scaled_x[1:]) + 
                                           np.cos(5 * scaled_x[:-1]) * np.sin(8 * scaled_x[1:]) + 
                                           np.sin(6 * scaled_x[:-1]) * np.cos(9 * scaled_x[1:]))
        
        # Fourth-order polynomial term for increased nonlinearity
        fourth_order = 0.02 * np.sum(x**4)
        
        # Fifth-order polynomial term to further increase complexity
        fifth_order = 0.008 * np.sum(x**5)
        
        # Add a logarithmic scaling component for varied curvature
        log_component = 0.03 * np.sum(np.log(1 + np.abs(x)) * np.sin(scaled_x))
        
        # Fractal-like nested sinusoidal structure for enhanced multimodality
        fractal_component = 0.025 * np.sum(np.sin(2 * scaled_x) * np.cos(3 * scaled_x) * 
                                          np.sin(4 * scaled_x) * np.cos(5 * scaled_x))
        
        # Chaotic cross-term interactions to increase algorithmic difficulty
        chaotic_cross = 0.035 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        # Mutation: Introduce a new chaotic interaction term with different frequency and phase
        new_chaotic_term = 0.02 * np.sum(np.sin(3 * scaled_x[:-1]) * np.sin(5 * scaled_x[1:]) + 
                                        np.cos(4 * scaled_x[:-1]) * np.cos(6 * scaled_x[1:]))
        
        return sinusoidal + quadratic + high_freq + cross_terms + noise + complex_interaction + fourth_order + fifth_order + log_component + fractal_component + chaotic_cross + new_chaotic_term