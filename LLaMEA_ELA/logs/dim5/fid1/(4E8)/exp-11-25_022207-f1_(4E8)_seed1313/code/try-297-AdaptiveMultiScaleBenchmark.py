import numpy as np

class AdaptiveMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multi-scale sinusoidal components with adaptive frequencies and amplitudes
        scale_factors = np.linspace(0.5, 3.0, self.dim)
        freq_modulators = np.linspace(1.2, 4.8, self.dim)
        
        # Base multi-scale harmonic structure
        harmonic_sum = 0
        for i in range(self.dim):
            freq = scale_factors[i] * freq_modulators[i]
            amplitude = 1.0 + 0.5 * np.sin(0.5 * i)
            harmonic_sum += amplitude * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Adaptive conditioning with dynamic exponentiation
        cond_exponent = 1.2 + 0.8 * np.sin(np.mean(x_norm))
        conditioned_term = np.sum(np.abs(x_norm)**cond_exponent)
        
        # Asymmetric coupling with phase-shifted harmonics
        asym_coupling = 0
        for i in range(self.dim - 1):
            asym_coupling += (np.sin(x_norm[i] + x_norm[i+1]) * 
                            np.cos(x_norm[i] - x_norm[i+1]) * 
                            np.exp(-0.3 * (x_norm[i]**2 + x_norm[i+1]**2)))
        
        # Multi-modal Gaussian peaks with dynamic positioning and scaling
        peak_sum = 0
        num_peaks = min(5, self.dim)
        for i in range(num_peaks):
            center = np.sin(i * 1.7) * 0.8
            scale = 0.3 + 0.4 * np.cos(i * 0.9)
            height = 2.0 + 1.5 * np.sin(i * 0.6)
            peak_sum += height * np.exp(-0.5 * ((x_norm - center) / scale)**2)
        
        # Fractal-like interaction with recursive scaling
        fractal_interaction = 0
        for i in range(1, min(4, self.dim)):
            if i < self.dim:
                fractal_interaction += (np.sin(3.1 * x_norm[i-1]) * 
                                     np.cos(2.7 * x_norm[i]) * 
                                     np.exp(-0.2 * np.abs(x_norm[i-1] - x_norm[i])))
        
        # Dynamic phase modulation with time-varying parameters
        phase_mod = np.sum(np.sin(2.3 * np.pi * x_norm + 0.5 * np.mean(x_norm)) * 
                          np.cos(1.8 * np.pi * x_norm + 0.3 * np.std(x_norm)))
        
        # Combined function with adaptive weighting
        result = (harmonic_sum + conditioned_term + asym_coupling + 
                 peak_sum + fractal_interaction + phase_mod)
        
        # Add noise for robustness
        noise = 0.05 * np.random.rand() * (1.0 + 0.3 * np.abs(np.mean(x_norm)))
        
        return result + noise