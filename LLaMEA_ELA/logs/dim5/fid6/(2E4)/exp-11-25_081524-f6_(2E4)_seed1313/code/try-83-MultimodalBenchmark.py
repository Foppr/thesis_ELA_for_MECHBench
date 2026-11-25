import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Nested chaotic modulation with multiple frequency layers
        chaotic_modulation = np.sum(np.sin(2.0 * np.exp(x)) * np.cos(4.0 * x) * 
                                   np.sin(0.5 * np.exp(2.0 * x)) * np.cos(8.0 * x))
        
        # Fractal-like ridge structures with recursive scaling
        ridge_terms = 0.2 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.5)
        
        # High-frequency oscillations with dynamic amplitude modulation
        high_freq = np.sum(np.sin(20.0 * x) * np.cos(10.0 * x) * 
                          (1.0 + 0.3 * np.sin(5.0 * x)))
        
        # Cross-dimensional exponential interactions with memory effect
        cross_interaction = 0.08 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * 
                                         (x[:-1]**3 + x[1:]**3))
        
        # Polynomial interaction with fractional powers and mixed signs
        poly_interaction = 0.05 * np.sum(x**3.5 + 0.3 * x**4.5 - 0.2 * x**2.5)
        
        # Non-smooth composite interactions with step-like discontinuities
        step_interaction = 0.1 * np.sum(np.floor(2.0 * np.sin(x)) * np.cos(x))
        
        # Additional chaotic cross-term with time-delayed feedback
        chaotic_cross = 0.03 * np.sum(np.sin(4.0 * x[:-1]) * np.cos(3.0 * x[1:]) * 
                                     np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)) * 
                                     np.sin(0.5 * x[:-1]))
        
        # Fractional dimensionality scaling with logarithmic modulation
        dim_scaling = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Add a new chaotic component with sine-cosine product and varying frequency
        new_chaotic = 0.15 * np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * 
                                  np.exp(-0.1 * x**2) * np.log(np.abs(x) + 1))
        
        # Introduce a new ridge-like structure with asymmetric exponential decay
        asym_ridge = 0.1 * np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2) * 
                                np.abs(x[:-1] - x[1:]) ** 1.2)
        
        # Add a new interaction term based on hyperbolic functions
        hyperbolic_interaction = 0.07 * np.sum(np.tanh(x[:-1]) * np.sinh(x[1:]))
        
        return (quadratic + chaotic_modulation + high_freq + cross_interaction + 
                poly_interaction + ridge_terms + step_interaction + chaotic_cross +
                new_chaotic + asym_ridge + hyperbolic_interaction) * dim_scaling