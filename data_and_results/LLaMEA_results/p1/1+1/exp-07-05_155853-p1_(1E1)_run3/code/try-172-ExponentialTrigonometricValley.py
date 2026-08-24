import numpy as np

class ExponentialTrigonometricValley:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with varying rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.1 + 0.4 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(2.0 * x[i])**2
        
        # Trigonometric wave interference with dynamic amplitudes
        wave_interference = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.8)
            wave_interference += amp * np.sin(x[i] * (1.0 + 0.3 * np.cos(i * 0.4))) * np.cos(x[i] * (0.7 + 0.2 * np.sin(i * 0.6)))
        
        # Adaptive parabolic valleys with chaotic positioning
        parabolic_valleys = 0
        for i in range(min(8, self.dim)):
            center = -4.0 + 8.0 * (i / max(1, self.dim - 1)) + 0.3 * np.sin(i * 1.2)
            width = 0.5 + 0.5 * np.abs(np.sin(i * 0.7))
            parabolic_valleys += (x[i] - center)**2 * np.exp(-0.5 * (x[i] - center)**2 / width**2)
        
        # Dynamic dimensionality scaling with chaotic weights
        dim_scaling = 0
        for i in range(self.dim):
            weight = 0.3 + 0.7 * np.abs(np.sin(i * 0.9))
            dim_scaling += weight * x[i]**4
        
        # Cross-dimensional symmetry breaking with chaotic phase shifts
        symmetry_break = 0
        for i in range(self.dim - 1):
            phase = 0.4 * np.sin(i * 0.6) + 0.3 * np.cos(i * 0.8)
            symmetry_break += np.sin(x[i] + phase) * np.cos(x[i+1] + phase) * (x[i]**2 + x[i+1]**2)
        
        # Multi-scale oscillation with exponential modulation
        multi_scale = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.3)
            multi_scale += np.exp(-0.1 * x[i]**2) * np.sin(scale * x[i])**3
        
        # Adaptive noise modulation with chaotic frequency components
        noise_mod = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * 0.7)
            noise_mod += 0.05 * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Combined fitness with refined balancing coefficients
        return 1.2 * exp_decay + 0.8 * wave_interference + 0.6 * parabolic_valleys + 0.4 * dim_scaling + 0.3 * symmetry_break + 0.2 * multi_scale + 0.1 * noise_mod