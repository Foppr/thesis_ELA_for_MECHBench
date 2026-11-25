import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like trigonometric component with varying frequencies
        fractal_trig = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.7 * x[i])
            fractal_trig += np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0) * np.tan(0.5 * x[i])
        
        # Self-adaptive radial basis functions with dynamic centers and widths
        rbf = 0
        for i in range(self.dim):
            center = np.sin(0.3 * x[i]) * 2.0
            width = 0.5 + 0.3 * np.cos(0.4 * x[i])
            for j in range(i+1, min(i+3, self.dim)):
                dist = (x[i] - center)**2 + (x[j] - center)**2
                rbf += np.exp(-dist / (2 * width**2)) * np.sin(2 * np.pi * dist)
        
        # Cross-dimensional fractal interactions with recursive scaling
        fractal_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.2 * np.sin(0.5 * (x[i] + x[j]))
                fractal_cross += scale_factor * np.sin(3 * x[i]) * np.cos(2 * x[j]) * np.tan(0.4 * (x[i] - x[j]))
        
        # Nested polynomial coupling with exponential modulation
        nested_poly = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
                nested_poly += term * np.sin(0.3 * (x[i] + x[j]))
        
        # Chaotic sine modulation with dynamic phase shift
        chaotic_mod = 0
        for i in range(self.dim):
            phase_shift = 0.1 * np.sin(0.6 * x[i])
            chaotic_mod += np.sin(2.5 * x[i] + phase_shift) * np.cos(1.8 * x[i] - phase_shift)
        
        # Multi-scale Gaussian with varying amplitudes and correlations
        gaussian = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.4 * x[i])
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                gaussian += amp * np.exp(-dist**2 / (2 * (0.3 + 0.2 * np.cos(x[i]))**2)) * np.sin(3 * dist)
        
        # Adaptive noise with fractal-like structure
        noise = 0.05 * np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        # Global scaling and shifting factor
        global_scale = 1.0 + 0.3 * np.log(self.dim + 1)
        shift = 0.2 * np.sum(x**2)
        
        # Combine all components with optimized weights
        return global_scale * (0.3 * fractal_trig + 0.25 * rbf + 0.2 * fractal_cross + 
                              0.15 * nested_poly + 0.1 * chaotic_mod + 0.05 * gaussian) + shift + noise