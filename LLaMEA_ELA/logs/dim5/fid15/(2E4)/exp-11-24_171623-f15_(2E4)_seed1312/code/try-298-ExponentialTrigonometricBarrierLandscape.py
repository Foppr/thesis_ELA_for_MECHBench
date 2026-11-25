import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential barrier parameters with varying decay rates
        self.barrier_rates = 0.3 + 1.8 * np.random.rand(dim)
        self.barrier_heights = 1.2 + 2.5 * np.random.rand(dim)
        # Trigonometric coupling coefficients with varying frequencies
        self.coupling_freqs = 1.5 + 3.5 * np.random.rand(dim)
        self.coupling_amplitudes = 0.7 + 1.8 * np.random.rand(dim)
        # Adaptive conditioning factors with exponential scaling
        self.condition_factors = 0.15 + 1.3 * np.random.rand(dim)
        # Phase shifts for trigonometric components
        self.phase_shifts = 2 * np.pi * np.random.rand(dim)
        # Additional nonlinear interaction terms
        self.interaction_strength = 0.4 + 0.6 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i]))
        
        # Trigonometric coupling between dimensions with modified interaction
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.coupling_amplitudes[i] * np.sin(self.coupling_freqs[i] * x_norm[j] + self.phase_shifts[i])
                    coupling_sum += coupling_term * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Adaptive conditioning with exponential scaling and modified nonlinearity
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.condition_factors[i] * np.exp(-0.15 * x_norm[i]**2) + 
                               self.interaction_strength[i] * np.sin(2 * x_norm[i]))
        
        # Combined landscape with weighted components and modified structure
        result = 0.35 * barrier_sum + 0.45 * coupling_sum
        
        # Add global penalty and conditioning with higher-order terms
        penalty = 0.15 * np.sum(x_norm**4)
        return result * condition_factor + penalty + 0.08 * np.sum(np.abs(x_norm)**7)