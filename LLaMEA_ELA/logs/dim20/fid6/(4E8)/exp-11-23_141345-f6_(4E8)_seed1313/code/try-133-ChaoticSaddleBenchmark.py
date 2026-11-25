import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Intensified chaotic oscillations with higher frequency modulation
        chaotic_osc = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(5.0 * np.pi * x) * np.cos(3.0 * np.pi * x) * np.tanh(2.0 * x))
        
        # Augmented fractal scaling with multi-fractal characteristics
        fractal_scale = np.sum(np.exp(-0.3 * np.abs(x)**1.8) * np.sin(4.0 * x) * np.cos(2.5 * x) * np.log(1.0 + np.abs(x)))
        
        # Stronger cross-dimensional coupling with exponential distance weighting
        strong_coupling = np.sum(np.exp(-0.4 * np.abs(x[:-1] - x[1:])**1.5) * (x[:-1]**3 + x[1:]**3) * np.sin(2.0 * x[:-1]) * np.cos(1.5 * x[1:]))
        
        # Novel hybrid interaction terms with adaptive coupling strength
        hybrid_interaction = np.sum((np.exp(-0.2 * np.abs(x)) * np.sin(3.5 * x) * np.cos(2.0 * x) + 
                                    0.3 * np.sin(0.5 * np.pi * x**2)) * (1.0 + 0.1 * np.sin(4.0 * x)))
        
        # Enhanced radial symmetry breaking with polynomial distance metrics
        radial_break = np.sum(np.exp(-0.6 * (x**2 + 0.5 * np.abs(x)**2.2)) * np.sin(2.8 * x) * np.cos(1.8 * x))
        
        # Multi-scale chaotic modulation with varying amplitudes and frequencies
        multi_scale = np.sum(np.sin(6.0 * x) * np.cos(4.5 * x) * (1.0 + 0.3 * np.sin(3.0 * x)) * np.exp(-0.2 * x**2))
        
        # Asymmetric hyperbolic modulation with saddle-point enhancement
        saddle_mod = np.sum(np.tanh(2.0 * x) * np.exp(-0.3 * x**2) * np.sin(4.0 * x) * (1.0 + 0.2 * np.cos(2.0 * x)))
        
        # Combined function with optimized weights for maximum difficulty
        return 0.25 * chaotic_osc + 0.20 * fractal_scale + 0.18 * strong_coupling + 0.15 * hybrid_interaction + 0.12 * radial_break + 0.08 * multi_scale + 0.02 * saddle_mod