import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Enhanced sinusoidal component with varying frequencies and phases
        sinusoidal = np.sum(np.sin(7 * scaled_x) * np.cos(6 * scaled_x) + np.sin(5 * scaled_x) * np.cos(8 * scaled_x))
        
        # Quadratic basin component to create wide optima regions
        quadratic = 0.2 * np.sum(x**2)
        
        # Additional harmonic component with higher frequency and phase shifts
        high_freq = 0.15 * np.sum(np.sin(12 * scaled_x) * np.cos(7 * scaled_x) + np.cos(9 * scaled_x) * np.sin(11 * scaled_x))
        
        # Modified cross-terms with non-linear interaction
        cross_terms = 0.06 * np.sum((x[:-1] ** 3) * x[1:] + x[:-1] * (x[1:] ** 3))
        
        # Add a noise term with varying frequency for increased complexity
        noise = 0.03 * np.sum(np.sin(10 * scaled_x) + np.cos(8 * scaled_x))
        
        # Complex interaction term with mixed frequencies and phase shifts
        complex_interaction = 0.07 * np.sum(np.sin(5 * scaled_x[:-1]) * np.cos(9 * scaled_x[1:]) + 
                                           np.cos(6 * scaled_x[:-1]) * np.sin(10 * scaled_x[1:]) + 
                                           np.sin(8 * scaled_x[:-1]) * np.cos(11 * scaled_x[1:]))
        
        # Fourth-order polynomial term for increased nonlinearity
        fourth_order = 0.03 * np.sum(x**4)
        
        # Fifth-order polynomial term to further increase complexity
        fifth_order = 0.012 * np.sum(x**5)
        
        # Add a logarithmic scaling component for varied curvature
        log_component = 0.04 * np.sum(np.log(1 + np.abs(x)) * np.sin(scaled_x))
        
        # Fractal-like nested sinusoidal structure for enhanced multimodality
        fractal_component = 0.035 * np.sum(np.sin(3 * scaled_x) * np.cos(4 * scaled_x) * 
                                          np.sin(5 * scaled_x) * np.cos(6 * scaled_x))
        
        # Chaotic cross-term interactions to increase algorithmic difficulty
        chaotic_cross = 0.05 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        # Introduce a small perturbation to the fractal component to enhance multimodality
        perturbed_fractal = 0.02 * np.sum(np.sin(4 * scaled_x) * np.cos(6 * scaled_x) * 
                                         np.sin(7 * scaled_x) * np.cos(9 * scaled_x))
        
        # New cross-term with exponential interaction for added complexity
        exp_cross = 0.025 * np.sum(np.exp(-x[:-1]**2) * x[1:] + x[:-1] * np.exp(-x[1:]**2))
        
        # Additional high-frequency sinusoidal component
        extra_freq = 0.03 * np.sum(np.sin(15 * scaled_x) * np.cos(13 * scaled_x))
        
        # Introduce a new chaotic interaction with higher frequency terms
        high_freq_chaos = 0.04 * np.sum(np.sin(13 * scaled_x[:-1]) * np.cos(14 * scaled_x[1:]) + 
                                       np.cos(15 * scaled_x[:-1]) * np.sin(16 * scaled_x[1:]))
        
        # Add a nested fractal component with recursive-like structure
        nested_fractal = 0.025 * np.sum(np.sin(2 * scaled_x) * np.cos(3 * scaled_x) * 
                                       np.sin(4 * scaled_x) * np.cos(5 * scaled_x) * 
                                       np.sin(6 * scaled_x) * np.cos(7 * scaled_x))
        
        # Introduce a new polynomial term with mixed exponents
        mixed_poly = 0.015 * np.sum(x**3 + x**6)
        
        # Add a component that emphasizes the interaction between distant dimensions
        long_range_interaction = 0.02 * np.sum(np.sin(2 * scaled_x[:-2]) * np.cos(3 * scaled_x[2:]) + 
                                             np.cos(4 * scaled_x[:-2]) * np.sin(5 * scaled_x[2:]))
        
        return sinusoidal + quadratic + high_freq + cross_terms + noise + complex_interaction + fourth_order + fifth_order + log_component + fractal_component + chaotic_cross + perturbed_fractal + exp_cross + extra_freq + high_freq_chaos + nested_fractal + mixed_poly + long_range_interaction