import numpy as np

class AdaptiveCubicCrossDimensionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial periodic component with adaptive frequency
        r = np.sqrt(np.sum(x**2))
        radial = np.sin(3.0 * r) * np.cos(2.0 * r) * np.exp(-0.1 * r**2)
        
        # Adaptive polynomial potentials with dimension-dependent exponents
        poly_potential = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.sin(i * 0.7)
            poly_potential += (x[i]**exp_factor) * np.exp(-0.5 * x[i]**2)
        
        # Cross-dimensional cubic coupling with varying interaction strengths
        cross_cubic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.3 + 0.2 * np.sin(i * j * 0.5)
                cross_cubic += coupling_strength * (x[i]**3) * (x[j]**3) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Multi-scale sinusoidal modulation with adaptive amplitudes
        modulated = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(i * 0.4)
            freq = 1.5 + 0.8 * np.cos(i * 0.6)
            modulated += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Asymmetric cubic wells with dynamic positions
        asymmetric_wells = 0.0
        for i in range(self.dim):
            well_pos = 1.0 + 0.5 * np.sin(i * 0.8)
            well_depth = 0.8 + 0.2 * np.cos(i * 0.9)
            asymmetric_wells += well_depth * (x[i] - well_pos)**3
        
        # Mixed harmonic and exponential decay components
        mixed = 0.0
        for i in range(self.dim):
            mixed += np.sin(4.0 * x[i]) * np.exp(-0.3 * np.abs(x[i])) + 0.5 * np.cos(3.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Final combination with dynamic weights
        return 0.6 * radial + 0.8 * poly_potential + 0.9 * cross_cubic + 1.0 * modulated + \
               1.1 * asymmetric_wells + 1.2 * mixed