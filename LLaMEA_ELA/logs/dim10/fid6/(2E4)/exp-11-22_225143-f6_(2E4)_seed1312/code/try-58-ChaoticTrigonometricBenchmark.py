import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map chaotic parameters
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        # Trigonometric coupling coefficients
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive noise parameters
        self.noise_amplitudes = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequencies = np.random.uniform(2.0, 8.0, dim)
        # Local minima positions
        self.minima_positions = np.random.uniform(-5.0, 5.0, (15, dim))
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic logistic map component
        for i in range(self.dim):
            x_i = x_norm[i]
            chaotic_val = 0.0
            for _ in range(10):  # Iterate chaos map
                x_i = self.r_params[i] * x_i * (1 - x_i)
            chaotic_val = x_i**2 + 0.1 * np.sin(10 * x_i)
            f_val += 0.3 * chaotic_val
        
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_coeffs[i, j] * np.sin(x_norm[i] + x_norm[j])
            f_val += 0.25 * coupling_sum**2
        
        # Adaptive noise component
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x_norm[i])
        f_val += 0.15 * noise_sum**2
        
        # Multi-modal component with local minima
        multimodal_sum = 0.0
        for i in range(15):
            dist = np.sum((x_norm - self.minima_positions[i])**2)
            multimodal_sum += np.exp(-dist / 0.5)
        f_val += 0.3 * multimodal_sum
        
        # Add global scaling and offset
        f_val = np.abs(f_val) + 0.5 * np.sum(x**2) / self.dim
        
        return f_val