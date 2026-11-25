import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal polynomial term with recursive scaling
        base_term = np.sum((x**2 + 0.1) * np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Hybrid trigonometric-polynomial interaction
        hybrid_term = np.sum(np.sin(x**3) * np.cos(x**2) * (1.0 + 0.2 * np.sin(2.0 * x)))
        
        # Multi-scale fractal structure with varying exponents
        fractal_term = np.sum(np.abs(x)**(1.5 + 0.5 * np.sin(3.0 * x)) * np.cos(4.0 * x))
        
        # Dynamic coupling with recursive dimension interaction
        coupling_term = np.sum((x[:-1]**2 + x[1:]**2) * np.exp(-0.1 * (x[:-1] - x[1:])**2) * np.sin(2.0 * x[:-1]))
        
        # Self-similar oscillatory pattern with scale invariance
        oscillation_term = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x) * np.sin(7.0 * x) * (1.0 + 0.3 * np.cos(2.0 * x)))
        
        # Multi-modal harmonic modulation with varying frequencies
        modal_term = np.sum(np.sin(4.0 * x) * np.cos(6.0 * x) * np.exp(-0.5 * x**2) * (1.0 + 0.25 * np.sin(8.0 * x)))
        
        # Recursive fractal scaling with feedback
        recursive_term = np.sum(np.sin(x) * np.cos(2.0 * x) * np.sin(3.0 * x) * (1.0 + 0.1 * np.sin(4.0 * x)))
        
        # Combined function with weighted contributions
        return 0.25 * base_term + 0.2 * hybrid_term + 0.15 * fractal_term + 0.15 * coupling_term + 0.1 * oscillation_term + 0.08 * modal_term + 0.07 * recursive_term