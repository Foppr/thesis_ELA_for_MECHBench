import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic scaling
        result = np.sum(x**2) * 0.15
        
        # Chaotic RBF components with logistic map modulation
        rbf_sum = 0.0
        for i in range(self.dim):
            center = 3.0 * np.sin(0.7 * i + 1.0) * np.cos(0.3 * i)
            width = 0.4 + 0.6 * np.sin(0.5 * i + 0.5) * np.cos(0.2 * i)
            rbf_sum += np.exp(-width * (x[i] - center)**2) * np.sin(3.0 * x[i]) * np.cos(1.5 * x[i])
        result += 2.5 * rbf_sum
        
        # Multi-scale chaotic sinusoidal oscillations with period doubling
        sin_sum = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.6 * i + 0.3) * np.cos(0.4 * i)
            amp = 2.0 + 1.0 * np.sin(0.5 * i + 0.7) * np.cos(0.3 * i)
            sin_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8) * np.sin(x[i]**2)
        result += 1.8 * sin_sum
        
        # Adaptive conditioning with chaotic parameter modulation
        cond_sum = 0.0
        for i in range(self.dim):
            cond_factor = 1.5 + 1.2 * np.sin(0.8 * i + 0.4) * np.cos(0.6 * i)
            cond_sum += cond_factor * x[i]**4
        result += 1.2 * cond_sum
        
        # Cross-dimensional coupling with chaotic interaction strengths
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                strength = 0.8 + 0.5 * np.sin(0.3 * (i + j) + 0.2) * np.cos(0.2 * (i - j))
                cross_sum += strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        result += 2.0 * cross_sum
        
        # Fractal-like self-similarity with chaotic polynomial terms
        poly_sum = 0.0
        for i in range(self.dim):
            val = x[i]
            for k in range(1, 5):
                coeff = 0.4 + 0.2 * np.sin(0.3 * i * k + 0.5) * np.cos(0.2 * i)
                poly_sum += coeff * val**(2*k)
                val = np.sin(val) * np.cos(val)
        result += 1.0 * poly_sum
        
        # Memory effect with chaotic weights and delayed feedback
        if self.dim > 1:
            mem_sum = 0.0
            for i in range(1, self.dim):
                weight = 0.8 + 0.4 * np.sin(0.6 * i + 0.3) * np.cos(0.4 * i)
                mem_sum += weight * x[i-1] * x[i] * np.sin(0.5 * (x[i-1] + x[i]))
            result += 1.4 * mem_sum
            
        # Exponential modulation with chaotic parameters and phase shifts
        exp_mod = 0.0
        for i in range(self.dim):
            amp = 1.8 + 0.7 * np.sin(0.4 * i + 0.2) * np.cos(0.3 * i)
            freq = 1.0 + 0.5 * np.sin(0.6 * i + 0.4) * np.cos(0.2 * i)
            phase = 0.5 * np.sin(0.3 * i + 0.1)
            exp_mod += amp * np.exp(-freq * np.abs(x[i])) * np.sin(2.0 * x[i] + phase)
        result += 1.9 * exp_mod
        
        # Add chaotic noise term with dynamic amplitude
        noise_amp = 0.5 + 0.3 * np.sin(0.7 * self.dim + 0.4)
        noise = np.sum(np.random.randn(self.dim) * noise_amp)
        result += 0.8 * noise
        
        return result