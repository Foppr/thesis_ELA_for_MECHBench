import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quad = np.sum(x**2)
        
        # Sine-cosine wave interactions with varying frequencies and amplitudes
        wave = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            wave += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Self-similar Gaussian components with fractal-like scaling
        gaussian = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.7 * i)
            center = 2.0 * np.cos(0.4 * i)
            width = 0.5 + 0.2 * np.sin(0.6 * i)
            gaussian += scale * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Multi-scale exponential modulation with chaotic parameter variation
        exp_mod = 0
        for i in range(self.dim):
            chaos_param = 1.5 + 0.5 * np.sin(0.8 * i * np.pi)
            exp_mod += np.exp(chaos_param * x[i]) * np.cos(2 * x[i])
        
        # Fractal-like polynomial interactions with recursive structure
        poly_fractal = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimensionality
                power_factor = 1.0 + 0.2 * np.sin(0.5 * (i + j))
                poly_fractal += x[i]**power_factor * x[j]**(3 - power_factor)
        
        # Logarithmic conditioning with oscillatory perturbation
        cond_factor = 1.0 + 0.7 * np.log(self.dim + 1) + 0.2 * np.sin(0.3 * self.dim)
        
        # Cross-dimensional coupling with hyperbolic secant functions
        sech_coupling = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                sech_coupling += (np.sech(x[i]) * np.sech(x[i+1])) * (x[i]**2 + x[i+1]**2)
        
        # Noise-like component with multi-frequency interference
        noise = 0
        for i in range(self.dim):
            noise += 0.2 * np.sin(5 * x[i]) * np.cos(7 * x[i]) + 0.1 * np.sin(11 * x[i])
        
        # Combine all components with appropriate weights
        return cond_factor * (0.3 * quad + 0.25 * wave + 0.2 * gaussian + 0.15 * exp_mod + 0.1 * poly_fractal + 0.05 * sech_coupling) + noise