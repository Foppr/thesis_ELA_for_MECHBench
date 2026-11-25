import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay parameters
        self.decay_rates = np.random.uniform(0.1, 1.0, dim)
        self.amplitude_scales = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Precompute trigonometric coupling coefficients
        self.coupling_strengths = np.random.uniform(0.5, 1.5, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term with adaptive scaling
        result += 0.2 * np.sum(x**2)
        
        # Exponential decay potentials with position-dependent rates
        for i in range(self.dim):
            decay_potential = self.amplitude_scales[i] * np.exp(-self.decay_rates[i] * np.abs(x[i]))
            result += decay_potential
            
        # Trigonometric coupling between dimensions with power-law interaction
        for i in range(self.dim):
            trig_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_strengths[i, j]
                    angle = coupling * (x[i] + x[j]) + self.phase_shifts[i]
                    # Power-law scaling on the trigonometric components
                    trig_term += np.sin(angle)**3 + 0.5 * np.cos(2 * angle)**2
            result += 0.3 * trig_term**1.5
            
        # Multi-scale sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(x[i])
            modulated = np.sin(freq * x[i] + self.phase_shifts[i]) * \
                       np.cos(2 * freq * x[i] + self.phase_shifts[i]**2)
            result += 0.4 * modulated
            
        # Power-law conditioned conditioning
        norm_x = np.linalg.norm(x, ord=1) / self.dim
        power_conditioning = 1.0 + 0.8 * (norm_x**1.3)
        result *= power_conditioning
        
        # Add chaotic noise with exponential amplitude modulation
        noise_amplitude = 0.05 * np.exp(-0.1 * np.sum(x**2))
        noise = noise_amplitude * np.sum(np.random.uniform(-1, 1, self.dim))
        result += noise
        
        return result