import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced sinusoidal oscillation with dynamic frequency and amplitude modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2.5 + 3.5 * np.sin(i * 0.75 + self.dim * 0.32)
            amp = 1.2 + 1.3 * np.cos(i * 0.65 + self.dim * 0.27)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.55)
        
        # Modified radial basis function with dynamic centers and varying widths
        radial_term = 0.0
        for i in range(self.dim):
            center = -3.2 + 6.8 * np.sin(i * 0.52 + self.dim * 0.22)
            width = 0.18 + 0.85 * np.cos(i * 0.42 + self.dim * 0.37)
            radial_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Enhanced asymmetric gradient field with directional bias and cubic components
        grad_term = 0.0
        for i in range(self.dim):
            bias = 1.3 * np.sin(i * 1.15 + self.dim * 0.37)
            grad_term += (x[i] ** 3) * np.exp(-0.32 * x[i] ** 2) * (1.0 + bias * 0.55)
        
        # Fractal-like recursive structure with self-similarity and multi-scale features
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 0.85 + 0.65 * np.sin(i * 1.42 + self.dim * 0.32)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.72)
        
        # Dynamic coupling terms with non-linear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.32 * np.sin(i * j * 0.27))
                coupling_term += coupling ** 2
        
        # Multi-peak landscape with varying peak heights, widths and positions
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 2.2 + 1.6 * np.sin(i * 0.82)
            w1 = 0.27 + 0.58 * np.cos(i * 0.52)
            h2 = 2.4 + 0.9 * np.sin(i * 0.72)
            w2 = 0.82 + 0.48 * np.cos(i * 0.62)
            p1 = 1.7 + 3.3 * np.sin(i * 1.12)
            p2 = -2.3 + 3.3 * np.cos(i * 0.82)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.42 * peak1 + 0.58 * peak2
        
        # Recursive chaotic perturbation with higher dimensional coupling (modified)
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.sin(x[i] * 0.37 + self.dim * 0.27) * np.cos(x[i] * 0.32)
            chaos_term += chaos_factor * np.sin(x[i] ** 2 * 0.42)
        
        # Final combination with adjusted weights for better conditioning
        total = 0.36 * sin_term + 0.24 * radial_term + 0.18 * grad_term + 0.14 * fractal_term + 0.05 * coupling_term + 0.06 * peak_term + 0.03 * chaos_term
        
        # Global scaling factor with chaotic modulation and adaptive behavior
        global_scale = 1.0 + 0.42 * np.sin(self.dim * 0.62) * np.cos(self.dim * 0.37)
        
        return total * global_scale