import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logarithmic barrier terms creating sharp gradients near boundaries
        barrier = np.sum(np.log(1.0 + 0.2 * np.abs(x_scaled)))
        
        # Trigonometric couplings with adaptive frequencies based on dimension
        freq_factor = 3.0 + 0.25 * np.sqrt(self.dim)
        trig_coupling = np.sum(np.sin(freq_factor * x_scaled) * np.cos(freq_factor * x_scaled**2))
        
        # Enhanced radial adaptive terms with varying influence
        radial = np.sum((x_scaled**2 + 0.2)**(-2.0)) * 0.5
        
        # Modified exponential and polynomial interactions
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + 0.9 * x_scaled**3))
        
        # High-frequency chaotic modulation with altered phase shifts
        chaotic = np.sum(np.sin(15 * np.sin(x_scaled)) * np.cos(8 * np.cos(x_scaled)))
        
        # Combined function with diverse curvature and multiple local minima
        return 4.0 * barrier + 1.0 * trig_coupling + 0.6 * radial + 0.4 * exp_poly + 0.3 * chaotic