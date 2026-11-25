import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.5 * np.sum(x**2)
        
        # Chaotic sine-cosine interactions with dynamic frequencies
        for i in range(self.dim):
            freq_i = 12 + 4 * np.sin(x[i])
            result += 0.9 * np.sin(freq_i * x[i]) * np.cos(6 * x[i]) * np.sin(4 * x[i]**2)
        
        # Fractal-like self-similar structure with multi-scale oscillations
        for i in range(self.dim):
            result += 0.7 * np.sin(18 * x[i]) * np.cos(15 * x[i]) * np.sin(10 * x[i]**3) * (1 + 0.25 * np.abs(x[i]))
        
        # Dynamic cross-dimensional coupling with time-varying amplitudes
        for i in range(self.dim):
            amp = 0.6 + 0.2 * np.sin(3 * x[i])
            result += amp * np.sin(9 * x[i]) * np.cos(5 * x[(i+1) % self.dim]) * np.tan(0.4 * (x[i] + x[(i+1) % self.dim]))
        
        # Multi-scale fractal oscillation with exponential decay
        for i in range(self.dim):
            result += 0.5 * np.sin(28 * x[i]) * np.cos(22 * x[i]) * np.sin(16 * x[i]**4) * np.exp(-0.12 * np.abs(x[i]))
        
        # Boundary-sensitive penalty with logarithmic scaling
        boundary_penalty = 0
        for i in range(self.dim):
            boundary_penalty += 2.5 * (np.abs(x[i]) - 5.0)**2 / (1 + np.exp(-np.abs(x[i])))
        result += boundary_penalty
        
        # Non-separable high-order polynomial with chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.35 * x[i]**3 * x[j]**2 * np.sin(6 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
        
        # Embedded fractal structure with recursive scaling
        for i in range(self.dim):
            result += 0.6 * np.sin(33 * x[i]) * np.cos(28 * x[i]) * np.sin(22 * x[i]**5) * (1 + 0.18 * x[i]**2)
        
        # Dynamic coupling with phase shifts and amplitude modulation
        for i in range(self.dim):
            phase_shift = np.sin(4 * x[i])
            result += 0.8 * np.sin(10 * x[i] + phase_shift) * np.cos(5 * x[(i+2) % self.dim]) * (1 + 0.25 * np.abs(x[i]))
        
        # Additional chaotic term with complex frequency modulation
        sum_x = np.sum(x)
        result += 1.0 * np.sin(38 * sum_x) * np.cos(33 * sum_x) * np.tan(2.2 * sum_x) * (1 + 0.12 * np.abs(sum_x))
        
        # Multi-modal structure with adaptive valley heights
        for i in range(self.dim):
            result += 0.5 * np.sin(43 * x[i]) * np.cos(38 * x[i]) * np.sin(32 * x[i]**6) * (1 + 0.28 * np.abs(x[i])**3)
        
        # Cross-dimensional exponential coupling with fractal scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-np.abs(x[i] - x[j]) / (1 + 0.6 * (np.abs(x[i]) + np.abs(x[j]))))
                result += 0.3 * coupling * np.sin(14 * (x[i] + x[j])) * np.cos(9 * (x[i] - x[j]))
        
        # Final chaotic oscillation with complex interaction
        for i in range(self.dim):
            result += 0.4 * np.sin(53 * x[i]) * np.cos(48 * x[i]) * np.tan(3.7 * x[i]) * (1 + 0.32 * x[i]**4)
        
        # Additional polynomial chaos term
        for i in range(self.dim):
            result += 0.2 * x[i]**6 * np.sin(7 * x[i])
        
        return result