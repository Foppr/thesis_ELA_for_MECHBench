import numpy as np

class QuasicrystalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Five-fold rotational symmetry pattern with quasicrystal-like structure
        symmetry_term = np.sum(np.cos(2 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.sin(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                              np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                              np.cos(5 * np.pi * (x_norm[:-1]**2 - x_norm[1:]**2)))
        
        # Competing exponential decay modes with varying time constants
        decay_terms = 0
        for i in range(self.dim):
            decay_terms += np.exp(-0.3 * (x_norm[i] - 1.5)**2) * np.exp(-0.7 * (x_norm[i] + 1.2)**2) * \
                          np.exp(-0.4 * (x_norm[i] - 0.8)**2) * np.exp(-0.6 * (x_norm[i] + 0.9)**2)
        
        # Hybrid trigonometric-polynomial interactions with phase modulation
        hybrid_term = 0
        for i in range(self.dim):
            hybrid_term += (np.sin(4 * np.pi * x_norm[i])**3 + np.cos(3 * np.pi * x_norm[i])**2) * \
                          (x_norm[i]**4 + x_norm[i]**3 - 2 * x_norm[i]**2 + x_norm[i])
        
        # Multi-scale oscillatory pattern with frequency modulation
        oscillatory = 0
        frequencies = [1.2, 2.7, 4.1, 5.8]
        amplitudes = [2.1, 1.8, 1.3, 0.9]
        for freq, amp in zip(frequencies, amplitudes):
            oscillatory += amp * np.sin(freq * np.pi * x_norm) * np.cos(freq * np.pi * x_norm) * \
                          np.exp(-0.2 * np.abs(x_norm))
        
        # Saddle-point harmonic coupling with competing gradient directions
        saddle_harmonic = np.sum((np.sin(2.5 * np.pi * x_norm)**2 - np.cos(1.8 * np.pi * x_norm)**2) * \
                                (x_norm[:-1]**2 + x_norm[1:]**2) * \
                                np.exp(-0.3 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Combined function with polynomial scaling and asymmetric weighting
        result = symmetry_term + decay_terms + hybrid_term + oscillatory + saddle_harmonic
        
        # Add controlled noise for robustness
        noise = 0.03 * np.random.rand() * (1.0 + 0.2 * np.abs(np.mean(x_norm)))
        
        return result + noise