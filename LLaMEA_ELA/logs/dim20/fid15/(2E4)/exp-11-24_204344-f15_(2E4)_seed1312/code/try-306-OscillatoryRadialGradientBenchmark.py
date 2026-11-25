import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced sinusoidal oscillation with dynamic frequency and amplitude modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = 1.2 + 3.8 * np.sin(i * 0.7 + self.dim * 0.2)
            amp = 0.9 + 1.1 * np.cos(i * 0.6 + self.dim * 0.35)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.35)
        
        # Modified radial basis function with dynamic centers and varying widths
        radial_term = 0.0
        for i in range(self.dim):
            center = -4.2 + 8.4 * np.sin(i * 0.35 + self.dim * 0.25)
            width = 0.25 + 0.75 * np.cos(i * 0.35 + self.dim * 0.4)
            radial_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Enhanced asymmetric gradient field with directional bias and cubic components
        grad_term = 0.0
        for i in range(self.dim):
            bias = 1.2 * np.sin(i * 1.1 + self.dim * 0.35)
            grad_term += (x[i] ** 3) * np.exp(-0.25 * x[i] ** 2) * (1.0 + bias * 0.35)
        
        # Fractal-like recursive structure with self-similarity and multi-scale features
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 0.7 + 0.6 * np.sin(i * 1.4 + self.dim * 0.2)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.55)
        
        # Dynamic coupling terms with non-linear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.3 * np.sin(i * j * 0.25))
                coupling_term += coupling ** 2
        
        # Multi-peak landscape with varying peak heights, widths and positions
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 1.9 + 1.5 * np.sin(i * 0.75)
            w1 = 0.35 + 0.45 * np.cos(i * 0.45)
            h2 = 2.1 + 0.7 * np.sin(i * 0.65)
            w2 = 0.75 + 0.35 * np.cos(i * 0.55)
            p1 = 1.2 + 2.8 * np.sin(i * 1.05)
            p2 = -2.8 + 2.8 * np.cos(i * 0.75)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.37 * peak1 + 0.63 * peak2
        
        # Recursive chaotic perturbation with higher dimensional coupling (modified)
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.sin(x[i] * 0.35 + self.dim * 0.22) * np.cos(x[i] * 0.27)
            chaos_term += chaos_factor * np.sin(x[i] ** 2 * 0.38)
        
        # Final combination with adjusted weights for better conditioning
        total = 0.4 * sin_term + 0.2 * radial_term + 0.19 * grad_term + 0.15 * fractal_term + 0.03 * coupling_term + 0.08 * peak_term + 0.05 * chaos_term
        
        # Global scaling factor with chaotic modulation and adaptive behavior
        global_scale = 1.0 + 0.3 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.32)
        
        return total * global_scale