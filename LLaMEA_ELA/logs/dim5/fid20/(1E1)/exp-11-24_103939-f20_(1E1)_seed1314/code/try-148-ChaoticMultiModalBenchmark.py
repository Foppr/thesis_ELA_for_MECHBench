import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Chaotic exponential decay landscape with sinusoidal modulation
        f1 = np.sum(np.exp(-np.abs(x_scaled)) * np.sin(2 * np.pi * x_scaled) ** 2)
        
        # Multi-modal structure with adaptive peaks and valleys
        f2 = 0.0
        for i in range(self.dim):
            f2 += (x_scaled[i] ** 4 - 2 * x_scaled[i] ** 2 + 1) * np.cos(3 * np.pi * x_scaled[i])
        
        # Cross-dimensional exponential coupling with varying strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.5 * np.sin((i + j) / self.dim * np.pi)
                f3 += strength * np.exp(-0.5 * (x_scaled[i] - x_scaled[j]) ** 2)
        
        # Sinusoidal high-frequency oscillation with adaptive frequency
        f4 = 0.0
        for i in range(self.dim):
            freq = 10 + 20 * np.sin(i / self.dim * np.pi)
            f4 += np.sin(freq * x_scaled[i]) ** 3
        
        # Asymmetric saddle point with exponential decay
        f5 = np.sum(np.exp(-0.5 * x_scaled**2) * (x_scaled**3 - x_scaled))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        f6 = condition_factor * np.sum(x_scaled**6)
        
        return f1 + f2 + f3 + f4 + f5 + f6