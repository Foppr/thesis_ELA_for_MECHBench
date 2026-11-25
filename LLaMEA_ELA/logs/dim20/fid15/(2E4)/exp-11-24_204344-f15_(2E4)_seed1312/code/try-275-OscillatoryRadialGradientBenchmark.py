import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced sinusoidal oscillation with dynamic frequency, amplitude, and harmonic modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.sin(i * 0.7 + self.dim * 0.4)
            amp = 1.0 + 0.8 * np.cos(i * 0.5 + self.dim * 0.3)
            harm = 0.5 * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6) + harm
        
        # Modified radial basis function with dynamic centers, varying widths, and multi-scale features
        radial_term = 0.0
        for i in range(self.dim):
            center = -4.0 + 8.0 * np.sin(i * 0.4 + self.dim * 0.2)
            width = 0.3 + 0.8 * np.cos(i * 0.3 + self.dim * 0.4)
            scale = 1.0 + 0.5 * np.sin(i * 0.6 + self.dim * 0.5)
            radial_term += scale * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Enhanced asymmetric gradient field with directional bias, cubic components, and harmonic perturbations
        grad_term = 0.0
        for i in range(self.dim):
            bias = 0.8 * np.sin(i * 0.9 + self.dim * 0.6)
            harm = 0.3 * np.sin(x[i] * 1.2) * np.cos(x[i] * 0.8)
            grad_term += (x[i] ** 3) * np.exp(-0.2 * x[i] ** 2) * (1.0 + bias * 0.7) + harm
        
        # Fractal-like recursive structure with self-similarity, multi-scale features, and chaotic modulation
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.6 * np.sin(i * 1.0 + self.dim * 0.5)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.8) + 0.2 * np.sin(x[i] * scale * 3.0)
        
        # Dynamic coupling terms with non-linear interaction and multi-frequency harmonic components
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.4 * np.sin(i * j * 0.3))
                coupling += 0.25 * np.sin(x[i] * 2.0) * np.cos(x[j] * 1.5)
                coupling_term += coupling ** 2
        
        # Multi-peak landscape with varying peak heights, widths, positions, and harmonic perturbations
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 2.5 + 1.0 * np.sin(i * 0.7)
            w1 = 0.6 + 0.5 * np.cos(i * 0.4)
            h2 = 2.0 + 0.8 * np.sin(i * 0.6)
            w2 = 1.2 + 0.7 * np.cos(i * 0.5)
            p1 = 2.0 + 2.5 * np.sin(i * 0.8)
            p2 = -2.5 + 2.0 * np.cos(i * 0.7)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            harm = 0.3 * np.sin(x[i] * 1.8) * np.cos(x[i] * 1.2)
            peak_term += 0.7 * peak1 + 0.3 * peak2 + harm
        
        # Recursive chaotic perturbation with higher dimensional coupling, harmonic components, and adaptive scaling
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.sin(x[i] * 0.5 + self.dim * 0.35) * np.cos(x[i] * 0.25)
            harm = 0.4 * np.sin(x[i] ** 2 * 0.6) * np.cos(x[i] * 1.2)
            chaos_term += chaos_factor * np.sin(x[i] ** 2 * 0.5) + harm
        
        # Final combination with adjusted weights for better conditioning and enhanced multimodality
        total = 0.3 * sin_term + 0.25 * radial_term + 0.25 * grad_term + 0.12 * fractal_term + 0.15 * coupling_term + 0.08 * peak_term + 0.05 * chaos_term
        
        # Global scaling factor with chaotic modulation and adaptive behavior
        global_scale = 1.0 + 0.4 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.4)
        
        return total * global_scale