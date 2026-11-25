import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Chaotic sine wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 * (i + 1) * (1.0 + 0.5 * np.sin(i * 0.7))
            amp = 1.5 + 0.8 * np.cos(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Radial basis functions with dynamic centers and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(i * 0.6 + np.sum(x) * 0.2)
            width = 0.5 + 0.3 * np.cos(i * 0.4)
            result += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Multi-scale chaotic modulation with adaptive scaling
        chaos_sum = 0.0
        for i in range(self.dim):
            chaos_freq = 3.0 + 2.0 * np.sin(i * 0.5 + np.sum(x) * 0.1)
            chaos_amp = 1.0 + 0.5 * np.cos(i * 0.3)
            chaos_sum += chaos_amp * np.sin(chaos_freq * x[i] + np.sum(x) * 0.2)
        result += 0.8 * chaos_sum**2
        
        # Adaptive conditioning factor based on dimensionality and position
        cond_factor = 1.0 + 0.3 * np.sin(np.sum(x) * 0.15) + 0.2 * np.cos(self.dim * 0.2)
        result *= cond_factor
        
        # Cross-dimensional interaction terms with fractal-like scaling
        for i in range(self.dim):
            interaction = 0.0
            for j in range(i+1, min(i+4, self.dim)):
                dist = abs(x[i] - x[j])
                coupling = 0.5 * np.sin((i + j) * 0.3 + np.sum(x) * 0.1)
                interaction += coupling * np.exp(-dist**2 / (2.0 * (j-i)**2))
            result += 0.6 * interaction
            
        # High-frequency harmonic interference
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 8.0 + 4.0 * np.sin(i * 0.4)
            harmonic_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        result += 0.5 * harmonic_sum**2
        
        # Radial fractal component
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 5.0 + 3.0 * np.sin(r * 0.1)
            result += 1.5 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.3)
            
        # Asymmetric barrier with dynamic scaling
        barrier = 0.0
        for i in range(self.dim):
            barrier += 2.0 * np.exp(0.8 * abs(x[i]) / 5.0) * (1.0 + 0.4 * np.sin(x[i] * 3.0))
        result += barrier
        
        return result