import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced sinusoidal oscillation with dynamic frequency and amplitude modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = 1.5 + 3.0 * np.sin(i * 0.6 + self.dim * 0.4)
            amp = 1.2 + 0.8 * np.cos(i * 0.5 + self.dim * 0.3)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6)
        
        # Modified radial basis function with dynamic centers and varying widths
        radial_term = 0.0
        for i in range(self.dim):
            center = -4.0 + 8.0 * np.sin(i * 0.4 + self.dim * 0.2)
            width = 0.2 + 0.8 * np.cos(i * 0.3 + self.dim * 0.4)
            radial_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Enhanced asymmetric gradient field with directional bias and cubic components
        grad_term = 0.0
        for i in range(self.dim):
            bias = 0.8 * np.sin(i * 0.9 + self.dim * 0.6)
            grad_term += (x[i] ** 4) * np.exp(-0.2 * x[i] ** 2) * (1.0 + bias * 0.6)
        
        # Fractal-like recursive structure with self-similarity and multi-scale features
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.5 * np.sin(i * 1.0 + self.dim * 0.5)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.8)
        
        # Dynamic coupling terms with non-linear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.4 * np.sin(i * j * 0.3))
                coupling_term += coupling ** 2
        
        # Multi-peak landscape with varying peak heights, widths and positions
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 2.5 + 1.0 * np.sin(i * 0.7)
            w1 = 0.5 + 0.5 * np.cos(i * 0.4)
            h2 = 2.0 + 0.7 * np.sin(i * 0.6)
            w2 = 0.9 + 0.6 * np.cos(i * 0.5)
            p1 = 2.0 + 3.0 * np.sin(i * 0.8)
            p2 = -3.0 + 2.0 * np.cos(i * 0.7)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.7 * peak1 + 0.3 * peak2
        
        # Recursive chaotic perturbation with higher dimensional coupling (modified)
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.sin(x[i] * 0.4 + self.dim * 0.3) * np.cos(x[i] * 0.25)  # Slight parameter change
            chaos_term += chaos_factor * np.sin(x[i] ** 2 * 0.5)  # Slight parameter change
        
        # Final combination with adjusted weights for better conditioning
        total = 0.25 * sin_term + 0.20 * radial_term + 0.25 * grad_term + 0.15 * fractal_term + 0.15 * coupling_term + 0.08 * peak_term + 0.02 * chaos_term
        
        # Global scaling factor with chaotic modulation and adaptive behavior
        global_scale = 1.0 + 0.5 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.4)
        
        return total * global_scale