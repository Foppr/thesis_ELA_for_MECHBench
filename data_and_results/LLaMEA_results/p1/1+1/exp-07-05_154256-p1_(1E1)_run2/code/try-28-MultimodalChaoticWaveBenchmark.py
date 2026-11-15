import numpy as np

class MultimodalChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.wave_freq = 2.0 * np.pi
        self.poly_degree = 4
        self.decay_rate = 0.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component
        r = np.sqrt(np.sum(x**2))
        radial_poly = np.sum(x**self.poly_degree)
        
        # Sinusoidal wave interference pattern
        wave_interference = 0
        for i in range(self.dim):
            wave_interference += np.sin(self.wave_freq * x[i]) * np.cos(self.wave_freq * x[i] * 0.7)
            
        # Exponential decay with radial distance
        exp_decay = np.exp(-self.decay_rate * r)
        
        # Additional chaotic modulation using sine of radial distance
        chaotic_mod = 1.0 + 0.3 * np.sin(5.0 * r)
        
        # Cross-term interactions with higher-order coupling
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))
                
        # Add a periodic component with varying frequency
        periodic_component = 0
        for i in range(self.dim):
            periodic_component += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Combine all components with different weights
        return (0.5 * radial_poly + 
                1.2 * wave_interference + 
                0.8 * exp_decay + 
                0.6 * chaotic_mod + 
                0.4 * cross_terms + 
                0.3 * periodic_component)