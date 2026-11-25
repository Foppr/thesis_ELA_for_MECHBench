import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with variable scaling
        base = 0.1 * np.sum(x**2)
        
        # Fractal-like basin structure using logarithmic scaling
        fractal_basin = 0.0
        for i in range(self.dim):
            # Logarithmic penalty that increases near boundaries
            log_penalty = 1.0 + np.log(1.0 + np.abs(x[i]))
            fractal_basin += log_penalty * (x[i]**2)
        
        # Chaotic sine-wave interactions with varying frequencies and amplitudes
        chaotic_interaction = 0.0
        for i in range(self.dim):
            # Use sine-cosine combinations with chaotic frequency modulation
            freq_mod = 1.0 + 0.5 * np.sin(0.7 * x[i])
            chaotic_interaction += 2.5 * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.8) + \
                                 1.2 * np.sin(freq_mod * x[i] * 1.3) * np.cos(freq_mod * x[i] * 1.1)
        
        # Cross-dimensional coupling with fractal-like interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear interaction with exponential scaling
                exp_interaction = np.exp(-0.1 * (x[i]**2 + x[j]**2))
                cross_coupling += 0.6 * exp_interaction * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Add a step-function like penalty for non-smooth behavior
        step_penalty = 0.0
        for i in range(self.dim):
            step_penalty += 0.5 * np.floor(2.0 + np.sin(x[i])) * (x[i]**2)
        
        # Additional high-frequency oscillation to increase condition number
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 1.5 * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i])
        
        return base + fractal_basin + chaotic_interaction + cross_coupling + step_penalty + high_freq