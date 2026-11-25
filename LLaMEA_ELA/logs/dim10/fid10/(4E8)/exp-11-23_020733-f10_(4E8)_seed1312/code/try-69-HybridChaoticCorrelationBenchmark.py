import numpy as np

class HybridChaoticCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic base with varying condition numbers
        result = 0.0
        for i in range(self.dim):
            condition = 10**(i % 4)  # Varying condition numbers
            result += 0.5 * condition * x[i]**2
        
        # Non-separable high-dimensional correlation terms with chaotic modulation
        for i in range(self.dim):
            corr_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic modulation using sine with varying frequencies
                    freq = 1.0 + 0.5 * np.sin(i * 0.7 + j * 0.3)
                    corr_sum += x[i] * x[j] * np.sin(freq * (x[i] - x[j]))
            result += 0.1 * corr_sum**2
        
        # Chaotic sine wave components with multi-frequency interactions
        for i in range(self.dim):
            # Multi-scale chaotic sine waves with different amplitudes and frequencies
            sine_component = 0.0
            for k in range(1, 6):
                amplitude = 0.3 / k
                frequency = k * 2.0 + 0.5 * np.sin(i * 0.8)
                sine_component += amplitude * np.sin(frequency * x[i])
            result += 0.2 * sine_component**2
        
        # Gradient-based penalty mechanism (novel approach)
        grad_penalty = 0.0
        for i in range(self.dim):
            # Compute finite difference gradient approximation
            h = 1e-5
            if i < self.dim - 1:
                grad_approx = (self._eval_single_dim(x, i, h) - self._eval_single_dim(x, i, -h)) / (2 * h)
                grad_penalty += 0.1 * grad_approx**2
        result += grad_penalty
        
        # High-dimensional saddle point interactions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                distance = np.abs(x[i] - x[j])
                interaction = np.exp(-distance) * np.cos(3 * distance)
                result += 0.05 * interaction * (x[i]**2 + x[j]**2)
        
        # Add boundary-sensitive penalty with fractal-like scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = min(np.abs(x[i] - 5.0), np.abs(x[i] + 5.0))
            boundary_penalty += 0.1 * dist_from_bound**2.5 * (1 + np.sin(10 * dist_from_bound))
        result += boundary_penalty
        
        return result
    
    def _eval_single_dim(self, x, idx, delta):
        """Helper to compute finite difference approximation"""
        x_copy = x.copy()
        x_copy[idx] += delta
        return self.f(x_copy)