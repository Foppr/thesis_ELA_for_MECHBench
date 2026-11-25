import numpy as np

class ChaoticLogisticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map components with varying parameters and enhanced complexity
        f1 = 0.0
        for i in range(self.dim):
            r = 3.9 + 0.3 * np.sin(0.4 * i + 0.2 * np.sum(x))
            x_prev = np.cos(i) if i > 0 else x[0]
            chaotic_term = r * x_prev * (1 - x_prev)
            f1 += np.abs(chaotic_term) * np.exp(-0.15 * x[i]**2)
            
        # Radial harmonic oscillations with adaptive frequencies and fractal scaling
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i + 0.4 * r + 0.1 * np.sum(x))
            amp = 1.5 + 1.5 * np.cos(0.4 * i + 0.3 * r)
            f2 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Cross-dimensional adaptive couplings with enhanced fractal-like scaling
        f3 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    scale = 1.2 + 0.5 * np.sin(0.4 * (i + j) + 0.5 * r + 0.2 * np.sum(x))
                    coupling = np.cos(x[i] * x[j]) * scale
                    coupling_sum += coupling
            f3 += coupling_sum * np.exp(-0.1 * x[i]**2)
            
        # Multi-scale fractal-like interactions with recursive structure and enhanced complexity
        f4 = 0.0
        for i in range(self.dim):
            fractal_scale = 1.5 + 0.5 * np.sin(0.7 * i + 0.4 * r + 0.3 * np.sum(x))
            f4 += fractal_scale * np.cos(np.pi * x[i] / (1.0 + 0.4 * r))**5
            
        # Adaptive penalty terms with logistic map conditioning and enhanced nonlinearity
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.8:
                penalty_strength = 1.5 + 0.7 * np.sin(0.6 * i + 0.5 * r + 0.2 * np.sum(x))
                f5 += penalty_strength * np.exp(-0.2 * (np.abs(x[i]) - 3.8)**2)
                
        # Multi-modal sinusoidal components with dynamic phase shifts and enhanced complexity
        f6 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.6 * i + 0.4 * r + 0.3 * np.sum(x))
            freq_mod = 1.5 + 1.2 * np.cos(0.5 * i + 0.2 * np.sum(x))
            f6 += np.cos(freq_mod * x[i] + phase_shift)**3
            
        # Exponential radial conditioning with logistic modulation and enhanced nonlinearity
        f7 = 0.0
        for i in range(self.dim):
            modulator = 1.2 + 0.6 * np.sin(0.5 * i + 0.4 * r + 0.3 * np.sum(x))
            f7 += modulator * np.exp(-0.15 * x[i]**2) * np.sin(2.0 * x[i])**3
            
        # Adaptive cross-dimensional polynomial interactions with enhanced complexity
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 1.0 + 0.4 * np.sin(0.5 * (i - j) + 0.3 * np.sum(x))
                interaction = x[i]**4 * x[j]**3
                f8 += coeff * interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Boundary-sensitive logistic oscillations with enhanced complexity
        f9 = 0.0
        for i in range(self.dim):
            boundary_factor = 1.2 + 0.6 * np.sin(0.9 * i + 0.3 * np.sum(x))
            if np.abs(x[i]) > 4.5:
                f9 += boundary_factor * np.exp(-2.0 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant harmonic components with time-varying amplitudes and enhanced complexity
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.6 * np.sin(0.4 * i + 0.3 * r + 0.2 * np.sum(x))
            freq = 2.5 + 2.0 * np.cos(0.5 * i + 0.2 * r + 0.1 * np.sum(x))
            f10 += amp * np.cos(freq * x[i]) * np.sin(freq * x[i])
            
        # Additional chaotic cross-dimensional interactions for enhanced complexity
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f11 += chaotic_interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Fractional Brownian motion inspired radial interactions
        f12 = 0.0
        for i in range(self.dim):
            fb_factor = 0.8 + 0.4 * np.sin(0.3 * i + 0.5 * r)
            f12 += fb_factor * np.log(1.0 + x[i]**2) * np.exp(-0.1 * r)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12