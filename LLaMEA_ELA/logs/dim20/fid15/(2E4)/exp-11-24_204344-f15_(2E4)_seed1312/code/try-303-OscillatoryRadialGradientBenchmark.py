import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced sinusoidal oscillation with dynamic frequency and amplitude modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 4.0 * np.sin(i * 0.7 + self.dim * 0.3)
            amp = 1.0 + 1.5 * np.cos(i * 0.6 + self.dim * 0.35)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Modified radial basis function with dynamic centers and varying widths
        radial_term = 0.0
        for i in range(self.dim):
            center = -4.5 + 9.0 * np.sin(i * 0.45 + self.dim * 0.25)
            width = 0.1 + 0.9 * np.cos(i * 0.35 + self.dim * 0.4)
            radial_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Enhanced asymmetric gradient field with directional bias and cubic components
        grad_term = 0.0
        for i in range(self.dim):
            bias = 1.5 * np.sin(i * 1.2 + self.dim * 0.35)
            grad_term += (x[i] ** 4) * np.exp(-0.3 * x[i] ** 2) * (1.0 + bias * 0.5)
        
        # Fractal-like recursive structure with self-similarity and multi-scale features
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 0.6 + 0.7 * np.sin(i * 1.4 + self.dim * 0.3)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.7)
        
        # Dynamic coupling terms with non-linear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.3 * np.sin(i * j * 0.25))
                coupling_term += coupling ** 2
        
        # Multi-peak landscape with varying peak heights, widths and positions
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 2.0 + 2.0 * np.sin(i * 0.75)
            w1 = 0.2 + 0.6 * np.cos(i * 0.45)
            h2 = 2.5 + 1.0 * np.sin(i * 0.65)
            w2 = 0.8 + 0.5 * np.cos(i * 0.55)
            p1 = 1.5 + 3.5 * np.sin(i * 1.05)
            p2 = -3.5 + 3.5 * np.cos(i * 0.75)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.4 * peak1 + 0.6 * peak2
        
        # Recursive chaotic perturbation with higher dimensional coupling (modified)
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.sin(x[i] * 0.35 + self.dim * 0.25) * np.cos(x[i] * 0.3)
            chaos_term += chaos_factor * np.sin(x[i] ** 2 * 0.4)
        
        # Final combination with adjusted weights for better conditioning
        total = 0.35 * sin_term + 0.25 * radial_term + 0.15 * grad_term + 0.17 * fractal_term + 0.03 * coupling_term + 0.08 * peak_term + 0.07 * chaos_term
        
        # Global scaling factor with chaotic modulation and adaptive behavior
        global_scale = 1.0 + 0.4 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.35)
        
        return total * global_scale