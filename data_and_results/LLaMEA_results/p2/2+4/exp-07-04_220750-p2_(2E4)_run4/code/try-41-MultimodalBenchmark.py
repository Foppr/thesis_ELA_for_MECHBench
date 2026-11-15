import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        sum_squares = np.sum(x_norm**2)
        
        # Product term with multiple local minima
        product_term = np.prod(np.cos(3 * x_norm))
        
        # Additional oscillatory term with higher frequency and amplitude
        oscillation = np.sum(np.sin(7 * x_norm**3))
        
        # Higher-order polynomial interaction term
        poly_term = np.sum(x_norm**8)
        
        # Cross-term interaction with increased complexity
        cross_term = np.sum(np.sin(x_norm) * np.cos(x_norm**3))
        
        # Adaptive oscillation term with variable frequency
        adaptive_osc = np.sum(np.sin(4 * x_norm) * np.cos(2 * x_norm**2))
        
        # Radial symmetry term with implicit surface interactions
        radial_term = np.sum(np.sin(np.pi * np.sqrt(np.sum(x_norm**2))) * np.cos(np.pi * np.sqrt(np.sum(x_norm**2))))
        
        # Coupled sinusoidal oscillations with varying amplitudes
        coupled_osc = np.sum(np.sin(5 * x_norm) * np.cos(3 * x_norm**2) * np.sin(x_norm**4))
        
        # Implicit surface interaction creating complex local minima
        implicit_surf = np.sum(np.sin(np.pi * x_norm) * np.cos(np.pi * x_norm**2) * np.sin(x_norm**3))
        
        # New: Increased coupling strength and added cubic interaction
        cubic_coupling = np.sum(np.sin(6 * x_norm**3) * np.cos(4 * x_norm**2) * np.sin(2 * x_norm))
        
        # New: Additional harmonic term with modified frequency
        harmonic_term = np.sum(np.sin(8 * x_norm) * np.cos(5 * x_norm**4))
        
        # Combined terms to create enhanced multimodal landscape
        return sum_squares + 0.3 * product_term + 0.05 * oscillation + 0.15 * poly_term + 0.07 * cross_term + 0.04 * adaptive_osc + 0.06 * radial_term + 0.05 * coupled_osc + 0.04 * implicit_surf + 0.03 * cubic_coupling + 0.02 * harmonic_term