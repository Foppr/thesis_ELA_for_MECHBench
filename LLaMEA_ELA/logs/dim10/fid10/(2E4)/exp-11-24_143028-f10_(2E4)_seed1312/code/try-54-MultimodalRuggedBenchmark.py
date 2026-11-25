import numpy as np

class MultimodalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Exponentially increasing frequency sinusoidal components
        for i in range(self.dim):
            freq = 2**(i+1)
            amp = 1.0 / (1.0 + i * 0.2)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.tan(0.05 * x[i]**4)
        
        # Polynomial chaos interactions with dynamic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = (i + 1) * (j + 1) * 0.01
                poly_interaction = x[i]**3 + x[j]**3 + coeff * x[i] * x[j]
                result += 0.5 * poly_interaction * np.exp(-0.02 * (x[i] - x[j])**2)
        
        # Nested fractal-like structure with recursive scaling
        for i in range(self.dim):
            result += 0.4 * np.sin(2 * x[i]) * np.cos(5 * x[i]) * np.sin(8 * x[i]**2) * np.cos(13 * x[i]**3)
        
        # Adaptive boundary penalties with varying intensities
        for i in range(self.dim):
            penalty_left = 0.3 * np.exp(-np.abs(x[i] + 5.0)) * np.sin(15 * x[i])
            penalty_right = 0.3 * np.exp(-np.abs(x[i] - 5.0)) * np.cos(15 * x[i])
            result += penalty_left + penalty_right
        
        # High-order polynomial with chaotic coefficient modulation
        sum_x = np.sum(x)
        modulator = 1.0 + 0.3 * np.sin(sum_x * 0.5)
        result += 0.15 * modulator * (sum_x**6 - 2*sum_x**4 + sum_x**2)
        
        # Multi-scale oscillatory component with adaptive amplitudes
        for i in range(self.dim):
            amp = 0.2 + 0.1 * np.sin(i * 0.7)
            result += amp * np.sin(60 * x[i]) * np.cos(50 * x[i]) * np.sin(40 * x[i]**2) * np.cos(30 * x[i]**3)
        
        # Cross-dimensional coupling with time-varying scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 + 0.4 * np.sin(x[i] * x[j])
                result += 0.25 * scale * np.sin(3 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        
        # Saddle-point enhancement with chaotic perturbations
        for i in range(self.dim):
            result += 0.12 * x[i]**9 - 0.25 * x[i]**8 + 0.18 * x[i]**7 - 0.1 * x[i]**6
        
        return result