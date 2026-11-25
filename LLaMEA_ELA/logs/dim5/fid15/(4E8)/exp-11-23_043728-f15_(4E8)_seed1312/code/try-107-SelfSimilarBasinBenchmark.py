import numpy as np

class SelfSimilarBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Self-similar fractal parameters
        self.fractal_scale = 1.2
        self.fractal_exponent = 0.7
        # Gradient modulation coefficients
        self.grad_mod_a = 1.5
        self.grad_mod_b = 0.8
        # Spectral interference parameters
        self.spectral_freq = 2.0 * np.pi
        self.spectral_amp = 0.3
        # Basin complexity control
        self.basin_complexity = 1.4
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Self-similar basin structure with fractal scaling
        basin_energy = 0.0
        for i in range(self.dim):
            # Multi-scale basin terms
            scale_factor = np.power(self.fractal_scale, i % 3)
            basin_term = np.power(np.abs(x_norm[i]), self.fractal_exponent) * scale_factor
            basin_energy += basin_term
        
        # Adaptive gradient modulation
        grad_energy = 0.0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            mod_factor = self.grad_mod_a + self.grad_mod_b * np.sin(0.5 * x_norm[i])
            grad_energy += mod_factor * diff**2
        
        # Spectral interference pattern
        spectral_energy = 0.0
        for i in range(self.dim):
            freq_term = self.spectral_freq * (i + 1) / self.dim
            spectral_energy += np.sin(freq_term * x_norm[i]) * np.cos(freq_term * x_norm[i])
        
        # Multi-modal attraction basins with varying complexity
        modal_energy = 0.0
        for i in range(self.dim):
            # Combination of polynomial and trigonometric terms
            poly_term = x_norm[i]**4 - 3 * x_norm[i]**2 + 1
            trig_term = np.sin(self.basin_complexity * x_norm[i])
            modal_energy += (poly_term + self.spectral_amp * trig_term)**2
        
        # Coupling between dimensions with dynamic strength
        coupling_energy = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling_strength = 0.5 + 0.3 * np.sin(0.8 * x_norm[i])
                coupling_energy += coupling_strength * (x_norm[i] - x_norm[i+1])**2
        
        # Combine all components
        total_energy = (basin_energy + grad_energy + spectral_energy + 
                       modal_energy + coupling_energy) / self.dim
        
        # Add controlled noise for ruggedness
        noise = 0.005 * np.random.rand() * (1 + 0.2 * np.sin(np.sum(x_norm**2)))
        
        return total_energy + noise