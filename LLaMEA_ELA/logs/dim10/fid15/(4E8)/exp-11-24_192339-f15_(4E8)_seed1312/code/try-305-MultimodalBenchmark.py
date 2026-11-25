import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal chaotic components with coupled oscillators
        chaotic_oscillators = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.5 * x[i])
            phase = 0.7 * np.cos(0.4 * x[i]) + 0.2 * np.sin(0.6 * x[i])
            chaotic_oscillators += np.sin(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis functions with dynamic centers and widths
        rbf_components = 0
        for i in range(self.dim):
            center = 2.0 * np.cos(0.3 * x[i]) + 0.5 * np.sin(0.7 * x[i])
            width = 0.8 + 0.2 * np.cos(0.4 * x[i])
            rbf_components += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(0.6 * x[i])
        
        # Spectral filtering with frequency modulation
        spectral_filter = 0
        for i in range(self.dim):
            mod_freq = 1.2 + 0.4 * np.sin(0.5 * x[i])
            spectral_filter += np.sin(mod_freq * x[i]) * np.cos(0.3 * x[i])
        
        # Energy-based potential with adaptive curvature
        energy_potential = 0
        for i in range(self.dim):
            curvature = 1.0 + 0.5 * np.sin(0.4 * x[i])
            energy_potential += curvature * (x[i]**2 - 2*x[i] + 1) + 0.3 * np.sin(0.8 * x[i])
        
        # Coupled nonlinear interactions with fractal modulation
        coupled_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for efficiency
                coupling_strength = 0.5 + 0.3 * np.cos(0.2 * (x[i] + x[j]))
                coupled_interaction += coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.3 * np.sin(0.2 * self.dim) + 0.1 * np.cos(0.1 * self.dim)
        
        # Combine all components with optimized weights
        return condition_factor * (0.3 * chaotic_oscillators + 
                                  0.25 * rbf_components + 
                                  0.2 * spectral_filter + 
                                  0.15 * energy_potential + 
                                  0.1 * coupled_interaction)