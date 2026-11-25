import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced sinusoidal oscillation with dynamic frequency and amplitude modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 4.0 * np.sin(i * 0.9 + self.dim * 0.5)
            amp = 1.0 + 1.5 * np.cos(i * 0.8 + self.dim * 0.4)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Modified radial basis function with dynamic centers and varying widths
        radial_term = 0.0
        for i in range(self.dim):
            center = -4.5 + 9.0 * np.sin(i * 0.7 + self.dim * 0.35)
            width = 0.15 + 1.2 * np.cos(i * 0.6 + self.dim * 0.3)
            radial_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Enhanced asymmetric gradient field with directional bias and cubic components
        grad_term = 0.0
        for i in range(self.dim):
            bias = 1.0 * np.sin(i * 1.4 + self.dim * 0.45)
            grad_term += (x[i] ** 3) * np.exp(-0.3 * x[i] ** 2) * (1.0 + bias * 0.7)
        
        # Fractal-like recursive structure with self-similarity and multi-scale features
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 0.7 + 1.1 * np.sin(i * 1.6 + self.dim * 0.4)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.9)
        
        # Dynamic coupling terms with non-linear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.5 * np.sin(i * j * 0.35))
                coupling_term += coupling ** 2
        
        # Multi-peak landscape with varying peak heights, widths and positions
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 2.0 + 2.5 * np.sin(i * 0.9)
            w1 = 0.25 + 0.8 * np.cos(i * 0.55)
            h2 = 1.7 + 1.6 * np.sin(i * 0.75)
            w2 = 0.35 + 0.9 * np.cos(i * 0.65)
            p1 = 1.5 + 4.5 * np.sin(i * 1.3)
            p2 = -4.5 + 4.5 * np.cos(i * 0.85)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.4 * peak1 + 0.6 * peak2
        
        # Recursive chaotic perturbation with higher dimensional coupling (modified)
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.sin(x[i] * 0.5 + self.dim * 0.35) * np.cos(x[i] * 0.4)
            chaos_term += chaos_factor * np.sin(x[i] ** 2 * 0.3)
        
        # Final combination with adjusted weights for better conditioning
        total = 0.38 * sin_term + 0.27 * radial_term + 0.16 * grad_term + 0.13 * fractal_term + 0.05 * coupling_term + 0.09 * peak_term + 0.02 * chaos_term
        
        # Global scaling factor with chaotic modulation and adaptive behavior
        global_scale = 1.0 + 0.4 * np.sin(self.dim * 0.65) * np.cos(self.dim * 0.45)
        
        return total * global_scale