import numpy as np

class ChaoticLogisticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map components with varying parameters
        f1 = 0.0
        for i in range(self.dim):
            r = 3.9 + 0.1 * np.sin(0.4 * i)
            x_prev = np.cos(i) if i > 0 else x[0]
            chaotic_term = r * x_prev * (1 - x_prev)
            f1 += np.abs(chaotic_term) * np.exp(-0.12 * x[i]**2)
            
        # Radial harmonic oscillations with adaptive frequencies
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.3 + 1.8 * np.sin(0.5 * i + 0.4 * r)
            amp = 1.2 + 1.0 * np.cos(0.4 * i + 0.3 * r)
            f2 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Cross-dimensional adaptive couplings with fractal-like scaling
        f3 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    scale = 1.0 + 0.5 * np.sin(0.4 * (i + j) + 0.5 * r)
                    coupling = np.cos(x[i] * x[j]) * scale
                    coupling_sum += coupling
            f3 += coupling_sum * np.exp(-0.06 * x[i]**2)
            
        # Multi-scale fractal-like interactions with recursive structure
        f4 = 0.0
        for i in range(self.dim):
            fractal_scale = 1.0 + 0.5 * np.sin(0.7 * i + 0.4 * r)
            f4 += fractal_scale * np.cos(np.pi * x[i] / (1.0 + 0.4 * r))**4
            
        # Adaptive penalty terms with logistic map conditioning
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.6:
                penalty_strength = 1.3 + 0.5 * np.sin(0.6 * i + 0.5 * r)
                f5 += penalty_strength * np.exp(-0.18 * (np.abs(x[i]) - 3.6)**2)
                
        # Multi-modal sinusoidal components with dynamic phase shifts
        f6 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.6 * i + 0.4 * r)
            freq_mod = 1.1 + 0.9 * np.cos(0.5 * i)
            f6 += np.cos(freq_mod * x[i] + phase_shift)**2
            
        # Exponential radial conditioning with logistic modulation
        f7 = 0.0
        for i in range(self.dim):
            modulator = 1.0 + 0.4 * np.sin(0.5 * i + 0.4 * r)
            f7 += modulator * np.exp(-0.15 * x[i]**2) * np.sin(1.3 * x[i])**2
            
        # Adaptive cross-dimensional polynomial interactions
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 1.0 + 0.2 * np.sin(0.5 * (i - j))
                interaction = x[i]**3 * x[j]**2
                f8 += coeff * interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Boundary-sensitive logistic oscillations
        f9 = 0.0
        for i in range(self.dim):
            boundary_factor = 1.0 + 0.6 * np.sin(0.9 * i)
            if np.abs(x[i]) > 4.3:
                f9 += boundary_factor * np.exp(-1.8 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant harmonic components with time-varying amplitudes
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.3 + 0.4 * np.sin(0.4 * i + 0.3 * r)
            freq = 2.2 + 1.3 * np.cos(0.5 * i + 0.2 * r)
            f10 += amp * np.cos(freq * x[i]) * np.sin(freq * x[i])
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10