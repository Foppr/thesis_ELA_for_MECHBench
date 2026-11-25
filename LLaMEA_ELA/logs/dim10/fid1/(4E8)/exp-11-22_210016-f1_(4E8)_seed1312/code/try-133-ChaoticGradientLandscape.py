import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Dynamic harmonic oscillation component with chaotic frequency modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.7) * np.cos(i * 0.3)
            phase = i * 0.5 + 0.2 * np.sin(i * 0.9)
            harmonic_sum += np.sin(x[i] * freq + phase) * np.cos(x[i] * (freq * 1.3) + phase)
        
        # Multi-scale exponential decay with adaptive weights
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.6) * np.cos(i * 0.4)
            exp_decay += np.exp(-np.abs(x[i]) / (1.5 * scale)) * (1.0 + 0.3 * np.sin(x[i] * 2.0))
        
        # Adaptive polynomial cross-terms with dynamic coupling strength
        poly_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 + 0.4 * np.sin(i * j * 0.5) * np.cos(i * j * 0.3)
                poly_cross += (x[i]**2 * x[j]**4 + x[i]**4 * x[j]**2) * coupling
        
        # Chaotic gradient modulation with fractal-like scaling
        grad_mod = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * 0.8) * np.cos(i * 0.6)
            grad_mod += x[i] * np.sin(x[i] * scale_factor * 3.0) * np.cos(x[i] * scale_factor * 2.0)
        
        # Dynamic radial component with time-varying harmonic interference
        r = np.sqrt(np.sum(x**2))
        radial_component = np.exp(-r**2 / 10.0) * (1.0 + 0.5 * np.sin(r * 2.0) * np.cos(r * 0.8))
        
        # Multi-scale chaotic interference with directional bias
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                bias = 0.2 * np.sin(i * j * 0.4)
                interference += (np.sin(x[i] * x[j] * 1.5 + bias) * np.cos(x[i] + x[j]) * 
                               (1.0 + 0.2 * np.sin(i + j * 0.3)))
        
        # Combine all components with optimized weights
        result = 0.7 * harmonic_sum + 0.5 * exp_decay + 0.4 * poly_cross + 0.3 * grad_mod + 0.25 * radial_component + 0.15 * interference
        
        return result