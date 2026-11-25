import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-inspired symmetry breaking with chaotic ridge modulation
        ridge_term = 0.0
        for i in range(self.dim):
            # Quaternion-like structure with complex phase interactions
            phase = np.sin(i * 1.57) * np.cos(i * 0.8) + 0.5 * np.sin(i * 2.3)
            steepness = 1.0 + 0.8 * np.sin(phase + x[i] * 0.3)
            ridge_term += np.tanh(steepness * x[i]) * np.exp(-0.15 * x[i]**2) * np.cos(x[i] * 0.7)
        
        # Multi-fractal basin boundaries with adaptive scaling
        basin_term = 0.0
        for i in range(self.dim):
            # Fractal-like scaling with dimension-dependent exponents
            fractal_exp = 1.0 + 0.4 * np.sin(i * 0.9) * np.cos(i * 0.6)
            log_scale = (1.0 + 0.25 * np.log(1.0 + np.abs(x[i]))) ** fractal_exp
            chaos_mod = np.sin(i * 1.7 + x[i] * 0.4) * np.cos(x[i] * 0.9)
            basin_term += log_scale * chaos_mod * np.exp(-0.08 * x[i]**2)
        
        # Adaptive multi-scale sinusoidal modulation with dynamic frequency coupling
        freq_term = 0.0
        for i in range(self.dim):
            # Frequency modulation based on neighbor interactions
            base_freq = 1.0 + 0.6 * np.sin(i * 0.4) * np.cos(i * 0.3)
            freq1 = base_freq * (1.0 + 0.3 * np.sin(x[i] * 0.5))
            freq2 = base_freq * (1.0 + 0.4 * np.cos(x[i] * 0.6))
            freq_term += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.03 * x[i]**2)
        
        # Adaptive cross-dimensional coupling with chaotic weight modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                # Chaotic weight modulation based on both variables
                dist = np.abs(x[i] - x[j])
                weight = np.exp(-dist * 0.3) * (1.0 + 0.2 * np.sin(x[i] * x[j]))
                cross_term += weight * np.sin(2.5 * x[i]) * np.cos(1.8 * x[j])
        
        # Fractal-like global structure with polynomial and hyperbolic components
        global_term = 0.0
        for i in range(self.dim):
            # Combine different scaling laws for complex global structure
            poly_component = 0.5 * x[i]**4 * np.exp(-0.1 * np.abs(x[i]))
            hyperbolic_component = 0.3 * np.tanh(1.5 * x[i]) * np.cos(0.9 * x[i])
            global_term += poly_component + hyperbolic_component
        
        # Enhanced chaotic noise with quaternion-like phase coupling
        noise = 0.0
        for i in range(self.dim):
            # Phase-coupled noise with dimension-specific frequencies
            freq1 = (i + 1) * 7.0 + 2.0 * np.sin(i * 0.5)
            freq2 = (i + 1) * 4.0 + 1.5 * np.cos(i * 0.3)
            noise += 0.03 * np.sin(x[i] * freq1) * np.cos(x[i] * freq2)
        
        return ridge_term + basin_term + freq_term + cross_term + global_term + noise