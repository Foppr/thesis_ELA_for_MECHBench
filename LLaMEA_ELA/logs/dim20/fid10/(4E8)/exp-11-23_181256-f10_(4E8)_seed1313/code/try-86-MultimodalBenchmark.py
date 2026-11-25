import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic barrier terms with variable steepness
        barrier = np.sum(np.log(1.0 + 0.2 * np.abs(x_scaled) + 0.05 * x_scaled**2))
        
        # Complex trigonometric couplings with dynamic frequencies and phase shifts
        freq_factor = 3.0 + 0.3 * np.sqrt(self.dim)
        phase_shift = 0.5 * np.sin(0.1 * self.dim)
        trig_coupling = np.sum(np.sin(freq_factor * x_scaled + phase_shift) * 
                              np.cos(freq_factor * x_scaled**2 + phase_shift * 0.5))
        
        # Adaptive radial terms with variable exponent and multi-scale influence
        radial_base = x_scaled**2 + 0.05
        radial = np.sum(radial_base**(-2.0)) * 0.7 + np.sum(radial_base**(-1.0)) * 0.3
        
        # Coupled exponential and polynomial interactions with phase modulation
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3 + 0.1 * np.sin(5 * x_scaled)))
        
        # Multi-scale chaotic modulation with varying amplitude and frequency
        chaotic = np.sum(np.sin(15 * np.sin(x_scaled)) * np.cos(12 * np.cos(x_scaled)) * 
                         np.tanh(2.0 * x_scaled) * (1.0 + 0.2 * np.sin(3 * x_scaled)))
        
        # Additional high-frequency oscillatory component
        high_freq = np.sum(np.sin(25 * x_scaled) * np.cos(20 * x_scaled**3))
        
        # Combined function with diverse curvature and multiple local minima
        return 4.0 * barrier + 1.0 * trig_coupling + 0.5 * radial + 0.4 * exp_poly + 0.3 * chaotic + 0.2 * high_freq