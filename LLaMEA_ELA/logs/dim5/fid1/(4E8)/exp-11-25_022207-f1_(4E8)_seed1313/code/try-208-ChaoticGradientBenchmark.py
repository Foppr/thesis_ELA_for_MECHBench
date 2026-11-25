import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial harmonic component with multi-scale sinusoidal modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial_harmonic = np.sin(5.0 * np.pi * r) * np.cos(3.0 * np.pi * r) * np.exp(-0.5 * r**2)
        
        # Multi-scale sinusoidal coupling with varying frequencies and amplitudes
        coupled_terms = 0
        frequencies = [1.0, 2.0, 4.0]
        amplitudes = [1.5, 0.8, 0.3]
        for freq, amp in zip(frequencies, amplitudes):
            coupled_terms += amp * np.sin(freq * np.pi * r) * np.cos(freq * np.pi * r)
        
        # Chaotic gradient modulation with exponential decay and sine coupling
        grad_mod = np.sum(np.exp(-0.3 * x_norm**2) * 
                         np.sin(4.0 * np.pi * x_norm) * 
                         np.cos(2.0 * np.pi * x_norm) * 
                         np.tan(0.6 * x_norm))
        
        # Multi-scale harmonic peaks with radial symmetry and phase shifts
        peaks = 0
        for i in range(1, 6):
            phase_shift = i * np.pi / 5.0
            scale = 1.0 / (i * 0.5 + 1.0)
            peaks += np.exp(-0.5 * ((r - scale) / (0.2 * scale))**2) * np.cos(i * phase_shift)
        
        # Adaptive saddle-point structure with enhanced coupling
        saddle = 0
        for i in range(self.dim - 1):
            saddle += (x_norm[i]**2 - x_norm[i+1]**2)**2 * np.exp(-0.2 * (x_norm[i] + x_norm[i+1])**2)
        
        # Fractal-like gradient structure with self-similar harmonic components
        fractal_grad = 0
        for i in range(1, 4):
            fractal_grad += np.sin(i * np.pi * r) * np.cos(i * np.pi * r) * (1.0 / i)
        
        # Combined function with adaptive noise
        result = radial_harmonic + coupled_terms + grad_mod + peaks + saddle + fractal_grad
        
        # Add robustness noise
        noise = 0.02 * np.random.rand() * (1.0 + 0.1 * np.abs(np.mean(x_norm)))
        
        return result + noise