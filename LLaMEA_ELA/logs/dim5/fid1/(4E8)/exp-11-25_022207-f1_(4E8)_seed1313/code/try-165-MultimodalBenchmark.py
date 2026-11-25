import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic modular structure with multiple logistic maps and dynamic scaling
        chaos_mod = 0
        for i in range(self.dim):
            chaos_mod += 3.8 * x_norm[i] * (1 - x_norm[i]) * np.sin(2 * np.pi * x_norm[i] * (i + 1))
        
        # Multi-scale fractal peaks with varying heights, widths, and positions
        peaks = 0
        scales = [0.2, 0.5, 1.0, 1.5, 2.0]
        heights = [2.0, 1.2, 0.8, 0.4, 0.2]
        positions = [np.sin(i * 1.3) for i in range(5)]
        for i, (scale, height, pos) in enumerate(zip(scales, heights, positions)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - pos) / scale)**2))
        
        # Gradient-asymmetric corridor structure with dynamic frequency and phase
        asym_corridor = 0
        for i in range(self.dim):
            asym_corridor += np.abs(x_norm[i]) * np.exp(-0.1 * x_norm[i]**2) * \
                           np.sin(5 * np.pi * x_norm[i] + i * 0.5) * \
                           np.cos(4 * np.pi * x_norm[i] + i * 0.3) * \
                           np.tan(0.6 * x_norm[i])
        
        # Polynomial coupling with trigonometric modulation and dynamic exponents
        poly_coupling = 0
        for i in range(self.dim - 1):
            term = (x_norm[i]**3 + x_norm[i+1]**3)**3 * \
                   np.cos(7 * np.pi * (x_norm[i] + x_norm[i+1])) * \
                   np.exp(-0.3 * (x_norm[i] - x_norm[i+1])**2)
            poly_coupling += term
        
        # Saddle-point repulsion with exponential decay and adaptive scaling
        saddle_repulse = 0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            sum_vals = x_norm[i] + x_norm[i+1]
            term = (x_norm[i]**3 - x_norm[i+1]**3)**2 * \
                   np.exp(-0.5 * sum_vals**2) * \
                   np.sin(8 * np.pi * diff)
            saddle_repulse += term
        
        # Fractal-like chaotic component with multiple frequency components and adaptive weights
        fractal = 0
        freqs = [15, 12, 9, 6, 3]
        for i in range(self.dim):
            fractal += np.sin(freqs[i % len(freqs)] * np.pi * x_norm[i]) * \
                      np.cos(freqs[i % len(freqs)] * np.pi * x_norm[i]) * \
                      np.exp(-0.3 * np.abs(x_norm[i])) * \
                      np.tan(0.5 * x_norm[i]) * \
                      np.sin(0.8 * x_norm[i])
        
        # Combined function with chaotic noise and dynamic scaling
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal
        
        # Add dynamic random perturbation for robustness
        noise = 0.15 * np.random.rand() * (1 + 0.6 * np.sin(np.sum(x_norm)))
        
        return result + noise