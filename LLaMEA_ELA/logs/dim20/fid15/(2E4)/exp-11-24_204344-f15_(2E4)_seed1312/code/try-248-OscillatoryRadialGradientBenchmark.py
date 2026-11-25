import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 1.5 * np.sin(i * 0.6 + self.dim * 0.2)
            amp = 0.8 + 0.4 * np.cos(i * 0.5 + self.dim * 0.3)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial basis function component with dynamic centers and widths
        radial_term = 0.0
        for i in range(self.dim):
            center = -2.0 + 4.0 * np.sin(i * 0.4 + self.dim * 0.1)
            width = 0.5 + 0.5 * np.cos(i * 0.3 + self.dim * 0.2)
            radial_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Asymmetric gradient field with directional bias
        grad_term = 0.0
        for i in range(self.dim):
            bias = 0.5 * np.sin(i * 0.7 + self.dim * 0.4)
            grad_term += (x[i] ** 3) * np.exp(-0.1 * x[i] ** 2) * (1.0 + bias)
        
        # Fractal-like recursive structure with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.8 + self.dim * 0.3)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale)
        
        # Dynamic coupling terms between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                coupling_term += coupling * (1.0 + 0.2 * np.sin(i * j * 0.1))
        
        # Multi-peak landscape with varying peak heights and widths
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 1.5 + 0.5 * np.sin(i * 0.6)
            w1 = 0.8 + 0.2 * np.cos(i * 0.4)
            h2 = 1.0 + 0.3 * np.sin(i * 0.5)
            w2 = 1.2 + 0.3 * np.cos(i * 0.3)
            p1 = 2.0 + 1.0 * np.sin(i * 0.7)
            p2 = -1.5 + 0.8 * np.cos(i * 0.6)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.7 * peak1 + 0.3 * peak2
        
        # Recursive chaotic perturbation
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.sin(x[i] * 0.5 + self.dim * 0.2) * np.cos(x[i] * 0.3)
            chaos_term += chaos_factor * np.sin(x[i] ** 2)
        
        # Final combination with adaptive weights
        total = 0.2 * sin_term + 0.15 * radial_term + 0.25 * grad_term + 0.1 * fractal_term + 0.2 * coupling_term + 0.08 * peak_term + 0.02 * chaos_term
        
        # Global scaling factor with chaotic modulation
        global_scale = 1.0 + 0.3 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.4)
        
        return total * global_scale