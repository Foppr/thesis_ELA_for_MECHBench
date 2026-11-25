import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential barrier parameters with varying decay rates
        self.barrier_rates = 0.2 + 1.9 * np.random.rand(dim)
        self.barrier_heights = 1.0 + 2.8 * np.random.rand(dim)
        # Trigonometric coupling coefficients with varying frequencies
        self.coupling_freqs = 1.2 + 4.0 * np.random.rand(dim)
        self.coupling_amplitudes = 0.5 + 2.0 * np.random.rand(dim)
        # Adaptive conditioning factors with exponential scaling
        self.condition_factors = 0.1 + 1.4 * np.random.rand(dim)
        # Phase shifts for trigonometric components
        self.phase_shifts = 2 * np.pi * np.random.rand(dim)
        # Additional nonlinear interaction terms
        self.interaction_strength = 0.3 + 0.7 * np.random.rand(dim)
        # Additional harmonic components for increased complexity
        self.harmonic_amplitudes = 0.4 + 0.8 * np.random.rand(dim)
        self.harmonic_frequencies = 0.8 + 2.2 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay barrier component with modified structure
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i]))
        
        # Trigonometric coupling between dimensions with enhanced interaction
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.coupling_amplitudes[i] * np.sin(self.coupling_freqs[i] * x_norm[j] + self.phase_shifts[i])
                    # Add distance-based weighting to coupling
                    distance_weight = np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
                    coupling_sum += coupling_term * distance_weight
        
        # Adaptive conditioning with enhanced nonlinearity and interaction
        condition_factor = 1.0
        for i in range(self.dim):
            # Enhanced conditioning with multiple nonlinear terms
            cond_term = (1.0 + self.condition_factors[i] * np.exp(-0.2 * x_norm[i]**2) + 
                        self.interaction_strength[i] * np.sin(2 * x_norm[i]) +
                        self.harmonic_amplitudes[i] * np.cos(self.harmonic_frequencies[i] * x_norm[i]))
            condition_factor *= cond_term
        
        # Combined landscape with refined components
        result = 0.4 * barrier_sum + 0.35 * coupling_sum
        
        # Add global penalty and conditioning with higher-order terms
        penalty = 0.2 * np.sum(x_norm**4)
        harmonic_penalty = 0.1 * np.sum(np.sin(self.harmonic_frequencies * x_norm))
        
        return result * condition_factor + penalty + harmonic_penalty + 0.1 * np.sum(np.abs(x_norm)**6)