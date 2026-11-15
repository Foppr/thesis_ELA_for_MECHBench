import numpy as np

class ExponentialTrigonometricParabolicBasin:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with adaptive rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.5 + 0.5 * np.sin(i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.cos(rate * x[i]**2)
        
        # Trigonometric wave interference with dynamic phases
        wave_interference = 0
        for i in range(self.dim):
            phase = 0.2 * np.sin(i * 0.4) + 0.1 * np.cos(i * 0.6)
            wave_interference += np.sin(x[i] + phase) * np.cos(x[i]**2 + phase) + 0.3 * np.sin(2.0 * x[i] + phase)
        
        # Adaptive parabolic basins with chaotic vertex positions
        parabolic_basins = 0
        for i in range(min(8, self.dim)):
            vertex = -3.0 + 6.0 * (i / max(1, self.dim - 1)) + 0.4 * np.sin(i * 0.8)
            width = 0.2 + 0.8 * np.abs(np.sin(i * 0.5))
            parabolic_basins += (x[i] - vertex)**2 * np.exp(-0.5 * (x[i] - vertex)**2 / width**2)
        
        # Dynamic dimensionality scaling with chaotic weights
        dim_scaling = 0
        for i in range(self.dim):
            weight = 0.3 + 0.7 * np.abs(np.sin(i * 0.9))
            dim_scaling += weight * x[i]**(2 + int(i * 0.3))
        
        # Quantum-like probability distributions with complex amplitudes
        prob_dist = 0
        for i in range(self.dim):
            amplitude = 0.5 + 0.5 * np.sin(i * 0.6)
            prob_dist += amplitude * np.exp(-0.5 * (x[i] - np.sin(i * 0.4))**2) * np.cos(x[i] * np.cos(i * 0.3))
        
        # Non-linear coupling terms with chaotic coefficients
        coupling_terms = 0
        for i in range(self.dim - 1):
            coeff = 0.4 + 0.6 * np.sin(i * 0.5)
            coupling_terms += coeff * np.sin(x[i] * x[i+1]) * np.cos(x[i]**2 + x[i+1]**2)
        
        # Fractal-like recursive patterns with exponential growth
        fractal_pattern = 0
        if self.dim >= 3:
            for i in range(0, self.dim - 2, 3):
                fractal_pattern += np.exp(-0.1 * (x[i]**2 + x[i+1]**2 + x[i+2]**2)) * np.sin(x[i] + x[i+1] + x[i+2])
        
        # High-frequency oscillation with dynamic frequency modulation
        high_freq = 0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(i * 0.7)
            high_freq += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**3) * np.exp(-0.1 * x[i]**2)
        
        # Combined fitness with refined weights
        return 1.2 * exp_decay + 0.9 * wave_interference + 0.7 * parabolic_basins + 0.5 * dim_scaling + 0.3 * prob_dist + 0.4 * coupling_terms + 0.2 * fractal_pattern + 0.1 * high_freq