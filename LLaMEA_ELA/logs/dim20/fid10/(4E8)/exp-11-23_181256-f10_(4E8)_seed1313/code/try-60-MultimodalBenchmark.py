import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable computation
        x_scaled = x / 5.0
        
        # Chaotic sine coupling with adaptive frequencies
        adaptive_freq = 10 + 5 * np.sin(x_scaled)
        chaotic_coupling = np.sum(np.sin(adaptive_freq * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Enhanced radial barrier with exponential scaling
        radial_barrier = np.sum(np.exp(2 * x_scaled**2) * np.log(1 + x_scaled**2 + 0.01))
        
        # Mixed polynomial interactions with varying exponents
        poly_interaction = np.sum(x_scaled**5 * np.sin(x_scaled)) + 0.8 * np.sum(x_scaled**6)
        
        # Trigonometric coupling with multiple frequency components
        trig_coupling = np.sum(np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Logarithmic barrier with quadratic scaling
        log_barrier = np.sum(np.log(1 + 0.5 * x_scaled**2))
        
        # Exponential decay with sinusoidal modulation
        exp_modulation = np.sum(np.exp(-np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled))
        
        # Combined function with increased complexity and conditioning
        return chaotic_coupling + radial_barrier + poly_interaction + trig_coupling + log_barrier + exp_modulation + 0.2 * np.sum(x_scaled**7)