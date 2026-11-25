import numpy as np

class ChaoticParticleFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range
        scaled_x = x * np.pi / 5.0
        
        # Particle swarm chaotic interaction terms
        particle_interaction = 0.1 * np.sum(np.sin(scaled_x) * np.cos(scaled_x) * 
                                          np.sin(2 * scaled_x) * np.cos(2 * scaled_x))
        
        # Fractal basin component with nested polynomial structures
        fractal_basin = 0.15 * np.sum((x**2 + 0.1 * np.sin(10 * x))**2)
        
        # Hybrid polynomial-trigonometric cross-terms
        hybrid_cross = 0.08 * np.sum(x[:-1]**3 * np.sin(x[1:]) + x[1:]**3 * np.cos(x[:-1]))
        
        # Multi-scale sinusoidal component with varying amplitudes
        multiscale_sin = 0.12 * np.sum(np.sin(3 * scaled_x) + np.sin(7 * scaled_x) + 
                                     np.sin(11 * scaled_x) + np.sin(15 * scaled_x))
        
        # Chaotic logistic map inspired component
        chaotic_map = 0.06 * np.sum(np.sin(x**2) * np.cos(x) * np.sin(x**3))
        
        # Nested exponential decay with trigonometric modulation
        nested_exp = 0.09 * np.sum(np.exp(-x**2) * np.sin(5 * x) + np.exp(-x**4) * np.cos(3 * x))
        
        # High-order polynomial with sinusoidal perturbations
        high_order_poly = 0.07 * np.sum(x**6 + 0.2 * np.sin(13 * x) * x**4)
        
        # Fractional power interaction with trigonometric functions
        frac_interaction = 0.05 * np.sum(np.abs(x[:-1])**0.7 * np.cos(x[1:]) + 
                                       np.abs(x[1:])**0.8 * np.sin(x[:-1]))
        
        # Multi-modal Gaussian-like structure with chaotic modulation
        gaussian_modulated = 0.1 * np.sum(np.exp(-0.5 * (x - 1)**2) * np.sin(4 * x) + 
                                        np.exp(-0.5 * (x + 1)**2) * np.cos(3 * x))
        
        # Complex cross-term with multiple interaction patterns
        complex_cross = 0.06 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * 
                                    (x[:-1]**2 + x[1:]**2))
        
        # Hyperbolic tangent and polynomial hybrid
        tanh_poly = 0.04 * np.sum(np.tanh(x) * x**3 + np.sinh(x) * x**2)
        
        # Fractal-like structure with recursive trigonometric components
        recursive_trig = 0.08 * np.sum(np.sin(np.sin(scaled_x)) + np.cos(np.cos(scaled_x)))
        
        # Combined quadratic and sinusoidal basin terms
        combined_basin = 0.1 * np.sum(x**2 + 0.3 * np.sin(5 * x)**2)
        
        # Final chaotic cross-term with mixed powers
        final_cross = 0.05 * np.sum(np.sin(x[:-1]**1.5) * np.cos(x[1:]**1.3) + 
                                  np.cos(x[:-1]**1.7) * np.sin(x[1:]**1.4))
        
        return (particle_interaction + fractal_basin + hybrid_cross + multiscale_sin + 
                chaotic_map + nested_exp + high_order_poly + frac_interaction + 
                gaussian_modulated + complex_cross + tanh_poly + recursive_trig + 
                combined_basin + final_cross)