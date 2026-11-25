import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine wave components with phase coupling
        chaotic_oscillators = 0
        for i in range(self.dim):
            freq = 1.5 + 0.4 * np.sin(0.6 * x[i])
            phase = 0.8 * np.cos(0.5 * x[i]) + 0.3 * np.sin(0.7 * x[i]) + 0.2 * np.cos(0.3 * x[i])
            chaotic_oscillators += np.sin(freq * x[i] + phase) * np.exp(-0.15 * x[i]**2)
        
        # Modified radial basis functions with dynamic centers and widths
        rbf_components = 0
        for i in range(self.dim):
            center = 2.5 * np.cos(0.4 * x[i]) + 0.7 * np.sin(0.8 * x[i])
            width = 0.9 + 0.3 * np.cos(0.5 * x[i])
            rbf_components += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(0.7 * x[i])
        
        # Enhanced spectral filtering with frequency modulation and harmonic mixing
        spectral_filter = 0
        for i in range(self.dim):
            mod_freq = 1.3 + 0.5 * np.sin(0.6 * x[i]) + 0.2 * np.cos(0.4 * x[i])
            spectral_filter += (np.sin(mod_freq * x[i]) * np.cos(0.4 * x[i]) + 
                               0.5 * np.cos(mod_freq * x[i]) * np.sin(0.3 * x[i]))
        
        # Energy-based potential with adaptive curvature and fractal modulation
        energy_potential = 0
        for i in range(self.dim):
            curvature = 1.2 + 0.6 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.3 * x[i])
            energy_potential += curvature * (x[i]**2 - 2*x[i] + 1) + 0.4 * np.sin(0.9 * x[i])
        
        # Coupled nonlinear interactions with enhanced fractal modulation and memory effects
        coupled_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling for complexity
                coupling_strength = 0.6 + 0.4 * np.cos(0.3 * (x[i] + x[j]))
                distance_factor = np.exp(-0.03 * (x[i] - x[j])**2)
                coupled_interaction += coupling_strength * np.sin(x[i] * x[j]) * distance_factor
        
        # Adaptive conditioning with dimensionality-dependent scaling and chaotic modulation
        condition_factor = 1.2 + 0.4 * np.sin(0.3 * self.dim) + 0.2 * np.cos(0.2 * self.dim) + 0.1 * np.sin(0.1 * self.dim)
        
        # Combine all components with optimized weights for better algorithm discrimination
        return condition_factor * (0.35 * chaotic_oscillators + 
                                  0.28 * rbf_components + 
                                  0.22 * spectral_filter + 
                                  0.12 * energy_potential + 
                                  0.03 * coupled_interaction)