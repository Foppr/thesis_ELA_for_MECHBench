import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested sinusoidal oscillations with varying frequencies
        nested_trig = 0.0
        for i in range(self.dim):
            freq = 2 ** (i + 1)
            nested_trig += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i] / 2)
        
        # Fractional polynomial scaling with non-integer exponents
        fractional_poly = 0.0
        exponents = [1.5, 2.5, 3.5]
        for i in range(min(len(exponents), self.dim)):
            fractional_poly += np.abs(x_norm[i]) ** exponents[i]
        
        # Adaptive radial barriers with dynamic thresholds
        radial_barrier = 0.0
        for i in range(self.dim):
            dist_from_origin = np.abs(x_norm[i])
            barrier_term = 1.0 / (1.0 + np.exp(5.0 * (dist_from_origin - 0.8)))
            radial_barrier += barrier_term
        
        # Chaotic cross-dimensional interactions with sine-cosine coupling
        chaotic_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(5.0 * (x_norm[i] + x_norm[j])) * np.cos(3.0 * (x_norm[i] - x_norm[j]))
                chaotic_cross += coupling / (1.0 + np.abs(x_norm[i] - x_norm[j]))
        
        # Enhanced Gaussian peaks with varying amplitudes and positions
        gaussian_peaks = 0.0
        num_peaks = min(5, self.dim)
        for i in range(num_peaks):
            center = np.sin(i * np.pi / num_peaks) * 0.8
            width = 0.2 + 0.3 * np.cos(i * np.pi / num_peaks)
            amplitude = 1.0 + 0.5 * np.sin(i * np.pi / num_peaks)
            gaussian_peaks += amplitude * np.exp(-0.5 * ((x_norm[i] - center) / width) ** 2)
        
        # Combine all components with optimized weights
        return 0.25 * nested_trig + 0.3 * fractional_poly + 0.15 * radial_barrier + 0.2 * chaotic_cross + 0.1 * gaussian_peaks