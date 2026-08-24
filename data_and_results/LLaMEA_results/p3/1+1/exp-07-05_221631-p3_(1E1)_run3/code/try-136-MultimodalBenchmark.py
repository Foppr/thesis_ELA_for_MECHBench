import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random phase shifts for each dimension
        np.random.seed(42)
        self.phase_shifts = np.random.uniform(0, 2 * np.pi, dim)
        # Adaptive frequency parameters
        self.frequencies = np.random.uniform(1.0, 8.0, dim)
        # Coupling coefficients for cross-dimensional interactions
        self.coupling_strength = 0.7
        # Chaotic modulation parameters
        self.chaos_factor = 3.0
        # Dimensional scaling
        self.scales = np.random.uniform(0.5, 2.0, dim)
        # Noise parameters
        self.noise_level = 0.05
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply scaling
        x_scaled = x * self.scales
        
        # Base quadratic term
        f_val = np.sum(x_scaled**2)
        
        # Add periodic sinusoidal modulations with chaotic phase shifts
        for i in range(self.dim):
            # Sinusoidal modulation with adaptive frequency and chaotic phase
            phase = self.frequencies[i] * x_scaled[i] + self.phase_shifts[i]
            chaotic_phase = phase + self.chaos_factor * np.sin(phase)
            modulation = np.sin(chaotic_phase) * np.cos(2 * chaotic_phase)
            f_val += 2.0 * np.sin(self.frequencies[i] * x_scaled[i]) * modulation
            
        # Add higher-order cross-dimensional interactions with chaotic coupling
        for i in range(self.dim - 2):
            # Chaotic coupling between three dimensions
            coupling = np.sin(x_scaled[i]) * np.cos(x_scaled[i+1]) * np.sin(x_scaled[i+2])
            interaction = self.coupling_strength * x_scaled[i] * x_scaled[i+1] * x_scaled[i+2] * coupling
            f_val += interaction
            
        # Add fractal-like chaotic oscillations with varying amplitudes
        fractal_term = 0.0
        for i in range(self.dim):
            # Nested chaotic oscillation with increasing frequency
            freq = 2**(i % 4 + 1)
            oscillation = np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
            fractal_term += oscillation * (i + 1) * 0.1
        f_val += fractal_term
        
        # Add stochastic noise with adaptive variance
        noise = np.random.normal(0, self.noise_level, self.dim)
        f_val += np.sum(noise * x_scaled)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.1
        
        return f_val