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
            freq_i = 15 + 5 * np.sin(x[i])
            result += 1.1 * np.sin(freq_i * x[i]) * np.cos(8 * x[i]) * np.sin(4 * x[i]**2)
        
        # Fractal-like self-similar structure with multi-scale oscillations
        for i in range(self.dim):
            result += 0.9 * np.sin(20 * x[i]) * np.cos(16 * x[i]) * np.sin(10 * x[i]**3) * (1 + 0.3 * np.abs(x[i]))
        
        # Dynamic cross-dimensional coupling with time-varying amplitudes
        for i in range(self.dim):
            amp = 0.7 + 0.25 * np.sin(2.5 * x[i])
            result += amp * np.sin(10 * x[i]) * np.cos(7 * x[(i+1) % self.dim]) * np.tan(0.7 * (x[i] + x[(i+1) % self.dim]))
        
        # Multi-scale fractal oscillation with exponential decay
        for i in range(self.dim):
            result += 0.6 * np.sin(30 * x[i]) * np.cos(24 * x[i]) * np.sin(17 * x[i]**4) * np.exp(-0.15 * np.abs(x[i]))
        
        # Boundary-sensitive penalty with logarithmic scaling
        boundary_penalty = 0
        for i in range(self.dim):
            boundary_penalty += 3.0 * (np.abs(x[i]) - 5.0)**2 / (1 + np.exp(-np.abs(x[i])))
        result += boundary_penalty
        
        # Non-separable high-order polynomial with chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * x[i]**3 * x[j]**2 * np.sin(6 * (x[i] + x[j])) * np.cos(5 * (x[i] - x[j]))
        
        # Embedded fractal structure with recursive scaling
        for i in range(self.dim):
            result += 0.7 * np.sin(35 * x[i]) * np.cos(29 * x[i]) * np.sin(22 * x[i]**5) * (1 + 0.2 * x[i]**2)
        
        # Dynamic coupling with phase shifts and amplitude modulation
        for i in range(self.dim):
            phase_shift = np.sin(4 * x[i])
            result += 0.9 * np.sin(10 * x[i] + phase_shift) * np.cos(7 * x[(i+2) % self.dim]) * (1 + 0.3 * np.abs(x[i]))
        
        # Additional chaotic term with complex frequency modulation
        sum_x = np.sum(x)
        result += 1.2 * np.sin(40 * sum_x) * np.cos(34 * sum_x) * np.tan(2.5 * sum_x) * (1 + 0.15 * np.abs(sum_x))
        
        # Multi-modal structure with adaptive valley heights
        for i in range(self.dim):
            result += 0.5 * np.sin(45 * x[i]) * np.cos(40 * x[i]) * np.sin(32 * x[i]**6) * (1 + 0.3 * np.abs(x[i])**3)
        
        # Cross-dimensional exponential coupling with fractal scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-np.abs(x[i] - x[j]) / (1 + 0.7 * (np.abs(x[i]) + np.abs(x[j]))))
                result += 0.35 * coupling * np.sin(15 * (x[i] + x[j])) * np.cos(12 * (x[i] - x[j]))
        
        # Final chaotic oscillation with complex interaction
        for i in range(self.dim):
            result += 0.45 * np.sin(58 * x[i]) * np.cos(53 * x[i]) * np.tan(4 * x[i]) * (1 + 0.4 * x[i]**4)
        
        # Add cubic nonlinearity to increase condition number
        for i in range(self.dim):
            result += 0.12 * x[i]**3
        
        return result