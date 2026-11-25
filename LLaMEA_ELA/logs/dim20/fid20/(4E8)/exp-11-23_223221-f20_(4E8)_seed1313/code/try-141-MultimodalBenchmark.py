import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with parameter modulation
        tent_term = 0.0
        for i in range(self.dim):
            # Tent map with dynamic parameter based on position
            mu = 3.8 + 0.2 * np.sin(0.5 * x[i])
            if x[i] < 0.5:
                tent_val = mu * x[i]
            else:
                tent_val = mu * (1 - x[i])
            tent_term += 0.1 * tent_val * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Spectral wave coupling with frequency modulation
        wave_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                freq_mod = 1.0 + 0.3 * np.sin(0.7 * (x[i] + x[j]))
                wave_coupling += 0.2 * np.sin(freq_mod * dist) * np.cos(freq_mod * (x[i] * x[j]))
        
        # Adaptive ridge structure with position-dependent curvature
        ridge_term = 0.0
        for i in range(self.dim):
            # Variable ridge height and width based on position
            ridge_height = 0.3 + 0.2 * np.sin(1.5 * x[i])
            ridge_width = 0.8 + 0.4 * np.cos(0.9 * x[i])
            ridge_term += ridge_height * np.exp(-0.5 * (x[i] / ridge_width)**2) * np.sin(3.0 * x[i])
        
        # Multi-scale fractal basin with noise injection
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 2.0:
                basin_term += 0.15 * x[i]**4 + 0.08 * np.sin(10 * x[i]) + 0.03 * np.random.rand()
            else:
                basin_term += 0.2 * np.abs(x[i])**3.2 + 0.05 * np.cos(7 * x[i]) + 0.02 * np.random.rand()
        
        # Cross-dimensional coupling with chaotic phase shifts
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic phase based on both coordinates
                phase = 0.5 * np.sin(0.4 * x[i]) + 0.3 * np.cos(0.6 * x[j]) + 0.2 * np.sin(0.8 * x[i] * x[j])
                cross_coupling += 0.1 * np.sin(x[i] + x[j] + phase) * np.cos(x[i] - x[j] + phase)
        
        # Exponential decay with position-dependent modulation
        decay_term = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.5 * np.sin(0.6 * x[i])
            decay_term += 0.25 * np.exp(-mod_factor * np.abs(x[i])) * np.sin(mod_factor * x[i]) * (1.0 + 0.1 * np.cos(0.4 * x[i]))
        
        # Final chaotic sine-wave with variable amplitude
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.7 + 0.3 * np.sin(0.9 * x[i])
            chaos_term += amp * np.sin(200 * x[i]) * np.exp(-0.5 * x[i]**2)
        
        return tent_term + wave_coupling + ridge_term + basin_term + cross_coupling + decay_term + chaos_term