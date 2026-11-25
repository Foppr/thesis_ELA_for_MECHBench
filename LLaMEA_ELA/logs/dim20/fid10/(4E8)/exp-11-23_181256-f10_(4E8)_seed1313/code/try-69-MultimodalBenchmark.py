import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable computation
        x_scaled = x / 5.0
        
        # Chaotic exponential decay with varying rates
        exp_decay = np.sum(np.exp(-np.abs(x_scaled) * (1 + 0.5 * np.sin(3 * x_scaled))) * np.cos(2 * np.pi * x_scaled))
        
        # Trigonometric coupling with adaptive frequencies
        trig_coupling = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Saddle-point interactions with polynomial modulation
        saddle_term = np.sum(x_scaled**2 * np.sin(4 * x_scaled) * np.cos(2 * x_scaled))
        
        # Enhanced radial barrier with logarithmic scaling
        radial_barrier = np.sum((x_scaled**2 + 0.05) * np.log(1 + 0.5 * x_scaled**2) * np.exp(-0.1 * x_scaled**2))
        
        # New chaotic sine modulation with quadratic frequency coupling
        chaotic_modulation = np.sum(np.sin(20 * np.pi * np.sin(3 * x_scaled)) * np.cos(10 * np.pi * x_scaled))
        
        # Mixed polynomial terms for varied curvature and conditioning
        poly_terms = 0.8 * np.sum(x_scaled**5) + 0.6 * np.sum(x_scaled**3) + 0.4 * np.sum(x_scaled**7)
        
        # Combined function with irregular structure and sharp transitions
        return exp_decay + trig_coupling + saddle_term + radial_barrier + chaotic_modulation + poly_terms + 0.2 * np.sum(np.abs(x_scaled))