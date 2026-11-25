import numpy as np

class PolynomialWaveInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion with adaptive exponents
        poly_term = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 1.5 * np.sin(i * 0.5 + self.dim * 0.3)
            poly_term += (x[i] ** exp_factor) * np.exp(-0.1 * np.abs(x[i]))
        
        # Trigonometric wave interference with dynamic phase shifts and amplitudes
        wave_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.7 + self.dim * 0.2)
            phase = 0.3 * np.cos(i * 0.4 + self.dim * 0.5)
            wave_term += amp * np.sin(x[i] * 2.0 + phase) * np.cos(x[i] * 1.5 + phase * 0.7)
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.6 + self.dim * 0.4)
            cond_term += scale * x[i] ** 2
        
        # Multi-scale sinusoidal modulation with frequency coupling
        multi_scale_term = 0.0
        for i in range(self.dim):
            freq1 = 1.0 + 0.8 * np.sin(i * 0.3)
            freq2 = 0.5 + 0.6 * np.cos(i * 0.4)
            multi_scale_term += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.05 * x[i] ** 2)
        
        # Cross-term coupling with nonlinear interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross = (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j]))
                cross_term += cross ** 2
        
        # Adaptive peak modulation with dynamic positioning
        peak_term = 0.0
        for i in range(self.dim):
            pos = -4.0 + 8.0 * np.sin(i * 0.5 + self.dim * 0.3)
            height = 1.5 + 1.0 * np.cos(i * 0.6)
            width = 0.5 + 0.5 * np.sin(i * 0.4)
            peak_term += height * np.exp(-0.5 * ((x[i] - pos) / width) ** 2)
        
        # Chaotic perturbation with logistic map dynamics
        chaos_term = 0.0
        r = 3.8 + 0.2 * np.sin(self.dim * 0.4)
        for i in range(self.dim):
            x_prev = np.sin(i * 0.7) if i > 0 else x[0]
            logistic_val = r * x_prev * (1 - x_prev)
            chaos_term += np.sin(logistic_val * 5.0) * np.cos(x[i] * 0.5)
        
        # Final weighted combination with dynamic normalization
        total = 0.25 * poly_term + 0.20 * wave_term + 0.15 * cond_term + 0.18 * multi_scale_term + 0.12 * cross_term + 0.08 * peak_term + 0.02 * chaos_term
        
        # Global normalization factor based on dimensionality
        norm_factor = 1.0 + 0.1 * np.log(self.dim + 1.0)
        
        return total * norm_factor