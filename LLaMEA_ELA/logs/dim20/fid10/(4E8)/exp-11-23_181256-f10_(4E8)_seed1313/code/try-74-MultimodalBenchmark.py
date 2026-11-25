import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logarithmic barrier terms creating sharp gradients near boundaries
        barrier = np.sum(np.log(1.0 + 0.1 * np.abs(x_scaled)))
        
        # Trigonometric couplings with adaptive frequencies based on dimension
        freq_factor = 2.0 + 0.5 * np.sqrt(self.dim)
        trig_coupling = np.sum(np.sin(freq_factor * x_scaled) * np.cos(freq_factor * x_scaled**2))
        
        # Radial adaptive terms with varying influence
        radial = np.sum((x_scaled**2 + 0.1)**(-1.5)) * 0.5
        
        # Coupled exponential and polynomial interactions
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3))
        
        # High-frequency chaotic modulation
        chaotic = np.sum(np.sin(10 * np.sin(x_scaled)) * np.cos(7 * np.cos(x_scaled)))
        
        # Combined function with diverse curvature and multiple local minima
        return 3.0 * barrier + 0.8 * trig_coupling + 0.4 * radial + 0.3 * exp_poly + 0.2 * chaotic