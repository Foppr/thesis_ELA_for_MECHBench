import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial harmonic component with higher frequency and multi-scale modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial_harmonic = np.sin(8.0 * np.pi * r) * np.cos(4.0 * np.pi * r) * np.exp(-0.3 * r**2)
        
        # Multi-scale sinusoidal coupling with increased frequency diversity and amplitude variation
        coupled_terms = 0
        frequencies = [1.5, 3.0, 6.0, 12.0]
        amplitudes = [2.0, 1.2, 0.6, 0.2]
        for freq, amp in zip(frequencies, amplitudes):
            coupled_terms += amp * np.sin(freq * np.pi * r) * np.cos(freq * np.pi * r)
        
        # Chaotic gradient modulation with enhanced exponential decay and multi-frequency sine coupling
        grad_mod = np.sum(np.exp(-0.5 * x_norm**2) * 
                         np.sin(6.0 * np.pi * x_norm) * 
                         np.cos(3.0 * np.pi * x_norm) * 
                         np.tan(0.8 * x_norm))
        
        # Enhanced multi-scale harmonic peaks with radial symmetry, phase shifts, and adaptive scaling
        peaks = 0
        for i in range(1, 8):
            phase_shift = i * np.pi / 7.0
            scale = 1.0 / (i * 0.3 + 1.0)
            peaks += np.exp(-0.5 * ((r - scale) / (0.15 * scale))**2) * np.cos(i * phase_shift)
        
        # Adaptive saddle-point structure with enhanced coupling and non-linear interaction terms
        saddle = 0
        for i in range(self.dim - 1):
            saddle += (x_norm[i]**3 - x_norm[i+1]**3)**2 * np.exp(-0.1 * (x_norm[i] + x_norm[i+1])**2)
        
        # Fractal-like gradient structure with self-similar harmonic components and exponential scaling
        fractal_grad = 0
        for i in range(1, 6):
            fractal_grad += np.sin(i * np.pi * r) * np.cos(i * np.pi * r) * (1.0 / (i**1.5))
        
        # Additional chaotic cross-dimensional coupling with non-linear interaction
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(2.0 * np.pi * x_norm[i] * x_norm[j]) * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combined function with enhanced noise and scaling
        result = radial_harmonic + coupled_terms + grad_mod + peaks + saddle + fractal_grad + cross_coupling
        
        # Add robustness noise with increased variance
        noise = 0.05 * np.random.rand() * (1.0 + 0.2 * np.abs(np.mean(x_norm)))
        
        return result + noise