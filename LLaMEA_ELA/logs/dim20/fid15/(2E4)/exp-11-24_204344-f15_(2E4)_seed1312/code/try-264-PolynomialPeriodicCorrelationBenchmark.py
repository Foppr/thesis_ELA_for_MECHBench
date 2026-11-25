import numpy as np

class PolynomialPeriodicCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial potential terms with varying degrees and coefficients
        poly_term = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4)
            coeff = 0.5 + 0.5 * np.sin(i * 0.5)
            poly_term += coeff * (x[i] ** degree)
        
        # Periodic boundary effects with chaotic frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.cos(i * 0.3) + 0.2 * np.sin(i * 0.7)
            amp = 1.0 + 0.3 * np.sin(i * 0.4) + 0.1 * np.cos(i * 0.6)
            periodic_term += amp * np.sin(freq * x[i] / 5.0) * np.cos(freq * x[i] / 5.0)
        
        # Adaptive correlation structure between dimensions with chaotic coupling
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_coeff = 0.3 + 0.2 * np.sin(i * j * 0.2) + 0.1 * np.cos(i + j * 0.3)
                corr_term += corr_coeff * x[i] * x[j]
        
        # Ruggedness modulation through multi-scale sinusoidal perturbations with chaotic scaling
        rugged_term = 0.0
        for i in range(self.dim):
            scale1 = 1.0 + 0.5 * np.sin(i * 0.6) + 0.2 * np.cos(i * 0.8)
            scale2 = 1.0 + 0.3 * np.cos(i * 0.4) + 0.1 * np.sin(i * 0.5)
            rugged_term += scale1 * np.sin(scale2 * x[i]) * np.cos(scale2 * x[i])
        
        # Directional bias with chaotic weights and gradient modulation
        bias_term = 0.0
        for i in range(self.dim):
            weight = 0.8 + 0.2 * np.sin(i * 0.5) + 0.1 * np.cos(i * 0.3)
            bias_term += weight * (x[i] ** 2) * np.exp(-0.1 * x[i] ** 2) + 0.05 * np.sin(x[i] * 3.0)
        
        # Multi-scale harmonic landscape with chaotic phase shifts
        harmonic_term = 0.0
        for i in range(self.dim):
            freq1 = 1.0 + 0.5 * np.sin(i * 0.3) + 0.1 * np.cos(i * 0.4)
            freq2 = 2.0 + 0.3 * np.cos(i * 0.4) + 0.2 * np.sin(i * 0.6)
            phase_shift = 0.5 * np.sin(i * 0.2) + 0.1 * np.cos(i * 0.3)
            harmonic_term += np.sin(freq1 * x[i] + phase_shift) * np.cos(freq2 * x[i] + phase_shift)
        
        # Chaotic gradient field modulation
        grad_field = 0.0
        for i in range(self.dim):
            coeff = 0.1 + 0.05 * np.sin(i * 0.8) + 0.03 * np.cos(i * 0.9)
            grad_field += coeff * np.exp(-0.5 * (x[i] - 2.0) ** 2) * np.sin(x[i])
        
        # Global scaling with chaotic modulation
        global_scale = 1.0 + 0.2 * np.sin(self.dim * 0.1) * np.cos(self.dim * 0.2) + 0.05 * np.sin(self.dim * 0.5)
        
        # Final combination with dynamic weights and chaotic mixing
        total = (0.3 * poly_term + 
                0.25 * periodic_term + 
                0.2 * corr_term + 
                0.1 * rugged_term + 
                0.1 * bias_term + 
                0.05 * harmonic_term +
                0.05 * grad_field)
        
        return total * global_scale