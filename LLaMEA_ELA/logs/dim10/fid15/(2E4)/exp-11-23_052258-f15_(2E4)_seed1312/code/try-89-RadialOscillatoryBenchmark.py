import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = r * np.sin(3.0 * r) * np.exp(-0.1 * r**2) * np.cos(0.7 * r)
        
        # Periodic oscillation in each dimension with chaotic phase shifts
        periodic_term = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(0.5 * i) * np.cos(0.3 * i)
            periodic_term += np.sin(2.0 * x[i] + phase_shift) * np.cos(1.5 * x[i] - 0.3 * np.sin(x[i]))
        
        # Adaptive conditioning with fractal-like scaling
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.2 * np.sin(np.log(self.dim + 1))
        
        # Chaotic cross-dimensional interaction with exponential weighting
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                weight = np.exp(-0.1 * dist**2) * (1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j])))
                cross_term += weight * np.sin(0.5 * r) * np.cos(0.3 * (x[i]**2 - x[j]**2))
        
        # Multi-scale harmonic component with dynamic amplitudes and frequencies
        harmonic_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.2 * i) * np.cos(0.1 * i)
            freq = 2.0 + 0.8 * np.cos(0.1 * i) * np.sin(0.3 * i)
            harmonic_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.05 * i)
        
        # Symmetric multimodal structure with chaotic peak positions and dynamic widths
        modal_term = 0.0
        for i in range(self.dim):
            peak_pos = 2.0 * np.sin(0.3 * i + 0.7 * np.cos(i))
            width = 0.5 + 0.2 * np.sin(0.4 * i)
            modal_term += np.exp(-0.5 * ((x[i] - peak_pos) / width)**2) * np.sin(3.0 * x[i]) * np.cos(0.5 * i)
        
        # Fractal-like scaling term with recursive component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.sin(x[i] * 2.0) + np.cos(x[i] * 1.5)) * np.exp(-0.1 * (x[i]**2))
        
        # Combined function with scaling and normalization
        total = condition_factor * (radial_term + periodic_term + cross_term + 
                                   harmonic_term + modal_term + fractal_term)
        
        return total