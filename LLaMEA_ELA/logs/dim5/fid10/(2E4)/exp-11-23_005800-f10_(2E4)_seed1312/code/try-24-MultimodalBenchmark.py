import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal base with varying frequencies and amplitudes
        f_val = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            amp = 1.0 + 0.5 * np.sin(i * np.pi / 4)
            f_val += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Enhanced polynomial terms with adaptive exponents
        poly_term = 0.0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.3 * np.sin(i * np.pi / 3)
            poly_term += (x_norm[i] ** (4 + exp_factor)) * (1.0 + 0.2 * np.cos(i * np.pi / 2))
        f_val += 2.0 * poly_term
        
        # Adaptive Gaussian peaks with dynamic centers and widths
        gaussian_sum = 0.0
        for i in range(9):
            center = np.sin(i * np.pi / 4.5)
            width = 0.5 + 0.3 * np.cos(i * np.pi / 3)
            gaussian_sum += np.exp(-((x_norm - center)**2) / (2 * width**2))
        f_val -= 1.5 * gaussian_sum
        
        # Cross-dimensional chaotic coupling with time-delayed interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                delay = (i + j) % 3
                coupling = np.sin(np.pi * (x_norm[i] + x_norm[j]) / (1 + delay))
                cross_term += coupling * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        f_val += 0.8 * cross_term
        
        # Final penalty term to ensure global minimum at origin with sharp curvature
        f_val += 0.3 * np.sum(np.abs(x_norm)**4.2)
        
        return f_val