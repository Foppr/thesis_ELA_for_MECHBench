import numpy as np

class ExponentialResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Exponential decay potentials with random exponents
        self.decay_exponents = np.random.rand(dim) * 3.0 + 1.0
        # Harmonic resonance frequencies
        self.resonance_freqs = np.random.rand(dim) * 10.0 + 5.0
        # Elliptic shaping parameters
        self.elliptic_axes = np.random.rand(dim) * 2.0 + 1.0
        self.elliptic_angles = np.random.rand(dim) * np.pi
        # Adaptive conditioning factors
        self.conditioning_factors = np.random.rand(dim) * 4.0 + 1.0
        # Cross-dimensional coupling strengths (modified)
        self.coupling_strengths = np.random.rand(dim, dim) * 0.8 + 0.2
        # Phase shift parameters for resonance
        self.phase_shifts = np.random.rand(dim) * 2.0 * np.pi
        # Additional cubic nonlinearities for increased complexity
        self.cubic_coefficients = np.random.rand(dim) * 0.5 + 0.1
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Exponential decay potential component
        exp_potential = 0.0
        for i in range(self.dim):
            exp_potential += np.exp(-self.decay_exponents[i] * np.abs(x_norm[i]))
            
        # Harmonic resonance component with phase shifts
        harmonic_resonance = 0.0
        for i in range(self.dim):
            harmonic_resonance += np.sin(self.resonance_freqs[i] * x_norm[i] + self.phase_shifts[i]) * \
                                np.cos(self.resonance_freqs[i] * x_norm[i] + self.phase_shifts[i])
                                
        # Elliptic shaping component
        elliptic_shaping = 0.0
        for i in range(self.dim):
            a = self.elliptic_axes[i]
            angle = self.elliptic_angles[i]
            x_rot = x_norm[i] * np.cos(angle) - x_norm[(i+1) % self.dim] * np.sin(angle)
            y_rot = x_norm[i] * np.sin(angle) + x_norm[(i+1) % self.dim] * np.cos(angle)
            elliptic_shaping += (x_rot**2 / a**2 + y_rot**2) * 0.5
            
        # Adaptive conditioning
        adaptive_conditioning = 0.0
        for i in range(self.dim):
            adaptive_conditioning += self.conditioning_factors[i] * x_norm[i]**2
            
        # Cross-dimensional coupling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_coupling += self.coupling_strengths[i, j] * x_norm[i] * x_norm[j]
                    
        # Cubic nonlinearities added for increased complexity
        cubic_nonlinearities = 0.0
        for i in range(self.dim):
            cubic_nonlinearities += self.cubic_coefficients[i] * x_norm[i]**3
            
        # Combined function with multiple interaction terms
        return (2.0 * exp_potential + 1.5 * harmonic_resonance + 0.8 * elliptic_shaping + 
                0.3 * adaptive_conditioning + 0.2 * cross_coupling + 0.1 * cubic_nonlinearities + 1.0)