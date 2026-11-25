import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay interactions with varying rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.5 + 0.3 * np.sin(0.4 * x[i])
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.cos(2 * x[i])
        
        # Trigonometric chaos with multi-scale oscillations
        trig_chaos = 0
        for i in range(self.dim):
            freq1 = 1.0 + 0.5 * np.sin(0.3 * x[i])
            freq2 = 2.0 + 0.8 * np.cos(0.7 * x[i])
            freq3 = 3.0 + 1.2 * np.sin(0.9 * x[i]**2)
            trig_chaos += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.tanh(freq3 * x[i])
        
        # Spherical harmonic couplings between dimensions
        sph_harm = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x[i]**2 + x[j]**2)
                # Spherical harmonic terms
                sph_term = (np.sin(dist) * np.cos(2 * dist) + 
                           0.5 * np.cos(dist) * np.sin(3 * dist)) / (dist + 1e-8)
                sph_harm += sph_term * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Power-law scaling with asymmetric modulation
        power_scale = 0
        for i in range(self.dim):
            # Asymmetric power scaling
            asym_factor = 1.0 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            power_scale += (np.abs(x[i])**2.5) * asym_factor * np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional coupling with radial basis functions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                width = 1.0 + 0.3 * np.sin(0.2 * (x[i] + x[j]))
                coupling = np.exp(-0.5 * (dist / width)**2) * np.sin(dist)
                cross_coupling += coupling
        
        # Fractal-like recursive structure with log-scaled components
        fractal = 0
        for i in range(self.dim):
            # Log-scale recursive term
            log_term = np.log(np.abs(x[i]) + 1.0) * np.sin(3 * x[i])
            fractal += log_term * np.exp(-0.2 * x[i]**2)
        
        # Global conditioning factor
        cond_factor = 1.0 + 0.2 * np.sin(self.dim * 0.2) + 0.1 * np.cos(self.dim * 0.1)
        
        # Combine all components with optimized weights
        return cond_factor * (0.25 * exp_decay + 0.3 * trig_chaos + 0.2 * sph_harm + 
                             0.15 * power_scale + 0.08 * cross_coupling + 0.02 * fractal)