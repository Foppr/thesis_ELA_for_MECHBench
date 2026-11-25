import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced quadratic basin term with dimension-dependent scaling and dynamic exponent
        quadratic_term = 0.4 * np.sum(x_normalized**2) * (1 + 0.15 * self.dim + 0.05 * np.sin(self.dim * 0.5))
        
        # Chaotic sinusoidal components with altered exponential decay rates, dynamic frequencies, and perturbed amplitudes
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 20 * (1.8 ** i) * (1 + 0.4 * np.sin(0.6 * i))
            amplitude = 1.2 * (1 + 0.2 * np.cos(0.3 * i))
            chaotic_term += amplitude * np.sin(freq * x_normalized[i]) * np.exp(-0.4 * i) * (1 + 0.4 * x_normalized[i]**3)
        
        # Cross-dimensional interactions with variable coupling strength, dynamic phase shifts, and non-linear interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.7 * (1 - np.exp(-0.2 * (i + j))) * (1 + 0.3 * np.cos(0.4 * (i - j)))
                phase_shift = 0.15 * np.sin(0.5 * (i + j))
                interaction = np.sin(12 * np.pi * x_normalized[i] + phase_shift) * np.cos(9 * np.pi * x_normalized[j] + phase_shift)
                cross_term += coupling * interaction * (1 + 0.1 * np.sin(0.2 * (i - j)))
        
        # Dynamic global minimum shift with enhanced complexity and non-uniform distribution
        shift = 0.5 * (self.dim / 20.0)
        shift_term = 1.2 * np.sum((x_normalized - shift)**3) + 0.6 * np.sum((x_normalized + shift)**2) + 0.3 * np.sum(np.abs(x_normalized))
        
        # Additional high-frequency oscillatory component with variable frequency and amplitude
        high_freq_term = 0.0
        for i in range(self.dim):
            freq = 30 * (1.5 ** i) * (1 + 0.2 * np.cos(0.4 * i))
            amp = 0.8 * (1 + 0.3 * np.sin(0.3 * i))
            high_freq_term += amp * np.sin(freq * x_normalized[i]) * np.cos(20 * x_normalized[i]) * np.exp(-0.25 * i)
        
        # Add a perturbed global minimum to increase challenge
        global_min_perturbation = 0.1 * np.sum(np.abs(x_normalized - 0.3))
        
        return quadratic_term + chaotic_term + cross_term + shift_term + high_freq_term + global_min_perturbation