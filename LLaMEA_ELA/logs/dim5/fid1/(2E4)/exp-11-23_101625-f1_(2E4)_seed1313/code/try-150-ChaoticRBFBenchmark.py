import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic scaling
        result = 0.2 * np.sum(x**2)
        
        # Chaotic sine wave components with enhanced modulation
        for i in range(self.dim):
            freq = 1.5 * (i + 1) * (1.0 + 0.6 * np.sin(i * 0.8))
            amp = 2.0 + 0.7 * np.cos(i * 0.4)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            
        # Radial basis functions with multi-scale centers and widths
        for i in range(self.dim):
            center = 1.5 * np.sin(i * 0.7 + np.sum(x) * 0.3)
            width = 0.6 + 0.4 * np.cos(i * 0.5)
            result += 1.8 * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Multi-scale chaotic modulation with enhanced coupling
        chaos_sum = 0.0
        for i in range(self.dim):
            chaos_freq = 2.5 + 3.0 * np.sin(i * 0.6 + np.sum(x) * 0.2)
            chaos_amp = 1.2 + 0.6 * np.cos(i * 0.4)
            chaos_sum += chaos_amp * np.sin(chaos_freq * x[i] + np.sum(x) * 0.3)
        result += 1.2 * chaos_sum**2
        
        # Adaptive conditioning factor with enhanced dimensionality impact
        cond_factor = 1.0 + 0.4 * np.sin(np.sum(x) * 0.2) + 0.3 * np.cos(self.dim * 0.3)
        result *= cond_factor
        
        # Cross-dimensional interaction terms with stronger coupling
        for i in range(self.dim):
            interaction = 0.0
            for j in range(i+1, min(i+5, self.dim)):
                dist = abs(x[i] - x[j])
                coupling = 0.6 * np.sin((i + j) * 0.4 + np.sum(x) * 0.2)
                interaction += coupling * np.exp(-dist**2 / (2.0 * (j-i)**2))
            result += 0.8 * interaction
            
        # High-frequency harmonic interference with enhanced complexity
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(i * 0.5)
            harmonic_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        result += 0.7 * harmonic_sum**2
        
        # Radial fractal component with enhanced frequency modulation
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 6.0 + 4.0 * np.sin(r * 0.15)
            result += 2.0 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.4)
            
        # Asymmetric barrier with enhanced dynamic scaling
        barrier = 0.0
        for i in range(self.dim):
            barrier += 2.5 * np.exp(1.0 * abs(x[i]) / 5.0) * (1.0 + 0.5 * np.sin(x[i] * 4.0))
        result += barrier
        
        return result