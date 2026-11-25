import numpy as np

class HybridChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base separable quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Non-separable high-dimensional interference patterns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic phase shifts and coupling strengths
                phase = np.sin(i * 0.7 + j * 0.5) * np.pi / 4
                coupling = 0.3 * np.exp(-0.1 * (i + j)) * (1 + 0.2 * np.sin(i * j * 0.3))
                interference = coupling * np.sin(3 * x[i] + phase) * np.cos(3 * x[j] + phase)
                result += interference * np.log(1 + abs(x[i] - x[j]))
        
        # Exponentially decaying sinusoidal modulations
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1) + 0.5 * np.sin(i * 0.6)
            decay = np.exp(-0.2 * abs(x[i]))
            modulation = 0.4 * np.sin(freq * x[i]) * decay
            result += modulation
        
        # Chaotic scaling and asymmetric distortions
        for i in range(self.dim):
            scale_factor = 1.5 + 0.3 * np.sin(i * 0.8)
            distortion = (x[i] ** 3 + 0.2 * x[i]) * scale_factor
            result += 0.25 * distortion * np.exp(-0.1 * abs(x[i]))
        
        # Multi-scale ridge structures with chaotic spacing
        for i in range(self.dim):
            ridge_freq = 5 * (i % 3 + 1) + np.cos(i * 0.5)
            ridge = 0.3 * np.cos(ridge_freq * x[i]) * np.exp(-0.15 * abs(x[i]))
            result += ridge
        
        # Asymmetric noise component
        noise = 0.1 * np.sum(np.sin(x * 7) * np.cos(x * 4)) + 0.05 * np.sum(np.sin(x * 11))
        result += noise
        
        return result