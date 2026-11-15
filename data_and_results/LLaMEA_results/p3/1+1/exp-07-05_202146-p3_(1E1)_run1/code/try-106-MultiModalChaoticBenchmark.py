import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic modulation coefficients
        self.coeffs = np.array([np.sin(i * 0.31) * np.cos(i * 0.57) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base
        result = np.sum(x**2)
        
        # Multi-modal sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.5 + 3.2 * np.sin(i * 0.41)
            amp = 1.3 + 0.7 * np.cos(i * 0.33)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.38)
            
        # Exponentially decaying correlation structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.12 * np.abs(i - j))
                result += 0.25 * decay * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Chaotic phase coupling with dynamic scaling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.07 * i))
        result += 0.42 * np.sin(phase_sum * 0.63) * np.cos(phase_sum * 0.81)
        
        # Logarithmic barrier to enforce global minimum
        result += 0.03 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Periodic attractor terms
        for i in range(self.dim):
            result += 0.15 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Fractal-like self-similarity with multi-scale modulation
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.05 * x[i])
        result += 0.18 * fractal_term
        
        # Memory-dependent interaction terms
        if hasattr(self, 'history'):
            hist_influence = 0.0
            for i in range(self.dim):
                hist_influence += 0.05 * self.history[i] * np.sin(x[i] * 0.45)
            result += hist_influence
        self.history = x.copy()
        
        # High-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.2 * np.sin(15.7 * x[i]) * np.cos(7.85 * x[i])
        result += noise
        
        # Multi-scale oscillatory basin boundaries
        for i in range(self.dim):
            result += 0.11 * np.sin(9.3 * x[i]) * np.cos(4.65 * x[i]) * np.exp(-0.03 * np.abs(x[i]))
            
        return result