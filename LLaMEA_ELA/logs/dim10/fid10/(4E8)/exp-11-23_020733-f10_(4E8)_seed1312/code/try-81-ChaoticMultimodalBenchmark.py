import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with variable conditioning
        result = np.sum(x**2) * 0.3
        
        # Chaotic sinusoidal components with logistic map modulation
        for i in range(self.dim):
            freq = 3.0 + 2.0 * (np.sin(i * 0.7) + 1.0) / 2.0
            amp = 2.0 + np.cos(i * 0.5) * 0.5
            # Logistic map modulation for chaotic behavior
            logistic_mod = 4.0 * (i / self.dim) * (1 - i / self.dim) if i < self.dim else 0.5
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * logistic_mod
        
        # Modified radial basis functions with dynamic centers and widths
        centers = np.linspace(-4.2, 4.2, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i]
            width = 1.0 + 0.3 * np.sin(i * 0.8)
            dist = np.sum((x - center)**2)
            result += 1.2 * np.exp(-dist / (2 * width**2)) * np.cos(4 * dist) * (1 + 0.2 * np.sin(i))
        
        # Cross-dimensional coupling with chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                # Chaotic coupling modulation
                chaos_mod = 0.5 + 0.5 * np.sin(i * j * 0.3)
                result += 0.4 * coupling * chaos_mod * (1 + 0.3 * np.sin(i + j))
        
        # Asymmetric saddle points with varying steepness and chaotic scaling
        for i in range(self.dim):
            # Add chaotic scaling factor
            chaos_scale = 1.0 + 0.5 * np.sin(i * 0.9)
            result += 0.3 * x[i]**4 - 0.6 * x[i]**2 + 0.15 * np.sin(12 * x[i]) * chaos_scale
        
        # Multi-scale periodic components with chaotic frequency modulation
        for i in range(self.dim):
            freq_mod = 1.0 + 0.8 * np.sin(i * 0.6)
            result += 0.2 * np.sin(10 * freq_mod * x[i]) * np.cos(7 * freq_mod * x[i]) * np.tan(4 * freq_mod * x[i])
        
        # Enhanced boundary penalty with chaotic penalty scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.6:
                penalty_scale = 15.0 + 5.0 * np.sin(i * 0.4)
                boundary_penalty += penalty_scale * (abs(x[i]) - 4.6)**2
        result += boundary_penalty
        
        # Global scaling factor with chaotic adjustment
        global_scale = 1.8 + 0.4 * np.sin(self.dim * 0.3)
        result *= global_scale
        
        return result