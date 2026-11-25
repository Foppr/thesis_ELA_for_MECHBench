import numpy as np

class ChaoticPhaseCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial harmonic oscillations with adaptive frequency
        f1 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * i + 0.2 * r)
            f1 += (x[i]**2 + 0.1) * np.cos(freq * x[i])**2
        
        # Adaptive conditioning gradients with exponential scaling
        f2 = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.3 * np.exp(-0.1 * np.abs(x[i]))
            f2 += cond_factor * (x[i]**4 - 2*x[i]**2 + 1)
        
        # Chaotic phase coupling with logistic map dynamics
        f3 = 0.0
        for i in range(self.dim):
            # Logistic map based phase modulation
            phase = np.sin(0.5 * x[i] + 0.1 * r)
            chaos_factor = 4.0 * phase * (1.0 - phase)
            f3 += np.sin(chaos_factor * x[i])**2
        
        # Multi-scale harmonic interactions with coupling strength modulation
        f4 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = 0.5 + 0.5 * np.sin(0.2 * (i - j) + 0.1 * r)
                    interaction = np.cos(x[i] - x[j])**2
                    coupling_sum += coupling_strength * interaction
            f4 += coupling_sum
        
        # Boundary-sensitive harmonic potential with chaotic modulation
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_mod = 1.0 + 0.4 * np.sin(0.7 * i + 0.3 * r)
                f5 += boundary_mod * np.exp(-0.2 * (np.abs(x[i]) - 4.0)**2)
        
        # Exponential radial conditioning with chaotic parameter variation
        f6 = 0.0
        for i in range(self.dim):
            param = 1.0 + 0.6 * np.sin(0.4 * i + 0.3 * r) * np.cos(0.2 * r)
            f6 += param * np.exp(-0.1 * x[i]**2) * (x[i]**2 - 1)**2
        
        # Fractal-like phase structure with multi-dimensional coupling
        f7 = 0.0
        for i in range(self.dim):
            phase_mod = np.sin(0.6 * x[i] + 0.3 * r) + 0.4 * np.cos(0.5 * r)
            f7 += np.cos(phase_mod)**2
        
        # Saddle-point harmonic resonance with adaptive coupling
        f8 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling = 1.0 + 0.3 * np.sin(0.2 * (i + j) + 0.1 * r)
                    saddle_interaction = coupling * np.sin(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f8 += saddle_sum
        
        # Complex harmonic resonance with chaotic phase shifts
        f9 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.4 * i + 0.2 * r) + 0.3 * np.cos(0.6 * r)
            f9 += np.sin(2.0 * x[i] + phase_shift)**3
        
        # Polynomial harmonic interactions with exponential decay
        f10 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                coeff = 1.0 + 0.4 * np.sin(0.3 * (i + j) + 0.2 * r)
                interaction = x[i]**2 * x[j]**2
                poly_sum += coeff * interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
            f10 += poly_sum
        
        # Additional fractal-like structure with modified coupling
        f11 = 0.0
        for i in range(self.dim):
            fractal_mod = 0.5 * np.sin(0.8 * x[i] + 0.4 * r) + 0.3 * np.cos(0.6 * r)
            f11 += np.sin(fractal_mod)**2
        
        # Enhanced chaotic modulation with multi-scale frequency
        f12 = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.7 * np.sin(0.5 * x[i] + 0.3 * r) * np.cos(0.4 * r)
            f12 += freq_mod * np.exp(-0.1 * x[i]**2) * (x[i]**3 - x[i])**2
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12