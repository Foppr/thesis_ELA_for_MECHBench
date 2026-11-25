import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced sinusoidal oscillation with dynamic frequency and amplitude modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = 3.5 + 4.5 * np.sin(i * 0.85 + self.dim * 0.42)
            amp = 1.7 + 1.8 * np.cos(i * 0.72 + self.dim * 0.32)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.62)
        
        # Modified radial basis function with dynamic centers and varying widths
        radial_term = 0.0
        for i in range(self.dim):
            center = -3.8 + 7.6 * np.sin(i * 0.62 + self.dim * 0.27)
            width = 0.25 + 0.95 * np.cos(i * 0.52 + self.dim * 0.42)
            radial_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Enhanced asymmetric gradient field with directional bias and cubic components
        grad_term = 0.0
        for i in range(self.dim):
            bias = 1.6 * np.sin(i * 1.22 + self.dim * 0.42)
            grad_term += (x[i] ** 3) * np.exp(-0.42 * x[i] ** 2) * (1.0 + bias * 0.62)
        
        # Fractal-like recursive structure with self-similarity and multi-scale features
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.05 + 0.65 * np.sin(i * 1.52 + self.dim * 0.37)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.82)
        
        # Dynamic coupling terms with non-linear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.42 * np.sin(i * j * 0.32))
                coupling_term += coupling ** 2
        
        # Multi-peak landscape with varying peak heights, widths and positions
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 2.6 + 1.9 * np.sin(i * 0.92)
            w1 = 0.32 + 0.68 * np.cos(i * 0.62)
            h2 = 2.9 + 1.1 * np.sin(i * 0.82)
            w2 = 0.92 + 0.58 * np.cos(i * 0.72)
            p1 = 2.1 + 3.9 * np.sin(i * 1.22)
            p2 = -2.9 + 3.9 * np.cos(i * 0.92)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.36 * peak1 + 0.64 * peak2
        
        # Recursive chaotic perturbation with higher dimensional coupling (modified)
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.sin(x[i] * 0.42 + self.dim * 0.32) * np.cos(x[i] * 0.37)
            chaos_term += chaos_factor * np.sin(x[i] ** 2 * 0.52)
        
        # Final combination with adjusted weights for better conditioning
        total = 0.39 * sin_term + 0.26 * radial_term + 0.20 * grad_term + 0.17 * fractal_term + 0.03 * coupling_term + 0.08 * peak_term + 0.02 * chaos_term
        
        # Global scaling factor with chaotic modulation and adaptive behavior
        global_scale = 1.0 + 0.48 * np.sin(self.dim * 0.72) * np.cos(self.dim * 0.42)
        
        return total * global_scale