import numpy as np

class ExponentialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add exponentially decaying sinusoidal waves with adaptive frequencies
        for i in range(1, min(self.dim + 1, 20)):
            freq = 2 ** i
            decay = np.exp(-i * 0.3)
            wave_term = decay * np.sin(freq * x[i-1]) * np.cos(freq * x[i-1] * 0.5)
            result += wave_term
            
        # Add multi-scale harmonic components with varying amplitudes
        for i in range(self.dim):
            scale = 2.0 / (i + 1)
            result += scale * np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.sin(5 * x[i])
        
        # Introduce adaptive gradient modulation based on position
        grad_mod = 1.0
        for i in range(self.dim):
            if x[i] < 0:
                grad_mod *= (1 + 0.5 * np.sin(x[i] * 2))
            else:
                grad_mod *= (1 + 0.3 * np.cos(x[i] * 1.5))
        
        # Add chaotic perturbation with dimensionality-dependent strength
        chaos_strength = 0.2 * self.dim / (self.dim + 1)
        chaos_perturb = chaos_strength * np.sum(np.sin(x * 10) * np.cos(x * 7) * np.sin(x * 3))
        
        # Add basin-shaped regions with varying depths
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += 2.0 * (np.abs(x[i]) - 2.0)**4 + 0.5 * (x[i] - 1.0)**2
        
        return result * grad_mod + chaos_perturb + basin_term