import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay with multi-frequency sine modulation and varying decay rates
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(6 * np.pi * x) * np.cos(4 * np.pi * x) * np.sin(3 * np.pi * x))
        
        # Multi-frequency trigonometric oscillations with amplitude modulation and phase shifts
        trig_term = np.sum(np.sin(8 * np.pi * x) * np.cos(10 * np.pi * x) + 
                          np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x) + 
                          np.sin(5 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # High-degree polynomial interaction terms with mixed nonlinearities and enhanced coupling
        poly_term = np.sum(0.4 * x**9 - 5 * x**7 + 8 * x**5 - 7 * x**3 + 4 * x**2 - 2 * x)
        
        # Cross-dimensional nonlinear coupling with chaotic phase shifts and enhanced interaction
        coupling_term = np.sum((x[:-1] - x[1:])**4 * np.sin(8 * np.pi * x[:-1]) * np.cos(5 * np.pi * x[1:]))
        
        # Additional chaotic correlation terms between all dimensions with increased complexity
        corr_term = np.sum(np.sin(np.pi * x) * np.cos(2 * np.pi * x) * np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Fractal-like self-similarity patterns with recursive scaling and multi-scale modulation
        fractal_term = np.sum(np.sin(12 * np.pi * x) * np.cos(15 * np.pi * x) * 
                             np.sin(9 * np.pi * x) * np.cos(11 * np.pi * x) * 
                             np.sin(7 * np.pi * x) * np.cos(13 * np.pi * x))
        
        # Enhanced multimodal peaks with varying heights and widths controlled by chaotic parameters
        peak_term = np.sum(0.3 * np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
                          np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x) * 
                          np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.25 * exp_term + 0.2 * trig_term + 0.04 * poly_term + 0.08 * coupling_term + 0.06 * corr_term + 0.05 * fractal_term + 0.07 * peak_term + 1.8