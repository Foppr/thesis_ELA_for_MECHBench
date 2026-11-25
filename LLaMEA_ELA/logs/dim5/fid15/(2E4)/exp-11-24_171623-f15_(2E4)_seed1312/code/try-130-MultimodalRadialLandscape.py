import numpy as np

class MultimodalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function components with dynamic centers and multi-scale Gaussians
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(7, self.dim))
        for i in range(self.dim):
            center_idx = i % len(centers)
            center = centers[center_idx]
            distance = np.abs(x_norm[i] - center)
            # Multi-scale Gaussian with varying widths and dynamic amplitudes
            width = 1.0 + 0.5 * np.sin(i * np.pi / 4.0)
            amplitude = 1.0 + 0.3 * np.cos(i * np.pi / 3.0)
            rbf_sum += amplitude * np.exp(-distance**2 / (2 * width**2)) * np.sin(15 * x_norm[i])
        
        # Enhanced cross-dimensional interaction terms with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Limited but chaotic coupling
                distance = np.abs(x_norm[i] - x_norm[j])
                # Chaotic coupling factor with dynamic scaling
                coupling = (1 + 0.8 * np.sin(x_norm[i] * x_norm[j] * 12.0 + np.sum(x_norm[:i]) * 0.5))
                cross_term += coupling * np.exp(-distance * 5.0) * (x_norm[i]**3 + x_norm[j]**3)
        
        # Multi-frequency sinusoidal oscillations with fractal-like behavior
        sin_sum = 0.0
        frequencies = [1.0, 2.5, 5.0, 8.0, 13.0, 21.0]  # Fibonacci-like spacing
        for i in range(self.dim):
            freq_idx = i % len(frequencies)
            freq = frequencies[freq_idx]
            # Fractal-like modulation with recursive sine terms
            modulator = np.sin(x_norm[i] * freq * np.pi) + 0.3 * np.sin(x_norm[i] * freq * np.pi * 2.0)
            sin_sum += modulator * np.cos(x_norm[i] * freq * np.pi / 4.0)
        
        # Saddle-point like behavior with higher-order polynomial conditioning
        saddle_sum = 0.0
        for i in range(self.dim):
            # Higher-order saddle point with chaotic scaling
            base_term = x_norm[i]**6 - 5 * x_norm[i]**4 + 6 * x_norm[i]**2
            scaling = 1.0 + 0.4 * np.sin(x_norm[i] * 7.0)
            saddle_sum += scaling * base_term
        
        # Enhanced chaotic modulation with multi-dimensional dynamic scaling
        chaos_factor = 1.0 + 0.5 * np.sin(np.sum(x_norm**3) * 8.0 + np.sum(np.abs(x_norm)) * 2.0)
        
        # Add noise-like perturbations for increased complexity
        noise_term = 0.05 * np.sum(np.sin(10 * x_norm + np.pi/4.0))
        
        # Combine all terms with adaptive weighting
        result = 0.25 * rbf_sum + 0.3 * cross_term + 0.2 * sin_sum + 0.25 * saddle_sum + noise_term
        
        return result * chaos_factor * (1 + 0.15 * np.sum(np.abs(x_norm)) + 0.05 * np.sum(x_norm**4))