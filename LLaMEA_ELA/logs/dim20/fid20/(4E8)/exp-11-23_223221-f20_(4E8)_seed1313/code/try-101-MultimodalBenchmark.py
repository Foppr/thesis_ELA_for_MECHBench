import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent ridge structure with asymmetric steepness
        ridge_term = 0.0
        for i in range(self.dim):
            # Asymmetric ridge with varying steepness based on dimension
            steepness = 1.0 + 0.5 * np.sin(i * 0.7)
            ridge_term += np.tanh(steepness * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Logarithmic basin boundary with multi-scale modulation
        basin_term = 0.0
        for i in range(self.dim):
            # Basin boundaries with logarithmic scaling and chaotic modulation
            log_scale = 1.0 + 0.3 * np.log(1.0 + np.abs(x[i]))
            chaos_mod = np.sin(i * 1.3 + x[i] * 0.5) * np.cos(x[i] * 0.8)
            basin_term += log_scale * chaos_mod * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale sinusoidal modulation with fractal-like frequency scaling
        freq_term = 0.0
        for i in range(self.dim):
            # Multiple frequencies with dimension-dependent scaling
            base_freq = 1.0 + 0.5 * np.sin(i * 0.3)
            freq1 = base_freq * (1.0 + 0.2 * np.sin(i * 0.8))
            freq2 = base_freq * (1.0 + 0.3 * np.cos(i * 0.6))
            freq_term += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional coupling with exponential interaction weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                # Exponentially decaying interaction based on distance
                dist = np.abs(x[i] - x[j])
                weight = np.exp(-dist * 0.5)
                cross_term += weight * np.sin(2 * x[i]) * np.cos(1.5 * x[j])
        
        # Asymmetric global modulation with polynomial and trigonometric components
        global_term = 0.0
        for i in range(self.dim):
            # Combine different scaling laws for complex global structure
            poly_component = 0.4 * x[i]**3 * np.exp(-0.1 * np.abs(x[i]))
            trig_component = 0.2 * np.sin(1.2 * x[i]) * np.cos(0.8 * x[i])
            global_term += poly_component + trig_component
        
        # Add chaotic noise with dimension-dependent amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(x[i] * (i + 1) * 5.0) * np.cos(x[i] * (i + 1) * 3.0)
        
        return ridge_term + basin_term + freq_term + cross_term + global_term + noise