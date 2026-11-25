import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial base with adaptive exponents and varying coefficients
        poly_term = np.sum((x_normalized**3 + 0.5 * x_normalized**2 + 0.1 * x_normalized) * (1 + 0.1 * np.arange(self.dim)))
        
        # Trigonometric components with frequency modulation and amplitude scaling
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (1 + 0.5 * np.sin(0.3 * i)) * (i + 1)
            amp = 1.5 * (1 + 0.3 * np.cos(0.4 * i))
            trig_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i])
        
        # Radial basis function with dynamic centers and adaptive widths
        rbf_term = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(0.2 * i)
            width = 0.8 + 0.2 * np.cos(0.3 * i)
            rbf_term += np.exp(-width * (x_normalized[i] - center)**2)
        
        # Cross-dimensional interaction with non-linear coupling and phase shifts
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * np.sin(0.5 * (i + j)) * np.cos(0.4 * (i - j))
                phase_shift = 0.2 * np.sin(0.6 * i) * np.cos(0.7 * j)
                cross_term += coupling * np.sin(3 * x_normalized[i] + phase_shift) * np.cos(2 * x_normalized[j] + phase_shift)
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = 1 + 0.5 * np.sin(0.4 * i) * (self.dim / 10.0)
            cond_term += cond_factor * x_normalized[i]**4
        
        # Global minimum perturbation with sinusoidal modulation
        min_shift = 0.2 * np.sin(0.3 * self.dim)
        shift_term = 0.8 * np.sum((x_normalized - min_shift)**2) + 0.4 * np.sum((x_normalized + min_shift)**3)
        
        return poly_term + trig_term + rbf_term + cross_term + cond_term + shift_term